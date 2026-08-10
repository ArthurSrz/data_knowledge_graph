---
foundationalPaper: Random Search for Hyper-Parameter Optimization (Bergstra & Bengio, 2012)
keyPapers:
  - Practical Bayesian Optimization of Machine Learning Algorithms (Snoek, Larochelle & Adams, 2012)
  - Algorithms for Hyper-Parameter Optimization (Bergstra et al., 2011)
  - Sequential Model-Based Optimization for General Algorithm Configuration (Hutter et al., 2011)
tunes: "[[algorithm]]"
optimizedBy:
  - "[[Grid search]]"
  - "[[Random search]]"
  - "[[Bayesian optimization]]"
  - "[[Hyperband]]"
affects:
  - "[[Model performance]]"
  - "[[Training time]]"
  - "[[Generalization]]"
broader: "[[machine learning]]"
inferred:skos:ancestor:
  - "[[AI]]"
  - "[[Artificial Intelligence (AI)]]"
  - "[[machine learning]]"
inferred:skos:narrower: "[[Learning rate]]"
---

# Hyperparameters

The formal study of hyperparameter optimization emerged in the 2010s, with Bergstra and Bengio's work establishing key principles and methods.

## Original Definition

From Bergstra & Bengio (2012):
"In machine learning, a hyperparameter is a parameter whose value is set before the learning process begins. By contrast, the values of other parameters are derived via training. Examples of hyperparameters include learning rate, number of hidden layers, and batch size."

From Snoek, Larochelle & Adams (2012):
"The performance of many machine learning algorithms depends critically on hyperparameter settings. The problem of finding optimal hyperparameters is essentially one of global optimization of an expensive black-box function."

## Historical Development

1. **Manual Tuning Era (pre-2010)**: Trial and error
2. **Grid Search (2000s)**: Systematic but inefficient
3. **Random Search (2012)**: Bergstra & Bengio showed superiority
4. **Bayesian Optimization (2012)**: Snoek et al. for efficiency
5. **AutoML Era (2015+)**: Automated hyperparameter optimization

## Key Insights

From Bergstra & Bengio:
"For most datasets only a few of the hyperparameters really matter, but that different hyperparameters are important on different datasets. This phenomenon makes grid search a poor choice for configuring algorithms for new datasets."

They demonstrated: "Random search is more efficient than grid search in high-dimensional spaces because it doesn't waste time evaluating unimportant dimensions."

## Types of Hyperparameters

1. **Model Architecture**: Number of layers, units per layer
2. **Training Process**: Learning rate, batch size, epochs
3. **Regularization**: L1/L2 penalties, dropout rate
4. **Optimization**: Momentum, Adam parameters
5. **Data Preprocessing**: Feature scaling, augmentation

## Optimization Methods

### Grid Search
- Exhaustive search over specified parameter values
- Exponentially expensive with dimensionality

### Random Search (Bergstra & Bengio)
- Randomly sample from parameter distributions
- More efficient for high-dimensional spaces

### Bayesian Optimization (Snoek et al.)
- Build probabilistic model of objective function
- Use acquisition function to guide search
- Efficient for expensive evaluations

## Mathematical Formulation

The hyperparameter optimization problem:
θ* = argmin_{θ∈Θ} E_{(x,y)~D} [L(M_θ(x), y)]

Where:
- θ are hyperparameters
- M_θ is the model with hyperparameters θ
- L is the loss function
- D is the data distribution

## Historical Significance

The formalization of hyperparameter optimization:
- Transformed model tuning from art to science
- Enabled automated machine learning (AutoML)
- Improved reproducibility in ML research
- Made complex models more accessible

As Bergstra & Bengio noted: "Hyperparameter optimization is a meta-learning problem that is crucial for the practical application of machine learning algorithms."
