---
subclass of:
  - "[[Artificial neural network]]"
facet of:
  - "[[deep learning]]"
  - "[[unsupervised learning]]"
foundationalPaper: "Reducing the Dimensionality of Data with Neural Networks (Hinton & Salakhutdinov, 2006)"
keyPapers: ["Learning Internal Representations by Error Propagation (Rumelhart, Hinton & Williams, 1986)", "Auto-Association by Multilayer Perceptrons (Bourlard & Kamp, 1988)"]
relatedTo: ["[[Dimensionality reduction]]", "[[Feature learning]]", "[[Representation learning]]"]
broader: "[[artificial neural network]]"
inferred:skos:ancestor:
  - "[[Deep learning]]"
  - "[[artificial neural network]]"
  - "[[machine learning]]"
---

![Autoencoder Thumbnail](https://upload.wikimedia.org/wikipedia/commons/3/37/Autoencoder_schema.png)
[Autoencoder](https://en.wikipedia.org/wiki/Autoencoder)

# Autoencoder

The concept of autoencoders originated from the work of Rumelhart, Hinton, and Williams (1986) in "Learning Internal Representations by Error Propagation," where they introduced the idea of using neural networks to learn compressed representations of input data.

As defined by Hinton and Salakhutdinov in their seminal 2006 Science paper "Reducing the Dimensionality of Data with Neural Networks," an autoencoder is "a neural network that is trained to attempt to copy its input to its output" with the constraint that it must pass through a bottleneck layer with fewer units than the input.

## Original Definition

From Hinton & Salakhutdinov (2006):
"We describe an effective way of initializing the weights that allows deep autoencoder networks to learn low-dimensional codes that work much better than principal components analysis as a tool to reduce the dimensionality of data."

The autoencoder consists of:
1. **Encoder function**: f(x) that maps input x to a hidden representation h
2. **Decoder function**: g(h) that maps the hidden representation back to a reconstruction r
3. **Loss function**: L(x,r) that measures the reconstruction error

Bourlard and Kamp (1988) formally demonstrated that autoencoders with linear activations learn the same subspace as PCA, establishing the connection between autoencoders and classical dimensionality reduction techniques.

The foundational insight was that by constraining the network to pass through a bottleneck (a layer with fewer neurons than the input), the network is forced to learn a compressed representation that captures the most salient features of the data.

## Historical Significance

The 2006 paper by Hinton and Salakhutdinov was groundbreaking because it showed how to effectively train deep autoencoders using a layer-wise pretraining approach, which helped revive interest in deep neural networks and sparked the deep learning revolution.
