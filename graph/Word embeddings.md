---
foundationalPaper: "Efficient Estimation of Word Representations in Vector Space (Mikolov et al., 2013)"
keyPapers: ["Distributed Representations of Words and Phrases (Mikolov et al., 2013)", "GloVe: Global Vectors for Word Representation (Pennington et al., 2014)", "A Neural Probabilistic Language Model (Bengio et al., 2003)"]
typeOf: "[[Distributed representation]]"
usedIn: ["[[Natural Language Processing]]", "[[Deep learning]]"]
techniques: ["[[Word2Vec]]", "[[GloVe]]", "[[FastText]]"]
properties: ["[[Semantic similarity]]", "[[Analogy completion]]", "[[Vector arithmetic]]"]
broader: "[[Embeddings]]"
inferred:skos:ancestor:
  - "[[Artificial Intelligence (AI)]]"
  - "[[Embeddings]]"
  - "[[Natural Language Processing]]"
---

# Word Embeddings

Word embeddings as dense vector representations gained prominence with Mikolov et al.'s Word2Vec in 2013, though the idea of distributed representations dates back to earlier work.

## Original Definition

From Mikolov et al. (2013):
"We propose two novel model architectures for computing continuous vector representations of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks."

From Bengio et al. (2003) who laid the groundwork:
"A word can be represented by a vector of real-valued features... learning a distributed representation for each word along with the probability function for word sequences expressed in terms of these representations."

## Historical Development

1. **Early Foundations (1980s)**: Hinton's distributed representations
2. **Neural Language Models (2003)**: Bengio's neural probabilistic model
3. **Word2Vec (2013)**: Mikolov's efficient training algorithms
4. **GloVe (2014)**: Pennington's global vector approach

## Key Innovations

Word2Vec introduced two architectures:
1. **Continuous Bag-of-Words (CBOW)**: Predicts word from context
2. **Skip-gram**: Predicts context from word

From the paper:
"The main observation is that similar words tend to have similar contexts, and as a result, training a model to predict words from contexts results in word vectors that capture semantic relationships."

## Mathematical Properties

Word embeddings exhibit remarkable properties:
- vector("King") - vector("Man") + vector("Woman") ≈ vector("Queen")
- Cosine similarity corresponds to semantic similarity
- Linear substructures encode linguistic patterns

## Training Objective

Skip-gram objective function:
maximize 1/T Σ_{t=1}^T Σ_{-c≤j≤c,j≠0} log p(w_{t+j}|w_t)

Where c is the context window size and T is the corpus length.

## Historical Significance

Word embeddings revolutionized NLP by:
- Moving from sparse to dense representations
- Capturing semantic relationships mathematically
- Enabling transfer learning in NLP
- Reducing dimensionality while preserving meaning
- Providing foundation for modern language models

As Mikolov noted: "The word vectors... carry semantic information: similar words are close to each other and different words are far from each other. Somewhat surprisingly, the vectors capture many linguistic regularities."

## Impact

Word embeddings became fundamental to:
- Machine translation
- Sentiment analysis
- Information retrieval
- Question answering
- Text classification

The success of word embeddings paved the way for contextual embeddings and transformer models.
