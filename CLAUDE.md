# CLAUDE.md

## Learnings

### Chart scaling: use smart y-axis limits, not starting from 0

When plotting time-series data with matplotlib (e.g. `stats/chart.png`), don't start y-axes from 0 — it squishes trends to the top and hides day-to-day progression. Instead, use smart scaling that zooms into the data range with padded, rounded margins. See `smart_ylim()` in `scripts/count_richness.py`.

Also always disable matplotlib's offset/scientific notation (`ax.ticklabel_format(useOffset=False, style='plain')`) so tick labels show actual values like 1770, not `-1.0` with a `+1.77e3` offset.

### Modeling conventions (enforced by the logic gate)

Every write to `graph/` goes through `scripts/reason.py gate`: the PreToolUse/Stop hooks (`scripts/hooks/kg-gate.py`), the `kg_upsert_concept` MCP tool, and the `kg-gate` CI workflow all call it. Only *new* logical violations count (cycles, SKOS S27, opposites, disjointness, instance/subclass crossing, part-whole cycles). Decisions are logged in `stats/gate-log.md`; current violations are in `stats/violations.md`. Mode: `KG_GATE=warn|block|off` (off is logged).

- **Keys follow `schema.yml`** (prefixed): `iso-thes:broaderGeneric` (is a kind of, Wikidata P279), `iso-thes:broaderInstantial` (instance of, P31), `iso-thes:broaderPartitive` (part of, P361), `has part`, `skos:broader` (thematic shelving only), `skos:related` and its sub-properties (`kg:uses`, `kg:oppositeOf`, `kg:accountableFor`…), `skos:exactMatch: wd:Q…`. Inferred facts live in `inferred/<note>.json`, never in notes. `scripts/validate.py` flags keys outside the schema.
- **Occurrent or continuant first.** Before any `iso-thes:broaderGeneric` link, decide which BFO branch the concept is on. The two branches are disjoint.
- **Cross-branch links are transversal relations, not hierarchy.** A role (continuant) linked to a process (occurrent) takes `kg:accountableFor`, `kg:uses`, `kg:hasUse`… never `iso-thes:broaderGeneric` (see `process owner`).
- **Check Wikidata** (P279 / P31) before asserting a hierarchy, and keep `iso-thes:broaderInstantial` apart from `iso-thes:broaderGeneric`.
- **Record deviations in `skos:scopeNote`** whenever a link departs from Wikidata or from a strict reading.
- When the gate refuses, revise the relations (belief revision): don't force the link through.
