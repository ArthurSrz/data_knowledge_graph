---
foundationalPaper: A Training Algorithm for Optimal Margin Classifiers (Boser, Guyon & Vapnik, 1992)
keyPapers:
  - Support-Vector Networks (Cortes & Vapnik, 1995)
  - The Nature of Statistical Learning Theory (Vapnik, 1995)
typeOf: "[[Supervised learning algorithm]]"
usedFor:
  - "[[classification]]"
  - "[[Regression]]"
relatedTo:
  - "[[Kernel methods]]"
  - "[[Margin]]"
  - "[[Hyperplane]]"
  - "[[Support vectors]]"
inspiredBy: "[[Statistical learning theory]]"
broader: "[[supervised learning]]"
inferred:skos:ancestor:
  - "[[machine learning]]"
  - "[[supervised learning]]"
---

# Support Vector Machine (SVM)

Support Vector Machines were developed by Vladimir Vapnik and colleagues at AT&T Bell Laboratories in the early 1990s, building on Vapnik's earlier work on statistical learning theory.

## Original Definition

From Boser, Guyon & Vapnik (1992):
"We propose a training algorithm for optimal margin classifiers. The algorithm is based on a recent theoretical result: the generalization performance of a classifier can be controlled by its margin on the training set."

From Cortes & Vapnik (1995):
"The support-vector network is a new learning machine for two-group classification problems. The machine conceptually implements the following idea: input vectors are non-linearly mapped to a very high-dimension feature space. In this feature space a linear decision surface is constructed."

## Core Concept

SVMs find the optimal hyperplane that maximizes the margin between two classes. The margin is defined as the distance between the hyperplane and the nearest data points from each class (the support vectors).

## Mathematical Formulation

The optimization problem:
minimize: (1/2)||w||²
subject to: yᵢ(w·xᵢ + b) ≥ 1, for all i

Where:
- w is the normal vector to the hyperplane
- b is the bias term
- xᵢ are the training examples
- yᵢ ∈ {-1, +1} are the class labels

## Key Innovations

1. **Maximum Margin Principle**: Instead of just finding any separating hyperplane, SVM finds the one with the largest margin
2. **Kernel Trick**: Allows efficient computation in high-dimensional spaces without explicitly computing the transformation
3. **Soft Margin**: Introduced by Cortes & Vapnik to handle non-linearly separable data
4. **Structural Risk Minimization**: Theoretical foundation based on Vapnik's work

## Historical Significance

SVMs represented a breakthrough in machine learning by providing:
- Strong theoretical foundations in statistical learning theory
- Excellent generalization performance
- Ability to handle high-dimensional data
- Elegant solution to the non-linear classification problem

The development of SVMs marked a shift from heuristic-based to theory-driven machine learning approaches.
