---
subclassOf: "[[ML models]]"
composed_of: "[[Artificial neuron]]"
uses: "[[Weights]]"
includes: "[[bias]]"
enables: "[[Deep learning]]"
broader: "[[ML models]]"
inferred:skos:ancestor: "[[ML models]]"
---

# Neural Network Models

Neural networks are computational models inspired by the structure and function of biological neural networks in animal brains. They consist of interconnected nodes (artificial neurons) organized in layers that process information through weighted connections.

## Architecture Components

### Basic Building Blocks
1. **Input Layer**: Receives raw data features
2. **Hidden Layers**: Process information through transformations
3. **Output Layer**: Produces final predictions
4. **[[Artificial neuron]]**: Basic computational unit
5. **[[Weights]]**: Connection strengths between neurons
6. **[[bias]]**: Offset terms for each neuron

### Key Concepts
- **Activation Functions**: Non-linear transformations (ReLU, Sigmoid, Tanh)
- **Forward Propagation**: Data flow from input to output
- **Backpropagation**: Algorithm for updating weights during training
- **Loss Function**: Measures prediction error
- **Gradient Descent**: Optimization algorithm

## Types of Neural Networks

### Feedforward Networks
- **Multilayer Perceptron (MLP)**: Basic fully-connected network
- **Convolutional Neural Networks (CNN)**: Specialized for image processing
- **Recurrent Neural Networks (RNN)**: Process sequential data

### Advanced Architectures
- **[[Transformers]]**: Attention-based models for sequence processing
- **Autoencoders**: Unsupervised learning of efficient representations
- **Generative Adversarial Networks (GANs)**: Generate new data samples
- **Graph Neural Networks (GNNs)**: Process graph-structured data

## Training Process

1. **Initialization**: Random weight assignment
2. **Forward Pass**: Compute predictions
3. **Loss Calculation**: Measure error
4. **Backward Pass**: Compute gradients
5. **Weight Update**: Adjust parameters
6. **Iteration**: Repeat until convergence

## Applications

- Computer Vision
- Natural Language Processing
- Speech Recognition
- Time Series Forecasting
- Recommendation Systems
- Anomaly Detection

## Challenges

- **Vanishing/Exploding Gradients**: Training stability issues
- **Overfitting**: Poor generalization to new data
- **Computational Cost**: High resource requirements
- **Interpretability**: "Black box" nature
- **Data Requirements**: Need for large training datasets

See also: [[Deep learning]], [[Backpropagation]], [[Convolutional neural networks]], [[Transformers]]
