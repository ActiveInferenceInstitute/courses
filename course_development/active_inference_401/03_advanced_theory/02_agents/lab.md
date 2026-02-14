# Lab: Information Geometry and Natural Gradients

> **Learning Goal:** Work through the mathematics of statistical manifolds and natural gradient optimization.

## Part 1: Fisher Information Computation

**Exercise**: Compute the Fisher information matrix for these distribution families:

**a) Bernoulli(p)**: q(x; p) = p^x (1-p)^{1-x}

1. Compute ∂/∂p ln q(x; p) = x/p - (1-x)/(1-p)
2. Compute E[(∂/∂p ln q)²] = 1/(p(1-p))
3. The Fisher information G(p) = 1/(p(1-p)). Note: this diverges at p = 0 and p = 1 — distribution changes near certainty are "large"

**b) Exponential(λ)**: q(x; λ) = λ exp(-λx), x ≥ 0

1. Compute G(λ) = ?
2. Interpret the result geometrically

**c) Multivariate Gaussian N(μ, Σ)**: Compute the Fisher information with respect to mean μ and covariance Σ.

{fill:textarea}

## Part 2: Natural vs. Euclidean Gradient Comparison

> **Learning Goal:** See the difference between natural and Euclidean gradients.

**Exercise**: Consider minimizing F(θ) = D_KL[q(x; θ) || p(x)] where q is Gaussian N(μ, σ²) and p is a fixed target distribution N(3, 4). Starting from θ₀ = (μ₀, σ₀²) = (0, 1):

1. Compute the Euclidean gradient ∇_θ F at θ₀
2. Compute the Fisher information G(θ₀) for Gaussian parameters (μ, σ²)
3. Compute the natural gradient G⁻¹ ∇_θ F at θ₀
4. Take one step of each (with learning rate η = 0.1) and compare the resulting distributions
5. Which step produces a larger change in the distribution? Which produces a larger change in parameters?

{fill:textarea}

## Part 3: Exponential Family Geometry

> **Learning Goal:** Explore the dual geometry of exponential families.

**Exercise**: For the Gaussian family N(μ, σ²):

**Natural parameters**: η₁ = μ/σ², η₂ = -1/(2σ²)
**Expectation parameters**: m₁ = μ, m₂ = μ² + σ²

1. Express the KL divergence D_KL[q(η₁) || q(η₂)] in natural parameters
2. Express the same KL divergence in expectation parameters  
3. How does the duality between these coordinate systems simplify computation?
4. What is the log-partition function A(η)? Verify that ∂A/∂ηᵢ = mᵢ

{fill:textarea}

## Part 4: Geodesics on the Gaussian Manifold

> **Learning Goal:** Visualize belief updating as geodesic flow.

**Exercise**: Consider updating a belief from N(0, 1) to N(3, 4):

1. The geodesic (shortest path on the manifold) connects these two Gaussians. In the (μ, σ²) plane, this is NOT a straight line — it curves due to the metric.
2. Sketch (or describe) the geodesic path from (0, 1) to (3, 4) in the (μ, σ²) plane, noting that the Fisher metric scales distances differently in each direction.
3. Compare this to the straight-line (Euclidean) path from (0, 1) to (3, 4). Which path is shorter in parameter space? Which is shorter in distributional space (Fisher metric)?
4. How does this relate to belief updating in the brain?

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: Information geometry provides an elegant mathematical framework, but does the brain actually perform natural gradient descent? What neural evidence supports or challenges this hypothesis? Is the Fisher information matrix biologically computable?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Mathematical derivation | Fisher information computation |
| 2 | Comparison analysis | Natural vs. Euclidean gradients |
| 3 | Exponential family theory | Dual geometry |
| 4 | Geometric reasoning | Geodesics on manifolds |
| 5 | Critical reflection | Biological plausibility |
