# Module 06: Learning — Parameter and Structure Learning

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Define **parameter learning** mathematically: updating the sufficient statistics of the A, B, C, D matrices.
2. Introduce **Bayesian Model Reduction** (BMR) as the mechanism for structure learning.
3. Explain how learning operates on a **slower timescale** than perception using Dirichlet distributions.

## Introduction

Perception updates beliefs about hidden states (fast timescale). Learning updates the model itself — its parameters and structure (slow timescale). This module formalizes the difference mathematically.

## Key Concepts

### 1. Parameter Learning — Updating Model Parameters

In the POMDP, the A and B matrices are initially uncertain. **Parameter learning** means updating them based on experience.

Mathematically, we represent uncertainty about parameters using **Dirichlet distributions**:

- Before experience: The A matrix starts with weak beliefs — A_prior = small concentration parameters (e.g., α = 1)
- After experience: Each time the agent observes state-observation pair (s, o), the corresponding entry is incremented: α(o, s) → α(o, s) + 1
- Over time: The entries grow, the distribution sharpens, and the A matrix becomes more certain

This is **Dirichlet-Categorical conjugacy** — a mathematically elegant property where the posterior stays in the same distribution family as the prior.

### 2. Concentration Parameters and Confidence

The concentration parameters α control how confident the agent is:

- **Small α (e.g., [1, 1, 1])**: Maximum uncertainty — all outcomes equally likely
- **Large α (e.g., [100, 5, 5])**: High confidence — heavily favors the first outcome
- **Sum of α**: Total "experience count" — larger sum = stronger confidence = slower updating

This explains why young animals learn fast (small α, weak priors) while experienced adults change slowly (large α, strong priors).

### 3. Learning Rate Emerges from Experience

The effective learning rate decreases naturally:

- After 1 observation: Learning rate ≈ 1/2 (each new data point has 50% influence)
- After 100 observations: Learning rate ≈ 1/101 (each new data point has ~1% influence)
- After 1000 observations: Learning rate ≈ 1/1001 (~0.1% influence)

This automatic decay of learning rate is optimal — early observations should matter more, later observations refine but don't fundamentally change the model.

### 4. Structure Learning — Bayesian Model Reduction (BMR)

**Structure learning** asks: "Does my model have the right structure?" — too many states? Wrong factorization? Unnecessary connections?

**Bayesian Model Reduction** compares the current model to simpler alternatives:

- Compute the model evidence F for the current model
- Compute F for simpler models (with some connections removed)
- If a simpler model has equal or better evidence → adopt it

BMR prunes unnecessary model complexity, implementing the mathematical version of Occam's razor. It's done offline (during rest/sleep) and is computationally cheap once the full model is learned.

### 5. Learning vs. Inference — Timescale Separation

| Property | Inference (Perception) | Learning |
|----------|----------------------|---------|
| What updates? | q(s) — beliefs about states | Parameters α — the model itself |
| Timescale | Milliseconds | Minutes to years |
| Mathematical object | Posterior over states | Posterior over parameters |
| Effect of one observation | Can completely change beliefs | Slight nudge to parameters |

## Summary

Parameter learning updates the A and B matrices using Dirichlet distributions, with learning rate naturally decreasing with experience. Structure learning (BMR) prunes unnecessary model complexity by comparing simpler alternatives. Learning operates on a slower timescale than perception, with the timescale separation emerging naturally from the accumulation of concentration parameters.

## Further Reading

- Friston, K. J. et al. (2016). Active inference and learning. *Neuroscience & Biobehavioral Reviews*, 68, 862-879.
- Friston, K. J. et al. (2018). Bayesian model reduction. *arXiv:1805.07092*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press. (Chapter 7)
