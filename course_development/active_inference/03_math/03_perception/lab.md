# Lab: Derivation Exercise — Predictive Coding Message Passing

## Objective

Derive the predictive coding equations step by step for increasingly complex generative models, connecting the mathematics to the neural architecture.

## Part 1: Single-Level Gaussian Inference

**Goal**: Derive belief updating for the simplest possible model.

**Generative model**: p(s) = N(s; μ₀, σ₀²), p(o|s) = N(o; s, σ_o²)

**Recognition density**: q(s) = N(s; μ, σ²)

**Task**:

1. Write the free energy F = -E_q[ln p(o|s)] + D_KL[q(s) ‖ p(s)]
2. Expand each term analytically using Gaussian integrals
3. Compute ∂F/∂μ and set to zero → derive μ*
4. Show that μ* = (σ_o² · μ₀ + σ₀² · o) / (σ_o² + σ₀²) — a precision-weighted average of prior and observation

{fill:textarea}

## Part 2: Two-Level Hierarchical Model

**Goal**: Derive message passing in a hierarchy.

**Generative model**:

- Level 2 prior: p(s₂) = N(s₂; μ₂₀, σ₂₀²)
- Level 2 → Level 1: p(s₁|s₂) = N(s₁; g₂(s₂), σ₂²) where g₂(s₂) = A·s₂ (linear)
- Level 1 → Observations: p(o|s₁) = N(o; g₁(s₁), σ₁²) where g₁(s₁) = C·s₁ (linear)

**Recognition density**: q(s₁) = N(μ₁, Σ₁), q(s₂) = N(μ₂, Σ₂)

**Task**:

1. Write the free energy as a sum of terms across levels
2. Compute ∂F/∂μ₁ and ∂F/∂μ₂
3. Identify the prediction errors ε₁ = o - C·μ₁ and ε₂ = μ₁ - A·μ₂
4. Show that each level's update depends on bottom-up prediction errors (from below) and top-down predictions (from above)

{fill:textarea}

## Part 3: Nonlinear Extensions

**Goal**: Extend to nonlinear generative mappings.

Replace g₁(s₁) = C·s₁ with a nonlinear function g₁(s₁) (e.g., sigmoid, polynomial).

**Task**:

1. Derive the modified prediction error equation using the Jacobian ∂g₁/∂s₁
2. Show that the gradient ∂F/∂μ₁ now involves the Jacobian transposed times the precision-weighted prediction error
3. Explain why this requires the Laplace approximation (evaluating the Jacobian at the current estimate μ₁)

{fill:textarea}

## Part 4: Generalized Coordinates

**Goal**: Extend predictive coding to temporal dynamics using generalized coordinates.

In generalized coordinates, the state vector is extended to include the state and its temporal derivatives: x̃ = [x, x', x'', ...]

**Task**:

1. Write the generalized state-space model: p(o|s̃) and p(s̃) in generalized coordinates
2. Show that the free energy gradient in generalized coordinates has the form: dμ̃/dt = Dμ̃ - ∂F/∂μ̃, where D is the shift operator
3. Explain how this enables the system to predict the temporal evolution of sensory input

{fill:textarea}

## Part 5: Synthesis

In 200 words, explain how Parts 1-4 build a complete mathematical framework: from single-level inference to hierarchical message passing to temporal prediction — and how this framework maps onto the cortical hierarchy.

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Gaussian inference | Precision-weighted averaging (Bayesian updating) |
| 2 | Hierarchical derivation | Bottom-up/top-down message passing |
| 3 | Nonlinear extension | Jacobian-based prediction error propagation |
| 4 | Temporal dynamics | Generalized coordinates and prediction |
| 5 | Integration | Connecting math to neural predictive coding |
