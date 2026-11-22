---
skos:exactMatch:
  - "wd:Q1469824"
  - "http://purl.org/spar/fabio/ControlledVocabulary"
iso-thes:broaderGeneric:
  - "[[knowledge organization system]]"
  - "[[vocabulary]]"
  - "[[data set]]"
has part:
  - "[[preferred term]]"
  - "[[non-preferred term]]"
  - "[[subject heading]]"
---
**Controlled vocabulary**: standardized, organized set of words and phrases for retrieving and disambiguating information, which separates preferred from non-preferred terms.

A BPM tool's dictionary (e.g. the [[Signavio]] Dictionary) is one: every BPMN lane, pool, system and KPI must link to an existing entry. A knowledge store applies the rule that a similar title doesn't make two terms equivalent: two role names are only the same role once someone maps them explicitly. A local alias is kept as a non-preferred term, and a new term goes through a review step before it becomes preferred.

My own graph is the same kind of object: Wikidata QIDs as the authority, `skos:altLabel` as non-preferred terms, `skos:scopeNote` for my usage.
