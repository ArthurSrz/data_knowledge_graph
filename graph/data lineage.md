---
iso-thes:broaderGeneric: "[[Metadata management]]"
skos:exactMatch: "wd:Q1172162"
skos:broader: "[[data]]"
skos:related: "[[single source of truth]]"
---
**[[data]] lineage** refers to the [[process]] of tracking how [[data]] is generated, transformed, transmitted and used across systems over time. It documents [[data]]'s origins, transformations and movements, providing detailed [[visibility]] into its life cycle. This [[process]] simplifies the identification of errors in [data analytics](https://en.wikipedia.org/wiki/Analytics "Analytics") workflows, by enabling users to trace issues back to their root causes

![[lineage.png]]

## Lineage has to be *visible to the business owner*, not just recorded

A lineage that only the engineer can read does not answer the owner's real question: "is the tool using *my* file, and how do I change it?".

Typical case: a spreadsheet tab → a warehouse external table that reads it → a scheduled native copy → the application. If the application's status only shows the last copy, the link to the spreadsheet is invisible to the person who maintains it.

Two lessons:
- Name the **hop where the source is declared**, not the last table in the chain, and give the owner a way to change it there.
- An indirection added for access reasons (e.g. a [[service account]] that can't receive a share) moves the source out of sight; compensate by surfacing it.

Not the same as [[Provenance]]: lineage follows data *between systems*; provenance says where a *statement* (a price, a rule) comes from and on what assumptions.
