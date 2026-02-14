# Station: Action (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Action
- **Subtitle**: Designing Motor Control and Decision-Making Experiments
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must cover the design of experiments that test active inference accounts of motor control and decision-making, with particular emphasis on paradigms that can distinguish active inference predictions from those of alternative frameworks (optimal control, reinforcement learning, drift-diffusion models). Classic motor control paradigms — reaching under force-field perturbation (Shadmehr & Mussa-Ivaldi, 1994), saccade adaptation, grip force modulation — provide well-characterized behavioral signatures that active inference models make specific predictions about (e.g., the role of precision in movement vigor, the relationship between sensory attenuation and self-generated movement). For decision-making, students should learn to fit active inference models to choice and reaction time data, comparing them against drift-diffusion models (DDM) and standard RL models. Key methodological topics include: How do active inference and optimal control make different predictions about movement variability and correction? When does the expected free energy formulation make qualitatively different predictions from reward maximization? How do you handle the computational challenge of fitting continuous-state active inference models to motor data? Students should work through concrete examples of model fitting to behavioral data (Smith et al., 2022) and understand when active inference provides explanatory value beyond simpler accounts.

## Key Concepts

- **Reaching and grasping paradigms**: Force-field adaptation (Shadmehr & Mussa-Ivaldi, 1994), visuomotor rotation, grip force scaling — paradigms where active inference makes specific predictions about error correction, aftereffects, and the role of precision in motor planning
- **Saccade experiments**: Saccadic adaptation, anti-saccade tasks, and smooth pursuit as test beds for active inference models of oculomotor control; these paradigms allow tight control over sensory prediction errors and motor commands
- **Force field adaptation**: The paradigm of Shadmehr & Mussa-Ivaldi (1994) as a canonical test of internal model updating; active inference predicts that adaptation reflects updating of the generative model's transition dynamics ($\mathbf{B}$ matrices) rather than direct error correction
- **Drift-diffusion models (DDM)**: The DDM as the primary competitor for modeling reaction time and choice data; understanding when active inference and DDM make distinguishable predictions (e.g., speed-accuracy tradeoff, confidence ratings, changes of mind) and when they are empirically equivalent
- **Fitting active inference to behavioral data**: Practical methods for estimating active inference model parameters from trial-by-trial behavioral data — including maximum likelihood estimation, expectation-maximization, and hierarchical Bayesian approaches; software implementations in PyMDP (discrete) and custom code (continuous)
- **Active inference vs. optimal control**: Key experimental signatures that distinguish active inference from classical optimal control (LQR/LQG): active inference predicts that action minimizes sensory prediction error directly (proprioceptive predictions drive motor commands), whereas optimal control computes an explicit cost function; testable via perturbation experiments and movement variability analysis

## Key References

- Shadmehr, R., & Mussa-Ivaldi, F. A. (1994). Adaptive representation of dynamics during learning of a motor task. *Journal of Neuroscience*, 14(5), 3208-3224.
- Smith, R., Friston, K. J., & Whyte, C. J. (2022). A step-by-step tutorial on active inference and its application to empirical data. *Journal of Mathematical Psychology*, 107, 102632.
- Fountas, Z., Sajid, N., Mediano, P. A. M., & Friston, K. J. (2020). Deep active inference agents using Monte-Carlo methods. *Advances in Neural Information Processing Systems*, 33.
- Sajid, N., Ball, P. J., Parr, T., & Friston, K. J. (2021). Active inference: Demystified and compared. *Neural Computation*, 33(3), 674-712.
- Adams, R. A., Shipp, S., & Friston, K. J. (2013). Predictions not commands: Active inference in the motor system. *Brain Structure and Function*, 218(3), 611-643.
- Ratcliff, R., & McKoon, G. (2008). The diffusion decision model: Theory and data for two-choice decision tasks. *Neural Computation*, 20(4), 873-922.

## Prerequisite Modules

- Module 03: Perception (establishes DCM and the neuroimaging model comparison framework; action extends this to motor control and behavioral paradigms)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/05_action/module.md](../../03_advanced_theory/05_action/module.md)): Derives the path integral formulation of control and the relationship between KL control and active inference — this module designs experiments to test those theoretical predictions behaviorally
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/05_action/module.md](../../02_neuroscientific_frontiers/05_action/module.md)): Reviews spinal reflexes as prediction error minimization, cerebellar forward models, and the motor hierarchy — this module provides the experimental paradigms and model-fitting tools to test those neural implementations
- **Philosophical Foundations** ([../../01_philosophical_foundations/05_action/module.md](../../01_philosophical_foundations/05_action/module.md)): Examines enactivism, affordances, and the action-perception cycle — this module asks what experiments could distinguish the enactivist predictions of active inference from traditional motor planning accounts

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
