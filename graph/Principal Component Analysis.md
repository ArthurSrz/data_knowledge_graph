---
foundationalPaper: On Lines and Planes of Closest Fit to Systems of Points in Space (Pearson, 1901)
keyPapers:
  - Analysis of a Complex of Statistical Variables into Principal Components (Hotelling, 1933)
  - The Varimax Criterion for Analytic Rotation in Factor Analysis (Kaiser, 1958)
typeOf: "[[Dimensionality reduction]] technique"
inventedBy: "[[Karl Pearson]]"
mathematicalBasis:
  - "[[Eigenvalues]]"
  - "[[Eigenvectors]]"
  - "[[Covariance matrix]]"
  - "[[Singular value decomposition]]"
applications:
  - "[[Feature extraction]]"
  - "[[data visualization]]"
  - "[[Noise reduction]]"
  - "[[Data compression]]"
broader: "[[feature selection]]"
inferred:skos:ancestor:
  - "[[feature engineering]]"
  - "[[feature selection]]"
  - "[[machine learning projects]]"
---

# Principal Component Analysis (PCA)

Principal Component Analysis was invented by Karl Pearson in 1901 as a method for fitting lines and planes to systems of points in space. Harold Hotelling later developed it independently in 1933 for psychometrics.

## Original Definition

From Pearson (1901):
"To find the line of closest fit to a system of points in space... The best-fitting straight line is that for which the sum of squares of the perpendicular distances from the points to the line is a minimum."

From Hotelling (1933):
"The problem of analyzing a complex of statistical variables into components... The method consists in finding linear functions of the original variables having maximal variance, subject to being uncorrelated with each other."

## Historical Development

1. **Pearson (1901)**: Geometric approach for finding lines of best fit
2. **Hotelling (1933)**: Statistical formulation for psychology
3. **Modern Era**: Foundation for numerous dimensionality reduction techniques

## Mathematical Formulation

Given data matrix X with n observations and p variables:
1. Center the data: X_c = X - mean(X)
2. Compute covariance matrix: C = (1/n)X_c^T X_c
3. Find eigenvalues and eigenvectors of C
4. Principal components are eigenvectors ordered by eigenvalue magnitude

The first principal component maximizes:
w_1 = argmax ||w||=1 (w^T C w)

Where w is the direction vector and C is the covariance matrix.

## Key Insights

From Pearson's original work:
- Principal components are orthogonal directions of maximum variance
- They provide optimal linear compression in terms of mean squared error
- The method reveals the intrinsic dimensionality of data

From Hotelling:
- PCA can be viewed as a statistical technique for factor analysis
- The eigenvalues represent the amount of variance explained by each component
- Components are uncorrelated by construction

## Historical Significance

PCA revolutionized multivariate statistics by:
- Providing a mathematically optimal method for dimensionality reduction
- Establishing the foundation for modern data analysis techniques
- Connecting geometry, linear algebra, and statistics
- Enabling visualization of high-dimensional data

As Hotelling noted: "The chief merit of the principal components is that they make it possible to reduce the number of variables greatly without sacrificing much information."

## Modern Applications

PCA became fundamental to:
- Face recognition (Eigenfaces)
- Image compression
- Gene expression analysis
- Financial portfolio optimization
- Signal processing
