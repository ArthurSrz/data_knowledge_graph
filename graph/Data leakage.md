---
rdf:type: "skos:Concept"
skos:altLabel:
  - "target leakage"
  - "fuite de cible"
skos:broader:
  - "[[feature selection]]"
  - "[[Overfitting]]"
skos:related:
  - "[[Target]]"
  - "[[measurement bias]]"
  - "[[feedback loop bias]]"
---
A [[feature]] leaks when it already "knows" the [[Target]]: it was recorded during or after the event the model must predict. The model then looks excellent on past data and is worthless on the next case, where that information does not exist yet.

Test: could this column have been filled in *before* the outcome? If not, it is out.

Example (union election score, 2026-11): columns filled during the 2022 phone campaign (number of calls, e-mails sent, call outcome) show 91 % of voters when `email_nb = 0` versus 55 % when it is empty. They are excluded from the turnout model, as are older scores derived from the same vote.
