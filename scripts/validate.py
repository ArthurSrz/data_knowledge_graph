#!/usr/bin/env python3
"""Validate graph/ notes against schema.yml (ontology-plan, phase 2). Read-only.

Reports: keys outside the schema, domain/range violations, duplicates
(same exactMatch, label conflicts, case), SKOS integrity S13, S14, S27.
Run: .venv-gate/bin/python scripts/validate.py   (exit 1 if findings)
"""
import collections
import subprocess
import sys
from pathlib import Path

import yaml

import reason

VAULT = reason.VAULT
SCHEMA = yaml.safe_load((VAULT / "schema.yml").read_text(encoding="utf-8"))
NOTE_TYPES = {"skos:Concept": "Concept", "Concept": "Concept", "Research Note": "Concept"}


def key_action(key):
    """How the schema treats a frontmatter key: (action, canonical property or None).
    action ∈ keep, rename, closeMatch, cache, drop, inferred, outside."""
    props, wd = SCHEMA["properties"], SCHEMA["wikidata"]
    if key.startswith("inferred:"):
        return "inferred", None
    if key.startswith("role:") or key in SCHEMA["passthrough"]:
        return "keep", None
    for name, p in props.items():
        if key == p.get("noteKey"):
            return "keep", name
    if key in props:
        return ("rename" if props[key].get("noteKey") else "keep"), key
    if key in wd["translate"]:
        return "rename", wd["translate"][key]
    for name, p in props.items():
        if key in p.get("aliases", []):
            return "rename", name
    if key in wd["to_close_match"]:
        return "closeMatch", "skos:closeMatch"
    if key in wd["to_cache"]:
        return "cache", None
    if key in wd["drop"] or key in SCHEMA["derived_not_written"]:
        return "drop", None
    return "outside", None


def note_key(prop):
    """Key written in notes for a canonical property (noteKey overrides the prefixed name)."""
    return SCHEMA["properties"].get(prop, {}).get("noteKey", prop)


def load():
    """{name: frontmatter dict} for every note (empty dict if none/invalid)."""
    out = {}
    for p in sorted(reason.GRAPH_DIR.glob("*.md")):
        fm = reason.extract_frontmatter(p.read_text(encoding="utf-8"))
        out[p.stem] = fm if isinstance(fm, dict) else {}
    return out


def as_list(v):
    return v if isinstance(v, list) else ([] if v is None else [v])


def note_type(fm):
    t = fm.get("dcterms:type") or fm.get("rdf:type") or "Concept"
    return NOTE_TYPES.get(t, t)


def check(notes):
    findings = collections.defaultdict(list)
    lower = {n.lower(): n for n in notes}

    # 1. keys outside the schema
    for name, fm in notes.items():
        for k in fm:
            if key_action(k)[0] == "outside":
                findings["Clés hors schéma"].append(f"{name}: `{k}`")

    # 2. domain / range (only for properties that declare classes)
    classes = set(SCHEMA["classes"])
    for name, fm in notes.items():
        for k, v in fm.items():
            action, prop = key_action(k)
            spec = SCHEMA["properties"].get(prop or "", {})
            dom, rng = spec.get("domain"), spec.get("range")
            if dom in classes and note_type(fm) != dom:
                findings["Violations de domaine"].append(f"{name} ({note_type(fm)}): `{k}` attend {dom}")
            if rng in classes:
                for t in reason.parse_targets(v):
                    target = notes.get(lower.get(t.lower(), ""), None)
                    if target is not None and note_type(target) != rng:
                        findings["Violations de portée"].append(f"{name}: `{k}` → [[{t}]] ({note_type(target)}), attend {rng}")

    # 3. duplicates
    by_q = collections.defaultdict(list)
    for name, fm in notes.items():
        for q in as_list(fm.get("wikidata entity id")) + as_list(fm.get("skos:exactMatch")):
            by_q[str(q).replace("wd:", "")].append(name)
    for q, names in sorted(by_q.items()):
        if len(names) > 1:
            findings["Doublons : même exactMatch"].append(f"{q}: " + ", ".join(names))
    for name, fm in notes.items():
        for alt in as_list(fm.get("skos:altLabel")):
            other = lower.get(str(alt).lower())
            if other and other != name:
                findings["Doublons : altLabel = nom d'une autre note"].append(f"{name}: altLabel '{alt}' = [[{other}]]")
    tracked = subprocess.run(["git", "-C", str(VAULT), "ls-files", "-z", "graph/"],
                             capture_output=True, text=True).stdout.split("\0")
    tracked = [Path(t).stem for t in tracked if t.endswith(".md")]
    groups = collections.defaultdict(list)
    for t in tracked:
        groups[t.lower()].append(t)
    for names in groups.values():
        if len(names) > 1:
            findings["Doublons : casse (git)"].append(" / ".join(names))
    for t in tracked:
        disk = lower.get(t.lower())
        if disk and disk != t:
            findings["Doublons : casse (git ≠ disque)"].append(f"git `{t}` / disque `{disk}`")
    linked = collections.defaultdict(set)
    for name, fm in notes.items():
        for v in fm.values():
            for t in reason.parse_targets(v):
                real = lower.get(t.lower())
                if real and real != t:
                    linked[f"[[{t}]] → {real}"].add(name)
    for k, srcs in sorted(linked.items()):
        findings["Doublons : liens qui ne diffèrent que par la casse"].append(f"{k} (depuis {', '.join(sorted(srcs)[:3])})")

    # 4. SKOS integrity
    for name, fm in notes.items():
        pref = as_list(fm.get("skos:prefLabel")) or [name]
        alts = {str(a).lower() for a in as_list(fm.get("skos:altLabel"))}
        if {str(p).lower() for p in pref} & alts:  # S13: prefLabel and altLabel are disjoint
            findings["SKOS S13 (prefLabel ∩ altLabel)"].append(name)
        if len(as_list(fm.get("skos:prefLabel"))) > 1:  # S14: one prefLabel per language
            findings["SKOS S14 (plusieurs prefLabel)"].append(name)
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        violations, _, _ = reason.logic_violations()
    for kind, x, y in sorted(violations):
        if kind == "s27_violation":
            findings["SKOS S27 (related + hiérarchique)"].append(f"{x} ↔ {y}")
    return findings


def main():
    findings = check(load())
    total = sum(map(len, findings.values()))
    for label, items in findings.items():
        print(f"\n⚠ {label} ({len(items)}):")
        for i in items[:15]:
            print(f"  {i}")
        if len(items) > 15:
            print(f"  … ({len(items) - 15} de plus)")
    print(f"\n{total} constat(s)." if total else "\n✓ Conforme au schéma.")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
