#!/usr/bin/env python3
"""Formal reasoning over the knowledge glossary using Datalog."""

import argparse
import re
import sys
import time
import unicodedata
from pathlib import Path

import yaml

GRAPH_DIR = Path("graph")
STATS_DIR = Path("stats")
REPORT_FILE = STATS_DIR / "reasoning_report.md"

RELATION_MAP = {
    "broader": "broader",
    "skos:broader": "broader",
    "subclass of": "broader",
    "skos:narrower": "narrower",
    "skos:related": "related",
    "related_to": "related",
    "oppositeOf": "opposite_of",
    "uses": "uses",
    "dependencies": "depends_on",
    "studied in": "studied_in",
    "CanBeConstructedWith": "constructed_with",
    "contributing factor of": "contributing_factor",
    "has use": "has_use",
}

INFERRED_PREFIX = "inferred:skos:"

INFERRED_PREDICATES = {
    "ancestor": "ancestor",
    "broader": "broader",
    "narrower": "narrower",
    "related_s": "related",
}

SKOS_RULES = [
    "ancestor(X, Y) :- broader(X, Y)",
    "ancestor(X, Y) :- broader(X, Z), ancestor(Z, Y)",
    "broader(X, Y) :- narrower(Y, X)",
    "narrower(X, Y) :- broader(Y, X)",
    "related_s(X, Y) :- related(X, Y)",
    "related_s(X, Y) :- related(Y, X)",
    "in_cycle(X) :- ancestor(X, X)",
    "conflict(X, Y) :- related_s(X, Y), opposite_of(X, Y)",
    "s27_violation(X, Y) :- related_s(X, Y), ancestor(X, Y)",
]


def slugify(name):
    s = unicodedata.normalize("NFKD", name)
    s = s.encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return f"c_{s}" if s else "c_unnamed"


def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def parse_targets(value):
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    targets = []
    for v in value:
        if not isinstance(v, str):
            continue
        for m in re.finditer(r"\[\[([^\]|#]+)\]\]", v):
            t = m.group(1)
            t = re.sub(r"^graph/", "", t)
            t = re.sub(r"\.md$", "", t)
            targets.append(t.strip())
    return targets


def load_notes(graph_dir):
    notes = {}
    filenames = {}
    parse_errors = []
    unmapped_keys = set()

    for p in sorted(graph_dir.glob("*.md")):
        name = p.stem
        filenames[name.lower()] = name
        fm = extract_frontmatter(p.read_text(encoding="utf-8"))
        if fm is None:
            if p.read_text(encoding="utf-8").startswith("---"):
                parse_errors.append(name)
            notes[name] = {}
            continue
        if not isinstance(fm, dict):
            notes[name] = {}
            continue
        rels = {}
        for key, value in fm.items():
            if key.startswith(INFERRED_PREFIX):
                continue
            canon = RELATION_MAP.get(key)
            if canon is None:
                unmapped_keys.add(key)
                continue
            targets = parse_targets(value)
            if targets:
                rels.setdefault(canon, []).extend(targets)
        notes[name] = rels

    return notes, filenames, parse_errors, unmapped_keys


def build_atom_maps(notes, filenames):
    atom_of = {}
    name_of = {}

    def register(name):
        if name in atom_of:
            return atom_of[name]
        slug = slugify(name)
        if slug in name_of:
            i = 2
            while f"{slug}_{i}" in name_of:
                i += 1
            slug = f"{slug}_{i}"
        atom_of[name] = slug
        name_of[slug] = name
        return slug

    for name in notes:
        register(name)

    for name, rels in notes.items():
        for targets in rels.values():
            for t in targets:
                resolved = filenames.get(t.lower(), t)
                if resolved not in atom_of:
                    register(resolved)

    return atom_of, name_of


def resolve_target(target, filenames):
    return filenames.get(target.lower(), target)


class ReasonerBackend:
    def __init__(self):
        from semantica.reasoning import DatalogReasoner
        self._engine = DatalogReasoner()
        self._fact_count = 0

    def add_fact(self, fact_str):
        self._engine.add_fact(fact_str)
        self._fact_count += 1

    def add_rule(self, rule_str):
        self._engine.add_rule(rule_str)

    def query(self, query_str):
        return self._engine.query(query_str)

    @property
    def fact_count(self):
        return self._fact_count


