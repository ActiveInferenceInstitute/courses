# Module 01: Systems

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Dynamic Causal Modelling and Model Inversion

Part of **Research Methods**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Dynamic Causal Modelling and Model Inversion |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Implementing DCM for fMRI and EEG |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Apply** Dynamic Causal Modelling (DCM) to neuroimaging data, specifying the generative model (neural state equation, hemodynamic forward model, observation equation) and performing model inversion via variational Laplace
2. **Analyze** the mathematical structure of model inversion: derive the variational Laplace algorithm, showing how it iteratively updates the posterior over model parameters by jointly optimizing the variational free energy with respect to sufficient statistics (mean and covariance)
3. **Evaluate** DCM results including effective connectivity estimates, Bayesian model comparison across competing network architectures, and parametric empirical Bayes for group-level inference
4. **Design** a complete DCM analysis pipeline for a novel dataset, from experimental paradigm specification through preprocessing, model specification, inversion, and family-wise model comparison

## Prerequisites

- Graduate-level neuroimaging methods (fMRI BOLD signal, EEG/MEG source reconstruction, experimental design)
- Proficiency in MATLAB/SPM or equivalent for DCM implementation
- Understanding of variational Bayes and the Laplace approximation

## Key References

- Friston, K. J. et al. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273--1302.
- Stephan, K. E. et al. (2010). Ten simple rules for dynamic causal modelling. *NeuroImage*, 49(4), 3099--3109.
- Penny, W. D. et al. (2004). Comparing dynamic causal models. *NeuroImage*, 22(3), 1157--1172.
- Friston, K. J. et al. (2007). Variational free energy and the Laplace approximation. *NeuroImage*, 34(1), 220--234.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
