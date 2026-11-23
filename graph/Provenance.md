---
skos:exactMatch:
  - "wd:Q1773840"
  - "http://purl.org/dc/terms/provenance"
iso-thes:broaderGeneric:
  - "[[chronology]]"
  - "[[documentation]]"
skos:broader: "[[authentication]]"
skos:definition: "chronology of the ownership, custody or location of a historical object or economic good"
skos:scopeNote: "My usage: the provenance of a *statement* in a knowledge store — which interview, document chunk or decision it comes from, and who said it. Wikidata's sense is the custody chain of an object; dcterms:provenance (its exact match) already widens it to any resource. Not [[Data lineage]], which tracks data moving between systems."
---
In a Clarifeye store, provenance is what lets [[tacit knowledge]] become [[explicit knowledge]] without losing its weight: the artifact states the [[business rule]] impersonally, and the source link (interview turn, document chunk) carries who said it.

Rule: names stay out of method and rule text (state the rule, not "the expert reports…"); attribution stays in the register's evidence and decision fields and in the link. Cite the dedicated chunk (e.g. one section of a handbook), not the whole document.

Risk: an impersonal sentence reads as a [[normative statement]] even when it rests on one [[positive statement]] by one person. The link is the only thing keeping the single-source status visible.

Complements the [[audit trail]] (who edited) and rests on [[documentary evidence]].

## Provenance of a machine-made statement: the AI estimate

When the statement is produced by a model rather than a person, provenance must carry the **assumptions**, not just the source.

Pattern: each AI estimate (e.g. a part's cost) is recorded as an event in an append-only log ([[event sourcing]]). The event stores every assumption (material and unit price, dimensions and mass, tolerances, process, investment), the model, the date, and a **confidence score**. The table users see shows only the result and its breakdown; querying the event returns the full reasoning. A correction never overwrites: it adds a new event that points to the old one.

Consequence: an estimate without its event is not a price, it is a number. A low-confidence estimate is not a [[ground truth]]; when confidence is low because an input was missing (e.g. the technical drawing could not be read), the fix is access to the input, not a better model.

## Training material is not provenance

A training module or onboarding deck shows how a tool or process is *taught*, not how it is *practised today*. In a store it goes in its own collection, described as a lead to confirm with a [[subject-matter expert]], never cited as the source of a step, a [[business rule]] or a RACI assignment. See [[training]].

Audit method, to prove no artifact cites an excluded document:
1. List the document's chunk ids (document outline) and match every reference link in every artifact against them, plus the document id.
2. Search the document names and their short forms.
3. Read the **abbreviation legends**: a legend defining a short form ("Tool = training module 2026") turns every "Tool p.X" in that artifact into a citation. Another artifact reusing the same short form without a legend may mean a different document; check the page numbers against both before flagging it.

When the excluded document was the **only** source, do not leave the statement unsourced: keep it, marked "to confirm with <role>", so it does not read as a [[normative statement]]. A gap phrased as "the training says X, practice says Y" loses one side: rewrite it from the remaining sources.
