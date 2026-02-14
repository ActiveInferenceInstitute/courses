# Lab: Derivation Exercise — Precision Optimization and Attention

## Objective

Derive the mathematical equations governing precision estimation and show how precision optimization implements attention in hierarchical models.

## Part 1: Univariate Precision Estimation

**Goal**: Derive the optimal precision for the simplest Gaussian model.

**Model**: p(o|μ) = N(o; μ, π⁻¹), with known mean μ and unknown precision π. Prior: p(π) = Gamma(π; α₀, β₀).

**Task**:

1. Write the log-likelihood ln p(o₁:N | μ, π) for N observations
2. Combine with the log-prior ln p(π) = (α₀ - 1)ln π - β₀π + const
3. Find the posterior p(π | o₁:N) by recognizing it as a Gamma distribution with updated parameters
4. Show that the posterior mean E[π | o₁:N] is related to the inverse sample variance

{fill:textarea}

## Part 2: Precision in Hierarchical Predictive Coding

**Goal**: Derive how precision modulates message passing at each level.

**Model**: Two-level hierarchy with precision parameters π₁ (observation level) and π₂ (state level):

- p(o|s₁) = N(o; s₁, π₁⁻¹)
- p(s₁|s₂) = N(s₁; s₂, π₂⁻¹)

**Task**:

1. Write the free energy F as a function of sufficient statistics μ₁, μ₂ and precision parameters π₁, π₂
2. Compute ∂F/∂μ₁ and show it depends on the ratio π₁/π₂ — the relative precision of sensory and prior prediction errors
3. Show that when π₁ >> π₂ (high sensory precision), updates are driven primarily by sensory data; when π₂ >> π₁ (high prior precision), updates are driven primarily by priors

{fill:textarea}

## Part 3: Log-Precision Dynamics

**Goal**: Derive the gradient flow for log-precision γ = ln π.

**Task**:

1. Express free energy as a function of γ (not π directly)
2. Compute ∂F/∂γ = ∂F/∂π · ∂π/∂γ = ∂F/∂π · π
3. Show that the dynamics dγ/dt = -∂F/∂γ stably estimate precision from prediction error statistics
4. Explain why using log-precision (which ranges over all reals) is numerically more stable than raw precision (which must be positive)

{fill:textarea}

## Part 4: Fisher Information and Confidence

**Goal**: Connect precision to the information content of observations.

**Task**:

1. Compute the Fisher information I(θ) = -E[∂²ln p(o|θ)/∂θ²] for p(o|θ) = N(θ, π⁻¹)
2. Show that I(θ) = π — higher precision observations carry more information about hidden states
3. State the Cramér-Rao bound: Var(θ̂) ≥ 1/I(θ). Explain what this means for inference under different precision regimes
4. Discuss the implication: attention (increasing π) → more Fisher information → tighter Cramér-Rao bound → more confident inference

{fill:textarea}

## Part 5: Synthesis

In 200 words, explain how precision serves as the mathematical bridge between free energy theory (abstract variational inference) and attention (concrete cognitive process). Connect the derivations from Parts 1-4 into a unified account.

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Bayesian estimation | Conjugate precision estimation (Gamma-Gaussian) |
| 2 | Hierarchical analysis | Precision ratio modulates sensory vs. prior influence |
| 3 | Dynamical systems | Log-precision gradient flow |
| 4 | Information geometry | Fisher information = precision; Cramér-Rao bound |
| 5 | Conceptual integration | Precision as the math of attention |
