---
rdf:type: skos:Concept
skos:altLabel:
  - quantile cut
  - découpage par quantiles
  - rank-based labelling
skos:broader:
  - "[[Threshold value]]"
  - "[[feature engineering]]"
skos:related:
  - "[[heuristic]]"
  - "[[Hyperparameters]]"
  - "[[discrimination threshold]]"
  - "[[calibration]]"
inferred:skos:ancestor:
  - "[[Threshold value]]"
  - "[[feature engineering]]"
---
Turning a continuous score into classes by fixing the *share* of each class (bottom 30 %, middle 40 %, top 30 %) instead of fixing a [[Threshold value]] on the score. The cut points are then read off the data, group by group.

What it buys: every group gets the same mix of classes, whatever its level. What it costs: a class is a **rank inside the group**, not a level. The same score can get two different labels in two groups, and the bottom class is never empty, even when everyone is good.

The shares are not learned: they are a [[heuristic]], closer to [[Hyperparameters]] than to a model output, and should be set from how the classes will be *used* (capacity to act on the top or to drop the bottom), not from the data.

Example (union election score, 2026-11): letters A/B/C cut 30/40/30 inside each département, kept as an acknowledged arbitrary convention; only the share of C really matters, because it decides who is not called.
