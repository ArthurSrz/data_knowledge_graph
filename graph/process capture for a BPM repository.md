---
dcterms:type: Situation
iso-thes:broaderGeneric: "[[tacit knowledge spread across expert profiles]]"
skos:related:
  - "[[business process mapping]]"
  - "[[Business Process Model and Notation]]"
  - "[[controlled vocabulary]]"
  - "[[enterprise architecture]]"
  - "[[process owner]]"
---
Sub-situation of [[tacit knowledge spread across expert profiles]]: an organisation captures its as-is processes from documents and expert interviews, and the resulting [[Business Process Model and Notation]] models must be imported into a corporate BPM repository (e.g. [[Signavio]]) that already has its own method and vocabulary.

Constraints specific to it:
- Every lane, pool, system and KPI must link to an entry of the repository's [[controlled vocabulary]]; a similar name is not a match, and a proposed term waits in the [[sandbox]].
- IT systems come only from the [[enterprise architecture]] repository; a missing one is requested, never invented.
- The method caps the size of a diagram (a task limit per model, one process level per diagram), so a large process must be split and linked.
- Tool round-trips lose data: what an import parser drops (e.g. BPMN extension elements) must be written where it survives, such as the element's documentation.
- Only the [[process owner]] can settle disagreements between experts; nothing becomes a rule until they do.
