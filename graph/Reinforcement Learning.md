---
foundationalPaper: "Reinforcement Learning: A Survey (Kaelbling, Littman & Moore, 1996)"
keyPapers:
  - Learning from Delayed Rewards (Sutton, 1988)
  - Q-Learning (Watkins, 1989)
  - "Reinforcement Learning: An Introduction (Sutton & Barto, 1998)"
typeOf: "[[Machine learning paradigm]]"
inspiredBy:
  - "[[Behaviorist psychology]]"
  - "[[Dynamic programming]]"
  - "[[Control theory]]"
keyComponents:
  - "[[Agent 1]]"
  - "[[Environment]]"
  - "[[State]]"
  - "[[Action]]"
  - "[[Reward]]"
  - "[[Policy]]"
algorithms:
  - "[[Q-learning]]"
  - "[[SARSA]]"
  - "[[Policy gradient]]"
  - "[[Actor-critic methods]]"
broader: "[[machine learning]]"
inferred:skos:ancestor:
  - "[[machine learning]]"
---

# Reinforcement Learning

Reinforcement Learning emerged from the intersection of dynamic programming, control theory, and animal learning theory. The term was first used in its current context by Minsky (1961), but the field was formalized in the 1980s and 1990s.

## Original Definition

From Sutton & Barto (1998):
"Reinforcement learning is learning what to do—how to map situations to actions—so as to maximize a numerical reward signal. The learner is not told which actions to take, but instead must discover which actions yield the most reward by trying them."

From Kaelbling, Littman & Moore (1996):
"Reinforcement learning is the problem faced by an agent that must learn behavior through trial-and-error interactions with a dynamic environment."

## Historical Development

1. **Early Foundations (1950s)**: 
   - Bellman's dynamic programming
   - Minsky's SNARC (1951)
   - Samuel's checkers player (1959)

2. **Temporal Difference Learning (1988)**:
   Sutton: "Temporal-difference learning is a prediction method. It has been mostly used for solving the reinforcement learning problem... TD learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas."

3. **Q-Learning (1989)**:
   Watkins: "Q-learning... provides agents with the capability of learning to act optimally in Markovian domains by experiencing the consequences of actions, without requiring them to build maps of the domains."

## Mathematical Framework

The core problem is formalized as a Markov Decision Process (MDP):
- S: Set of states
- A: Set of actions
- P: State transition probabilities
- R: Reward function
- γ: Discount factor

The goal is to find a policy π that maximizes the expected cumulative reward:
V^π(s) = E[Σ_{t=0}^∞ γ^t r_t | s_0 = s, π]

## Key Concepts

1. **Exploration vs. Exploitation**: The fundamental dilemma identified by Sutton
2. **Value Functions**: Estimate of future rewards
3. **Policy**: Mapping from states to actions
4. **Temporal Difference**: Learning from differences between predictions

## Historical Significance

Reinforcement Learning represented a paradigm shift in machine learning:
- Learning from interaction rather than labeled examples
- Delayed rewards and sequential decision making
- Connection between artificial intelligence and neuroscience
- Foundation for modern AI achievements (game playing, robotics)

As Sutton & Barto noted: "Reinforcement learning is the first field to seriously address the computational issues that arise when learning from interaction with an environment in order to achieve long-term goals."
