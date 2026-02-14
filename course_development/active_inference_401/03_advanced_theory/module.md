# Module 03: Perception in 401

## Learning Objectives

1.  Define **Perception** within the context of 401.
2.  Analyze how Perception interacts with other components of the Active Inference framework.
3.  Apply specific constraints of 401 to the formal definition of Perception.

## Introduction

This module explores **Perception**. In the **401** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Perception is a critical component of the 8-part Active Inference spine, bridging the gap between Neuroscientific Frontiers and Research Methods.

The advanced theory unit is where Active Inference meets its most rigorous mathematical and theoretical extensions. At the PhD level, students are expected to work with the full apparatus of variational inference on continuous and discrete state spaces, understand the relationship between Active Inference and adjacent formalisms (control theory, information geometry, statistical mechanics), and critically evaluate theoretical proposals that extend the framework into new domains. Perception, treated here as advanced theory, moves far beyond introductory treatments of Bayesian inference into the deep structure of how generative models can be specified, inverted, and compared.

Across the eight modules, the advanced theory unit covers: systems theory through the lens of nonequilibrium steady-state thermodynamics and the fluctuation theorems; agents formalized through information geometry on statistical manifolds; perception as exact and approximate inference with renormalization group methods; cognition as Bayesian model comparison and structure learning; action through stochastic optimal control and the complete class theorem; learning as structure learning and hyperparameter optimization; communication through multi-agent generative models and the free energy of a group; and planning through sophisticated inference and the relationship between expected free energy, KL control, and risk-sensitive control.

## Key Concepts

### 1. Perception as a Markov Blanket Boundary
How does Perception define the boundary between the agent and the environment?

### 2. Generative Models of Perception
What parameters involved in Perception must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Perception drive the perception-action loop?

## Applications

In 401, we see Perception manifest in:
*   **Specific Example 1**: Generalised filtering and dynamic expectation maximization (DEM) as advanced inference schemes for continuous-state Active Inference (Friston, Trujillo-Barreto, & Daunizeau, 2008). Unlike standard Kalman filtering, DEM performs inference over generalised coordinates of motion (position, velocity, acceleration, and higher orders), enabling the agent to track the smooth trajectory of hidden causes in the environment. The mathematical formulation requires students to work with generalised state-space models, embedding ordinary differential equations within a variational framework. A key theoretical result is that DEM subsumes Kalman-Bucy filtering as a special case when generalised coordinates are truncated at zeroth order. Students should derive this relationship formally and explore the conditions under which higher-order generalised coordinates improve inference, connecting to empirical applications in DCM (dynamic causal modeling) for fMRI and EEG source reconstruction.
*   **Specific Example 2**: The deep temporal model framework for discrete-state Active Inference (Friston et al., 2017, "Active Inference: A Process Theory"), which introduces hierarchical depth in both space and time. In this formulation, each level of the generative model operates at a different temporal scale, with higher levels generating the priors for lower-level transitions. Perception at the lowest level unfolds rapidly (e.g., inferring phonemes from acoustic features), while higher levels unfold more slowly (e.g., inferring the topic of a conversation). The mathematical structure involves Bayesian model reduction for efficient structure learning and marginal message passing for scalable inference. Students should compare this approach to hidden Markov models, hierarchical HMMs, and deep temporal models in machine learning (e.g., clockwork RNNs, hierarchical recurrent networks), identifying what Active Inference adds beyond existing sequence modeling frameworks and where it faces computational challenges.

## Conclusion

Understanding Perception allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
