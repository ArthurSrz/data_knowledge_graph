---
iso-thes:broaderGeneric: "[[Metadata management]]"
skos:exactMatch: "wd:Q1172162"
skos:broader: "[[data]]"
skos:related: "[[single source of truth]]"
---
**[[data]] lineage** refers to the [[process]] of tracking how [[data]] is generated, transformed, transmitted and used across systems over time. It documents [[data]]'s origins, transformations and movements, providing detailed [[visibility]] into its life cycle. This [[process]] simplifies the identification of errors in [data analytics](https://en.wikipedia.org/wiki/Analytics "Analytics") workflows, by enabling users to trace issues back to their root causes

![[lineage.png]]

## Lineage has to be *visible to the business owner*, not just recorded

A lineage that only the engineer can read does not answer the owner's real question, which is "is the tool using *my* file, and how do I change it?".

**Example (Bom Bom Boom, 2026-11-23).** The purchasing BOM travels Google Sheet tab → BigQuery external table (`bom_produit_sheet`, read with the requester's Drive rights) → hourly native copy (`bom_produit`) → BBB. When asked "which sheet does BBB read?", `bbb_status` only showed the BigQuery copy, so the link to the sheet was invisible. Fix: point the owner at the one hop that names the source (the external table's *Details* tab) and give them a saved query that swaps it. That one table is the BOM's [[single source of truth]].

Two lessons:
- Name the **hop where the source is declared**, not the last table in the chain.
- An indirection added for access reasons (the service account cannot receive a Drive share) moves the source out of sight; compensate by surfacing it.

Not the same as [[Provenance]]: lineage follows data *between systems*; provenance says where a *statement* (a price, a rule) comes from and on what assumptions.
