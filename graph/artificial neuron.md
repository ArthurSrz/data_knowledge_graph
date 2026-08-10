---
foundationalPaper: A Logical Calculus of Ideas Immanent in Nervous Activity (McCulloch & Pitts, 1943)
keyPapers:
  - "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain (Rosenblatt, 1958)"
  - "Perceptrons: An Introduction to Computational Geometry (Minsky & Papert, 1969)"
inventedBy:
  - "[[Warren McCulloch]]"
  - "[[Walter Pitts]]"
inspiredBy: "[[Biological neuron]]"
components:
  - "[[Weights]]"
  - "[[bias]]"
  - "[[Activation function]]"
  - "[[Summation function]]"
usedIn:
  - "[[Neural network models]]"
  - "[[Perceptron]]"
  - "[[multilayer perceptron]]"
broader: "[[artificial neural network]]"
inferred:skos:ancestor:
  - "[[Deep learning]]"
  - "[[artificial neural network]]"
  - "[[machine learning]]"
---

# Artificial Neuron

The artificial neuron was first proposed by Warren McCulloch and Walter Pitts in 1943 as a mathematical model of biological neurons.

## Original Definition

From McCulloch & Pitts (1943):
"Because of the 'all-or-none' character of nervous activity, neural events and the relations among them can be treated by means of propositional logic... Every net, if furnished with a tape, scanners connected to afferents, and suitable efferents to perform the necessary motor-operations, can compute any computable number."

## Historical Development

1. **McCulloch-Pitts Neuron (1943)**: Binary threshold unit
2. **Perceptron (Rosenblatt, 1958)**: Added learning capability
3. **ADALINE (Widrow & Hoff, 1960)**: Continuous outputs
4. **Modern Artificial Neuron**: Non-linear activation functions

## Mathematical Model

The McCulloch-Pitts neuron computes:
y = θ(Σᵢ wᵢxᵢ - T)

Where:
- xᵢ are binary inputs
- wᵢ are binary weights
- T is the threshold
- θ is the step function

Rosenblatt's Perceptron generalized this:
y = f(Σᵢ wᵢxᵢ + b)

Where:
- f is an activation function
- b is the bias term
- weights are real-valued

## Key Components

1. **Inputs**: Correspond to dendrites
2. **Weights**: Represent synaptic strengths
3. **Summation**: Models spatial integration
4. **Activation Function**: Models neural firing
5. **Output**: Corresponds to axon signal

## Biological Inspiration

From McCulloch & Pitts:
"The neuron is the base logic unit in the brain. It receives signals from other neurons, processes them, and sends signals to other neurons. The 'all-or-none' law of nervous activity is sufficient to ensure that the activity of any neuron may be represented as a proposition."

## Historical Significance

The artificial neuron was groundbreaking because:
- First mathematical model of neural computation
- Showed how logic could emerge from neural structure
- Demonstrated computational universality
- Founded the field of neural networks
- Connected neuroscience, logic, and computation

## Modern Form

Today's artificial neuron:
- Uses continuous values
- Employs various activation functions (ReLU, sigmoid, tanh)
- Can have complex structures (LSTM units, attention mechanisms)
- Forms building blocks of deep neural networks

As McCulloch noted: "What we thought we were doing... was treating the brain as a Turing machine."

## Related concepts

- [[Layer]] - Neurons are organized into layers
- [[Neuron layer]] - Collection of artificial neurons
- [[multilayer perceptron]] - Network with multiple neuron layers
- [[ReLU activation function]] - Common activation function
- [[Sigmoid function]] - Another activation function
- [[biological neural network]] - Inspiration for artificial neurons
- [[Neural network models]] - Built from artificial neurons
