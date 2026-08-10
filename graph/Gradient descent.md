---
typeOf: "[[Optimization algorithm]]"
uses: "[[Backpropagation]]"
requires:
  - "[[Learning rate]]"
  - "[[Gradient]]"
  - "[[Loss function]]"
minimizes: "[[Loss function]]"
updatesBy: "[[Weight updates]]"
variantsInclude:
  - "[[Batch gradient descent]]"
  - "[[Stochastic gradient descent]]"
  - "[[Mini-batch gradient descent]]"
broader: "[[Optimizer algorithm]]"
inferred:skos:ancestor: "[[Optimizer algorithm]]"
inferred:skos:narrower:
  - "[[Batch gradient descent]]"
  - "[[Mini-batch gradient descent]]"
---

# Gradient Descent

Gradient descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function. It is the fundamental algorithm for training machine learning models, particularly neural networks.

## Definition

Gradient descent is an iterative method to find the values of parameters (weights) that minimize a cost function. The algorithm repeatedly takes steps proportional to the negative of the gradient of the function at the current point.

## Mathematical Formulation

The update rule for gradient descent is:

θ = θ - α∇J(θ)

Where:
- θ represents the parameters (weights)
- α is the learning rate
- ∇J(θ) is the gradient of the cost function with respect to parameters
- J(θ) is the cost function

## Core Components

1. **Learning rate (α)**: Controls the step size at each iteration
   - Too small: Slow convergence
   - Too large: May overshoot the minimum or diverge

2. **Gradient**: Direction and magnitude of steepest ascent
   - Computed using backpropagation in neural networks
   - Points towards the direction of maximum increase

3. **Iterations**: Number of steps taken
   - Can range from 50 to millions depending on problem complexity
   - Convergence is often hard to estimate in advance

## Variants of Gradient Descent

### 1. Batch Gradient Descent
- Computes gradient using entire dataset
- Stable convergence but computationally expensive
- Memory intensive for large datasets

### 2. Stochastic Gradient Descent (SGD)
- Updates parameters for each training example
- Faster but noisier updates
- Can escape local minima due to noise

### 3. Mini-batch Gradient Descent
- Balances between batch and stochastic
- Updates based on small random subsets
- Most commonly used in practice

## Advanced Optimization Methods

### Momentum
- Accelerates convergence by accumulating a velocity vector
- Helps navigate ravines and plateaus
- Update rule: v = βv - α∇J(θ); θ = θ + v

### Adaptive Methods
1. **Adagrad**: Adapts learning rate for each parameter
2. **RMSprop**: Addresses Adagrad's diminishing learning rates
3. **Adam**: Combines momentum with adaptive learning rates
4. **AdamW**: Adam with weight decay decoupling

## Convergence Properties

- Guaranteed to converge to a local minimum for convex functions
- May get stuck in local minima for non-convex functions
- Convergence rate depends on:
  - Function smoothness
  - Learning rate selection
  - Initialization of parameters

## Challenges

1. **Choosing learning rate**: Critical for convergence
2. **Local minima and saddle points**: Can trap optimization
3. **Vanishing/exploding gradients**: In deep networks
4. **Ill-conditioning**: Different scales of features
5. **Non-convexity**: Multiple local optima

## Applications

- Neural network training
- Linear regression
- Logistic regression
- Support Vector Machines
- Recommendation systems
- Computer vision tasks

See also: [[Backpropagation]], [[Learning rate]], [[Loss function]], [[Optimization algorithm]], [[Neural network models]]
