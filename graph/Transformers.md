---
introducedin: "[[Attention Is All You Need]]"
enablesArchitecture: "[[Large Language Model]]"
uses: "[[attention weights]]"
processes: "[[Word embeddings]]"
foundationFor:
  - "[[BERT]]"
  - "[[GPT2]]"
  - "[[Natural Language Processing]]"
broader: "[[Deep learning]]"
inferred:skos:ancestor:
  - "[[Deep learning]]"
  - "[[machine learning]]"
inferred:skos:narrower:
  - "[[Decoder-only]]"
  - "[[Encoder-only]]"
  - "[[attention weights]]"
---

# Transformers

Transformers are a revolutionary neural network architecture introduced by Vaswani et al. in the 2017 paper "Attention Is All You Need". They have become the foundation of modern Natural Language Processing (NLP) and form the basis for Large Language Models (LLMs).

## Key Innovation

The transformer architecture is based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. This design allows for significantly more parallelization during training, leading to substantial improvements in model training efficiency.

## Architecture Components

### 1. Self-Attention Mechanism
- Allows the model to weigh the importance of different words in a sequence
- Computes attention scores between all pairs of positions in a sequence
- Enables the model to capture long-range dependencies

### 2. Word Embeddings
- Converts text tokens into continuous vector representations
- These embeddings are the input to the transformer architecture

### 3. Positional Encodings
- Since transformers don't have built-in sequence order awareness
- Adds position information to word embeddings
- Uses sine and cosine functions to encode position

### 4. Multi-Head Attention
- Multiple attention mechanisms running in parallel
- Each head learns different aspects of relationships between words
- Outputs are concatenated and transformed

### 5. Feed-Forward Networks
- Applied to each position separately and identically
- Consists of two linear transformations with a ReLU activation

## Architecture Variants

1. **Encoder-Decoder**: Original transformer design (translation tasks)
2. **Encoder-only**: BERT-like models (understanding tasks)
3. **Decoder-only**: GPT-like models (generation tasks)

## Pre-training Paradigm

Transformers can work using:
- **Pre-trained models**: Trained on large corpora with general language understanding
- **Fine-tuning**: Adaptation to specific tasks or domains
- **Specific corpus training**: Training from scratch on specialized data

> [!image] Image of word embeddings 
![[word_embeddings.png]]

## Impact and Applications

- Machine Translation
- Text Generation
- Question Answering
- Sentiment Analysis
- Document Classification
- Named Entity Recognition
- Speech Recognition
- Computer Vision (Vision Transformers)

## Advantages

- Parallelization: Unlike RNNs, can process all tokens simultaneously
- Long-range dependencies: Captures relationships across entire sequences
- Scalability: Performance improves with model size and data
- Transfer learning: Pre-trained models adapt well to new tasks

## Limitations

- Computational requirements: Large memory and compute needs
- Quadratic complexity: Self-attention scales quadratically with sequence length
- Black box nature: Difficult to interpret decision processes
- Data requirements: Needs massive amounts of training data

## Related concepts

- [[attention weights]] - Core mechanism of transformers
- [[Hidden states]] - Internal representations in transformers
- [[Encoder-only]] - Architecture type (e.g., BERT)
- [[Decoder-only]] - Architecture type (e.g., GPT)
- [[BERT]] - Famous encoder-only transformer
- [[GPT2]] - Example of decoder-only transformer
- [[Large Language Model]] - Built on transformer architecture
- [[Embeddings]] - Input representation for transformers

See also: [[Natural Language Processing]], [[Deep learning]], [[Self-attention]], [[Multi-head attention]]
