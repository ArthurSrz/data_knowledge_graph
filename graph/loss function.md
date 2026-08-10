---
foundationalPaper: Method of Least Squares (Legendre, 1805)
keyPapers:
  - Theory of Errors of Observations (Gauss, 1809)
  - A General Theory of Discriminant Analysis (Fisher, 1936)
  - Theory of Games and Economic Behavior (von Neumann & Morgenstern, 1944)
minimizedBy:
  - "[[Gradient descent]]"
  - "[[backpropagation]]"
examples:
  - "[[Mean squared error]]"
  - "[[Cross-entropy]]"
  - "[[Hinge loss]]"
  - "[[Kullback-Leibler divergence]]"
properties:
  - "[[Convexity]]"
  - "[[Differentiability]]"
  - "[[Continuity]]"
usedIn:
  - "[[Supervised learning]]"
  - "[[Optimization]]"
  - "[[Neural network training]]"
broader: "[[machine learning]]"
inferred:skos:ancestor:
  - "[[AI]]"
  - "[[Artificial Intelligence (AI)]]"
  - "[[machine learning]]"
---

# Loss Function

Loss functions have their roots in statistical estimation theory, with foundations laid by Legendre and Gauss in the early 19th century for least squares.

## Original Definition

From Legendre (1805) on least squares:
"De tous les principes qu'on peut proposer pour cet objet, je pense qu'il n'en est pas de plus général, de plus exact, ni d'une application plus facile que celui dont nous avons fait usage dans les recherches précédentes, et qui consiste à rendre minimum la somme des carrés des erreurs."
("Of all the principles that can be proposed for this purpose, I think there is none more general, more exact, or easier to apply than that which we have used in the preceding researches, which consists of minimizing the sum of the squares of the errors.")

From modern machine learning (Vapnik, 1995):
"A loss function measures the discrepancy between the prediction ŷ of a model and the true value y. The goal of learning is to find the model parameters that minimize the expected loss."

## Historical Development

1. **Least Squares (1805)**: Legendre's method for regression
2. **Maximum Likelihood (1912)**: Fisher's estimation framework
3. **Statistical Decision Theory (1950)**: Wald's formalization
4. **Empirical Risk Minimization (1970s)**: Vapnik & Chervonenkis

## Mathematical Formulation

General form:
L(θ) = E_{(x,y)~P}[ℓ(f_θ(x), y)]

Where:
- θ are model parameters
- f_θ is the model function
- ℓ is the loss for a single example
- P is the data distribution

## Common Loss Functions

### Mean Squared Error (Legendre/Gauss)
MSE = (1/n)Σ(y_i - ŷ_i)²

### Cross-Entropy (Kullback & Leibler, 1951)
CE = -Σ y_i log(ŷ_i)

### Hinge Loss (Vapnik, 1995)
Hinge = max(0, 1 - y·ŷ)

## Properties

1. **Convexity**: Ensures unique global minimum
2. **Differentiability**: Enables gradient-based optimization
3. **Robustness**: Resistance to outliers
4. **Statistical Consistency**: Convergence properties

## Design Principles

From statistical decision theory:
- Loss should reflect the true cost of errors
- Consider computational tractability
- Balance bias-variance tradeoff
- Ensure statistical properties (consistency, efficiency)

## Historical Significance

Loss functions bridge:
- Statistics and machine learning
- Theory and practice
- Optimization and learning

As Vapnik noted: "The choice of loss function is one of the most critical decisions in machine learning, as it directly determines what the model learns to optimize."

## Modern Developments

- Task-specific losses (perceptual loss, focal loss)
- Adversarial losses (GANs)
- Multi-objective losses
- Differentiable approximations of non-differentiable metrics
