---
rdf:type: "skos:Concept"
skos:altLabel:
  - "probability calibration"
  - "reliability"
skos:broader: "[[model fit]]"
skos:related:
  - "[[Probability]]"
  - "[[Odds]]"
  - "[[Logit link function]]"
  - "[[confusion matrix]]"
---
A model is calibrated when its probabilities can be read as frequencies: among the people it gives 70 %, about 70 % do the thing. Ranking well ([[True Positive Rate (Recall)]], AUC) does not imply calibration, and a product of two scores only reads as a [[Probability]] if each factor is calibrated.

Check: sort predictions into ten bins and compare, bin by bin, the predicted share with the observed share (reliability table).

Example (union election score, 2026-11): predicted versus observed turnout by decile, then predicted versus actual number of voters per département.
