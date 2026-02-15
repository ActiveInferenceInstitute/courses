# Notation Table: Active Inference 101: College First Semester

> Standard symbols and notation used throughout the curriculum.
> Level: College 1st semester undergraduates

## Core Symbols

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| s | Hidden state | The true state of the world, not directly observable | Course 1, M1 |
| o | Observation | Sensory data received by the agent | Course 1, M3 |
| a | Action | An intervention the agent makes on the world | Course 1, M5 |
| pi | Policy | A sequence of planned actions [a_0, a_1, ..., a_T] | Course 1, M8 |

## Probability and Inference

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| P(o, s) | Joint probability | The generative model's probability of observations and states together | Course 3, M1 |
| P(o \| s) | Likelihood | Probability of observing o given hidden state s | Course 3, M1 |
| P(s) | Prior | The agent's belief about states before seeing any observation | Course 3, M2 |
| P(s \| o) | Posterior | Updated belief about states after observing o (via Bayes' theorem) | Course 3, M3 |
| q(s) | Approximate posterior | The agent's tractable approximation to the true posterior | Course 3, M3 |
| D_KL(q \|\| p) | KL divergence | Measures how different distribution q is from distribution p; always >= 0 | Course 3, M3 |

## Generative Model Components (POMDP)

| Symbol | Plain English | Formal Meaning | Dimensions | First Introduced |
| --- | --- | --- | --- | --- |
| A | Likelihood matrix | P(o \| s); maps hidden states to expected observations | num_obs x num_states | Course 3, M1 |
| B | Transition matrix | P(s_t \| s_{t-1}, a); how states change given actions | num_states x num_states (per action) | Course 3, M2 |
| C | Preference vector | ln P(o); log prior preferences over observations | num_obs x 1 | Course 3, M5 |
| D | Initial state prior | P(s_0); prior belief about the initial hidden state | num_states x 1 | Course 3, M2 |

## Free Energy Quantities

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| F | Variational free energy | Upper bound on surprise; F = E_q[ln q(s) - ln P(o, s)] | Course 3, M4 |
| G(pi) | Expected free energy | Expected future free energy under policy pi | Course 3, M5 |
| -ln P(o) | Surprise | Negative log probability of an observation under the model | Course 1, M3 |
| H[q] | Entropy | Uncertainty of distribution q; H = -sum q(s) ln q(s) | Course 3, M3 |

## Free Energy Decompositions

| Decomposition | Components | Interpretation |
| --- | --- | --- |
| F = Complexity - Accuracy | Complexity = D_KL(q(s) \|\| P(s)); Accuracy = E_q[ln P(o \| s)] | Trade-off between fitting data and staying close to prior |
| F = Energy - Entropy | Energy = -E_q[ln P(o, s)]; Entropy = -E_q[ln q(s)] | Balancing internal energy with uncertainty |
| G = Pragmatic + Epistemic | Pragmatic = -E_q[ln P(o \| C)]; Epistemic = -E_q[information gain] | Balancing reward-seeking with curiosity |

## Learning Parameters

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| alpha | Concentration parameters | Dirichlet parameters storing accumulated evidence for A matrix | Course 3, M6 |
| eta | Learning rate | Scalar controlling how much each observation updates parameters (0 < eta <= 1) | Course 4, M6 |
| gamma | Precision (action) | Inverse temperature for softmax policy selection; higher = more exploitative | Course 3, M5 |

## Neuroscience Correspondences

| Mathematical Symbol | Neural Correlate | Course 2 Module |
| --- | --- | --- |
| q(s) | Neural population activity encoding beliefs | M3 (Perception) |
| Prediction error (o - E_q[o]) | Superficial pyramidal cell activity | M3 (Perception) |
| Predictions (E_q[o]) | Deep pyramidal cell activity (top-down signals) | M3 (Perception) |
| Precision (gamma) | Synaptic gain modulation (NMDA receptors) | M4 (Cognition) |
| Dopamine | Precision on prior preferences (C vector) | M5 (Action) |
| Norepinephrine | Precision on sensory evidence | M3 (Perception) |
| Hebbian plasticity | Parameter learning (A matrix updates) | M6 (Learning) |

## Conventions

- **Bold** symbols (e.g., **A**, **B**) denote matrices
- Lower-case letters (s, o, a) denote variables
- Upper-case letters (P, F, G) denote distributions or functions
- Greek letters (pi, gamma, eta, alpha) denote parameters
- Subscripts denote time (s_t) or indices (o_i)
- Superscripts denote policy (s^pi) or layer in hierarchy

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Cross-Course Map](./cross_course_map.md)
- [Home](../README.md)
