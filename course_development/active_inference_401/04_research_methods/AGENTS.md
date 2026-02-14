# Course AGENTS: Research Methods

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: Research Methods
- **Number**: 4
- **Perspective**: Experimental design, model comparison, computational modeling, open problems
- **Lab Type**: Research Proposal
- **Audience**: PhD students and researchers preparing to conduct original active inference research
- **Tone**: Practical, methodologically rigorous, computationally concrete. Pseudocode and tool references welcome. Emphasis on falsifiability, statistical power, model identifiability, and reproducibility.

## Core Question

How do we *test* Active Inference claims? What experiments, simulations, and model comparisons would provide evidence for or against specific predictions of the framework? What are the practical challenges of implementing active inference models?

## Methodological Frameworks

This unit draws on and teaches:

- **Bayesian Model Comparison**: Bayesian model selection (BMS), random-effects BMS, family inference, protected exceedance probability (Stephan et al., 2009; Rigoux et al., 2014)
- **Dynamic Causal Modeling (DCM)**: Generative model specification, Bayesian model inversion, parametric empirical Bayes (Friston et al., 2003, 2007)
- **Computational Modeling**: PyMDP for discrete POMDP agents, RxInfer.jl for message passing, SPM for neuroimaging (Heins et al., 2022)
- **Simulation and Validation**: Parameter recovery, simulation-based calibration, posterior predictive checks, model identifiability analysis (Wilson & Collins, 2019; Talts et al., 2018)
- **Experimental Design**: Power analysis, adaptive designs, within- vs. between-subject designs for computational phenotyping
- **Open Science**: Pre-registration, data sharing, code reproducibility, open-source tooling

## Key Journals

*NeuroImage*, *PLOS Computational Biology*, *Frontiers in Computational Neuroscience*, *Journal of Mathematical Psychology*, *eLife*, *Nature Methods*, *Journal of Open Source Software*

## Conventions

All modules in this course must:

1. Use language appropriate for PhD students preparing to conduct research
2. Frame all concepts through practical methodology: How would you actually test this? What would the experiment look like? What could go wrong?
3. Include Research Proposal lab activities requiring students to design complete studies (hypotheses, methods, analysis plans, expected results, limitations)
4. Include pseudocode or tool-specific code examples (PyMDP, SPM, RxInfer.jl) where appropriate
5. Address practical challenges: computational cost, model identifiability, parameter degeneracy, sample size requirements
6. Emphasize falsifiability: What observation would disconfirm the active inference account? What would the alternative account predict differently?
7. Adhere to notation standards in [../resources/notation_table.md](../resources/notation_table.md)
8. Cross-reference the shared [../resources/glossary.md](../resources/glossary.md)
9. Link to corresponding modules in other units

## Assessment Philosophy

Research Proposals should require students to:
- Formulate a specific, falsifiable hypothesis derived from active inference theory
- Design an experiment (or simulation study) to test it
- Specify the generative model, inversion scheme, and model comparison criterion
- Conduct a power analysis or sample size justification
- Identify limitations and alternative explanations
- Address practical feasibility (cost, time, equipment, ethics)
