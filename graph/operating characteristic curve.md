---
described by source: "[[graph/ISO 3534-2_2006(en) Statistics — Vocabulary and symbols — Part 2_ Applied statistics]]"
Commons category: "Operating characteristics"
wikidata entity id: "Q1517752"
---
Curve showing how a decision rule performs as its threshold is varied. Its [[best]]-known case is the [[receiver operating characteristics|ROC curve]], used to evaluate binary classifiers in [[graph/machine learning]].

## The ROC story, simply told (spam filter)

A spam filter gives every email a score from 0 to 100: how spammy it looks. You pick a **cutoff**: everything scoring above it goes to the spam folder.

Where do you put the cutoff?
- **High cutoff** → hardly anything is flagged. Normal emails are safe, but lots of spam slips through.
- **Low cutoff** → almost all spam is caught, but some normal emails land in spam by mistake.

The ROC curve shows all these choices in one picture. For each cutoff, it asks two questions:
1. **How much of the spam did I catch?** → up–down axis (true positive rate)
2. **How many normal emails did I wrongly flag?** → left–right axis ([[false positive rate]])

Toy example: 10 emails, 5 spam and 5 normal.

| Email | Score |
|---|---|
| Spam | 95 |
| Spam | 85 |
| Normal | 80 |
| Spam | 70 |
| Spam | 55 |
| Normal | 50 |
| Normal | 40 |
| Spam | 30 |
| Normal | 20 |
| Normal | 10 |

- Cutoff **100** → nothing flagged → catch 0% spam, 0% mistakes → bottom-left corner.
- Cutoff **60** → 3 of 5 spam caught (60%), 1 of 5 normal flagged (20%) → point (20%, 60%).
- Cutoff **0** → everything flagged → 100% spam caught, but 100% mistakes → top-right corner.

Put a dot for every cutoff, join them: that line is the **ROC curve**.

**How to read it**
- Curve hugging the **top-left corner** → good filter: catches spam without many mistakes.
- Curve along the **diagonal** → useless filter, no better than a coin flip.

**AUC** ("area under the curve") is one number summing up the whole curve: **1.0 = perfect**, **0.5 = coin flip**.
