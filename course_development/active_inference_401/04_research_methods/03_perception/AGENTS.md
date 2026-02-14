# Station: Perception (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Perception
- **Subtitle**: Testing Predictive Coding with Neuroimaging
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must cover the design and analysis of neuroimaging experiments that test predictions of the predictive coding framework. The central methodological tool is Dynamic Causal Modeling (DCM), which allows researchers to specify competing generative models of neural dynamics (e.g., a predictive coding model vs. an adaptive coding model) and compare them using Bayesian model selection (Stephan et al., 2009). Students should learn the full DCM workflow: specifying the neural model (state equations, observation model), inverting the model using variational Laplace, computing the log model evidence (approximated by the negative variational free energy $F$), and performing group-level Bayesian model comparison. The canonical experimental paradigm is the oddball or roving standard paradigm, which generates mismatch negativity (MMN) and repetition suppression effects that predictive coding models explain via precision-weighted prediction error signaling (Garrido et al., 2009). Students must also grapple with confounds: Can adaptation alone (without prediction) explain MMN? Does repetition suppression reflect prediction error reduction or neural fatigue? How do you design experiments that distinguish these accounts?

## Key Concepts

- **Dynamic Causal Modeling (DCM)**: A Bayesian framework for specifying and comparing generative models of neural dynamics from fMRI or EEG data; involves defining state equations for neural populations, an observation model mapping neural states to measured signals, and inverting the model via variational Laplace to obtain posterior parameter estimates and model evidence
- **Bayesian model comparison**: Fixed-effects BMS (group Bayes factor), random-effects BMS (Dirichlet-multinomial model; Stephan et al., 2009), family-level inference (grouping models by shared features), and protected exceedance probability (Rigoux et al., 2014) to guard against overconfidence when evidence is weak
- **Oddball and roving paradigms**: Experimental designs that manipulate stimulus predictability to elicit prediction error responses (MMN, P300); the roving standard paradigm (Garrido et al., 2009) is particularly useful because it parametrically varies repetition count, allowing dose-response analysis of prediction error attenuation
- **Computational phenotyping**: Using DCM-derived parameters (e.g., intrinsic connection strengths, precision parameters) as individual-difference measures; parametric empirical Bayes (PEB) for group-level inference on parameter-trait associations (Friston et al., 2016)
- **Mismatch negativity (MMN) studies**: The MMN as a canonical marker of predictive processing — experimental designs that distinguish prediction error accounts from adaptation accounts, including omission paradigms, controlled-adaptation designs (Summerfield et al., 2008), and multi-level hierarchical paradigms

## Key References

- Stephan, K. E., Penny, W. D., Daunizeau, J., et al. (2009). Bayesian model selection for group studies. *NeuroImage*, 46(4), 1004-1017.
- Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273-1302.
- Friston, K. J., Ashburner, J., Kiebel, S. J., Nichols, T. E., & Penny, W. D. (Eds.). (2007). *Statistical Parametric Mapping: The Analysis of Functional Brain Images*. Academic Press.
- Garrido, M. I., Kilner, J. M., Stephan, K. E., & Friston, K. J. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology*, 120(3), 453-463.
- Adams, R. A., Stephan, K. E., Brown, H. R., Frith, C. D., & Friston, K. J. (2013). The computational anatomy of psychosis. *Frontiers in Psychiatry*, 4, 47.
- Rigoux, L., Stephan, K. E., Friston, K. J., & Daunizeau, J. (2014). Bayesian model selection for group studies — Revisited. *NeuroImage*, 84, 971-985.

## Prerequisite Modules

- Module 02: Agents (provides the POMDP agent framework and model-fitting skills that DCM extends to neural data)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/03_perception/module.md](../../03_advanced_theory/03_perception/module.md)): Derives the predictive coding update equations from variational message passing and proves convergence properties — this module tests those predictions with neuroimaging data
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/03_perception/module.md](../../02_neuroscientific_frontiers/03_perception/module.md)): Reviews the cortical microcircuit evidence for predictive coding (laminar specificity, oscillatory coupling) — this module provides the DCM and experimental design tools to evaluate that evidence rigorously
- **Philosophical Foundations** ([../../01_philosophical_foundations/03_perception/module.md](../../01_philosophical_foundations/03_perception/module.md)): Examines the phenomenology of perception and the compatibility of predictive processing with direct perception (Gibson) — this module asks what experiments could adjudicate between these philosophical positions

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
