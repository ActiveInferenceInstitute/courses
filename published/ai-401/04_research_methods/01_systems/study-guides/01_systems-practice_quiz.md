# Practice Quiz: Systems / DCM (Research Methods)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Dynamic Causal Modelling infers:
A) Functional connectivity (correlations)
B) Effective connectivity — the directed causal influence of one brain region on another, estimated via a generative model of neural dynamics
C) Anatomical connectivity
D) Statistical correlations only

**2.** The A matrix in DCM represents:
A) Attention modulation
B) Intrinsic (endogenous) connectivity — connections present regardless of experimental condition
C) Driving input
D) Hemodynamic parameters

**3.** Model inversion in DCM uses:
A) Simple linear regression
B) Variational Laplace — approximating the posterior over parameters as Gaussian and minimizing free energy via Newton's method
C) Maximum likelihood only
D) Random search

**4.** Model comparison in DCM uses:
A) p-values
B) Free energy as an approximation to log model evidence — models with lower F (higher evidence) are preferred
C) R-squared
D) Cross-validation only

**5.** Spectral DCM fits:
A) Time series directly
B) Power spectra and cross-spectra — more robust to model misspecification and computationally efficient
C) Raw EEG
D) Behavioral data

**6.** The Balloon model:
A) Describes behavior
B) Maps neural activity through a hemodynamic cascade (vasodilation → blood flow → volume → BOLD) to generate predicted fMRI signals
C) Models neurotransmitters
D) Is used for EEG only

**7.** Parametric Empirical Bayes (PEB) in DCM enables:
A) Single-subject analysis only
B) Group-level analysis that estimates both group means and between-subject variability in connectivity parameters — while using group information to regularize noisy individual estimates
C) Ignoring individual differences
D) Only comparing two subjects

**8.** The key difference between functional and effective connectivity is:
A) They measure the same thing
B) Functional connectivity measures statistical dependencies (correlations) while effective connectivity measures directed causal influence — DCM estimates the latter
C) Effective connectivity is easier to measure
D) Functional connectivity requires a model

## Part B: Short Answer

**1.** A DCM analysis reveals that the modulatory parameter (B-matrix) for the connection from amygdala → visual cortex is significantly increased during emotional stimuli. Interpret this finding in Active Inference terms — what does it mean about precision modulation of prediction errors in visual cortex? (200 words)

**2.** You run a DCM with 5 brain regions and want to compare all possible connectivity patterns. Explain why the model space is too large for exhaustive comparison via model inversion, and describe how BMR + PEB solves this problem. (200 words)

## Part C: Essay Questions

**1.** Describe the complete DCM analysis pipeline for an fMRI study of emotional regulation. Include: (a) hypothesis specification (competing models), (b) task design and ROI selection, (c) model specification (A, B, C matrices for each model), (d) model inversion procedure, (e) model comparison, (f) parameter interpretation. (600 words)

**2.** Critically evaluate DCM's limitations. Address: (a) sensitivity to model space specification (what if the true model is not in the model space?), (b) ROI selection dependence, (c) hemodynamic confounds, (d) scalability, (e) replicability. For each limitation, suggest a methodological solution or mitigation. (400 words)

**3.** How does DCM relate to the broader Active Inference framework? Specifically: (a) How is DCM's generative model an instance of the general Active Inference generative model? (b) How does model inversion correspond to variational inference? (c) How does model comparison correspond to Bayesian Model Selection? (d) What aspects of Active Inference does DCM NOT capture (e.g., action, planning)? (400 words)
