# Practice Quiz: Learning / Model Selection (Advanced Theory)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Bayesian Model Selection automatically implements Occam's Razor because:
A) It prefers simpler models always
B) Model evidence marginalizes over parameters — integrating out the parameter space penalizes models with large, poorly-utilized parameter spaces
C) It uses p-values
D) It ignores model complexity

**2.** Bayesian Model Reduction's key advantage is:
A) Better fit
B) Computing evidence for reduced models analytically from the full model's posterior, without refitting — making it computationally efficient for comparing many nested models
C) Needing more data
D) Random simplification

**3.** Structure learning discovers:
A) Only parameter values
B) The topology of the generative model — which variables exist and which connections are present
C) Only the data
D) The training algorithm

**4.** Parametric Empirical Bayes "borrows strength" by:
A) Ignoring individual data
B) Regularizing individual-level estimates toward the group mean — subjects with noisy data are pulled more strongly toward the group
C) Averaging all data
D) Using only one subject

**5.** Dirichlet process priors enable:
A) Fixed model size
B) Learning the number of hidden states from data — the model can "grow" to accommodate complexity as needed
C) Only shrinkage
D) Infinite parameters always

**6.** Bayes factors quantify:
A) Statistical significance (p-value)
B) The ratio of model evidences — how much more the data support one model over another
C) Effect size
D) Sample size

**7.** Sleep-dependent model simplification corresponds to BMR because:
A) Sleep deletes random memories
B) Synaptic downscaling during sleep weakens low-evidence connections while preserving high-evidence ones — implementing a form of posterior pruning that improves model generalization
C) Sleep has no computational role
D) BMR requires sleep

**8.** The Savage-Dickey density ratio enables:
A) Comparing non-nested models only
B) Computing Bayes factors for nested models using only the posterior evaluated at the restricted parameter value — avoiding full model re-estimation
C) Comparing more than two models
D) Standard hypothesis testing

## Part B: Short Answer

**1.** A researcher uses BMR to compare 256 possible brain connectivity models. Explain why this is computationally feasible with BMR but infeasible with standard model inversion. What assumption does BMR make that enables this efficiency, and when might this assumption fail? (200 words)

**2.** Explain the difference between fixed-effects and random-effects Bayesian Model Selection at the group level. Why does random-effects BMS better handle between-subject variability in brain connectivity? What does a protected exceedance probability of 0.95 tell you? (200 words)

## Part C: Essay Questions

**1.** Derive the Bayesian Model Reduction formula under the Laplace approximation. Show how the evidence for a reduced model can be computed from the full model's posterior without refitting. Explain each term's meaning. When might BMR give misleading results? (500 words)

**2.** Compare Bayesian Model Selection with classical hypothesis testing (null hypothesis significance testing). What are the conceptual differences (prior probabilities, evidence quantification, multiple comparisons)? What are the practical differences (computational cost, interpretability, replicability)? In what scenarios does each approach excel? (400 words)

**3.** Design a structure learning study to discover the effective connectivity of a brain network. Specify: (a) the brain regions of interest, (b) the data modality (fMRI, EEG, MEG), (c) the full model, (d) the BMR procedure for pruning connections, (e) the group-level analysis (PEB), and (f) what the discovered structure would tell us about brain function. (500 words)