def load_reasoner(notes, filenames, atom_of):
    engine = ReasonerBackend()
    self_loops = []
    broken_links = []
    note_names = set(notes.keys())

    for name in notes:
        engine.add_fact(f"concept({atom_of[name]})")

    for name, rels in notes.items():
        src = atom_of[name]
        for rel, targets in rels.items():
            for t in targets:
                resolved = resolve_target(t, filenames)
                tgt = atom_of[resolved]
                if src == tgt:
                    self_loops.append((name, rel))
                    continue
                engine.add_fact(f"{rel}({src}, {tgt})")
                if resolved not in note_names:
                    broken_links.append((name, rel, resolved))

    for rule in SKOS_RULES:
        engine.add_rule(rule)

    return engine, self_loops, broken_links


def find_orphans(notes):
    has_edges = set()
    for name, rels in notes.items():
        if rels:
            has_edges.add(name)
        for targets in rels.values():
            for t in targets:
                has_edges.add(t)
    return sorted(set(notes.keys()) - has_edges)


def compute_inferred_facts(engine, notes, filenames, name_of):
    """Return {concept_name: {skos_rel_name: [target_names]}} for write-back."""
    note_names = set(notes.keys())
    inferred = {}

    for pred, skos_name in INFERRED_PREDICATES.items():
        results = engine.query(f"{pred}(?X, ?Y)")
        if not results:
            continue
        for row in results:
            src_name = name_of.get(row["X"])
            tgt_name = name_of.get(row["Y"])
            if not src_name or not tgt_name:
                continue
            if src_name not in note_names:
                continue
            if tgt_name not in note_names:
                continue
            asserted = notes.get(src_name, {})
            if skos_name in asserted and tgt_name in asserted[skos_name]:
                continue
            if pred == "broader" and "broader" in asserted and tgt_name in asserted["broader"]:
                continue
            if pred == "narrower" and "narrower" in asserted and tgt_name in asserted["narrower"]:
                continue
            if pred == "related_s" and "related" in asserted and tgt_name in asserted["related"]:
                continue
            entry = inferred.setdefault(src_name, {})
            entry.setdefault(skos_name, []).append(tgt_name)

    for concept in inferred:
        for rel in inferred[concept]:
            inferred[concept][rel] = sorted(set(inferred[concept][rel]))

    return inferred


def write_inferred_to_notes(inferred, graph_dir):
    """Write inferred facts into note frontmatter as inferred:skos:* keys."""
    written = 0
    for concept, rels in sorted(inferred.items()):
        path = graph_dir / f"{concept}.md"
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8")
        fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)

        if fm_match:
            fm_text = fm_match.group(1)
            body = text[fm_match.end():]
            clean_lines = []
            skip_list = False
            for line in fm_text.split("\n"):
                if line.startswith(INFERRED_PREFIX):
                    skip_list = True
                    continue
                if skip_list and line.startswith("  - "):
                    continue
                skip_list = False
                clean_lines.append(line)

            for rel_name, targets in sorted(rels.items()):
                key = f"{INFERRED_PREFIX}{rel_name}"
                clean_lines.append(f"{key}:")
                for t in targets:
                    clean_lines.append(f'  - "[[{t}]]"')

            new_text = "---\n" + "\n".join(clean_lines) + "\n---" + body
        else:
            # No frontmatter yet — create one
            fm_lines = []
            for rel_name, targets in sorted(rels.items()):
                key = f"{INFERRED_PREFIX}{rel_name}"
                fm_lines.append(f"{key}:")
                for t in targets:
                    fm_lines.append(f'  - "[[{t}]]"')
            new_text = "---\n" + "\n".join(fm_lines) + "\n---\n" + text

        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            written += 1

    return written


def run_query(engine, query_str, atom_of, name_of, raw=False):
    if not raw:
        m = re.match(r"(\w+)\((.+)\)", query_str)
        if m:
            pred = m.group(1)
            raw_args = [a.strip() for a in m.group(2).split(",")]
            converted_args = []
            for a in raw_args:
                if a.startswith("?"):
                    converted_args.append(a)
                else:
                    slug = atom_of.get(a)
                    if slug is None:
                        for name, s in atom_of.items():
                            if name.lower() == a.lower():
                                slug = s
                                break
                    converted_args.append(slug if slug else slugify(a))
            query_str = f"{pred}({', '.join(converted_args)})"

    results = engine.query(query_str)
    if not raw:
        for row in results:
            for k, v in row.items():
                if v in name_of:
                    row[k] = name_of[v]
    return results


