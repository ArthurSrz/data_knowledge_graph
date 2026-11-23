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

Hidden breach: the *address* of the source is stored in two places that both look authoritative (e.g. an environment variable and a warehouse table definition), but only one is actually used because it takes precedence. Whoever edits the other one changes nothing. Tell the owner which one counts (see [[data lineage]]).
