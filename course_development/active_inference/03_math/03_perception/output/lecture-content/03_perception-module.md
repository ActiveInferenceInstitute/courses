# Module 03: Perception — Belief Updating, Message Passing, and Predictive Coding Equations

## Learning Objectives

1. Derive the **belief updating equations** for perception: how the recognition density q(s) is updated in response to new observations.
2. Formalize **message passing** in hierarchical generative models — how prediction errors propagate up and predictions propagate down.
3. Connect these equations to the **predictive coding** scheme of Rao and Ballard (1999).
4. Show the relationship between predictive coding and the **Kalman filter** as a special case.

## Introduction

Perception in Active Inference is the optimization of the recognition density q(s) given new observations o — updating beliefs about hidden states to minimize free energy. This module derives the mathematical equations governing this process, showing how they give rise to the message-passing architecture known as predictive coding.

## Key Concepts

### 1. Perception as Free Energy Minimization

Given an observation oₜ, perception updates the recognition density:

**q*(sₜ) = argmin_{q(sₜ)} F(oₜ, q)**

For a Gaussian recognition density q(sₜ) = N(μₜ, Σₜ), this reduces to gradient descent on free energy with respect to the sufficient statistics:

**dμ/dt = -∂F/∂μ**

This is the **perception equation**: internal states (sufficient statistics) flow in the direction that minimizes free energy.

### 2. Hierarchical Message Passing

For a hierarchical generative model with L levels:

**p(o, s₁, ..., s_L) = p(o | s₁) ∏ₗ p(sₗ | sₗ₊₁)**

The free energy gradient at level l takes the form:

**dμₗ/dt = -Πₗ · εₗ + Πₗ₊₁ · (∂g/∂μₗ)ᵀ · εₗ₊₁**

where:

- **εₗ = μₗ - gₗ(μₗ₊₁)** is the prediction error at level l (difference between the current estimate and the prediction from the level above)
- **Πₗ** is the precision (inverse covariance) at level l
- **gₗ(·)** is the generative mapping from level l+1 to level l

This decomposes into two streams:

- **Bottom-up**: prediction errors εₗ weighted by their precision Πₗ
- **Top-down**: predictions gₗ(μₗ₊₁) from the level above

### 3. Predictive Coding

The message-passing equations above are exactly the **predictive coding** scheme:

1. Each level generates a prediction of the level below: **prediction = g(μₗ₊₁)**
2. The prediction error is computed: **εₗ = observed - predicted**
3. Precision-weighted prediction errors drive updates at each level
4. The system iterates until prediction errors are minimized

Rao and Ballard (1999) showed this scheme reproduces classical receptive field properties in V1. Friston (2005) showed it arises naturally from free energy minimization in hierarchical Gaussian models.

### 4. Worked Example: Two-Level Gaussian Perception

Consider a simple two-level model:

- **Observation**: o = s₁ + ε₁, where ε₁ ~ N(0, σ₁²)
- **Prior**: s₁ = s₂ + ε₂, where ε₂ ~ N(0, σ₂²)

The prediction errors are:

- **Level 1**: ε₁ = o - μ₁ (observation minus current belief)
- **Level 2**: ε₂ = μ₁ - g(μ₂) = μ₁ - μ₂ (belief minus prior prediction)

The belief update for μ₁ balances these two errors:

**dμ₁/dt = π₁ · (o - μ₁) - π₂ · (μ₁ - μ₂)**

At equilibrium, solving dμ₁/dt = 0:

**μ₁* = (π₁ · o + π₂ · μ₂) / (π₁ + π₂)**

This is the **precision-weighted average** of the observation and the prior prediction — the classic Bayesian posterior mean. High sensory precision (π₁ >> π₂) pulls the belief toward the observation; high prior precision (π₂ >> π₁) pulls it toward the prior.

### 5. Connection to the Kalman Filter

For a linear-Gaussian dynamical system, predictive coding reduces exactly to the **Kalman filter**:

- **Prediction step**: μₜ|ₜ₋₁ = A · μₜ₋₁|ₜ₋₁ (top-down prediction)
- **Update step**: μₜ|ₜ = μₜ|ₜ₋₁ + K · (oₜ - C · μₜ|ₜ₋₁) (prediction error correction)

where K = Σ · Cᵀ · (C · Σ · Cᵀ + R)⁻¹ is the Kalman gain — a precision-weighted scaling of the prediction error. The Kalman filter is thus a special case of Active Inference perception in linear-Gaussian state-space models.

This connection shows that Active Inference perception is a **generalization** of classical optimal estimation: the Kalman filter handles linear dynamics; Active Inference handles arbitrary nonlinear generative models through gradient descent on free energy.

## Derivation Exercises

1. For a two-level Gaussian model p(o|s₁) = N(g₁(s₁), Σ₁) and p(s₁|s₂) = N(g₂(s₂), Σ₂), derive the prediction error form of the free energy gradient ∂F/∂μ₁.
2. Show that the fixed point of dμ/dt = -∂F/∂μ corresponds to the MAP estimate of the posterior p(s|o).
3. Derive the precision-weighted prediction error message passing for a three-level hierarchy.
4. Show that the two-level Gaussian case with linear generative mappings recovers the Kalman filter update equations.

## Conclusion

Perception is gradient descent on free energy, implemented through precision-weighted prediction error message passing in a hierarchical generative model. This is the formal foundation of predictive coding, which generalizes the Kalman filter to nonlinear, hierarchical settings. Module 04 extends this to the mathematics of precision and attention.

## Further Reading

- Rao, R. P. N. & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79-87.
- Friston, K. (2005). A theory of cortical responses. *Philosophical Transactions of the Royal Society B*, 360(1456), 815-836.
- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering*, 82(1), 35-45.
