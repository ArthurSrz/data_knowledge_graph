---
foundationalPaper: "Communication-Efficient Learning of Deep Networks from Decentralized Data (McMahan et al., 2017)"
keyPapers: ["Federated Optimization: Distributed Machine Learning for On-Device Intelligence (Konečný et al., 2016)", "Federated Learning: Challenges, Methods, and Future Directions (Li et al., 2020)", "Advances and Open Problems in Federated Learning (Kairouz et al., 2019)"]
protects: "[[Data privacy]]"
enables: ["[[Decentralized learning]]", "[[Privacy-preserving ML]]", "[[Edge computing]]"]
challenges: ["[[Communication efficiency]]", "[[System heterogeneity]]", "[[Statistical heterogeneity]]"]
algorithms: ["[[FedAvg]]", "[[FedProx]]", "[[FedSGD]]"]
broader: "[[machine learning]]"
inferred:skos:ancestor:
  - "[[machine learning]]"
---

# Federated Learning

Federated Learning is a distributed machine learning approach that enables training models on decentralized data while preserving privacy.

## Original Definition

From McMahan et al. (2017):
"We term our approach Federated Learning, since the learning task is solved by a loose federation of participating devices (clients) which are coordinated by a central server."

Key principle:
"The data remains distributed on the clients, and the server never stores or even sees the data. Instead, each client computes an update to the current model maintained by the server, and only this update is communicated."

## Historical Context

Federated Learning emerged from:
1. Growing privacy concerns
2. GDPR and data regulations
3. Edge computing proliferation
4. Mobile device capabilities

## Core Algorithm - FedAvg

From McMahan et al.:
```
Server executes:
  Initialize w₀
  for each round t = 1, 2, ... do
    m ← max(C·K, 1)
    Sₜ ← random set of m clients
    for each client k ∈ Sₜ in parallel do
      wₜ₊₁ᵏ ← ClientUpdate(k, wₜ)
    wₜ₊₁ ← Σₖ (nₖ/n)wₜ₊₁ᵏ

ClientUpdate(k, w):
  B ← split Pₖ into batches
  for each local epoch i from 1 to E do
    for batch b ∈ B do
      w ← w - η∇ℓ(w; b)
  return w
```

## Key Challenges

### 1. Communication Efficiency
From Konečný et al. (2016):
"Communication constraints require developing algorithms that can reduce the number of communication rounds and/or the size of messages transmitted per round."

### 2. Statistical Heterogeneity
"The data across devices is non-IID (not independent and identically distributed), which can cause model divergence and slow convergence."

### 3. System Heterogeneity
"Devices vary in computational power, network connectivity, and availability, requiring robust asynchronous algorithms."

## Privacy Guarantees

From Kairouz et al. (2019):
1. **Data Minimization**: Raw data never leaves devices
2. **Secure Aggregation**: Encrypted model updates
3. **Differential Privacy**: Add noise to updates
4. **Secure Multi-party Computation**: Cryptographic protocols

## Applications

1. **Mobile Keyboards**: Next-word prediction
2. **Healthcare**: Patient data analysis
3. **Financial Services**: Fraud detection
4. **IoT**: Smart home devices
5. **Autonomous Vehicles**: Shared learning

## Variations and Extensions

### 1. Vertical Federated Learning
Different features across organizations

### 2. Federated Transfer Learning
Knowledge transfer across domains

### 3. Hierarchical Federated Learning
Multi-tier aggregation structure

## Historical Significance

Federated Learning revolutionized:
- Privacy-preserving machine learning
- Decentralized AI systems
- Edge intelligence
- Collaborative learning paradigms

As McMahan noted: "Federated Learning makes it possible to train models on data that cannot be centralized due to privacy, regulatory, or practical constraints."

## Modern Developments

- Personalized federated learning
- Federated reinforcement learning
- Cross-silo vs cross-device FL
- Federated analytics
- Production systems (Google, Apple)

The field continues to evolve, addressing challenges in:
- Robustness to attacks
- Fairness across clients
- Efficiency improvements
- Regulatory compliance
