# Lab: Derivation Exercise — Free Energy and Markov Blankets

## Objective

Derive the core mathematical results underlying Active Inference: the Markov Blanket partition, the variational free energy bound, and the decomposition of free energy into accuracy and complexity.

## Part 1: Markov Blanket Derivation

**Goal**: Prove the conditional independence conditions from the graphical model.

Given a Bayesian network with four variable sets: internal (μ), external (η), sensory (s), active (a), where:

- η → s (external states cause sensory states)
- μ → a (internal states cause active states)
- s → μ (sensory states influence internal states)
- a → s (active states influence sensory states)

**Derivation task**: Using the d-separation criterion, prove that μ ⊥ η | {s, a}.

Show all steps, starting from the graphical structure and applying the d-separation rules (blocking via conditioning on colliders vs. non-colliders).


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: The Free Energy Bound

**Goal**: Derive the ELBO inequality.

Starting from:

F = E_q[ln q(η) - ln p(η, s)]

**Step 1**: Expand p(η, s) = p(η|s) · p(s)

**Step 2**: Substitute and rearrange to obtain:

F = D_KL[q(η) ‖ p(η|s)] - ln p(s)

**Step 3**: Since D_KL ≥ 0, conclude F ≥ -ln p(s)

Write out each step of the derivation completely, showing all algebraic manipulations.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Accuracy-Complexity Decomposition

**Goal**: Derive the alternative decomposition of free energy.

Starting from F = E_q[ln q(η) - ln p(η, s)], show that:

**F = -E_q[ln p(s|η)] + D_KL[q(η) ‖ p(η)]**

where:

- **-E_q[ln p(s|η)]** is the *negative accuracy* (expected negative log-likelihood)
- **D_KL[q(η) ‖ p(η)]** is the *complexity* (divergence of posterior from prior)

Explain why minimizing F requires balancing accuracy (explaining the data) with complexity (not deviating too far from priors).


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Gaussian Example

**Goal**: Compute free energy analytically for Gaussian distributions.

Let the generative model be:

p(η) = N(η; μ₀, σ₀²)
p(s|η) = N(s; η, σ_s²)

And the recognition density be: q(η) = N(η; μ_q, σ_q²)

**Task**: Compute F = -E_q[ln p(s|η)] + D_KL[q(η) ‖ p(η)] analytically. Show all integrals.

Then find the optimal μ_q and σ_q by setting ∂F/∂μ_q = 0 and ∂F/∂σ_q = 0.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Synthesis

**Goal**: Connect the mathematical results to the conceptual framework.

In 200 words, explain how the three derivations (Markov Blanket, ELBO, accuracy-complexity) together establish the mathematical foundation of Active Inference: that a self-organizing system with a Markov Blanket can always be described as minimizing free energy, which entails approximate Bayesian inference.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Graphical model reasoning | Markov Blanket conditional independence proof |
| 2 | Variational calculus | ELBO derivation and bound proof |
| 3 | Decomposition | Accuracy-complexity trade-off |
| 4 | Analytic computation | Gaussian free energy optimization |
| 5 | Mathematical-conceptual integration | Connecting derivations to Active Inference |