def run_reasoning_and_write(quiet=False):
    """Full cycle: load, reason, write inferred facts back. Returns stats."""
    notes, filenames, parse_errors, unmapped = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, self_loops, broken_links = load_reasoner(notes, filenames, atom_of)

    inferred = compute_inferred_facts(engine, notes, filenames, name_of)
    written = write_inferred_to_notes(inferred, GRAPH_DIR)

    total_inferred = sum(len(ts) for rels in inferred.values() for ts in rels.values())
    concepts_touched = len(inferred)

    if not quiet:
        print(f"  {total_inferred} inferred facts across {concepts_touched} concepts, {written} files updated")

    return {
        "total_inferred": total_inferred,
        "concepts_touched": concepts_touched,
        "files_written": written,
    }


def cmd_infer(args):
    notes, filenames, _, _ = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, _, _ = load_reasoner(notes, filenames, atom_of)

    if not SKOS_RULES:
        print("No rules defined in SKOS_RULES. Edit scripts/reason.py to add your Datalog rules.")
        return

    limit = args.limit
    for pred in ["ancestor", "related_s", "narrower", "broader"]:
        results = engine.query(f"{pred}(?X, ?Y)")
        if results:
            print(f"\n{pred}: {len(results)} derived facts")
            for row in results[:limit]:
                x = name_of.get(row["X"], row["X"])
                y = name_of.get(row["Y"], row["Y"])
                print(f"  {x} → {y}")
            if len(results) > limit:
                print(f"  ... ({len(results) - limit} more)")


def cmd_check(args):
    notes, filenames, parse_errors, unmapped = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, self_loops, broken_links = load_reasoner(notes, filenames, atom_of)
    orphans = find_orphans(notes)
    findings = 0

    if parse_errors:
        findings += len(parse_errors)
        print(f"\n⚠ YAML parse errors ({len(parse_errors)}):")
        for n in parse_errors:
            print(f"  {n}.md")

    if self_loops:
        findings += len(self_loops)
        print(f"\n⚠ Self-loops ({len(self_loops)}):")
        for name, rel in self_loops:
            print(f"  {name}: {rel} → itself")

    if broken_links:
        findings += len(broken_links)
        print(f"\n⚠ Broken wikilink targets ({len(broken_links)}):")
        for name, rel, target in broken_links[:20]:
            print(f"  {name}: {rel} → [[{target}]] (no matching note)")
        if len(broken_links) > 20:
            print(f"  ... ({len(broken_links) - 20} more)")

    if orphans:
        findings += len(orphans)
        print(f"\n⚠ Orphan concepts ({len(orphans)}) — no edges in or out:")
        for n in orphans[:20]:
            print(f"  {n}")
        if len(orphans) > 20:
            print(f"  ... ({len(orphans) - 20} more)")

    if SKOS_RULES:
        for check_name, label in [
            ("in_cycle", "Broader cycles (concept is its own ancestor)"),
            ("conflict", "Related + OppositeOf conflicts"),
            ("s27_violation", "SKOS S27 violations (related + hierarchical)"),
        ]:
            results = engine.query(f"{check_name}(?X, ?Y)") if check_name != "in_cycle" else engine.query(f"{check_name}(?X)")
            if results:
                findings += len(results)
                print(f"\n⚠ {label} ({len(results)}):")
                for row in results[:20]:
                    if "Y" in row:
                        x = name_of.get(row["X"], row["X"])
                        y = name_of.get(row["Y"], row["Y"])
                        print(f"  {x} ↔ {y}")
                    else:
                        x = name_of.get(row["X"], row["X"])
                        print(f"  {x}")
    else:
        print("\nNote: No SKOS_RULES defined — skipping cycle/conflict/S27 checks.")

    if unmapped:
        print(f"\nℹ Unmapped frontmatter keys (ignored): {', '.join(sorted(unmapped))}")

    if findings == 0:
        print("\n✓ No issues found.")
    else:
        print(f"\n{findings} total findings.")
        sys.exit(1)


def cmd_query(args):
    notes, filenames, _, _ = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, _, _ = load_reasoner(notes, filenames, atom_of)

    results = run_query(engine, args.query, atom_of, name_of, raw=args.raw)
    if not results:
        print("No results.")
    else:
        print(f"{len(results)} results:")
        for row in results:
            print("  " + ", ".join(f"{k}={v}" for k, v in row.items()))


