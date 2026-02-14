# Module 04: Cognition — Precision Optimization and Attention

## Learning Objectives

1. Derive the **precision optimization** equations — how the brain estimates and adjusts the precision (inverse variance) of prediction errors.
2. Formalize **attention as precision optimization**: increasing the gain on relevant prediction errors to weight them more heavily.
3. Derive the relationship between precision, Fisher information, and model confidence.

## Introduction

Precision — the inverse variance of a probability distribution — is the fundamental quantity that determines which prediction errors drive belief updating and which are ignored. This module derives the mathematics of precision optimization: how it is estimated from data, how it modulates message passing, and how its optimization corresponds to attention.

## Key Concepts

### 1. Precision as a Parameter of the Generative Model

In a Gaussian generative model, precision appears as:

**p(oₜ | sₜ) = N(oₜ; g(sₜ), Π⁻¹)**

where Π = diag(π₁, ..., π_D) is the precision matrix (inverse covariance). High precision π_d means low variance in dimension d — observations are reliable. Low precision means high variance — observations are noisy.

Precision is itself a hidden variable that must be inferred:

**q(Π) = Wishart(Π; ν, V) or q(πd) = Gamma(πd; α, β)**

### 2. Precision Optimization Equations

The free energy gradient with respect to precision parameters:

**∂F/∂π = -½ · [π⁻¹ - E_q[(oₜ - g(sₜ))²]]**

At the fixed point (∂F/∂π = 0):

**π* = 1 / E_q[(oₜ - g(sₜ))²]**

The optimal precision equals the inverse of the expected squared prediction error. This means the brain learns precision from the statistics of its own prediction errors: consistently large errors → low precision; consistently small errors → high precision.

### 3. Precision and the Fisher Information Matrix

The Fisher information matrix I(θ) measures the curvature of the log-likelihood:

**I(θ) = -E[∂²/∂θ² ln p(o | θ)]**

For Gaussian models, the Fisher information is directly related to precision:

**I = Π**

This connects precision to **confidence**: high precision (high Fisher information) means the data carry a lot of information about the hidden states, enabling confident inference. This is the mathematical basis for the claim that attention enhances confidence.

### 4. Attention as Precision Optimization

In hierarchical predictive coding, attention corresponds to optimizing precision at each level:

**dγₗ/dt = -∂F/∂γₗ**

where γₗ is the log-precision at level l. This modulates the gain on prediction errors:

- Increasing γₗ → amplifying prediction errors at level l → "paying attention" to data at that level
- Decreasing γₗ → attenuating prediction errors → "ignoring" data at that level

## Derivation Exercises

1. For a Gaussian likelihood p(o|s) = N(g(s), π⁻¹), derive ∂F/∂π and find the optimal precision π*.
2. Show that the Fisher information I = Π for a univariate Gaussian with known mean and unknown variance.
3. Derive the precision update equation for a two-level hierarchy with different precisions at each level.

## Conclusion

Precision is the key quantity that bridges perception (what to believe) and attention (what to attend to). Its optimization provides the mathematical foundation for understanding how the brain allocates its computational resources. Module 05 extends the framework to action — how the agent changes the world, not just its beliefs.
