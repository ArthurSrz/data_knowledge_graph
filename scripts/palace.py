"""Build a memory palace (Obsidian Canvas) from a note's typed subgraph.

    env/bin/python scripts/palace.py "Large Language Model" [--depth 2]
    env/bin/python scripts/palace.py --selftest

Containment relations nest notes as rooms inside rooms; everything else is a
labelled corridor. Output: palace/<note>.canvas (JSON Canvas 1.0).
"""
import json
import re
import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from reason import extract_frontmatter, parse_targets  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent
GRAPH = VAULT / "graph"
OUT = VAULT / "palace"

# ---------------------------------------------------------------------------
# TODO(Arthur): this table IS the palace. Tune it to your ontology.
#   "inside"   -> the TARGET is a bigger place; this note is a room inside it
#   "contains" -> the TARGET is a room inside this note
#   "across"   -> the target sits on the far side of the street (opposition)
#   anything not listed -> a labelled corridor between two rooms
SPATIAL_ROLE = {
    "broader": "inside", "skos:broader": "inside", "subclass of": "inside",
    "instance of": "inside", "partOf": "inside", "part of": "inside",
    "facet of": "inside", "inferred:skos:broader": "inside",
    "subclassOf": "inside", "instanceOf": "inside", "subFieldOf": "inside", "TypeOf": "inside",
    "skos:narrower": "contains", "inferred:skos:narrower": "contains",
    "has part(s)": "contains",
    "oppositeOf": "across", "opposite of": "across", "different from": "across",
}
SKIP = {"inferred:skos:ancestor"}  # redundant with broader chains
# ---------------------------------------------------------------------------

LEAF_W, LEAF_H, PAD, HEAD = 260, 80, 40, 50


