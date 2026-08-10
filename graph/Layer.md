---
foundationalPaper: "Perceptrons: An Introduction to Computational Geometry (Minsky & Papert, 1969)"
keyPapers:
  - Learning Internal Representations by Error Propagation (Rumelhart, Hinton & Williams, 1986)
  - Deep Learning (LeCun, Bengio & Hinton, 2015)
composedOf:
  - "[[Artificial neuron]]"
  - "[[Weights]]"
  - "[[Activation function]]"
types:
  - "[[Input layer]]"
  - "[[Hidden layer]]"
  - "[[Output layer]]"
  - "[[Convolutional layer]]"
  - "[[Pooling layer]]"
connectsThrough:
  - "[[Forward propagation]]"
  - "[[backpropagation]]"
formsPartOf: "[[Neural network models]]"
---

# Layer

The concept of layers in neural networks evolved from early perceptron models to the deep architectures we use today.

## Original Definition

From Minsky & Papert (1969):
"A perceptron is a network that contains a layer of input units connected to a layer of output units... Multi-layer networks can compute functions that single-layer networks cannot."

From Rumelhart, Hinton & Williams (1986):
"A typical multilayer network consists of a set of input units, one or more layers of hidden units, and a set of output units. Each unit in one layer is connected to each unit in the next layer, and each connection has a weight associated with it."

## Historical Development

1. **Single Layer (1958)**: Rosenblatt's Perceptron
2. **Multi-Layer (1969)**: Minsky & Papert's analysis
3. **Hidden Layers (1986)**: Backpropagation breakthrough
4. **Deep Layers (2006+)**: Deep learning revolution

## Mathematical Structure

A layer transforms its input:
y = f(Wx + b)

Where:
- x is the input vector
- W is the weight matrix
- b is the bias vector
- f is the activation function
- y is the output vector

## Types of Layers

### Input Layer
- Receives raw data
- No computation, just data forwarding
- Size matches input dimensionality

### Hidden Layers
From Rumelhart et al.:
"Hidden units allow the network to develop its own internal representations. The network can extract higher-order features from the input data."

### Output Layer
- Produces final predictions
- Activation function matches task (softmax, sigmoid, linear)
- Size matches output requirements

### Specialized Layers
- Convolutional: Feature extraction in grids
- Pooling: Dimensionality reduction
- Recurrent: Temporal dependencies
- Attention: Dynamic weighting

## Key Properties

1. **Compositionality**: Layers build hierarchical representations
2. **Modularity**: Layers can be mixed and matched
3. **Differentiability**: Enables gradient-based learning
4. **Abstraction**: Each layer learns increasingly abstract features

## Historical Significance

The layer concept enabled:
- Breaking the limitations of single-layer perceptrons
- Learning hierarchical representations
- The deep learning revolution
- Modular neural network design

As Hinton noted: "Deep neural networks exploit the property that many natural signals are compositional hierarchies in which higher-level features are obtained by composing lower-level ones."

## Modern Developments

- Residual connections (skip connections)
- Normalization layers (batch norm, layer norm)
- Transformer layers (self-attention)
- Dynamic layers (conditional computation)
