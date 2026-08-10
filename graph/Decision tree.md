---
foundationalPaper: Induction of Decision Trees (Quinlan, 1986)
keyPapers:
  - "C4.5: Programs for Machine Learning (Quinlan, 1993)"
  - Classification and Regression Trees (Breiman et al., 1984)
  - Experiments in Induction (Hunt, Marin & Stone, 1966)
typeOf: "[[Supervised learning]] algorithm"
usedFor:
  - "[[classification]]"
  - "[[Regression]]"
components:
  - "[[Root node]]"
  - "[[Internal nodes]]"
  - "[[Leaf nodes]]"
  - "[[Branches]]"
algorithms:
  - "[[ID3]]"
  - "[[C4.5]]"
  - "[[CART]]"
  - "[[CHAID]]"
extendedBy:
  - "[[Random forest]]"
  - "[[Gradient boosting trees]]"
broader: "[[supervised learning]]"
inferred:skos:ancestor:
  - "[[machine learning]]"
  - "[[supervised learning]]"
inferred:skos:narrower:
  - "[[Recursive tree building]]"
  - "[[Regression trees]]"
  - "[[Tree depth]]"
---

# Decision Tree

Decision trees were developed incrementally through the work of Hunt (CLS algorithm, 1960s), Breiman (CART, 1984), and Quinlan (ID3/C4.5, 1986-1993).

## Original Definition

From Quinlan (1986) in "Induction of Decision Trees":
"The decision tree is a classification method that has been receiving increasing attention... A decision tree consists of nodes that form a rooted tree, meaning it is a directed tree with a node called 'root' that has no incoming edges. All other nodes have exactly one incoming edge."

From Breiman et al. (1984) in CART:
"A tree structured classifier consists of a sequence of questions, the answer to each question determining what question is asked next. Finally a leaf is arrived at, and associated with the leaf is a class label."

## Historical Development

1. **CLS (Hunt et al., 1966)**: Concept Learning System
2. **CART (Breiman et al., 1984)**: Classification And Regression Trees
3. **ID3 (Quinlan, 1986)**: Iterative Dichotomiser 3
4. **C4.5 (Quinlan, 1993)**: Enhanced version of ID3

## Core Algorithm (ID3)

From Quinlan's original algorithm:
1. Select attribute with highest information gain
2. Create branch for each value of that attribute
3. Recursively build tree for each branch
4. Stop when all instances in a node belong to same class

## Splitting Criteria

ID3/C4.5 use Information Gain:
IG(S,A) = Entropy(S) - Σᵥ (|Sᵥ|/|S|) × Entropy(Sᵥ)

CART uses Gini impurity:
Gini(S) = 1 - Σᵢ pᵢ²

Where pᵢ is the probability of class i.

## Key Innovations

From Quinlan (C4.5):
- Handling continuous attributes
- Dealing with missing values
- Pruning to avoid overfitting
- Converting trees to rules

From Breiman (CART):
- Binary splits only
- Regression tree capability
- Cost-complexity pruning
- Surrogate splits for missing values

## Historical Significance

Decision trees revolutionized machine learning by:
- Providing interpretable models
- Handling both categorical and numerical data
- Requiring minimal data preparation
- Enabling automatic feature selection
- Forming foundation for ensemble methods

As Quinlan noted: "Decision trees have a number of advantages over other learning methods. They are easy to understand, can handle both numeric and categorical data, and the resulting classification model is a simple tree structure that can be interpreted by domain experts."

## Modern Impact

Decision trees became fundamental to:
- Random forests (Breiman, 2001)
- Gradient boosting machines (Friedman, 2001)
- Interpretable AI systems
- Business rule extraction
- Medical diagnosis systems
