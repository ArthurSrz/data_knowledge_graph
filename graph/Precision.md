---
leadsTo:
  - "[[Ground truth]]"
same:
  - "[[variance]]"
meanTo: "[[communicate uncertainty]]"
broader: "[[Evaluation metrics]]"
inferred:skos:ancestor: "[[Evaluation metrics]]"
---
Of **all** the predicted positives, how many were actually positives. Ratio of [[True Positive (TP)]] divided by the sum of [[True Positive (TP)]] and [[False positives]]. 

Optimizing precision means making sure we get the right answers even if it involves leaving out a few right answers. We minimize the number of wrong answers. 

During the [[evaluation]] phase of the [[CRISP-DM Process]], there is a tradeoff between the precision and the [[Accuracy 1]]

Statisticians prefer the term [[variance]].



## Related concepts (Adamic-Adar connections)

- [[Recall]] - Complementary metric (Adamic-Adar: 1.072)
- [[F1 Score]] - Harmonic mean of precision and recall (Adamic-Adar: 1.072)
- [[confusion matrix]] - Source of precision calculation
- [[True Positive (TP)]] - Used in precision formula
- [[False Positive (FP)]] - Used in precision formula
