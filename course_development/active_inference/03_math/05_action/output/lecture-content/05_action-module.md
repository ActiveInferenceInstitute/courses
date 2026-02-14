# Module 05: Action — Active Inference, Expected Free Energy, and the POMDP Framework

## Learning Objectives

1. Derive the **action equation**: how actions minimize free energy by changing sensory states.
2. Define the **Expected Free Energy (EFE)** functional G(π) and decompose it into epistemic and pragmatic components.
3. Formalize the **POMDP** (Partially Observed Markov Decision Process) framework for Active Inference policy selection.

## Introduction

Action in Active Inference is not governed by a separate optimization principle (like reward maximization). Instead, actions serve the same objective as perception: minimizing free energy. But where perception updates beliefs (internal states), action changes the world (blanket states). This module derives the mathematics of action selection and introduces the Expected Free Energy functional.

## Key Concepts

### 1. The Action Equation

The free energy F depends on sensory states s, which depend on actions a:

**a* = argmin_a F(s(a), μ)**

For continuous systems, action follows gradient descent:

**da/dt = -∂F/∂a = -∂F/∂s · ∂s/∂a**

The first factor (∂F/∂s) is the prediction error at the sensory level. The second factor (∂s/∂a) is the sensorimotor mapping. Together, they drive action to fulfill sensory predictions — if the brain predicts the arm is *here*, action moves the arm to make that prediction true.

### 2. Expected Free Energy

For discrete-time planning over policies π = (a₁, a₂, ..., aT), the agent evaluates the **Expected Free Energy** G(π):

**G(π) = ∑ₜ E_{q(oₜ,sₜ|π)}[ln q(sₜ|π) - ln p(oₜ, sₜ)]**

This decomposes into:

**G(π) = -∑ₜ E_q[ln p(oₜ)] + ∑ₜ E_q[H[p(oₜ|sₜ)]]**

where:

- **-E_q[ln p(oₜ)]** is the **pragmatic value** — negative log-prior preferences (how much the expected outcomes align with preferred outcomes)
- **E_q[H[p(oₜ|sₜ)]]** is the **epistemic value** — expected ambiguity (how much information the policy provides about hidden states)

Alternatively:

**G(π) = ∑ₜ {-E_q[D_KL[q(sₜ|oₜ,π) ‖ q(sₜ|π)]] + E_q[-ln p(oₜ)]}**

where the first term is **information gain** (negative) — policies that resolve uncertainty about states are preferred.

### 3. Policy Selection via Softmax

Policies are selected according to a softmax function over negative Expected Free Energy:

**P(π) = σ(-γ · G(π))**

where γ is an **inverse temperature** parameter controlling the precision of policy selection. High γ → deterministic selection of the best policy; low γ → more random (exploratory) selection.

### 4. The POMDP Framework

Active Inference in discrete time is implemented within a POMDP:

- **A** matrix: p(oₜ | sₜ) — likelihood mapping
- **B** matrix: p(sₜ | sₜ₋₁, aₜ₋₁) — transition dynamics conditioned on action
- **C** vector: ln p(oₜ) — log-prior preferences over outcomes
- **D** vector: p(s₁) — prior over initial states

The agent inverts this model to infer hidden states and select policies that minimize Expected Free Energy.

## Derivation Exercises

1. Derive the action equation da/dt = -∂F/∂a for a continuous system with linear sensorimotor mapping.
2. Starting from G(π) = ∑ₜ E_q[ln q(sₜ|π) - ln p(oₜ, sₜ)], derive the pragmatic-epistemic decomposition.
3. Show that maximizing information gain is equivalent to minimizing expected ambiguity.

## Conclusion

Action and perception are two sides of the same coin — both minimize (expected) free energy. The EFE decomposition reveals that intelligent behavior naturally balances exploitation (pragmatic value) and exploration (epistemic value). Module 06 extends this to the mathematics of learning.
