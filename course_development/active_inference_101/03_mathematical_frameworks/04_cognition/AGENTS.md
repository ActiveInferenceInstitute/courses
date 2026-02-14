# Station: Cognition (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: POMDPs, A/B/C/D matrices, state inference over time, message passing, information gain
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module formalizes cognition within the POMDP framework. Content should:

1. **Define the full POMDP generative model**: Specify all components (A, B, C, D matrices) and show how they combine into the complete generative model for decision-making under uncertainty.
2. **Define key terms precisely**:
   - **POMDP**: Partially Observable Markov Decision Process -- a generative model where the agent cannot directly observe hidden states but must infer them from noisy observations
   - **A matrix (likelihood)**: P(o|s) mapping from hidden states to observations
   - **B matrix (transitions)**: P(s_t|s_{t-1}, a) mapping from previous states and actions to next states
   - **C vector (preferences)**: The agent's preferred observations, encoding goals as prior expectations
   - **D vector (initial prior)**: P(s_1) -- the agent's initial belief about hidden states
3. **Introduce message passing**: Show how belief updating in a POMDP involves forward (filtering) and backward (smoothing) passes through time.
4. **Connect to information gain**: Define mutual information and show how it quantifies the epistemic value of observations.

## Active Inference Integration

- The POMDP is the canonical generative model for discrete Active Inference (Parr et al., 2022, Chapter 5)
- Cognition involves inference over hidden states across time, not just at a single moment
- Information gain (expected reduction in entropy of q(s)) drives epistemic, curiosity-driven behavior

## Assessment Alignment

Questions should test the ability to:
- Specify the A, B, C, D matrices for a given scenario (e.g., the T-maze task)
- Perform one step of state inference given a POMDP and an observation sequence
- Calculate information gain for different possible observations

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