def load_graph():
    """{name: {relation: [targets]}} over graph/ + daily/ (prose notes -> 'mentions')."""
    notes, canon = {}, {}
    for p in list(GRAPH.glob("*.md")) + list((VAULT / "daily").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        rels = {}
        if isinstance(fm, dict):
            for k, v in fm.items():
                if k in SKIP:
                    continue
                t = parse_targets(v)
                if t:
                    rels[k] = t
        else:
            t = parse_targets(re.findall(r"\[\[[^\]]+\]\]", text))
            if t:
                rels["mentions"] = t
        notes[p.stem] = rels
        canon[p.stem.lower()] = p.stem
    # resolve case-insensitive targets to real note names, drop dangling ones
    for rels in notes.values():
        for k, ts in rels.items():
            rels[k] = [canon[t.lower()] for t in ts if t.lower() in canon]
    return notes


def subgraph(notes, root, depth):
    """BFS over all relations (both directions). Returns (node set, [(src, rel, dst)])."""
    rev = {}
    for s, rels in notes.items():
        for r, ts in rels.items():
            for t in ts:
                rev.setdefault(t, []).append((s, r))
    seen, q = {root: 0}, deque([root])
    while q:
        n = q.popleft()
        if seen[n] >= depth:
            continue
        nbrs = [t for ts in notes.get(n, {}).values() for t in ts] + [s for s, _ in rev.get(n, [])]
        for m in nbrs:
            if m not in seen:
                seen[m] = seen[n] + 1
                q.append(m)
    edges = [(s, r, t) for s in seen for r, ts in notes.get(s, {}).items() for t in ts if t in seen]
    return set(seen), sorted(set(edges))


def containment(nodes, edges):
    """parent[node] from inside/contains roles; cycle-safe (first parent by name wins)."""
    parent = {}
    for s, r, t in edges:
        role = SPATIAL_ROLE.get(r)
        child, par = (s, t) if role == "inside" else (t, s) if role == "contains" else (None, None)
        if child and child != par and child not in parent:
            parent[child] = par
    for c in list(parent):  # break cycles: walk up, drop the link that closes a loop
        seen, n = {c}, c
        while n in parent:
            n = parent[n]
            if n in seen:
                parent.pop(c)
                break
            seen.add(n)
    return parent


def layout(nodes, parent, order):
    """Recursive grid packing. Returns {name: (x, y, w, h)}; groups wrap their children."""
    kids = {}
    for n in nodes:
        kids.setdefault(parent.get(n), []).append(n)
    for k in kids.values():
        k.sort(key=lambda n: (order.get(n, 0), n))
    rect = {}

    def size(n):
        ch = kids.get(n, [])
        if not ch:
            return LEAF_W, LEAF_H
        sizes = [size(c) for c in ch]
        cols = max(1, round(len(ch) ** 0.5))
        rows = [sizes[i:i + cols] for i in range(0, len(sizes), cols)]
        w = max(sum(s[0] for s in row) + PAD * (len(row) + 1) for row in rows)
        h = sum(max(s[1] for s in row) for row in rows) + PAD * (len(rows) + 1) + HEAD
        return w, h

    def place(n, x, y):
        w, h = size(n)
        rect[n] = (x, y, w, h)
        ch = kids.get(n, [])
        if not ch:
            return
        cols = max(1, round(len(ch) ** 0.5))
        cy = y + HEAD + PAD
        for i in range(0, len(ch), cols):
            row, cx, rh = ch[i:i + cols], x + PAD, 0
            for c in row:
                place(c, cx, cy)
                cw, chh = size(c)
                cx += cw + PAD
                rh = max(rh, chh)
            cy += rh + PAD

    # top level: a street. Across-the-street roots get order 1 and land at the end.
    x = 0
    for n in kids.get(None, []):
        place(n, x, 0)
        x += size(n)[0] + 2 * PAD
    return rect


def build_canvas(nodes, edges, parent, rect):
    ids = {n: f"n{i:04x}" for i, n in enumerate(sorted(nodes))}
    out = {"nodes": [], "edges": []}
    for n in sorted(nodes):
        x, y, w, h = rect[n]
        if any(parent.get(c) == n for c in nodes):
            out["nodes"].append({"id": ids[n], "type": "group", "label": n, "x": x, "y": y, "width": w, "height": h})
            # the room's own note, as a card in its top-left corner
            out["nodes"].append({"id": ids[n] + "f", "type": "file", "file": note_path(n),
                                 "x": x + PAD, "y": y + HEAD - 30, "width": LEAF_W, "height": 50})
        else:
            out["nodes"].append({"id": ids[n], "type": "file", "file": note_path(n), "x": x, "y": y, "width": w, "height": h})
    for i, (s, r, t) in enumerate(edges):
        role = SPATIAL_ROLE.get(r)
        if role in ("inside", "contains"):
            continue  # already expressed by nesting
        e = {"id": f"e{i:04x}", "fromNode": ids[s], "toNode": ids[t], "fromSide": "right", "toSide": "left", "label": r}
        if role == "across":
            e["color"] = "1"  # red
        out["edges"].append(e)
    return out


def note_path(n):
    return f"graph/{n}.md" if (GRAPH / f"{n}.md").exists() else f"daily/{n}.md"


def build(root, depth=2, notes=None):
    notes = notes if notes is not None else load_graph()
    if root not in notes:
        sys.exit(f"no note named {root!r}")
    nodes, edges = subgraph(notes, root, depth)
    parent = containment(nodes, edges)
    across = {t for s, r, t in edges if s == root and SPATIAL_ROLE.get(r) == "across"}
    rect = layout(nodes, parent, {n: 1 for n in across})
    return build_canvas(nodes, edges, parent, rect)


def selftest():
    notes = {"A": {"subclass of": ["B"], "uses": ["C"], "oppositeOf": ["D"]},
             "B": {}, "C": {"broader": ["B"]}, "D": {}}
    cv = build("A", depth=2, notes=notes)
    rect = {n["label"] if n["type"] == "group" else Path(n["file"]).stem: n for n in cv["nodes"] if not n["id"].endswith("f")}
    b, a = rect["B"], rect["A"]
    assert b["x"] <= a["x"] and a["x"] + a["width"] <= b["x"] + b["width"], "A not inside B (x)"
    assert b["y"] <= a["y"] and a["y"] + a["height"] <= b["y"] + b["height"], "A not inside B (y)"
    labels = sorted(e["label"] for e in cv["edges"])
    assert labels == ["oppositeOf", "uses"], labels
    assert rect["D"]["x"] > b["x"] + b["width"], "D not across the street"
    print("selftest ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--selftest"]:
        selftest()
        sys.exit()
    depth = int(args[args.index("--depth") + 1]) if "--depth" in args else 2
    root = [a for a in args if not a.startswith("--") and a != str(depth)][0]
    canvas = build(root, depth)
    OUT.mkdir(exist_ok=True)
    path = OUT / f"{root}.canvas"
    path.write_text(json.dumps(canvas, indent=1), encoding="utf-8")
    print(f"{path.relative_to(VAULT)}  nodes={len(canvas['nodes'])} edges={len(canvas['edges'])}")
