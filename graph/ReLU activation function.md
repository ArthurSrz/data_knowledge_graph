---
foundationalPaper: "Deep Sparse Rectifier Neural Networks (Glorot, Bordes & Bengio, 2011)"
keyPapers: ["Rectified Linear Units Improve Restricted Boltzmann Machines (Nair & Hinton, 2010)", "ImageNet Classification with Deep Convolutional Neural Networks (Krizhevsky et al., 2012)"]
typeOf: "[[Activation function]]"
advantages: ["[[Computational efficiency]]", "[[Sparse activation]]", "[[Gradient propagation]]"]
variants: ["[[Leaky ReLU]]", "[[Parametric ReLU]]", "[[ELU]]", "[[GELU]]"]
usedIn: ["[[Deep neural networks]]", "[[Convolutional neural networks]]"]
broader: "[[artificial neural network]]"
inferred:skos:ancestor:
  - "[[Deep learning]]"
  - "[[artificial neural network]]"
  - "[[machine learning]]"
---

# ReLU (Rectified Linear Unit)

ReLU revolutionized deep learning by providing a simple yet effective activation function that enabled training of much deeper networks.

## Original Definition

From Glorot, Bordes & Bengio (2011):
"The rectifier activation function is defined as: f(x) = max(0, x). Despite its simplicity, we will show that it allows networks to learn sparse representations and helps train deep supervised neural networks."

From Nair & Hinton (2010):
"We show that using rectified linear units (ReLUs) instead of logistic sigmoid units leads to much faster training of deep neural networks."

## Mathematical Form

f(x) = max(0, x) = {
    x, if x > 0
    0, if x ≤ 0
}

Derivative:
f'(x) = {
    1, if x > 0
    0, if x ≤ 0
}

## Historical Context

Before ReLU:
- Sigmoid and tanh dominated (1980s-2000s)
- Suffered from vanishing gradients
- Limited network depth

ReLU breakthrough:
- Simple computation
- No vanishing gradients for positive values
- Enabled much deeper networks

## Key Advantages

From Glorot et al. (2011):
1. **Biological Plausibility**: "More similar to biological neurons"
2. **Sparsity**: "Typically 50% of hidden units are active"
3. **Efficient Computation**: "Comparison and multiplication only"
4. **Gradient Propagation**: "No gradient vanishing for positive values"

## Empirical Success

From Krizhevsky et al. (2012) AlexNet paper:
"Deep convolutional neural networks with ReLUs train several times faster than their equivalents with tanh units."

## Variants

### Leaky ReLU (Maas et al., 2013)
f(x) = max(αx, x), where α is small (e.g., 0.01)

### Parametric ReLU (He et al., 2015)
f(x) = max(αx, x), where α is learned

### ELU (Clevert et al., 2015)
f(x) = {
    x, if x > 0
    α(exp(x) - 1), if x ≤ 0
}

## Problems and Solutions

### Dead ReLU Problem
Neurons can become permanently inactive (output 0 for all inputs).
Solutions: Leaky ReLU, careful initialization, lower learning rates

### Non-zero Centered
ReLU outputs are always non-negative.
Solutions: Batch normalization, zero-centered variants

## Historical Significance

ReLU's impact:
- Enabled training of AlexNet (2012)
- Made deep learning practical
- Simplified neural network design
- Accelerated the deep learning revolution

As Glorot et al. noted:
"The rectifier activation function allows a network to easily obtain sparse representations, which seems to be an important component of successful deep learning."

## Modern Usage

ReLU remains the default choice for:
- Hidden layers in deep networks
- Convolutional neural networks
- Most computer vision architectures
- Many NLP models (before transformer era)

The simplicity and effectiveness of ReLU exemplify the principle that sometimes the simplest solutions work best.
