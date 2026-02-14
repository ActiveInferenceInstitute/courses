# Station: Cognition (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Cognition
- **Subtitle**: Bayesian Model Comparison and Structure Learning in Practice
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must provide a thorough practical treatment of Bayesian model comparison as the primary inferential tool for adjudicating between competing cognitive models. Students should learn the distinction between fixed-effects BMS (appropriate when assuming a single model generated all subjects' data) and random-effects BMS (appropriate when different subjects may use different strategies; Stephan et al., 2009), including the computation of protected exceedance probability to guard against spurious confidence when model evidence is uniformly weak (Rigoux et al., 2014). The module should cover family-level inference for testing qualitative model features (e.g., "does the model need a precision parameter?" rather than "which exact model is best?"), the relationship between variational free energy $F$, BIC, AIC, and cross-validation as approximations to log model evidence, and the practical conditions under which each approximation is adequate or misleading. Critical attention must be given to model identifiability: when can two structurally different models produce indistinguishable predictions? Students should work through a complete BMS workflow in SPM, from model space definition through group-level inference, and understand the pitfalls of model comparison with misspecified model spaces (Piray et al., 2019).

## Key Concepts

- **Bayesian model selection (BMS)**: The framework for comparing models by their log model evidence $\ln p(o \mid m)$, approximated by the negative variational free energy $-F$; includes the distinction between fixed-effects (sum of log evidences) and random-effects (Dirichlet-multinomial model over model attributions) approaches
- **Family inference**: Grouping models into families that share a qualitative feature and comparing at the family level; useful when the model space is large and the question is about a structural feature rather than a specific parameterization
- **Protected exceedance probability**: A correction to the exceedance probability $\varphi_k = p(\text{model } k \text{ is most frequent})$ that accounts for the possibility that observed differences in model evidence are due to chance alone; computed by comparing against a null distribution of equal model frequencies (Rigoux et al., 2014)
- **Computational model comparison**: Practical considerations for defining a model space — ensuring the space is comprehensive (includes plausible alternatives), ensuring models are distinguishable (design optimization, parameter recovery), and avoiding comparison artifacts (cherry-picking, post-hoc model construction)
- **Model identifiability**: Structural identifiability (can parameters be uniquely determined from the likelihood function in principle?) vs. practical identifiability (can they be recovered with realistic sample sizes and noise levels?); techniques for diagnosing non-identifiability including profile likelihood analysis, Fisher information matrix inspection, and simulation-based approaches
- **Cross-validation**: Leave-one-out cross-validation and $k$-fold CV as alternatives to Bayesian model evidence for model comparison; the relationship between CV predictive accuracy and free energy; when CV is preferred (e.g., model misspecification concerns)

## Key References

- Stephan, K. E., Penny, W. D., Daunizeau, J., et al. (2009). Bayesian model selection for group studies. *NeuroImage*, 46(4), 1004-1017.
- Rigoux, L., Stephan, K. E., Friston, K. J., & Daunizeau, J. (2014). Bayesian model selection for group studies — Revisited. *NeuroImage*, 84, 971-985.
- Friston, K. J., & Penny, W. D. (2011). Post hoc Bayesian model selection. *NeuroImage*, 56(4), 2089-2099.
- Piray, P., Dezfouli, A., Heskes, T., Frank, M. J., & Daw, N. D. (2019). Hierarchical Bayesian inference for concurrent model fitting and comparison for group studies. *PLOS Computational Biology*, 15(6), e1007043.
- Penny, W. D. (2012). Comparing dynamic causal models using AIC, BIC and free energy. *NeuroImage*, 59(1), 319-330.
- Wagenmakers, E. J. (2007). A practical solution to the pervasive problems of p values. *Psychonomic Bulletin & Review*, 14(5), 779-804.

## Prerequisite Modules

- Module 03: Perception (introduces DCM and Bayesian model comparison in the context of neuroimaging; this module generalizes those tools to cognitive modeling more broadly)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/04_cognition/module.md](../../03_advanced_theory/04_cognition/module.md)): Proves that the variational free energy provides a bound on log model evidence and derives the formal properties of different variational families — this module applies those bounds as practical model comparison criteria
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/04_cognition/module.md](../../02_neuroscientific_frontiers/04_cognition/module.md)): Reviews prefrontal hierarchies and precision-based attention as neural implementations of cognitive inference — this module provides the model comparison tools to test whether hierarchical active inference models explain neural and behavioral data better than flat alternatives
- **Philosophical Foundations** ([../../01_philosophical_foundations/04_cognition/module.md](../../01_philosophical_foundations/04_cognition/module.md)): Examines the extended cognition debate and whether Markov blankets settle questions about cognitive boundaries — this module operationalizes those debates as model comparison questions (e.g., does a model with extended state space fit better?)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
