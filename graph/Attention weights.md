---
foundationalPaper: "Attention Is All You Need (Vaswani et al., 2017)"
keyPapers: ["Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau et al., 2014)", "Effective Approaches to Attention-based Neural Machine Translation (Luong et al., 2015)"]
goesOnInside: "[[Large Language Model]]"
usedIn: ["[[Transformers]]", "[[Self-attention]]", "[[Multi-head attention]]"]
computedBy: "[[Softmax function]]"
relatedTo: ["[[Query-Key-Value]]", "[[Scaled dot-product attention]]"]
broader: "[[Transformers]]"
inferred:skos:ancestor:
  - "[[Deep learning]]"
  - "[[Transformers]]"
  - "[[machine learning]]"
---

# Attention Weights

Attention weights were first introduced in the context of neural machine translation by Bahdanau et al. (2014), but gained prominence with the transformer architecture in "Attention Is All You Need" (Vaswani et al., 2017).

## Original Definition

From Bahdanau et al. (2014):
"The attention mechanism computes a weighted sum of the encoder hidden states, where the weight of each hidden state is computed by a feedforward neural network that takes as input the previous decoder state and the encoder hidden state."

From Vaswani et al. (2017):
"An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key."

## Mathematical Formulation

The attention weights are computed as:

α_ij = exp(e_ij) / Σ_k exp(e_ik)

Where:
- e_ij is the alignment score between position i and j
- α_ij is the attention weight from position i to position j

In the transformer's scaled dot-product attention:

Attention(Q, K, V) = softmax(QK^T / √d_k)V

Where:
- Q, K, V are the query, key, and value matrices
- d_k is the dimension of the keys
- The softmax output represents the attention weights

## Key Properties

1. **Normalized**: Attention weights sum to 1 across all attended positions
2. **Context-dependent**: Weights change based on the input
3. **Learnable**: The mechanism for computing weights is learned during training
4. **Interpretable**: Weights can reveal which parts of the input the model focuses on

## Historical Significance

The introduction of attention weights revolutionized sequence modeling by allowing models to focus on relevant parts of the input, effectively solving the long-range dependency problem that plagued RNNs and leading to the transformer architecture.
