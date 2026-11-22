---
dcterms:type: "Concept"
skos:altLabel:
  - "lagged scoring"
  - "notation décalée"
skos:broader: "[[feature engineering]]"
skos:related:
  - "[[data leakage]]"
  - "[[Target]]"
  - "[[concept drift]]"
  - "[[Machine Leaning Baseline]]"
---
Train on (what was known at t−1) → outcome at t, then score t+1 by sliding every [[feature]] forward one period into the same columns. The model never sees the outcome it must predict, and the training setup mirrors the real use.

Its weak point: a feature must mean the same thing in both periods. When the source of a column changes between training and scoring, the shift is a [[concept drift]] introduced by hand, to be measured.

Example (union election score, 2026-11): learn (2014 vote, 2018 vote, interactions before 2022) → 2022 vote; score 2026 with (2018 vote, 2022 vote, interactions since 2022).
