---
skos:exactMatch: "wd:Q7523885"
iso-thes:broaderInstantial: "[[best practice]]"
skos:broader: "[[data management]]"
iso-thes:broaderGeneric: "[[source of information]]"
kg:uses:
  - "[[data deduplication]]"
  - "[[canonicalization]]"
skos:altLabel:
  - "SSoT"
  - "SSOT"
---
**Single source of truth**: information-systems practice of normalising data by using one source for each data element.

In a knowledge store, an agent applies it by updating the one existing draft rather than adding parallel alternatives next to it. It's breached when several registers (a working table, a decision register, an older review brief) show different statuses for the same gap, which is the drift to watch.

**Example (Bom Bom Boom, 2026-11-23).** One sheet tab is the only source for the BOM structure, but its address lived in two places: a Railway variable (unused, because the BigQuery table takes precedence) and the BigQuery external table (actually used). Two places that look authoritative and only one that is = a hidden SSoT breach. The owner must be told which one counts (see [[data lineage]]).
