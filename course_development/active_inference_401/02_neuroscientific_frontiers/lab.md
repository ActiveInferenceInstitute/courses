# Lab: Neuroscientific Frontiers of Active Inference

## Objective

Design, analyze, and critically evaluate a neuroscientific experiment that tests a specific, falsifiable prediction of the Active Inference framework. This lab requires integration of computational modeling with empirical neuroscience methods.

## Prerequisites

- Graduate-level neuroanatomy (cortical hierarchies, subcortical structures, neuromodulatory systems)
- Competence in at least one neuroimaging/electrophysiological method (fMRI, EEG/MEG, or intracranial recordings)
- Familiarity with Dynamic Causal Modelling (DCM) or comparable model inversion techniques
- Proficiency in MATLAB/SPM or Python for computational modeling

## Part 1: Neural Architecture Analysis

1. **Circuit Mapping**: Select a specific neural circuit (e.g., the canonical microcircuit in V1, the cortico-basal ganglia-thalamo-cortical loop, the interoceptive network).
2. **Generative Model Specification**: Formally specify the generative model that the circuit implements. Identify:
   - Which neural populations encode predictions (top-down, deep pyramidal cells)
   - Which encode prediction errors (superficial pyramidal cells, ascending projections)
   - Which encode precision (neuromodulatory gain control: dopamine, norepinephrine, acetylcholine, serotonin)
3. **Empirical Constraints**: Cite at least 5 empirical studies that constrain the model specification. For each, state what aspect of the generative model it constrains and the strength of evidence.

## Part 2: Experimental Design

1. **Hypothesis Generation**: Derive a specific, falsifiable prediction from the Active Inference model of your chosen circuit. The prediction must be:
   - Quantitative (specify the direction and approximate magnitude of the expected effect)
   - Distinguishable from predictions of at least one competing framework (e.g., reinforcement learning, classical Bayesian brain, predictive coding without active inference)
2. **Paradigm Design**: Design an experimental paradigm that tests this prediction:
   - Specify stimuli, task structure, and trial timing
   - Identify the key experimental manipulation (e.g., volatility, precision, model complexity)
   - Specify the neural measure (BOLD, ERP component, oscillatory power, phase-amplitude coupling)
3. **Power Analysis**: Estimate the required sample size using prior effect sizes from the literature.

## Part 3: Computational Modeling

1. **Simulate** the generative model in your chosen software environment (SPM, pymdp, or custom code).
2. **Generate** synthetic neural data under both the Active Inference model and at least one alternative model.
3. **Demonstrate** that your experimental design can discriminate between models using Bayesian model comparison (compute log Bayes factors).

## Deliverables

- A pre-registration-quality experimental protocol (following OSF or AsPredicted format)
- Simulation code with documentation
- A figure showing predicted neural signatures under competing models
- A 2000-word methods and rationale section suitable for a grant application

## Discussion Requirements

- Present your experimental design to the seminar for peer review
- Address potential confounds and alternative interpretations
- Discuss the translational implications of your predicted findings (e.g., for computational psychiatry or neuroprosthetics)
