---
dcterms:type: Pattern
kg:appliesIn: "[[shared rules across knowledge stores]]"
kg:achieves: "[[one rule set shared by every store]]"
role:source: "[[single source of truth]]"
role:reader: "[[skills]]"
role:container: "[[knowledge base]]"
kg:requiresRole:
  - "source"
  - "reader"
kg:hasCondition: "[[knowledge base]]"
kg:hasLimitation: "[[information retrieval]]"
---
A reusable instruction (a skill) names the master store and the artifacts it must read (rule list, templates, roles), and fetches them at each run through the store link, instead of carrying a copy. Findings that concern the method are written back to the master.

Condition: the dependent store is linked to the master and the needed content is shared.

Limitation: reading through a link is slower and limited to what is shared (search, not always navigation tools or templates), so a rule-heavy task can take minutes; share the master's navigation tools when speed matters.
