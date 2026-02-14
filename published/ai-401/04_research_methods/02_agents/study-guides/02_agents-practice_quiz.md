# Practice Quiz: Agents / Computational Phenotyping (Research Methods)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Computational phenotyping characterizes individuals by:
A) Behavioral scores alone
B) Their generative model parameters — latent computational variables that explain observed behavior
C) Genetic markers
D) fMRI activation patterns

**2.** Parameter recovery is important because:
A) It makes models complex
B) It validates that the model can distinguish different parameter settings from behavioral data — ensuring parameter estimates are meaningful
C) It replaces data collection
D) It proves the model is correct

**3.** A transdiagnostic approach to psychiatry:
A) Uses DSM categories
B) Clusters patients by computational parameters rather than diagnostic labels — potentially grouping differently diagnosed patients with similar computational profiles
C) Ignores diagnosis
D) Uses only medication

**4.** Normative modeling:
A) Compares groups
B) Maps each individual's deviation from a population-level normative distribution in parameter space — enabling personalized anomaly detection
C) Averages all patients
D) Uses only means

**5.** Hierarchical fitting (PEB) improves individual estimates by:
A) Ignoring group information
B) Regularizing individual parameter estimates toward the group mean — benefiting subjects with noisy data while preserving individual differences
C) Fitting one model to all
D) Using only priors

**6.** Parameter identifiability means:
A) Parameters are arbitrary
B) Different parameter values produce distinguishable behavior — the model can uniquely determine each parameter from data
C) All parameters are the same
D) Parameters are fixed

**7.** Confusion matrices in parameter recovery:
A) Measure behavioral performance
B) Show whether each parameter can be uniquely recovered — off-diagonal elements indicate that changes in one parameter are absorbed by another, revealing identifiability problems
C) Count correct responses
D) Test model fit

**8.** The minimum description length (MDL) principle relates to computational phenotyping because:
A) It minimizes data collection
B) The simplest model that captures individual behavioral variation is preferred — analogous to free energy's complexity-accuracy trade-off, preventing overfitting
C) It maximizes parameters
D) It is unrelated to Bayesian methods

## Part B: Short Answer

**1.** A computational phenotyping study finds that patients with depression have lower precision on reward prediction errors (ζ_reward). However, test-retest reliability for ζ_reward is only ICC = 0.45. Explain what this means for the clinical utility of this parameter, and suggest two approaches to improve reliability. (200 words)

**2.** Describe how you would validate a computational phenotyping pipeline using simulated data before applying it to real patient data. What specific checks would you perform at each stage? (200 words)

## Part C: Essay Questions

**1.** Design a complete computational phenotyping study for a clinical condition of your choice. Include: (a) task design with rationale for parameter dissociation, (b) Active Inference model specification, (c) fitting procedure, (d) parameter recovery validation, (e) clinical group comparison design, (f) normative modeling plan, (g) expected results. (600 words)

**2.** Critically evaluate the test-retest reliability of computational parameters. If a person's computational phenotype changes between sessions (separated by two weeks), does this mean: (a) the model is unreliable, (b) the parameters capture genuine state changes, or (c) the task is too noisy? How would you distinguish these explanations? (400 words)

**3.** Compare computational phenotyping using Active Inference with computational phenotyping using reinforcement learning models. What parameters does each framework provide? What are the conceptual differences in how they characterize individual variation? Which approach is more useful clinically, and why? (400 words)
