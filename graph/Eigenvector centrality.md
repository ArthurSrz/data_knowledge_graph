---
broader: "[[Centrality]]"
inferred:skos:ancestor:
  - "[[Graph algorithm]]"
  - "[[Metric]]"
  - "[[algorithm]]"
  - "[[centrality]]"
inferred:skos:broader: "[[centrality]]"
---
# Eigenvector Centrality

## Definition

Eigenvector centrality is a measure of the influence of a node in a network, based on the principle that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes.

## Historical Development

1. **Original Formulation (1972)**: Phillip Bonacich introduced eigenvector centrality in "Factoring and Weighting Approaches to Status Scores and Clique Identification"

2. **Mathematical Foundation**: Based on the principal eigenvector of the adjacency matrix of the network

## Key Principles from Bonacich (1972)

According to Bonacich:
- A node's centrality depends on the centrality of its neighbors
- The measure captures both direct and indirect connections
- The eigenvector approach weights connections by their importance

## Mathematical Definition

For a given graph G with adjacency matrix A, the eigenvector centrality x of node i is given by:

x_i = (1/λ) ∑_j A_ij x_j

Where:
- λ is the largest eigenvalue of A
- A_ij is the element of the adjacency matrix (1 if nodes i and j are connected, 0 otherwise)
- The sum is over all nodes j connected to node i

## Key Properties

1. **Recursive Definition**: A node is important if it's connected to important nodes
2. **Global Measure**: Considers the entire network structure
3. **Proportion to Neighboring Centralities**: Score is proportional to the sum of neighbors' scores
4. **Non-local Effects**: Captures indirect influence through the network

## Applications

1. **Social Networks**: Identifying influential individuals
2. **Web Search**: Google's PageRank algorithm (modified version)
3. **Economic Networks**: Determining key economic actors
4. **Biological Networks**: Finding important proteins or genes
5. **Power Grids**: Identifying critical infrastructure nodes

## Advantages

- Considers quality of connections, not just quantity
- Captures indirect influence
- Mathematically well-founded
- Computationally efficient for large networks

## Limitations

- May converge slowly for some network structures
- Can be dominated by a few highly connected nodes
- Less intuitive than simpler centrality measures
- May not be well-defined for disconnected graphs

## Related Concepts
- [[Centrality measures]]
- [[PageRank]]
- [[Katz centrality]]
- [[graph theory]]
- [[Network analysis]]

## References

Bonacich, P. (1972). Factoring and weighting approaches to status scores and clique identification. Journal of Mathematical Sociology, 2(1), 113-120.