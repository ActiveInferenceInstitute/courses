# Lab: Neuroscientific Frontiers of Active Inference

## Objective

Design, analyze, critically evaluate, and computationally simulate a neuroscientific experiment that tests a specific, falsifiable prediction of the Active Inference framework. This capstone-level lab requires the seamless integration of formal computational modeling with cutting-edge empirical neuroscience methods.

## Prerequisites

- Graduate-level neuroanatomy (cortical hierarchies, canonical microcircuits, subcortical structures, and precisely-mapped neuromodulatory projection systems).
- Competence in at least one advanced neuroimaging or electrophysiological method (fMRI, EEG/MEG, or invasive intracranial recordings).
- Familiarity with Dynamic Causal Modelling (DCM), specifically DCM for electrophysiology (neural mass models) or comparable Bayesian model inversion techniques.
- Proficiency in MATLAB (SPM12) or Python (pymdp) for generating synthetic neural data.

## Part 1: Neural Architecture Analysis & Mapping

1. **Circuit Selection & Justification**: Select a specific, well-characterized neural circuit. Examples include the canonical layer-IV microcircuit in V1, the cortico-basal ganglia-thalamo-cortical loop, or the insular interoceptive network. Justify your choice based on its amenability to Active Inference modeling.
2. **Generative Model Specification**: Formally specify the generative model that this target circuit mathematically implements. Provide a wiring diagram that explicitly identifies:
   - Which specific neural populations encode predictions (e.g., top-down, deep pyramidal cells in layer V/VI).
   - Which populations encode prediction errors (e.g., superficial pyramidal cells in layer II/III driving ascending projections).
   - Which populations encode precision (e.g., specific neuromodulatory gain control mechanisms via dopamine, norepinephrine, acetylcholine, or serotonin projections).
3. **Empirical Constraints Map**: Create an annotated bibliography citing at least 5 primary empirical neurophysiology or neuroanatomy papers that physically constrain your model specification. For each paper, explicitly state *what specific parameter or connection* in the generative model it constrains, and grade the strength of the anatomical/physiological evidence.

## Part 2: Rigorous Experimental Design

1. **Hypothesis Generation**: Derive a highly specific, falsifiable prediction from the Active Inference model of your chosen circuit. To receive full credit, the prediction must be:
   - **Quantitative**: Specify the expected direction, approximate magnitude, and temporal latency of the anticipated neural effect.
   - **Discriminative**: The prediction must explicitly diverge from the predictions of at least one major competing framework (e.g., standard model-free reinforcement learning, classical "passive" Bayesian brain models, or predictive coding models *without* active inference).
2. **Paradigm Architecture**: Design a complete experimental paradigm capable of testing this precise prediction:
   - Specify the stimuli parameters, exact trial structure, timing, and inter-trial intervals.
   - Identify the core experimental manipulation (e.g., manipulating environmental volatility, inducing sensory attenuation, or altering task predictability).
   - Specify the precise neural dependent measure (e.g., BOLD signal in a specific ROI, amplitude of a specific ERP component like the MMN, high-gamma oscillatory power, or phase-amplitude coupling indices).
3. **Statistical Power**: Conduct a formal power analysis estimating the required sample size. Justify the assumed effect size using prior literature studying similar computational parameters.

## Part 3: Computational Simulation & Synthetic Data

1. **Simulation Engine**: Build and execute the generative model in your chosen software environment (SPM `spm_MDP_VB_X.m` routines, Python `pymdp`, or custom code).
2. **Data Generation**: Generate synthetic neural time-series data (e.g., simulated LFP or BOLD) under two distinct conditions:
   - Assuming your Active Inference model is the true data-generating process.
   - Assuming your *alternative* competing model is the true data-generating process.
3. **Model Inversion & Recovery**: Add physiological noise to your synthetic data. Demonstrate that your proposed experimental design and analysis pipeline can successfully recover the hidden parameters and cleanly discriminate between the two generating models using Bayesian model comparison (calculating and plotting the log Bayes factors).

## Deliverables

- A comprehensive, pre-registration-quality experimental protocol (strictly following OSF or AsPredicted formatting standards).
- A documented GitHub repository containing your simulation code, synthetic data generation scripts, and model recovery pipelines.
- A multi-panel Publication-quality figure: Panel A showing the circuit diagram, Panel B showing the synthetic neural time-series, and Panel C showing the model recovery confusion matrix.
- A 2,500-word Methods and Rationale section, written in the specific tone and format required for a National Institutes of Health (NIH) R01 grant application.

## Discussion & Defense Requirements

- Present your experimental design and synthetic data to the seminar cluster for a strenuous 20-minute peer review process.
- Formally address potential physiological confounds, artifact contamination, and alternative interpretations of your simulated results.
- Write a final 500-word reflection discussing the translational clinical implications of your paradigm (e.g., how this specific task could be deployed as a computational phenotyping tool in psychiatry or as a calibration paradigm for neuroprosthetics).
