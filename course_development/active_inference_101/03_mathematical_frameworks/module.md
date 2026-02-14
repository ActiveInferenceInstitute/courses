# Module 03: Perception in 101

## Learning Objectives

1.  Define **Perception** within the context of 101.
2.  Analyze how Perception interacts with other components of the Active Inference framework.
3.  Apply specific constraints of 101 to the formal definition of Perception.

## Introduction

This module explores **Perception**. In the **101** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Perception is a critical component of the 8-part Active Inference spine, bridging the gap between Computational Neuroscience and Implementation.

This unit introduces the mathematical frameworks that formalize perception as approximate Bayesian inference. Building on the systems concepts and neuroscience foundations from the previous two units, we now give precise mathematical expression to ideas like "minimizing surprise" and "updating beliefs." Students will work with variational free energy, Kullback-Leibler divergence, and generative models expressed as probabilistic graphical models. The mathematics is kept at the level of multivariate calculus and introductory probability theory, with derivations presented step by step.

The eight modules in this unit follow the Active Inference spine through a mathematical lens. You will see how systems are formalized as random dynamical systems, how agents are described by their sufficient statistics, how perception reduces to variational message passing, how cognition emerges from hierarchical inference, how action follows from expected free energy minimization, how learning corresponds to parameter estimation, how communication maps onto shared generative models, and how planning is realized through temporal depth in policy evaluation.

## Key Concepts

### 1. Perception as a Markov Blanket Boundary
How does Perception define the boundary between the agent and the environment?

### 2. Generative Models of Perception
What parameters involved in Perception must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Perception drive the perception-action loop?

## Applications

In 101, we see Perception manifest in:
*   **Specific Example 1**: Visual perception of ambiguous figures (such as the Necker cube or the duck-rabbit illusion) provides an accessible mathematical example. The brain maintains two competing hypotheses (e.g., duck vs. rabbit) in its generative model, each with associated prior probabilities and likelihoods. Perception corresponds to variational inference over these hypotheses: the brain settles on the interpretation that minimizes variational free energy given the current sensory data. Bistable perception -- the spontaneous switching between interpretations -- can be modeled as transitions between local free energy minima, and students can work through the math by computing free energy for each hypothesis using simple Gaussian generative models.
*   **Specific Example 2**: Consider how you perceive speech in a noisy environment, such as understanding a friend at a loud party (the cocktail party problem). Mathematically, the auditory system implements a hierarchical generative model where higher levels predict phonemes and words, and lower levels predict spectral features of the acoustic signal. Perception is the process of inverting this model: given noisy sensory input, the brain uses variational inference to infer the most likely sequence of words. The precision (inverse variance) of prediction errors at each level is modulated by attention, which mathematically corresponds to optimizing the precision parameters of the variational distribution. Students can formalize this as a two-level generative model and compute how changing the signal-to-noise ratio affects the posterior beliefs.

## Conclusion

Understanding Perception allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
