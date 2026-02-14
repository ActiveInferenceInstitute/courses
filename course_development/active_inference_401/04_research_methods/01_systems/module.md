# Module 01: Systems — Dynamic Causal Modelling and Model Inversion

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Apply **Dynamic Causal Modelling (DCM)** — the primary neuroimaging method based on Active Inference.
2. Analyze the mathematical structure of **model inversion** — fitting generative models to empirical data.
3. Evaluate DCM results including effective connectivity, model comparison, and clinical applications.

## Key Concepts

### 1. Dynamic Causal Modelling Overview

DCM is a framework for inferring the causal architecture of neural systems from neuroimaging data. It is the most mature empirical application of Active Inference:

**Core idea**: DCM specifies a generative model of how neural states give rise to observed signals (fMRI, EEG, MEG). The model includes:

- **Neural state equation**: dx/dt = f(x, u, θ_A) — how hidden neural states x evolve over time, driven by inputs u, with connectivity parameters θ_A
- **Observation equation**: y = g(x, θ_H) — how neural states generate observable signals, with hemodynamic/electromagnetic parameters θ_H

**Effective connectivity**: DCM infers the directed, causal influence of one brain region on another. Unlike functional connectivity (correlations), effective connectivity estimates the parameters of the neural state equation — the actual causal connections.

### 2. The Generative Model in DCM

**Neural dynamics**: The neural state equation typically takes the form:

dx/dt = (A + Σ_j u_j B_j) x + C u

where:

- A is the intrinsic (endogenous) connectivity matrix — connections present without experimental input
- B_j are modulatory connectivity matrices — how experimental condition j changes connections
- C is the driving input matrix — where external stimuli enter the network
- u is the experimental input vector

**Hemodynamic model** (for fMRI): Neural activity drives a hemodynamic cascade:

Neural activity → vasodilatory signal → blood flow → blood volume → deoxygenated hemoglobin → BOLD signal

This is modeled by the Balloon model (Buxton et al.), which maps neural states to observed fMRI timeseries.

**Electromagnetic model** (for EEG/MEG): Neural activity generates electrical currents that propagate to the scalp. DCM includes neural mass models (populations of neurons with characteristic dynamics) and forward models mapping neural currents to observed sensor signals.

### 3. Model Inversion

Model inversion is the process of estimating model parameters and comparing models given observed data:

**Variational Bayes**: DCM uses variational Laplace (VL) for model inversion:

1. Define the generative model: p(y, θ | m) = p(y | θ, m) p(θ | m)
2. Define the approximate posterior: q(θ) = N(μ, Σ)
3. Minimize free energy: F = -E_q[ln p(y | θ)] + D_KL[q(θ) || p(θ)]
4. Iterate: Update μ and Σ using Newton's method until convergence

**Model comparison**: After inverting multiple models, compare them using free energy:

- Best model = lowest free energy (most evidence)
- Bayes factors provide strength-of-evidence measures

### 4. Practical DCM Workflow

A complete DCM analysis follows these steps:

**Step 1 — Hypothesis specification**: Define competing models encoding different connectivity hypotheses (e.g., "region A drives region B" vs. "region B drives region A").

**Step 2 — Region selection**: Choose regions of interest (ROIs) based on prior knowledge or functional localizer scans.

**Step 3 — Time series extraction**: Extract representative time series from each ROI after standard preprocessing.

**Step 4 — Model specification**: For each model, specify A, B, C matrices encoding the hypothesized connectivity.

**Step 5 — Model inversion**: Fit each model using variational Laplace. Obtain posterior parameter estimates and free energy.

**Step 6 — Model comparison**: Compare models using Bayesian Model Selection (fixed effects or random effects at the group level).

**Step 7 — Parameter inference**: From the winning model, examine posterior parameter estimates for connectivity strengths, directions, and modulations.

### 5. Extensions and Modern DCM

DCM has evolved significantly:

**Spectral DCM**: Fits power spectra rather than time series directly. More robust to model misspecification and computationally efficient.

**Regression DCM (rDCM)**: Dramatically faster approximation using variational regression. Scales to hundreds of regions.

**DCM for phase coupling**: Models phase relationships between oscillating neural populations. Relevant for understanding neural synchrony.

## Summary

DCM is the primary empirical instantiation of Active Inference for neuroimaging. It specifies a generative model of neural dynamics and observations, inverts this model using variational Bayes to estimate effective connectivity, and compares models using Bayesian Model Selection. Modern extensions handle larger networks and different data modalities.

## Further Reading

- Friston, K. J. et al. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273-1302.
- Zeidman, P. et al. (2019). A guide to group effective connectivity analysis. *NeuroImage*, 200, 172-189.
- Razi, A. et al. (2017). Construct validation of a DCM for resting state fMRI. *NeuroImage*, 106, 1-14.