def cmd_report(args):
    STATS_DIR.mkdir(exist_ok=True)
    notes, filenames, parse_errors, unmapped = load_notes(GRAPH_DIR)
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, self_loops, broken_links = load_reasoner(notes, filenames, atom_of)
    orphans = find_orphans(notes)

    lines = ["# Reasoning Report\n"]

    total_facts = engine.fact_count
    total_concepts = len(notes)
    total_edges = sum(len(t) for rels in notes.values() for t in rels.values())
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Concepts | {total_concepts} |")
    lines.append(f"| Asserted edges | {total_edges} |")
    lines.append(f"| Loaded facts | {total_facts} |")
    lines.append(f"| Rules | {len(SKOS_RULES)} |")

    if SKOS_RULES:
        lines.append(f"\n## Inferred relations\n")
        for pred in ["ancestor", "related_s", "narrower", "broader"]:
            results = engine.query(f"{pred}(?X, ?Y)")
            if results:
                lines.append(f"- **{pred}**: {len(results)} derived facts")

    lines.append(f"\n## Findings\n")

    if parse_errors:
        lines.append(f"### YAML parse errors ({len(parse_errors)})\n")
        for n in sorted(parse_errors):
            lines.append(f"- {n}.md")

    if self_loops:
        lines.append(f"\n### Self-loops ({len(self_loops)})\n")
        for name, rel in sorted(self_loops):
            lines.append(f"- {name}: {rel}")

    if broken_links:
        lines.append(f"\n### Broken wikilink targets ({len(broken_links)})\n")
        for name, rel, target in sorted(broken_links):
            lines.append(f"- {name}: {rel} → [[{target}]]")

    if orphans:
        lines.append(f"\n### Orphan concepts ({len(orphans)})\n")
        for n in sorted(orphans):
            lines.append(f"- {n}")

    if SKOS_RULES:
        for check_name, label in [
            ("in_cycle", "Broader cycles"),
            ("conflict", "Related + OppositeOf conflicts"),
            ("s27_violation", "SKOS S27 violations"),
        ]:
            if check_name == "in_cycle":
                results = engine.query(f"{check_name}(?X)")
            else:
                results = engine.query(f"{check_name}(?X, ?Y)")
            if results:
                lines.append(f"\n### {label} ({len(results)})\n")
                for row in sorted(results, key=lambda r: tuple(r.values())):
                    if "Y" in row:
                        x = name_of.get(row["X"], row["X"])
                        y = name_of.get(row["Y"], row["Y"])
                        lines.append(f"- {x} ↔ {y}")
                    else:
                        x = name_of.get(row["X"], row["X"])
                        lines.append(f"- {x}")

    if unmapped:
        lines.append(f"\n## Unmapped frontmatter keys\n")
        for k in sorted(unmapped):
            lines.append(f"- `{k}`")

    report = "\n".join(lines) + "\n"
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Report written to {REPORT_FILE}")


def cmd_write(args):
    """One-shot: run reasoning and write inferred facts into notes."""
    print("Running reasoning...")
    stats = run_reasoning_and_write()
    print(f"Done. {stats['total_inferred']} inferred facts, {stats['files_written']} files updated.")


