---
wikidata entity id: Q1469824
subclass of:
  - "[[knowledge organization system]]"
  - "[[vocabulary]]"
  - "[[data set]]"
has part:
  - "[[preferred term]]"
  - "[[non-preferred term]]"
  - "[[subject heading]]"
exact match: http://purl.org/spar/fabio/ControlledVocabulary
inferred:skos:ancestor:
  - "[[knowledge organization system]]"
inferred:skos:narrower:
  - "[[thesaurus]]"
---
**Controlled vocabulary**: standardized, organized set of words and phrases for retrieving and disambiguating information, which separates preferred from non-preferred terms.

The [[Signavio]] Dictionary is one: every BPMN lane, pool, system and KPI must link to an existing entry. Clara's register applies the rule that a similar title doesn't make two terms equivalent: "Customer Service Manager" isn't an order-taking role until someone maps it explicitly. A local alias goes in Documentation as a non-preferred term. A new term goes through a *sandbox* (candidate terms pending review), and who reviews it and how often is still open.

My own graph is the same kind of object: Wikidata QIDs as the authority, `skos:altLabel` as non-preferred terms, `skos:scopeNote` for my usage.
