#!/usr/bin/env python3
"""Migrate graph/ notes to schema.yml (ontology-plan, phase 2).

--dry-run (the only mode for now): writes stats/migration_report.md with, for
each note, what it would become, plus the review queue of `broader` edges,
pre-classified from Wikidata (P279 / P31 / P361) when both ends have a Q-id.
Never writes to graph/. The real migration waits for the user's approval.

Run: .venv-gate/bin/python scripts/migrate.py --dry-run
"""
import collections
import json
import sys
import urllib.parse
import urllib.request

import reason
from validate import SCHEMA, VAULT, as_list, key_action, load, note_key

REPORT = VAULT / "stats" / "migration_report.md"
CACHE = VAULT / "cache" / "broader_classification.json"
RDF_TYPES = {"skos:Concept": "Concept", "Concept": "Concept", "Research Note": "Concept"}

# Verdicts already given by the user (ontology-plan §3.5)
VERDICTS = {
    ("Recursive tree building", "Decision tree"): "kg:methodFor",
    ("Trainer", "hugging face"): "iso-thes:broaderPartitive",
    ("vanilla RAG design", "RAG (Retrieval-Augmented Generation)"): "iso-thes:broaderGeneric",
}


VERDICTS_CI = {(a.lower(), b.lower()): v for (a, b), v in VERDICTS.items()}


def plan_note(name, fm, lower):
    """List of human-readable changes for one note, plus side effects."""
    changes, moved_narrower = [], []
    for k, v in fm.items():
        action, prop = key_action(k)
        if prop == "skos:narrower":
            action = "rename"
        if action == "rename":
            if prop == "skos:narrower":
                for t in reason.parse_targets(v):
                    moved_narrower.append((lower.get(t.lower(), t), name))
                changes.append(f"`{k}` → retiré ; chaque cible reçoit `skos:broader: [[{name}]]`")
            elif k == "wikidata entity id":
                changes.append(f"`{k}: {v}` → `skos:exactMatch: wd:{v}`")
            elif k == "rdf:type":
                changes.append(f"`rdf:type: {v}` → `dcterms:type: {RDF_TYPES.get(str(v), v)}`"
                               + (" (à confirmer : note de recherche)" if v == "Research Note" else ""))
            elif k == "different from":
                changes.append(f"`{k}` → `skos:scopeNote` (« différent de … »)")
            else:
                changes.append(f"`{k}` → `{note_key(prop)}`")
        elif action == "inferred":
            changes.append(f"`{k}` → `inferred/{name}.json`")
        elif action == "closeMatch":
            changes.append(f"`{k}` → `skos:closeMatch`")
        elif action == "cache":
            changes.append(f"`{k}` → `cache/wikidata.jsonl` (fait sur le monde)")
        elif action == "drop":
            changes.append(f"`{k}` → supprimé (maintenance/média Wikidata ou dérivé de PROV)")
        elif action == "outside":
            changes.append(f"`{k}` → **à décider** (hors schéma)")
    return changes, moved_narrower


def broader_edges(notes, lower):
    """(source, target) for every edge that lands on skos:broader by default."""
    edges = set()
    for name, fm in notes.items():
        for k, v in fm.items():
            if key_action(k) == ("rename", "skos:broader") or k == "skos:broader":
                if k == "facet of":
                    continue  # facet of is skos:broader by decision, not in the queue
                for t in reason.parse_targets(v):
                    edges.add((name, lower.get(t.lower(), t)))
    return sorted(edges)


def qid(fm):
    q = str(fm.get("wikidata entity id") or fm.get("skos:exactMatch") or "").replace("wd:", "").strip()
    return q if q.startswith("Q") and q[1:].isdigit() else None


def ask(pattern):
    req = urllib.request.Request(
        "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(f"ASK {{ {pattern} }}"),
        headers={"User-Agent": "knowledge-glossary-migrate/0.1 (ontology migration dry run)"})
    return json.load(urllib.request.urlopen(req, timeout=60))["boolean"]


def classify_wikidata(pairs):
    """{(qa, qb): 'generic'|'instantial'|'partitive'|None} via SPARQL, cached on disk."""
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    todo = [p for p in pairs if f"{p[0]}|{p[1]}" not in cache]
    paths = [("generic", "wdt:P279+"), ("instantial", "wdt:P31/wdt:P279*"), ("partitive", "wdt:P361+")]
    for a, b in todo:  # one small ASK per relation: batched EXISTS queries time out on WDQS
        try:
            cache[f"{a}|{b}"] = next((kind for kind, path in paths if ask(f"wd:{a} {path} wd:{b}")), None)
        except Exception as e:  # leave uncached: rerun to retry, the report says so
            print(f"  Wikidata {a}→{b} non classé ({e.__class__.__name__})", file=sys.stderr)
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True))
    return {tuple(k.split("|")): v for k, v in cache.items()}


