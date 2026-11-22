---
rdf:type: "skos:Concept"
skos:altLabel:
  - "grouped cross validation"
  - "validation croisée par groupes"
skos:broader: "[[cross validation]]"
skos:related:
  - "[[N-Fold Cross Validation]]"
  - "[[Overfitting]]"
  - "[[data leakage]]"
---
[[N-Fold Cross Validation]] where all rows of a group (a patient, a school, a département) stay in the same fold. Each group is judged by a model that never saw it, so the score measures generalisation to *new groups* rather than to new rows of known groups.

Use it when rows of a group resemble each other or share a context the model could memorise.

Example (union election score, 2026-11): each département's 2022 turnout is predicted by a model trained on the other départements.
