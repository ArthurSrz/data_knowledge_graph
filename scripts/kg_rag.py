#!/usr/bin/env python3
"""Mini GraphRAG over the Obsidian graph: lexical seed search + typed-edge expansion.

Used by scripts/kg_mcp.py (MCP server) and ~/.claude/hooks/kg-ground.py (prompt hook).
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from reason import extract_frontmatter, parse_targets  # noqa: E402

GRAPH_DIR = Path(__file__).resolve().parent.parent / "graph"
STOP = set("""the and for with from that this what how les des une est pour dans avec sur par que qui
quoi comment mon mes ton tes son ses pas plus est-ce peux peut faire avoir être aux du au""".split())


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def tokens(s):
    return {t for t in norm(s).split() if len(t) >= 3 and t not in STOP}


def load(graph_dir=GRAPH_DIR):
    """Return {name: note}. Re-read on every call: 940 files, ~sub-second, always fresh."""
    # ponytail: no cache, add an mtime-keyed cache if the graph grows past ~10k notes
    notes = {}
    for p in graph_dir.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        fm = extract_frontmatter(text) or {}
        if not isinstance(fm, dict):
            fm = {}
        body = re.sub(r"^---\n.*?\n---\n?", "", text, count=1, flags=re.DOTALL).strip()
        aliases = fm.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        edges = [(k, t) for k, v in fm.items() if k != "aliases" for t in parse_targets(v)]
        notes[p.stem] = {"name": p.stem, "fm": fm, "body": body, "aliases": aliases,
                         "edges": edges, "back": []}
    lower = {n.lower(): n for n in notes}
    for n, note in notes.items():
        note["edges"] = [(k, lower.get(t.lower(), t)) for k, t in note["edges"]]
        for k, t in note["edges"]:
            if t in notes:
                notes[t]["back"].append((k, n))
    return notes


def score(query, note):
    """Lexical relevance of a note to a query. Phrase hits on name/aliases dominate."""
    q, qt = f" {norm(query)} ", tokens(query)
    s = 0.0
    for label in [note["name"], *note["aliases"]]:
        nl = norm(str(label))
        if len(nl) >= 3 and f" {nl} " in q:
            s += 10 * len(nl.split())
        s += 2 * len(qt & tokens(str(label)))
    s += min(3.0, 0.3 * len(qt & tokens(note["body"])))
    return s


def search(query, k=5, notes=None):
    notes = notes or load()
    ranked = sorted(((score(query, n), name) for name, n in notes.items()), reverse=True)
    return [name for s, name in ranked[:k] if s > 0]


def render(note, excerpt=600):
    lines = [f"## [[{note['name']}]]"]
    if note["aliases"]:
        lines.append("aliases: " + ", ".join(map(str, note["aliases"])))
    wid = note["fm"].get("wikidata entity id")
    if wid:
        lines.append(f"wikidata: {wid}")
    for k, t in note["edges"]:
        lines.append(f"- {k} → [[{t}]]")
    for k, src in note["back"][:15]:
        lines.append(f"- ← [[{src}]] ({k})")
    body = note["body"]
    lines.append(body[:excerpt] + ("…" if len(body) > excerpt else "") if body else "(stub : pas de corps)")
    return "\n".join(lines)


def retrieve(query, k=3, hops=1, notes=None):
    """GraphRAG context: top-k seed notes rendered in full + their n-hop neighbourhood names."""
    notes = notes or load()
    seeds = search(query, k, notes)
    if not seeds:
        return ""
    seen, frontier = set(seeds), set(seeds)
    for _ in range(hops):
        nxt = set()
        for n in frontier:
            note = notes.get(n)
            if note:
                nxt |= {t for _, t in note["edges"]} | {s for _, s in note["back"]}
        frontier = nxt - seen
        seen |= frontier
    parts = [render(notes[s]) for s in seeds]
    around = sorted(seen - set(seeds))
    if around:
        parts.append(f"Voisinage ({hops} saut) : " + ", ".join(f"[[{n}]]" for n in around[:40]))
    return "\n\n".join(parts)


def neighbors(name, depth=1, notes=None):
    notes = notes or load()
    lower = {n.lower(): n for n in notes}
    name = lower.get(name.lower(), name)
    out, frontier, seen = [], {name}, {name}
    for d in range(1, depth + 1):
        nxt = set()
        for n in frontier:
            note = notes.get(n)
            if not note:
                continue
            for k, t in note["edges"]:
                out.append(f"{d}: [[{n}]] —{k}→ [[{t}]]")
                nxt.add(t)
            for k, s in note["back"]:
                out.append(f"{d}: [[{s}]] —{k}→ [[{n}]]")
                nxt.add(s)
        frontier = nxt - seen
        seen |= nxt
    return "\n".join(dict.fromkeys(out)) or f"[[{name}]] : aucune relation (ou hors graphe)."


if __name__ == "__main__":
    notes = load()
    assert "draft document" in search("qu'est-ce qu'une ébauche ?", 3, notes), "alias match broken"
    assert search("zzzz qqqq", 3, notes) == [], "noise query should return nothing"
    ctx = retrieve(" ".join(sys.argv[1:]) or "context engineering avec MCP server", notes=notes)
    print(ctx)
    print("\nself-check OK")
