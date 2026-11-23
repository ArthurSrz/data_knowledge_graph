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

**Example (Bom Bom Boom, 2026-11-23).** Every AI price estimate is an event in the append-only log (`cout.estime`, e.g. `evt_12272`). It stores the assumed material and €/kg per lot size, assumed dimensions and mass, tolerances, process per lot size, investment, model, date and a **confidence score** (0.2 here, because the 2D drawing was not read: `plan_lu: false`). The spreadsheet shows only the cost breakdown; querying the event returns every assumption. A correction never overwrites: it emits a new event that points to the old one.

Consequence: an estimate without its event is not a price, it is a number. And a low-confidence estimate is not a [[ground truth]]: the missing input (here, Drive access to the drawings) is what limits it, not the model.
