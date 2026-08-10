---
foundationalPaper: Learning Internal Representations by Error Propagation (Rumelhart, Hinton & Williams, 1986)
keyPapers:
  - "Perceptrons: An Introduction to Computational Geometry (Minsky & Papert, 1969)"
  - "Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences (Werbos, 1974)"
typeOf: "[[Neural network models]]"
composedOf:
  - "[[Layer]]"
  - "[[Artificial neuron]]"
  - "[[Activation function]]"
enables:
  - "[[Universal approximation]]"
  - "[[Non-linear classification]]"
  - "[[Feature learning]]"
trainedBy: "[[backpropagation]]"
broader: "[[artificial neural network]]"
inferred:skos:ancestor:
  - "[[AI]]"
  - "[[Artificial Intelligence (AI)]]"
  - "[[Deep learning]]"
  - "[[artificial neural network]]"
  - "[[machine learning]]"
---
The Multilayer Perceptron resolved the limitations of single-[[layer]] perceptrons identified by Minsky and Papert, becoming the foundation of modern neural networks.

## Original Definition

From Rumelhart, Hinton & Williams (1986):
"We describe a new learning procedure, back-propagation, for networks of neuron-like units. The procedure repeatedly adjusts the [[weights]] of the connections in the network so as to minimize a [[measure]] of the difference between the actual [[output]] [[vector]] of the net and the desired [[output]] [[vector]]."

## Historical [[context]]

The MLP emerged from a crisis in neural network research:
1. **Perceptron Limitations (1969)**: Minsky & Papert showed single layers couldn't solve XOR
2. **Solution [[concept]] (1970s)**: Multiple layers could overcome limitations
3. **Training Breakthrough (1986)**: [[backpropagation]] made training feasible

## Architecture

From the original paper:
"A multilayer network consists of:
- A [[layer]] of input units
- One or more layers of hidden units
- A [[layer]] of [[output]] units
Each unit in one [[layer]] is connected to each unit in the next [[layer]]."

Mathematical representation:
[[Layer]] 1: h₁ = f₁(W₁x + b₁)
[[Layer]] 2: h₂ = f₂(W₂h₁ + b₂)
...
[[Output]]: y = fₙ(Wₙhₙ₋₁ + bₙ)

## Universal Approximation

From Cybenko (1989) and Hornik (1991):
"Standard multilayer feedforward networks with as few as one hidden [[layer]] using arbitrary squashing [[functions]] are capable of approximating any Borel measurable function from one finite dimensional space to another to any desired [[degree]] of [[accuracy]]."

## Training [[Process]]

The key innovation from Rumelhart et al.:
1. Forward pass: Compute outputs
2. Compute error: E = ½Σ(tᵢ - yᵢ)²
3. Backward pass: Propagate error gradients
4. Update [[weights]]: Δwᵢⱼ = -η∂E/∂wᵢⱼ

## Key [[Properties]]

1. **Non-linearity**: Activation [[functions]] enable complex mappings
2. **Hidden Representations**: Learn features automatically
3. **Scalability**: Can be extended to many layers
4. **Generality**: Applicable to various tasks

## Historical Significance

The MLP breakthrough:
- Resolved the XOR problem
- Revived neural network research
- Established foundations for [[deep learning]]
- Demonstrated automatic [[feature]] learning

As Rumelhart et al. concluded:
"The learning procedure is able to discover internal representations which allow it to learn complex nonlinear mappings."

## Modern Impact

MLPs remain fundamental:
- Basic building blocks in [[deep learning]]
- Components of more complex architectures
- Benchmark for new techniques
- Educational tool for understanding neural networks

The MLP architecture, combined with [[backpropagation]], marked the beginning of the modern neural network era.
