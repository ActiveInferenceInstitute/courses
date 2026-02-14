# Station: Learning (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Learning
- **Subtitle**: Fitting, Comparing, and Validating Generative Models
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must provide a comprehensive treatment of the model fitting and validation pipeline that underpins all computational modeling in active inference research. Students should learn the Expectation-Maximization (EM) algorithm as applied to active inference models — alternating between E-steps (updating beliefs about hidden states given current parameters) and M-steps (updating parameters given current state estimates) — as well as full variational Bayes approaches that maintain posterior uncertainty over parameters (Friston et al., 2007). The critical validation pipeline consists of four stages that every computational modeling study must address: (1) **Parameter recovery** — simulate data from known parameters, fit the model, assess whether parameters are accurately recovered, and characterize the confusion structure (Wilson & Collins, 2019); (2) **Simulation-based calibration** (SBC) — verify that the posterior inference algorithm has correct calibration by checking that posterior ranks of true parameters are uniformly distributed (Talts et al., 2018); (3) **Posterior predictive checks** — generate synthetic data from the fitted posterior and compare distributional features with observed data (Gelman et al., 2014); (4) **Out-of-sample prediction** — assess whether the model generalizes to held-out data using cross-validation or held-out test sets. The module must also cover diagnosing model misspecification: when systematic patterns in posterior predictive residuals indicate that the generative model is structurally wrong, not merely poorly parameterized.

## Key Concepts

- **Parameter estimation (EM, variational Bayes)**: The EM algorithm for point estimation of generative model parameters in active inference; variational Bayes for full posterior inference over parameters; Laplace approximation as a computationally efficient alternative; the relationship between EM, VB, and the free energy bound on model evidence
- **Model evidence computation**: Computing the log model evidence $\ln p(o \mid m)$ via the variational free energy bound $F$; the Laplace approximation to model evidence; understanding when the free energy bound is tight vs. loose and the implications for model comparison
- **Parameter recovery**: Simulating synthetic behavioral data from a generative model with known parameters, fitting the model to that synthetic data, and assessing recovery quality via correlation ($r$), bias (mean signed error), and root mean squared error; constructing confusion matrices to identify parameter trade-offs and non-identifiable parameter combinations
- **Simulation-based calibration (SBC)**: The method of Talts et al. (2018) for validating Bayesian inference algorithms — drawing parameters from the prior, simulating data, computing the posterior, and checking that the rank statistic of the true parameter within the posterior is uniformly distributed; diagnosing miscalibration patterns (overdispersion, underdispersion, bias)
- **Posterior predictive checks**: Generating simulated datasets from the posterior predictive distribution $p(o^{\text{rep}} \mid o) = \int p(o^{\text{rep}} \mid \theta) p(\theta \mid o) d\theta$ and comparing summary statistics of simulated vs. observed data; visual checks (e.g., comparing simulated and observed RT distributions, choice patterns) and formal discrepancy measures
- **Model misspecification diagnosis**: When posterior predictive checks reveal systematic deviations — interpreting residual structure to guide model revision; the distinction between parameter misspecification (wrong parameter values within the right model class) and structural misspecification (wrong model class entirely)

## Key References

- Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2014). *Bayesian Data Analysis* (3rd ed.). CRC Press.
- Talts, S., Betancourt, M., Simpson, D., Vehtari, A., & Gelman, A. (2018). Validating Bayesian inference algorithms with simulation-based calibration. *arXiv preprint arXiv:1804.06788*.
- Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife*, 8, e49547.
- Friston, K. J., Ashburner, J., Kiebel, S. J., Nichols, T. E., & Penny, W. D. (Eds.). (2007). *Statistical Parametric Mapping: The Analysis of Functional Brain Images*. Academic Press.
- Friston, K. J., & Penny, W. D. (2011). Post hoc Bayesian model selection. *NeuroImage*, 56(4), 2089-2099.
- Friston, K. J., Litvak, V., Oswal, A., et al. (2016). Bayesian model reduction and empirical Bayes for group (DCM) studies. *NeuroImage*, 128, 413-431.

## Prerequisite Modules

- Module 04: Cognition (provides the Bayesian model comparison framework that model validation extends and stress-tests)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/06_learning/module.md](../../03_advanced_theory/06_learning/module.md)): Derives Bayesian model reduction, the variational Laplacian, and the formal relationship between free energy and model evidence bounds — this module implements and validates those theoretical results computationally
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/06_learning/module.md](../../02_neuroscientific_frontiers/06_learning/module.md)): Reviews synaptic plasticity mechanisms as implementations of Bayesian learning (Hebbian plasticity as VFE minimization, neuromodulatory precision control) — this module provides the computational tools to fit and validate models linking plasticity to learning
- **Philosophical Foundations** ([../../01_philosophical_foundations/06_learning/module.md](../../01_philosophical_foundations/06_learning/module.md)): Examines the epistemology of model revision, Kuhnian paradigm shifts, and abductive inference — this module operationalizes those epistemological questions into practical model comparison and validation procedures

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
