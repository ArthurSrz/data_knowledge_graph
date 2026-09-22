---
foundationalPaper: "Ridge Regression: Biased Estimation for Nonorthogonal Problems (Hoerl & Kennard, 1970)"
keyPapers: ["Regression Shrinkage and Selection via the Lasso (Tibshirani, 1996)", "An Introduction to Statistical Learning (James et al., 2013)", "Regularization and Variable Selection via the Elastic Net (Zou & Hastie, 2005)"]
typeOf: "[[Overfitting]] prevention technique"
prevents: "[[Overfitting]]"
reduces: "[[Model complexity]]"
types: ["[[L1 regularization]]", "[[L2 regularization]]", "[[Elastic net]]", "[[Dropout]]"]
usedIn: ["[[Linear regression]]", "[[Neural networks]]", "[[Support Vector Machines]]"]
broader: "[[machine learning]]"
inferred:skos:ancestor: "[[machine learning]]"
---

# Regularization

Regularization techniques were introduced to address ill-posed problems in statistics and machine learning. The foundations were laid by Tikhonov in the 1940s, with significant developments by Hoerl & Kennard (Ridge) and Tibshirani (Lasso).

## Original Definition

From Hoerl & Kennard (1970) on Ridge Regression:
"Ridge regression is a technique for analyzing multiple regression data that suffer from multicollinearity. When multicollinearity occurs, least squares estimates are unbiased, but their variances are large so they may be far from the true value. By adding a degree of bias to the regression estimates, ridge regression reduces the standard errors."

From Tibshirani (1996) on Lasso:
"We propose a new method for estimation in linear models. The 'lasso' minimizes the residual sum of squares subject to the sum of the absolute value of the coefficients being less than a constant."

## Mathematical Formulation

### Ridge Regression (L2)
minimize: ||y - Xβ||² + λ||β||²

### Lasso (L1)
minimize: ||y - Xβ||² + λ||β||₁

### Elastic Net
minimize: ||y - Xβ||² + λ₁||β||₁ + λ₂||β||²

Where:
- β are the model parameters
- λ is the regularization parameter
- ||·||₁ and ||·||² are L1 and L2 norms

## Historical Development

1. **Tikhonov Regularization (1943)**: General framework for ill-posed problems
2. **Ridge Regression (1970)**: Hoerl & Kennard's approach for multicollinearity
3. **Lasso (1996)**: Tibshirani's method for feature selection
4. **Elastic Net (2005)**: Zou & Hastie's combination of L1 and L2

## Key Insights

From Hoerl & Kennard:
"There exists a value of k [regularization parameter] for which the mean squared error of the ridge estimator is less than that of the least squares estimator."

From Tibshirani:
"The lasso... has the property that it simultaneously does parameter estimation and variable selection; some coefficients are shrunk to exactly zero."

## Types of Regularization

1. **L2 (Ridge)**: Shrinks coefficients proportionally
2. **L1 (Lasso)**: Produces sparse solutions
3. **Elastic Net**: Combines L1 and L2 benefits
4. **Dropout**: Random neuron deactivation in neural networks
5. **Early Stopping**: Terminating training before convergence

## Historical Significance

Regularization fundamentally changed machine learning by:
- Providing theoretical framework for bias-variance tradeoff
- Enabling feature selection through sparsity
- Making high-dimensional problems tractable
- Improving generalization in complex models

As noted by Zou & Hastie: "Regularization is perhaps the key concept that distinguishes modern high-dimensional statistics from classical statistics."
