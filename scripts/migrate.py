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


if __name__ == "__main__":
    if "--dry-run" not in sys.argv:
        sys.exit("Seul --dry-run est disponible : la migration réelle attend la validation du rapport.")
    dry_run()
