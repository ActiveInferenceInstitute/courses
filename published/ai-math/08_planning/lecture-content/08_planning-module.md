# Module 08: Planning — Sophisticated Inference, Deep Temporal Models, and Hierarchical POMDPs

## Learning Objectives

1. Derive **sophisticated inference**: recursive belief updating where the agent models its own future beliefs and actions.
2. Formalize **deep temporal models** (multi-step planning) through policy trees and Expected Free Energy evaluation.
3. Introduce **hierarchical POMDPs** for multi-timescale planning.

## Introduction

Planning is the most computationally demanding component of Active Inference — it requires the agent to evaluate the consequences of action sequences extending into the future. This module develops three levels of mathematical sophistication: basic policy evaluation (flat EFE), sophisticated inference (recursive belief updating), and hierarchical POMDPs (multi-timescale planning).

## Key Concepts

### 1. Deep Temporal Planning

The Expected Free Energy for a policy π of length T is:

**G(π) = ∑_{τ=t}^{T} G_τ(π)**

where each term evaluates the expected free energy at future time τ under policy π. This requires:

1. **State prediction**: q(s_τ | π) = ∑_{s_{τ-1}} B(π_τ) · q(s_{τ-1} | π)
2. **Outcome prediction**: q(o_τ | π) = A · q(s_τ | π)
3. **EFE evaluation**: G_τ(π) = E_q[ln q(s_τ|π) - ln p(o_τ, s_τ)]

The number of policies grows exponentially with planning horizon: K^T policies for K actions over T steps. This necessitates pruning strategies.

### 2. Sophisticated Inference

**Sophisticated inference** (Friston et al., 2021) extends basic policy evaluation by having the agent model _what it will believe_ in the future:

**q(s_{t+1} | π) → q(s_{t+1} | o_{t+1}, π)**

The agent simulates not just future states but future observations and the belief updates they will produce. At each future timestep:

1. Predict future observation: q(o_{τ+1} | s_{τ+1})
2. Update future beliefs: q(s_{τ+1} | o_{τ+1}) using Bayesian updating
3. Evaluate EFE with these updated future beliefs

This recursive structure means the agent anticipates how its own beliefs will change — a form of meta-cognition. The recursion can be extended to arbitrary depth: the agent models what it will believe, about what it will believe, about what it will believe...

### 3. Hierarchical POMDPs

For multi-timescale planning, the generative model is organized hierarchically:

**Level 1 (fast)**: p(o | s₁, a₁) — moment-to-moment actions (e.g., individual keystrokes)
**Level 2 (slow)**: p(s₁ | s₂, a₂) — mid-level sub-goals (e.g., typing a word)
**Level 3 (slowest)**: p(s₂ | s₃, a₃) — high-level goals (e.g., writing a paragraph)

Higher levels set contexts (prior preferences, initial states) for lower levels. The temporal scale of each level is determined by its time constant — higher levels evolve more slowly.

The free energy minimization operates across levels:
**F_total = F₁ + F₂ + F₃**

with top-down and bottom-up messages connecting levels, analogous to the perceptual hierarchy but extended to the action-planning domain.

## Derivation Exercises

1. Derive the EFE for a two-step, two-action POMDP. Enumerate all policies and compute G for each.
2. Show how sophisticated inference modifies the EFE by incorporating future belief updates into the evaluation.
3. Write the generative model for a two-level hierarchical POMDP and derive the free energy for each level.

## Conclusion

Planning completes the Active Inference framework by extending inference into the future — from single-step EFE evaluation through sophisticated recursive belief simulation to multi-timescale hierarchical planning. Together, the eight modules provide the complete mathematical foundation: from Markov Blankets (systems) through generative models (agents), perception, precision, action, learning, communication, and planning — a unified mathematics of mind.
