# Module 04: Cognition in 401

## Learning Objectives

1.  Define **Cognition** within the context of 401.
2.  Analyze how Cognition interacts with other components of the Active Inference framework.
3.  Apply specific constraints of 401 to the formal definition of Cognition.

## Introduction

This module explores **Cognition**. In the **401** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Cognition is a critical component of the 8-part Active Inference spine, bridging the gap between Advanced Theory and course synthesis.

The research methods unit is the capstone of the 401 curriculum, equipping PhD students with the practical methodological toolkit needed to conduct original Active Inference research. Having traversed philosophical foundations, neuroscientific frontiers, and advanced theory, students now learn to design experiments, build computational models, analyze data, and write papers that contribute to the Active Inference literature. Cognition, as treated in this unit, refers to the cognitive aspects of scientific practice itself: how researchers form hypotheses (generative models of their domain), gather evidence (experiments as active inference), update their beliefs (Bayesian data analysis), and communicate findings (scientific publication as shared model construction).

The eight modules cover: systems-level research design (how to define the system under study and choose appropriate scales of analysis); agent modeling (specifying generative models for simulated and real agents); perceptual paradigms (designing experiments that probe predictive processing); cognitive modeling (Bayesian model comparison and computational phenotyping); action experiments (motor control paradigms and active sensing tasks); learning studies (longitudinal designs and parameter estimation); communication research (multi-agent paradigms and social neuroscience methods); and planning studies (temporal discounting tasks, prospection paradigms, and model-based decision-making experiments).

## Key Concepts

### 1. Cognition as a Markov Blanket Boundary
How does Cognition define the boundary between the agent and the environment?

### 2. Generative Models of Cognition
What parameters involved in Cognition must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Cognition drive the perception-action loop?

## Applications

In 401, we see Cognition manifest in:
*   **Specific Example 1**: Computational phenotyping using Active Inference models fitted to individual behavioral data (Schwartenbeck & Friston, 2016). In this research methodology, a generative model of a task (e.g., a reversal learning paradigm or a trust game) is specified at the group level, and subject-specific parameters (prior precision, learning rate, temporal horizon) are estimated via variational Laplace or sampling methods. These fitted parameters serve as computational phenotypes that can be compared across clinical populations. For example, Adams et al. (2016) used this approach to show that patients with schizophrenia exhibit aberrant precision weighting of sensory prediction errors, providing a computational account of positive symptoms. PhD students should implement this pipeline end-to-end: specify a task-specific generative model, simulate synthetic data to validate parameter recoverability, fit the model to empirical behavioral data, and perform Bayesian model comparison to evaluate competing hypotheses about cognitive mechanisms.
*   **Specific Example 2**: Dynamic causal modeling (DCM) as the empirical bridge between Active Inference theory and neuroimaging data (Friston, Harrison, & Penny, 2003). DCM inverts a generative model of neural dynamics to infer effective connectivity from fMRI, EEG, or MEG data. At the 401 level, students must understand DCM not merely as a neuroimaging analysis tool but as an application of the same variational principles that underlie Active Inference itself -- the researcher performing DCM is, in a precise sense, performing active inference over brain connectivity parameters. Advanced topics include spectral DCM for resting-state fMRI, regression DCM for large-scale networks, and the recent development of deep temporal models for DCM that allow inference over hierarchically structured neural dynamics. Students should critically evaluate the assumptions of DCM (bilinear vs. nonlinear models, the hemodynamic forward model, the mean-field approximation) and design a study protocol that uses DCM to test a specific Active Inference hypothesis about neural computation.

## Conclusion

Understanding Cognition allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