def cmd_watch(args):
    """Watch graph/ for changes and continuously re-run reasoning + write-back."""
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    debounce_seconds = args.debounce

    class Handler(FileSystemEventHandler):
        def __init__(self):
            self._last_run = 0

        def on_any_event(self, event):
            if not event.src_path.endswith(".md"):
                return
            # Skip events triggered by our own writes (inferred:skos: changes)
            now = time.time()
            if now - self._last_run < debounce_seconds:
                return
            self._last_run = now
            time.sleep(debounce_seconds)
            self._last_run = time.time()
            ts = time.strftime("%H:%M:%S")
            print(f"\n[{ts}] Change detected, re-running reasoning...")
            try:
                run_reasoning_and_write()
            except Exception as e:
                print(f"  Error: {e}")

    print(f"Watching {GRAPH_DIR}/ for changes (debounce {debounce_seconds}s). Ctrl+C to stop.")
    print("Running initial pass...")
    run_reasoning_and_write()

    handler = Handler()
    observer = Observer()
    observer.schedule(handler, str(GRAPH_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping watcher.")
        observer.stop()
    observer.join()


COMPETENCY_FILE = Path("competency_questions.yml")
COMPETENCY_REPORT = STATS_DIR / "competency_report.md"

MIN_COVERAGE = 5

RELATION_QUESTIONS = {
    "broader": [
        "What is the parent domain of {X}?",
        "What are all subtypes of {X}?",
        "What is the full ancestor chain from {X} to the root?",
        "Which concepts are root concepts (no broader parent)?",
        "What concepts share the same parent domain as {X}?",
    ],
    "narrower": [
        "What are the direct children of {X}?",
    ],
    "related": [
        "What concepts are semantically related to {X}?",
    ],
    "opposite_of": [
        "What is the opposite of {X}?",
    ],
    "uses": [
        "What tools or techniques does {X} use?",
        "Which concepts use {X}?",
    ],
    "has_use": [
        "What are the practical applications of {X}?",
    ],
    "depends_on": [
        "What are the dependencies of {X}?",
    ],
    "contributing_factor": [
        "What does {X} contribute to?",
    ],
    "studied_in": [
        "In what field is {X} studied?",
    ],
    "constructed_with": [
        "What can {X} be constructed with?",
    ],
}

INFERRED_QUESTIONS = {
    "ancestor": [
        "Is {X} a (transitive) specialization of {Y}?",
        "What are all ancestors of {X} up to the root?",
    ],
    "related_s": [
        "What concepts are related to {X} (including symmetric)?",
    ],
    "in_cycle": [
        "Does {X} have a cycle in its broader chain?",
    ],
    "s27_violation": [
        "Is {X} both hierarchically and associatively linked to {Y} (SKOS S27)?",
    ],
    "conflict": [
        "Is {X} both related-to and opposite-of {Y}?",
    ],
}


def get_relation_coverage(notes):
    from collections import Counter
    coverage = {}
    for rel in set(r for rels in notes.values() for r in rels):
        edges = sum(len(rels.get(rel, [])) for rels in notes.values())
        note_count = sum(1 for rels in notes.values() if rel in rels)
        coverage[rel] = {"edges": edges, "notes": note_count}
    return coverage


def cmd_competency(args):
    STATS_DIR.mkdir(exist_ok=True)
    notes, filenames, _, _ = load_notes(GRAPH_DIR)
    coverage = get_relation_coverage(notes)

    lines_out = []
    lines_report = ["# Competency Report\n"]

    # ── Part 1: Auto-discovered questions the graph CAN answer ──────
    lines_out.append("═══ Questions your graph CAN answer ═══\n")
    lines_report.append("## Questions your graph can answer\n")

    can_answer_total = 0
    for rel, questions in sorted(RELATION_QUESTIONS.items()):
        cov = coverage.get(rel)
        if not cov or cov["edges"] < 1:
            continue
        strength = "strong" if cov["notes"] >= MIN_COVERAGE else "weak"
        lines_out.append(f"  {rel} ({cov['edges']} edges, {cov['notes']} notes) [{strength} coverage]:")
        lines_report.append(f"\n### `{rel}` — {cov['edges']} edges across {cov['notes']} notes ({strength})\n")
        for q in questions:
            lines_out.append(f"    ✓ {q}")
            lines_report.append(f"- {q}")
            can_answer_total += 1
        lines_out.append("")

    # Inferred predicates
    atom_of, name_of = build_atom_maps(notes, filenames)
    engine, _, _ = load_reasoner(notes, filenames, atom_of)

    lines_out.append("  Inferred (via Datalog rules):")
    lines_report.append(f"\n### Inferred predicates (via {len(SKOS_RULES)} Datalog rules)\n")
    for pred, questions in sorted(INFERRED_QUESTIONS.items()):
        try:
            if pred == "in_cycle":
                results = engine.query(f"{pred}(?X)")
            else:
                results = engine.query(f"{pred}(?X, ?Y)")
            count = len(results)
        except Exception:
            count = 0
        if count > 0 or pred in ("ancestor", "related_s"):
            lines_out.append(f"    {pred} ({count} derived facts):")
            lines_report.append(f"\n**`{pred}`** — {count} derived facts\n")
            for q in questions:
                lines_out.append(f"      ✓ {q}")
                lines_report.append(f"- {q}")
                can_answer_total += 1
            lines_out.append("")

    # ── Part 2: User-defined competency questions ───────────────────
    if COMPETENCY_FILE.exists():
        cq_data = yaml.safe_load(COMPETENCY_FILE.read_text(encoding="utf-8"))
        user_questions = cq_data.get("questions", [])

        answerable = []
        unanswerable = []

        for q in user_questions:
            requires = q.get("requires", [])
            missing = []
            for req in requires:
                if req in coverage and coverage[req]["notes"] >= MIN_COVERAGE:
                    continue
                elif req in coverage:
                    missing.append(f"{req} (only {coverage[req]['notes']} notes, need {MIN_COVERAGE}+)")
                else:
                    missing.append(f"{req} (not found)")
            if missing:
                unanswerable.append((q, missing))
            else:
                answerable.append(q)

        lines_out.append(f"\n═══ User-defined competency questions ({COMPETENCY_FILE}) ═══\n")
        lines_report.append(f"\n## User-defined competency questions\n")
        lines_report.append(f"\n**{len(answerable)}/{len(user_questions)}** answerable\n")

        if answerable:
            lines_out.append(f"  ✓ Answerable ({len(answerable)}/{len(user_questions)}):\n")
            lines_report.append(f"\n### Answerable ({len(answerable)})\n")
            for q in answerable:
                pri = "!" * q.get("priority", 1)
                lines_out.append(f"    [{pri}] {q['question']}")
                lines_report.append(f"- [{q.get('category', '')}] {q['question']}")
            lines_out.append("")

        if unanswerable:
            lines_out.append(f"  ✗ NOT answerable ({len(unanswerable)}/{len(user_questions)}):\n")
            lines_report.append(f"\n### Not answerable ({len(unanswerable)})\n")
            for q, missing in unanswerable:
                pri = "!" * q.get("priority", 1)
                gaps = ", ".join(missing)
                lines_out.append(f"    [{pri}] {q['question']}")
                lines_out.append(f"         Missing: {gaps}")
                lines_report.append(f"- [{q.get('category', '')}] {q['question']}")
                lines_report.append(f"  - **Gap**: {gaps}")

        lines_out.append(f"\n  Summary: {len(answerable)}/{len(user_questions)} answerable, "
                        f"{len(unanswerable)} gaps to fill")
    else:
        lines_out.append(f"\nNo {COMPETENCY_FILE} found. Create one to define custom competency questions.")

    # ── Part 3: Coverage gaps ───────────────────────────────────────
    all_canonical = set(RELATION_MAP.values())
    unused = all_canonical - set(coverage.keys())
    thin = {r: c for r, c in coverage.items() if c["notes"] < MIN_COVERAGE and r not in unused}

    if unused or thin:
        lines_out.append(f"\n═══ Coverage gaps ═══\n")
        lines_report.append(f"\n## Coverage gaps\n")
        if unused:
            lines_out.append(f"  Relation types with zero edges: {', '.join(sorted(unused))}")
            lines_report.append(f"\n### Unused relation types\n")
            for r in sorted(unused):
                lines_report.append(f"- `{r}`")
        if thin:
            lines_out.append(f"  Thin coverage (<{MIN_COVERAGE} notes):")
            lines_report.append(f"\n### Thin coverage (<{MIN_COVERAGE} notes)\n")
            for r, c in sorted(thin.items(), key=lambda x: x[1]["notes"]):
                lines_out.append(f"    {r}: {c['edges']} edges, {c['notes']} notes")
                lines_report.append(f"- `{r}`: {c['edges']} edges across {c['notes']} notes")

    for line in lines_out:
        print(line)

    report = "\n".join(lines_report) + "\n"
    COMPETENCY_REPORT.write_text(report, encoding="utf-8")
    print(f"\nReport written to {COMPETENCY_REPORT}")


def main():
    parser = argparse.ArgumentParser(description="Formal reasoning over the knowledge glossary")
    sub = parser.add_subparsers(dest="command")

    p_infer = sub.add_parser("infer", help="Show inferred relations")
    p_infer.add_argument("--limit", type=int, default=10)

    sub.add_parser("check", help="Check SKOS consistency")

    p_query = sub.add_parser("query", help="Run a Datalog query")
    p_query.add_argument("query", help='e.g. "ancestor(AI agent, ?X)"')
    p_query.add_argument("--raw", action="store_true", help="Use raw atom names")

    sub.add_parser("report", help="Generate stats/reasoning_report.md")

    sub.add_parser("write", help="One-shot: write inferred facts into notes")

    p_watch = sub.add_parser("watch", help="Watch graph/ and continuously write inferred facts")
    p_watch.add_argument("--debounce", type=float, default=2.0, help="Seconds to wait after a change")

    sub.add_parser("competency", help="Validate competency questions against the vault")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return

    cmds = {
        "infer": cmd_infer, "check": cmd_check, "query": cmd_query,
        "report": cmd_report, "write": cmd_write, "watch": cmd_watch,
        "competency": cmd_competency,
    }
    cmds[args.command](args)


if __name__ == "__main__":
    main()
