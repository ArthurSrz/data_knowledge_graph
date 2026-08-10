---
foundationalPaper: "A Stochastic Approximation Method (Robbins & Monro, 1951)"
keyPapers: ["Adaptive Subgradient Methods for Online Learning (Duchi et al., 2011)", "ADAM: A Method for Stochastic Optimization (Kingma & Ba, 2014)", "Cyclical Learning Rates for Training Neural Networks (Smith, 2017)"]
usedIn: ["[[Gradient descent]]", "[[Stochastic gradient descent]]", "[[Adam optimizer]]"]
affects: ["[[Convergence rate]]", "[[Training stability]]", "[[Model performance]]"]
schedulingMethods: ["[[Learning rate decay]]", "[[Cyclical learning rates]]", "[[Warm-up]]", "[[Cosine annealing]]"]
broader: "[[Hyperparameters]]"
inferred:skos:ancestor: "[[Hyperparameters]]"
---

# Learning Rate

The learning rate concept originated in stochastic approximation theory and became crucial for neural network training.

## Original Definition

From Robbins & Monro (1951):
"Let {aₙ} be a sequence of positive constants such that Σaₙ = ∞ and Σaₙ² < ∞. Then the procedure xₙ₊₁ = xₙ - aₙYₙ will converge to the root θ."

In modern ML context (Goodfellow et al., 2016):
"The learning rate is perhaps the most important hyperparameter. If you have time to tune only one hyperparameter, tune the learning rate."

## Mathematical Role

Parameter update rule:
θₜ₊₁ = θₜ - η∇L(θₜ)

Where:
- θₜ are parameters at time t
- η is the learning rate
- ∇L(θₜ) is the gradient of the loss

## Historical Development

1. **Fixed Learning Rate (1960s)**: Simple, constant values
2. **Diminishing Rates (1970s)**: 1/t decay schedules
3. **Adaptive Methods (2011)**: AdaGrad, RMSProp
4. **Momentum-based (2014)**: Adam, AdamW
5. **Cyclic/Scheduled (2017)**: Cyclical LR, cosine decay

## Key Insights

Robbins-Monro conditions for convergence:
1. Σ ηₜ = ∞ (ensures reach)
2. Σ ηₜ² < ∞ (ensures convergence)

From modern research:
- Too high: Training diverges or oscillates
- Too low: Slow convergence, poor local minima
- Optimal: Problem and architecture dependent

## Learning Rate Schedules

### Classic Decay
η(t) = η₀/(1 + kt)

### Exponential Decay
η(t) = η₀ * γᵗ

### Cyclical (Smith, 2017)
"Instead of monotonically decreasing the learning rate, this method lets the learning rate cyclically vary between reasonable boundary values."

### Warm-up (Goyal et al., 2017)
"Gradually increase learning rate from 0 to target value over initial iterations."

## Adaptive Methods

### AdaGrad (Duchi et al., 2011)
Adapts learning rate based on historical gradients:
θₜ₊₁ = θₜ - η/√(Gₜ + ε) · gₜ

### Adam (Kingma & Ba, 2014)
Combines momentum and adaptive learning rates:
mₜ = β₁mₜ₋₁ + (1-β₁)gₜ
vₜ = β₂vₜ₋₁ + (1-β₂)gₜ²
θₜ₊₁ = θₜ - η·mₜ/√(vₜ + ε)

## Practical Guidelines

From empirical research:
- Start with 0.1, 0.01, or 0.001
- Use learning rate finder (Smith, 2015)
- Consider warm-up for large batch sizes
- Reduce on plateau for fine-tuning
- Architecture-specific defaults exist

## Historical Significance

Learning rate research revealed:
- The critical role of optimization dynamics
- The need for adaptive methods
- The interplay between batch size and LR
- The importance of scheduling strategies

As Leslie Smith noted: "Learning rate may be the most important hyperparameter for neural network training."
