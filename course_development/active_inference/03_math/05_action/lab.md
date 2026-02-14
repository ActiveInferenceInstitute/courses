# Lab: Derivation Exercise — Expected Free Energy and Policy Selection

## Objective

Derive the Expected Free Energy functional and its decomposition, then apply it to a concrete POMDP to compute policy values.

## Part 1: Continuous Action

**Goal**: Derive the action equation for a continuous system.

**Model**: Sensory state s depends on action a via s = h(a) + ω (e.g., h(a) = a for direct motor control). Free energy F = ½π(s - g(μ))².

**Task**:

1. Compute ∂F/∂a using the chain rule: ∂F/∂a = ∂F/∂s · ∂s/∂a
2. Show that da/dt = -∂F/∂a drives s toward g(μ) — action fulfills the sensory prediction
3. Interpret: action is "making predictions come true" through the sensorimotor mapping

{fill:textarea}

## Part 2: EFE Decomposition

**Goal**: Derive the pragmatic-epistemic decomposition of G.

Starting from: **G(π) = E_{q(oₜ,sₜ|π)}[ln q(sₜ|π) - ln p(oₜ, sₜ)]**

**Task**:

1. Expand p(oₜ, sₜ) = p(oₜ|sₜ) · p(sₜ) using the generative model
2. Add and subtract E_q[ln q(sₜ|oₜ, π)]
3. Show that G decomposes into:
   - **Information gain**: -E_q[D_KL[q(sₜ|oₜ,π) ‖ q(sₜ|π)]] (epistemic value)
   - **Pragmatic value**: E_q[-ln p(oₜ)] (how much outcomes deviate from preferences)
4. Explain why information gain is always negative (policies always have non-negative epistemic value)

{fill:textarea}

## Part 3: Concrete POMDP Computation

**Goal**: Compute EFE for a simple POMDP.

Consider a T-maze POMDP with:

- 4 states: {left-reward, right-reward, left-no-reward, right-no-reward}
- 4 observations: {reward, no-reward, left-cue, right-cue}
- 2 actions: {go-left, go-right}
- Preferences: C = [ln 2, ln(1/2), 0, 0] (prefer reward, avoid no-reward, neutral on cues)

The A matrix (likelihood):

```
A = [0.9  0.1  0.5  0.5;
     0.1  0.9  0.5  0.5;
     0.5  0.5  0.8  0.2;
     0.5  0.5  0.2  0.8]
```

**Task**:

1. For policy π₁ = go-left and state belief q(s) = [0.5, 0.5, 0, 0], compute the expected observations E_q[p(o|s)]
2. Compute the pragmatic value: E_q[-ln p(o)] using the C vector
3. Compute the epistemic value: expected information gain
4. Determine which policy (go-left vs go-right) has lower EFE

{fill:textarea}

## Part 4: Softmax Policy Selection

**Goal**: Derive the policy posterior from EFE values.

Given computed EFE values G(π₁), G(π₂), ..., G(πK):

**Task**:

1. Write the softmax: P(πₖ) = exp(-γ · G(πₖ)) / ∑ⱼ exp(-γ · G(πⱼ))
2. Compute P(π) for the T-maze example with γ = 1 and γ = 16
3. Show how increasing γ (inverse temperature) makes policy selection more deterministic
4. Discuss: what does γ → ∞ correspond to? What about γ → 0?

{fill:textarea}

## Part 5: Synthesis

In 200 words, explain how the EFE framework unifies exploration (epistemic value) and exploitation (pragmatic value) under a single objective, and how this resolves the exploration-exploitation dilemma that plagues classical reinforcement learning.

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Continuous calculus | Action equation via chain rule |
| 2 | Functional decomposition | EFE → epistemic + pragmatic components |
| 3 | Numerical computation | EFE for a concrete POMDP |
| 4 | Softmax analysis | Temperature-dependent policy selection |
| 5 | Conceptual integration | Exploration-exploitation unification |
