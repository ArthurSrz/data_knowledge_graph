---
foundationalPaper: Distributed Representations (Hinton, 1984)
keyPapers:
  - A Neural Probabilistic Language Model (Bengio et al., 2003)
  - Efficient Estimation of Word Representations in Vector Space (Mikolov et al., 2013)
  - Distributed Representations of Words and Phrases (Mikolov et al., 2013)
entity: "[[data structure]]"
storedInto: "[[vector database]]"
represents:
  - "[[Words]]"
  - "[[Entities]]"
  - "[[Concepts]]"
  - "[[Documents]]"
properties:
  - "[[Semantic similarity]]"
  - "[[Dense representation]]"
  - "[[Continuous space]]"
types:
  - "[[Word embeddings]]"
  - "[[Sentence embeddings]]"
  - "[[Document embeddings]]"
  - "[[Graph embeddings]]"
broader: "[[Natural Language Processing]]"
inferred:skos:ancestor:
  - "[[Artificial Intelligence (AI)]]"
  - "[[Natural Language Processing]]"
inferred:skos:narrower:
  - "[[Embeddings models]]"
  - "[[Word embeddings]]"
  - "[[latent space]]"
  - "[[vectorization]]"
---

A vector representation of a [[token]] 

Embeddings are dense vector representations that capture semantic meaning in a continuous [[vector space]], originating from Hinton's work on distributed representations.

## Original Definition

From Hinton (1984) on distributed representations:
"A distributed representation is one in which meaning is represented by a [[pattern]] of activity over many computing elements, and each computing element is involved in representing many different meanings."

From Bengio et al. (2003):
"Each word is associated with a [[feature]] vector in ℝᵐ... The [[feature]] vector represents different aspects of the word: each word is associated with a point in a [[vector space]]. The features are learned automatically."

## Historical Development

1. **Distributed Representations (1984)**: Hinton's theoretical foundation
2. **Neural Language Models (2003)**: Bengio's word [[feature]] [[vectors]]
3. **Word2Vec (2013)**: Mikolov's efficient training
4. **Modern Embeddings**: Universal sentence encoders, [[BERT]] embeddings

## Mathematical [[Properties]]

From Mikolov et al. (2013):
"The word representations are learned using a simple neural network [[model]] that tries to predict a word based on its [[context]]."

Key [[properties]]:
1. **Dimensionality**: Typically 50-1000 dimensions
2. **Density**: All dimensions contain information
3. **Continuity**: Similar items have similar [[vectors]]
4. **Compositionality**: Can be combined meaningfully

## Semantic [[Properties]]

The famous analogy from Mikolov:
vector("King") - vector("Man") + vector("Woman") ≈ vector("Queen")

This demonstrates:
- Linear relationships capture semantic regularities
- Vector arithmetic maps to semantic operations
- Embeddings encode multiple types of relationships

## Types of Embeddings

### [[Word Embeddings]]
- Word2Vec (Mikolov et al., 2013)
- GloVe (Pennington et al., 2014)
- FastText (Bojanowski et al., 2017)

### Contextual Embeddings
- ELMo (Peters et al., 2018)
- [[BERT]] (Devlin et al., 2019)
- GPT (Radford et al., 2018)

### Specialized Embeddings
- Sentence embeddings
- Document embeddings
- Graph/[[node]] embeddings
- Image embeddings

## Learning Methods

### Predictive Methods (Word2Vec)
Predict [[context]] from word or word from [[context]]:
- Skip-gram: P([[context]]|word)
- CBOW: P(word|[[context]])

### Count-based Methods (GloVe)
Factorize co-occurrence matrices:
J = Σᵢⱼ f(Xᵢⱼ)(wᵢᵀw̃ⱼ + bᵢ + b̃ⱼ - [[log]] Xᵢⱼ)²

## Applications

1. **Information Retrieval**: Semantic [[search]]
2. **Recommendation Systems**: Item similarity
3. **[[Natural Language Processing]]**: Text [[classification]], translation
4. **[[computer vision]]**: Image retrieval
5. **Bioinformatics**: Protein function [[prediction]]

## Historical Significance

Embeddings revolutionized ML by:
- Replacing sparse representations with dense ones
- Capturing semantic relationships mathematically
- Enabling [[transfer learning]] in NLP
- Providing foundation for modern AI systems

As Hinton predicted: "Distributed representations allow a system to automatically discover useful features and generalize to new instances based on their similarity in the [[feature]] space."

## Modern Impact

Embeddings are now fundamental to:
- Large language models
- Multimodal learning
- Cross-lingual applications
- Zero-shot learning

The [[concept]] has extended beyond words to represent any entity in a meaningful [[vector space]].
