---
dcterms:type: Pattern
kg:appliesIn: "[[process capture for a BPM repository]]"
kg:achieves: "[[process models importable into the BPM repository]]"
role:check: "[[audit]]"
role:decider: "[[process owner]]"
role:record: "[[changelog]]"
kg:requiresRole:
  - "check"
kg:hasCondition: "[[member check]]"
kg:hasLimitation: "[[business rule]]"
---
Once the review workshop's decisions are recorded, check every model against the method's rules and propose corrections as a table (element, today, proposed change, rule). Apply what the consultant approves; send what only the [[process owner]] can decide to the decision register; then pass the method's quality gates before validation and import.

Condition: the workshop has happened; auditing before it checks models that are about to change.

Limitation: the audit checks form against written rules; it cannot tell whether a [[business rule]] captured from an expert is true.