def dry_run():
    notes = load()
    lower = {n.lower(): n for n in notes}
    per_note, narrower_moves = {}, []
    stats, outside = collections.Counter(), collections.defaultdict(list)
    for name, fm in notes.items():
        changes, moved = plan_note(name, fm, lower)
        narrower_moves += moved
        if changes:
            per_note[name] = changes
        for k in fm:
            action, prop = key_action(k)
            stats["rename" if prop == "skos:narrower" else action] += 1
            if action == "outside":
                outside[k].append(name)

    edges = broader_edges(notes, lower)
    pairs = {(qid(notes[a]), qid(notes.get(b, {}))) for a, b in edges}
    pairs = sorted(p for p in pairs if all(p))
    wd = classify_wikidata(pairs)
    label = {"generic": "iso-thes:broaderGeneric", "instantial": "iso-thes:broaderInstantial",
             "partitive": "iso-thes:broaderPartitive"}
    queue = []
    for a, b in edges:
        verdict = VERDICTS_CI.get((a.lower(), b.lower()))
        if verdict:
            queue.append((a, b, verdict, "verdict utilisateur"))
            continue
        qa, qb = qid(notes[a]), qid(notes.get(b, {}))
        if qa and qb:
            c = wd.get((qa, qb), "absent")
            why = {"absent": " : requête non aboutie, relancer", None: " : aucun lien P279/P31/P361"}.get(c, "")
            queue.append((a, b, label.get(c, "à classer"), f"Wikidata {qa}→{qb}{why}"))
        else:
            queue.append((a, b, "à classer", "pas de Q-id aux deux extrémités"))

    L = ["# Rapport de migration (à blanc)\n",
         "Produit par `scripts/migrate.py --dry-run`. **Aucune note n'a été modifiée.** "
         "La migration réelle attend ta validation, puis tourne sur une branche, un commit par type de changement.\n",
         "## Synthèse\n", "| Changement | Occurrences |", "|---|---|"]
    names = {"rename": "clé renommée vers le schéma", "keep": "clé déjà conforme", "inferred": "bloc `inferred:` sorti vers `inferred/`",
             "closeMatch": "identifiant externe → `skos:closeMatch`", "cache": "fait sur le monde → cache Wikidata",
             "drop": "supprimé (maintenance, média, dérivé)", "outside": "**hors schéma, à décider**"}
    for action in ["rename", "keep", "inferred", "closeMatch", "cache", "drop", "outside"]:
        L.append(f"| {names[action]} | {stats[action]} |")
    L.append(f"| `skos:narrower` inversé en `skos:broader` sur la cible | {len(narrower_moves)} |")
    L.append(f"\nNotes touchées : **{len(per_note)}** / {len(notes)}.\n")

    counts = collections.Counter(c for c, *_ in [(q[2],) for q in queue])
    L += [f"## File de revue des arêtes `broader` ({len(queue)})\n",
          "Par défaut chaque arête devient `skos:broader` (rangement thématique). Pré-classement : "
          + ", ".join(f"{k} : {v}" for k, v in counts.most_common()) + ".\n",
          "| Source | Cible | Proposition | Fondement |", "|---|---|---|---|"]
    order = {"verdict utilisateur": 0}
    for a, b, prop, why in sorted(queue, key=lambda q: (q[2] == "à classer", order.get(q[3], 1), q[0].lower())):
        L.append(f"| [[{a}]] | [[{b}]] | {prop} | {why} |")

    L += [f"\n## Clés hors schéma ({len(outside)} clés)\n",
          "Décision par clé : la projeter sur une propriété, la mettre en cache, ou la supprimer. "
          "Règle validée : une clé rare n'entre au schéma que si une question de compétence en a besoin.\n",
          "| Clé | Notes |", "|---|---|"]
    for k, ns in sorted(outside.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        L.append(f"| `{k}` | {len(ns)} : " + ", ".join(f"[[{n}]]" for n in ns[:4]) + (" …" if len(ns) > 4 else "") + " |")

    L += ["\n## Détail par note\n"]
    for name, changes in sorted(per_note.items(), key=lambda kv: kv[0].lower()):
        L.append(f"- **[[{name}]]** : " + " ; ".join(changes))
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Rapport : {REPORT.relative_to(VAULT)} — {len(per_note)} notes touchées, "
          f"{len(queue)} arêtes broader en revue ({counts.get('à classer', 0)} à classer), "
          f"{len(outside)} clés hors schéma.")


# ── Real migration (approved 2026-11-22): one step = one commit ──────

STEPS = ["inferred", "rdf-type", "rename", "wikidata", "narrower"]
WIKIDATA_VALUE_KEYS = {"wikidata entity id", "exact match", "different from",
                       "said to be the same as", "equivalent class"}
FM_RE = reason.re.compile(r"^---\n(.*?)\n---", reason.re.DOTALL)


def step_of(key):
    action, prop = key_action(key)
    if action == "inferred":
        return "inferred"
    if key in ("rdf:type", "type"):
        return "rdf-type"
    if prop == "skos:narrower":
        return "narrower"
    if action in ("closeMatch", "cache", "drop") or key in WIKIDATA_VALUE_KEYS:
        return "wikidata"
    if action == "rename":
        return "rename"
    return None


