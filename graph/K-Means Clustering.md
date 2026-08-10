---
foundationalPaper: "Some Methods for Classification and Analysis of Multivariate Observations (MacQueen, 1967)"
keyPapers: ["Least Squares Quantization in PCM (Lloyd, 1957/1982)", "Algorithm AS 136: A K-Means Clustering Algorithm (Hartigan & Wong, 1979)"]
typeOf: "[[Clustering algorithm]]"
usedIn: ["[[Unsupervised learning]]", "[[Data mining]]", "[[Pattern recognition]]"]
optimizes: "[[Sum of squared distances]]"
relatedTo: ["[[Centroid]]", "[[Euclidean distance]]", "[[Voronoi diagram]]"]
broader: "[[Clustering]]"
inferred:skos:ancestor:
  - "[[clustering]]"
inferred:skos:broader:
  - "[[clustering]]"
---

# K-Means Clustering

K-means clustering was first described by Stuart Lloyd in 1957 (though not published until 1982) and independently by James MacQueen in 1967, who coined the term "k-means."

## Original Definition

From MacQueen (1967):
"The process, called 'k-means,' appears to give partitions which are reasonably efficient in the sense of within-class variance... The process consists of simply starting with k groups each of which consists of a single random point, and thereafter adding each new point to the group whose mean the new point is nearest. After a point is added to a group, the mean of that group is adjusted in order to take account of the new point. Thus at each stage the k-means are, in fact, the means of the groups they represent."

From Lloyd (1957/1982):
"Given a discrete set of input points, the problem is to find a discrete set of output points to minimize the average squared distance between the input points and their nearest output points."

## Algorithm Steps

As originally described:
1. Choose k initial centers (randomly or heuristically)
2. Assign each point to the nearest center
3. Recalculate centers as the mean of assigned points
4. Repeat steps 2-3 until convergence

## Mathematical Formulation

The objective function:
J = Σᵢ₌₁ⁿ Σⱼ₌₁ᵏ wᵢⱼ ||xᵢ - μⱼ||²

Where:
- xᵢ is the i-th data point
- μⱼ is the j-th cluster center
- wᵢⱼ is 1 if xᵢ belongs to cluster j, 0 otherwise

## Historical Context

Lloyd's work originated in pulse-code modulation (PCM) for signal processing, while MacQueen's work focused on multivariate statistical analysis. The algorithm's simplicity and effectiveness led to its widespread adoption across various fields.

## Key Properties

1. **Convergence**: Guaranteed to converge to a local minimum
2. **Complexity**: O(nkdi) where n=points, k=clusters, d=dimensions, i=iterations
3. **Sensitivity**: Results depend on initial center selection
4. **Assumption**: Assumes spherical clusters of similar size

The k-means algorithm remains one of the most widely used clustering methods due to its simplicity, scalability, and interpretability.
