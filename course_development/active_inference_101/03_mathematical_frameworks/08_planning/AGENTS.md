# Station: Planning (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Deep temporal models, hierarchical POMDPs, planning horizon, policy trees, sophisticated inference
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module formalizes planning as inference over deep temporal models. Content should:

1. **Extend the POMDP to multiple timescales**: Deep temporal models have hierarchical layers where higher levels make predictions about longer time horizons, and lower levels make predictions about immediate states.
2. **Define key terms precisely**:
   - **Deep temporal model**: A hierarchical generative model where each level predicts at a different temporal resolution (fast dynamics nested within slow dynamics)
   - **Policy tree**: The branching structure of possible future action sequences, evaluated by expected free energy at each branch
   - **Planning horizon**: The number of future time steps over which the agent evaluates policies; limited by computational resources
   - **Sophisticated inference**: A recursive form of planning where the agent considers how its future beliefs will change, not just how states will change
3. **Derive the planning as inference equations**: Show how EFE is evaluated over multiple future time steps, summing expected free energy at each step along each policy.
4. **Address computational complexity**: Show how the number of policies grows exponentially with horizon and discuss pruning strategies.

## Active Inference Integration

- Deep temporal models implement hierarchical planning (Friston et al., 2018)
- Sophisticated inference goes beyond standard EFE by accounting for future belief updating (Friston et al., 2021)
- Habit formation corresponds to collapsing the policy evaluation into a strong prior, bypassing deliberative EFE computation

## Assessment Alignment

Questions should test the ability to:
- Compute EFE over a multi-step planning horizon for a simple POMDP
- Compare standard and sophisticated inference in a given scenario
- Explain the trade-off between planning horizon length and computational tractability

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