def scalar(v):
    if v is None:
        return ""
    if hasattr(v, "isoformat"):  # dates/datetimes: unquoted ISO, YAML reads them back as dates
        return v.isoformat()
    if isinstance(v, (int, float, bool)):
        return str(v).lower() if isinstance(v, bool) else str(v)
    return json.dumps(str(v), ensure_ascii=False)  # JSON strings are valid YAML double-quoted


def dump_frontmatter(fm):
    lines = []
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f"{k}: []" if not v else f"{k}:\n" + "\n".join(f"  - {scalar(x)}" for x in v))
        else:
            lines.append(f"{k}: {scalar(v)}".rstrip())
    return "\n".join(lines)


def merge(fm, key, value):
    """Add value under key, merging with what is there (list union, order kept)."""
    if key not in fm or fm[key] in (None, [], ""):
        fm[key] = value
        return
    old, new = as_list(fm[key]), as_list(value)
    fm[key] = old + [x for x in new if x not in old]


def log_jsonl(path, note, key, value):
    path.parent.mkdir(exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps({"note": note, "key": key, "value": value}, ensure_ascii=False, default=str) + "\n")


def transform(name, fm, step, notes_fm, lower):
    """Return the new frontmatter dict for one note and one step (may edit other notes for narrower)."""
    out = {}
    for k, v in fm.items():
        if step_of(k) != step:
            merge(out, k, v) if k in out else out.__setitem__(k, v)
            continue
        action, prop = key_action(k)
        if step == "inferred":
            continue  # reason.py writes inferred/<note>.json; regenerated by `reason.py write`
        if step == "rdf-type":
            log_jsonl(VAULT / "cache" / "dropped.jsonl", name, k, v)  # keep the original label
            merge(out, "dcterms:type", RDF_TYPES.get(str(v), v))
        elif step == "rename":
            merge(out, note_key(prop), v)
        elif step == "wikidata":
            if k == "wikidata entity id":
                merge(out, "skos:exactMatch", f"wd:{v}")
            elif k == "different from":
                targets = reason.parse_targets(v) or [str(x) for x in as_list(v)]
                merge(out, "skos:scopeNote", [f"Different from [[{t}]]." for t in targets])
            elif prop in ("skos:exactMatch", "skos:closeMatch") and action != "closeMatch":
                merge(out, prop, v)
            elif action == "closeMatch":
                merge(out, "skos:closeMatch", [x if str(x).startswith("http") else f"{k}: {x}" for x in as_list(v)])
            elif action == "cache":
                log_jsonl(VAULT / "cache" / "wikidata.jsonl", name, k, v)
            elif action == "drop":
                log_jsonl(VAULT / "cache" / "dropped.jsonl", name, k, v)
        elif step == "narrower":
            kept = []
            for t in reason.parse_targets(v):
                target = lower.get(t.lower())
                if target is None:
                    kept.append(f"[[{t}]]")  # no note to carry the inverse: keep as is
                    continue
                merge(notes_fm[target], "skos:broader", [f"[[{name}]]"])
            if kept:
                out[k] = kept
    return out


def run_step(step):
    notes_fm, texts = {}, {}
    for p in sorted(reason.GRAPH_DIR.glob("*.md")):
        texts[p.stem] = p.read_text(encoding="utf-8")
        fm = reason.extract_frontmatter(texts[p.stem])
        notes_fm[p.stem] = dict(fm) if isinstance(fm, dict) else None
    lower = {n.lower(): n for n in notes_fm}
    before = {n: dict(fm) for n, fm in notes_fm.items() if fm is not None}
    for name in list(notes_fm):
        fm = notes_fm[name]
        if fm and any(step_of(k) == step for k in fm):
            notes_fm[name] = transform(name, fm, step, notes_fm, lower)
    changed = 0
    for name, fm in notes_fm.items():
        if fm is None or fm == before.get(name):
            continue
        text = texts[name]
        m = FM_RE.match(text)
        body = text[m.end():] if m else "\n" + text
        new = ("---\n" + dump_frontmatter(fm) + "\n---" + body) if fm else body.lstrip("\n")
        assert (reason.extract_frontmatter(new) or {}) == fm, f"round-trip failed for {name}"  # never corrupt a note
        (reason.GRAPH_DIR / f"{name}.md").write_text(new, encoding="utf-8")
        changed += 1
    print(f"step {step}: {changed} notes written")


if __name__ == "__main__":
    if "--dry-run" in sys.argv:
        dry_run()
    elif "--step" in sys.argv:
        step = sys.argv[sys.argv.index("--step") + 1]
        if step not in STEPS:
            sys.exit(f"step must be one of {STEPS}")
        run_step(step)
    else:
        sys.exit("Usage: migrate.py --dry-run | --step {" + ",".join(STEPS) + "}")
