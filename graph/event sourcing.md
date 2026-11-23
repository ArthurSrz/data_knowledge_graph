---
skos:exactMatch: "wd:Q17349088"
skos:related:
  - "[[audit trail]]"
  - "[[activity log]]"
  - "[[data lineage]]"
  - "[[Provenance]]"
---
architecture [[pattern]] where the state of a system is never stored directly. Each [[change]] is recorded as an immutable event in an append-only [[log]], and the current state is a *projection* rebuilt by replaying the events.

