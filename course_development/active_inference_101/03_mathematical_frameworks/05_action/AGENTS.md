# Station: Action (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Expected free energy (EFE), policy selection, pragmatic and epistemic value decomposition, softmax policy distribution
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module derives the mathematics of action selection via expected free energy. Content should:

1. **Derive Expected Free Energy (EFE)**: Starting from the definition G(pi) = E_q[ln q(s_tau) - ln P(o_tau, s_tau | pi)], show how it decomposes into pragmatic and epistemic terms.
2. **Define key terms precisely**:
   - **Expected Free Energy G(pi)**: The expected surprise under a policy pi, evaluated over future time steps
   - **Pragmatic value**: -E_q[ln P(o_tau)] -- the degree to which expected outcomes match preferences (C vector)
   - **Epistemic value**: -E_q[H[P(o_tau|s_tau)]] -- the expected information gain about hidden states
   - **Policy distribution**: P(pi) = softmax(-G(pi)) -- policies are selected in proportion to their negative expected free energy
3. **Work through policy evaluation**: Given a POMDP with two or three policies, compute G for each and derive the policy distribution.
4. **Show how exploration-exploitation emerges**: When uncertainty is high, epistemic value dominates; when uncertainty is low, pragmatic value dominates.

## Active Inference Integration

- EFE is the key quantity for action selection in Active Inference (Friston et al., 2015; Parr et al., 2022, Chapter 6)
- The softmax over negative EFE gives a probabilistic policy selection (the agent does not always choose the "best" policy)
- The balance between pragmatic and epistemic value resolves the exploration-exploitation trade-off mathematically

## Assessment Alignment

Questions should test the ability to:
- Compute EFE for a given policy in a simple POMDP
- Decompose EFE into pragmatic and epistemic components
- Derive the policy distribution from EFE values using softmax

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
