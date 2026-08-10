---
foundationalPaper: Discriminability-Based Transfer between Neural Networks (Pratt, 1993)
keyPapers:
  - A Survey on Transfer Learning (Pan & Yang, 2010)
  - How transferable are features in deep neural networks? (Yosinski et al., 2014)
  - Deep Learning of Representations for Unsupervised and Transfer Learning (Bengio, 2012)
typeOf: "[[Machine learning]] technique"
implements: "[[Fine-tuning]]"
usedIn:
  - "[[Deep learning]]"
  - "[[Neural network models]]"
  - "[[computer vision]]"
  - "[[Natural Language Processing]]"
benefitFrom: "[[Pre-trained models]]"
reducesNeedFor: "[[Large datasets]]"
accelerates: "[[Model training]]"
broader: "[[Deep learning]]"
inferred:skos:ancestor:
  - "[[Artificial Intelligence (AI)]]"
  - "[[Deep learning]]"
  - "[[machine learning]]"
---

# Transfer Learning

The concept of transfer learning was first formalized in machine learning by Lorien Pratt in 1993, though the idea of knowledge transfer has roots in cognitive science and psychology.

## Original Definition

From Pratt (1993):
"Transfer is the use of knowledge learned in one or more source tasks to bias learning and hence to improve performance in a related target task... Transfer between neural networks is effected by using the weights from one or more source networks to initialize the weights of a target network."

From Pan & Yang (2010) in their comprehensive survey:
"Transfer learning aims to extract the knowledge from one or more source tasks and applies the knowledge to a target task... In contrast to traditional machine learning methods that learn each task from scratch, transfer learning uses the previously learned knowledge to help learning the new task."

## Historical Development

1. **Early Neural Network Transfer (Pratt, 1993)**: Introduced weight transfer between neural networks
2. **Multi-task Learning (Caruana, 1997)**: Parallel learning of related tasks
3. **Domain Adaptation (2000s)**: Adapting models across different data distributions
4. **Deep Transfer Learning (2010s)**: Transfer learning with deep neural networks

## Key Concepts

As established in the foundational literature:
1. **Source Domain/Task**: Where the knowledge comes from
2. **Target Domain/Task**: Where the knowledge is applied
3. **Negative Transfer**: When transfer hurts performance
4. **Domain Adaptation**: Handling differences between domains
5. **Feature Transfer**: Transferring learned representations

## Types of Transfer Learning

From Pan & Yang's taxonomy:
1. **Inductive Transfer**: Different tasks, labeled data in target domain
2. **Transductive Transfer**: Same task, different domains
3. **Unsupervised Transfer**: No labels in either domain

## Breakthrough in Deep Learning

Yosinski et al. (2014) demonstrated:
"We quantify the generality versus specificity of neurons in each layer of a deep convolutional neural network and report a few surprising results. Transferability is negatively affected by two distinct issues: (1) the specialization of higher layer neurons to their original task at the expense of performance on the target task, and (2) optimization difficulties related to splitting networks between co-adapted neurons."

## Historical Significance

Transfer learning revolutionized deep learning by:
- Enabling effective learning with limited data
- Reducing computational requirements
- Demonstrating that deep networks learn hierarchical, transferable features
- Making deep learning practical for many real-world applications

As Bengio (2012) noted: "Deep learning algorithms have been found to be able to discover useful intermediate representations, and this is what makes transfer learning successful."
