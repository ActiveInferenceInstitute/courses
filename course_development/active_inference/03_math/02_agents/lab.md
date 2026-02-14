# Lab: Derivation Exercise — Generative Models and Variational Inference

## Objective

Derive the variational inference update equations for a concrete generative model, connecting the abstract mathematics to explicit computations.

## Part 1: Hidden Markov Model Specification

**Goal**: Write out a complete generative model.

Consider a Hidden Markov Model with:

- K = 3 hidden states (s ∈ {1, 2, 3})
- Observation model: p(oₜ | sₜ = k) = N(oₜ; μₖ, σₖ²) with known parameters
- Transition model: p(sₜ | sₜ₋₁) given by a 3×3 matrix **A** with rows summing to 1
- Prior: p(s₁) = categorical with probabilities [0.5, 0.3, 0.2]

**Task**: Write the complete joint distribution p(o₁:T, s₁:T) for T = 3 timesteps. Expand the product notation fully.

{fill:textarea}

## Part 2: Variational Free Energy for the HMM

**Goal**: Derive the free energy for this model.

Let q(s₁:T) = ∏ₜ q(sₜ) be the mean-field recognition density, where each q(sₜ) is a categorical distribution with parameters (probabilities) rₜ = [rₜ₁, rₜ₂, rₜ₃].

**Task**: Write the variational free energy:

F = E_q[ln q(s₁:T)] - E_q[ln p(o₁:T, s₁:T)]

Expand each term. The first term is the negative entropy of q. The second term involves the log-likelihood and log-transition probabilities.

{fill:textarea}

## Part 3: Optimal Update Equations

**Goal**: Derive the fixed-point equations for the sufficient statistics.

Taking the derivative ∂F/∂rₜₖ = 0 (with the constraint ∑ₖ rₜₖ = 1), derive the optimal q*(sₜ):

**ln q*(sₜ = k) ∝ ln p(oₜ | sₜ = k) + E_{q(sₜ₋₁)}[ln p(sₜ = k | sₜ₋₁)] + E_{q(sₜ₊₁)}[ln p(sₜ₊₁ | sₜ = k)]**

Show all steps. Explain why the update depends on messages from both the past (sₜ₋₁) and the future (sₜ₊₁).

{fill:textarea}

## Part 4: Gaussian State-Space Model

**Goal**: Repeat the derivation for a continuous model.

Consider a linear Gaussian state-space model:

- p(sₜ | sₜ₋₁) = N(sₜ; A·sₜ₋₁, Q) — state dynamics
- p(oₜ | sₜ) = N(oₜ; C·sₜ, R) — observation model
- p(s₁) = N(s₁; μ₀, Σ₀) — prior

With recognition density q(sₜ) = N(sₜ; mₜ, Vₜ).

**Task**: Derive the update equations for the sufficient statistics mₜ (mean) and Vₜ (covariance) by minimizing F. Show that these correspond to Kalman filter/smoother equations.

{fill:textarea}

## Part 5: Synthesis

In 200 words, explain the common mathematical structure across Parts 2-4: in both discrete and continuous cases, the optimal recognition density arises from minimizing free energy, and the update equations combine likelihood (data-driven) terms with transition (model-driven) terms.

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Model specification | Writing the HMM joint distribution |
| 2 | Free energy derivation | Expanding F for mean-field HMM |
| 3 | Variational calculus | Deriving optimal update equations |
| 4 | Continuous extension | Gaussian state-space / Kalman filtering |
| 5 | Conceptual synthesis | Unifying discrete and continuous cases |
