# Station: Action (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: EFE computation, policy evaluation, softmax policy selection, exploration-exploitation in the T-maze, action parameter sweep
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements policy selection via expected free energy. Content should:

1. **Implement compute_efe()**: A function that evaluates the expected free energy for each policy, decomposing it into pragmatic and epistemic components.
2. **Define key implementation concepts**:
   - **compute_efe(policy)**: Returns the expected free energy for a given policy (action sequence), using the A, B, C matrices
   - **Policy evaluation loop**: Iterating over all possible policies, computing EFE for each, and selecting via softmax
   - **Pragmatic component**: Computed from the C vector (preferences) and expected future observations
   - **Epistemic component**: Computed from the expected information gain (reduction in posterior entropy)
3. **Demonstrate exploration-exploitation**: Run the T-maze agent with different levels of uncertainty and show how the balance between epistemic and pragmatic action shifts.
4. **Parameter sweep**: Vary the precision parameter (gamma/alpha) and show its effect on action selection (more explorative vs. more exploitative).

## Active Inference Integration

- EFE computation is the core action selection mechanism in discrete Active Inference
- The T-maze demonstrates how the agent first explores (visits the cue) then exploits (goes to the rewarding arm)
- The precision parameter on policy selection controls the exploration-exploitation trade-off

## Assessment Alignment

Questions should test the ability to:
- Implement the EFE computation for a given policy
- Interpret the decomposition of EFE into pragmatic and epistemic terms
- Predict agent behavior under different precision settings

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
