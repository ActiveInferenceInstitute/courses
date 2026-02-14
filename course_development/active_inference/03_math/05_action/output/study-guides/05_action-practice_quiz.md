# Practice Quiz: Action

## Part A: Multiple Choice

1. The action equation da/dt = -∂F/∂a describes:
A) How beliefs are updated
B) How actions change sensory states to minimize free energy — "making predictions come true"
C) How parameters are learned
D) Static equilibrium only

2. Expected Free Energy G(π) differs from variational free energy F in that:
A) G evaluates *future* outcomes under a policy, while F evaluates *current* observations
B) G is always smaller than F
C) G does not involve probabilities
D) G is used only for perception

3. The pragmatic value component of EFE corresponds to:
A) Information gain
B) How well expected outcomes align with preferred outcomes (the C vector)
C) The entropy of the prior
D) The precision of observations

4. The epistemic value component of EFE corresponds to:
A) Reward maximization
B) Expected information gain — how much a policy will reduce uncertainty about hidden states
C) The log-likelihood
D) The number of actions available

5. In the softmax policy selection P(π) = σ(-γ · G(π)), the inverse temperature γ controls:
A) The speed of action execution
B) The precision of policy selection — high γ → more deterministic; low γ → more random
C) The number of policies considered
D) The prior probability of each policy

6. The A matrix in a POMDP encodes:
A) Actions
B) The likelihood mapping p(o|s) — how hidden states generate observations
C) Transition dynamics
D) Preferences

7. The C vector in a POMDP encodes:
A) Transition probabilities
B) Log-prior preferences over observations — ln p(o)
C) The likelihood
D) The initial state distribution

## Part B: Short Answer

1. For a two-policy POMDP with G(π₁) = -2 and G(π₂) = -5, compute P(π₁) and P(π₂) for γ = 1 and γ = 4. Show how increasing γ shifts probability toward the lower-EFE policy.
2. Explain the mathematical relationship between Expected Free Energy and the KL divergence between predicted and preferred outcomes. How does this formalize "goal-directed behavior"?
3. A policy π₁ has high pragmatic value but low epistemic value. Policy π₂ has low pragmatic value but high epistemic value. Under what conditions would the agent prefer π₂? How does this relate to curiosity-driven behavior?
