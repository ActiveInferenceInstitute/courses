# Station: Planning (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- decision trees, discounting, and expected free energy
- **Topics**: Decision Trees, Discounting Future Rewards, Expected Free Energy, Policy Evaluation
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with concrete decision trees students can draw and evaluate by hand.
- Discounting should use simple reward sequences with gamma = 0.5 and 0.9 for contrast.
- Expected free energy should be presented as pragmatic value + epistemic value (simplified).
- Policy evaluation should enumerate all policies in a small scenario (4 policies max).

## Active Inference Integration

- Planning in Active Inference means evaluating policies by their expected free energy.
- Expected free energy combines pragmatic value (expected reward) and epistemic value (information gain).
- Agents select policies in proportion to exp(-G), where G is expected free energy.
- The planning horizon determines how many future time steps the agent considers.

## Lab Design Principles

- Decision trees should have at most 2 levels with 2 branches each.
- Discounting exercises should compare steady vs. delayed reward policies.
- Expected free energy should be simplified as a sum of pragmatic and epistemic components.
- Policy tables should have 4 policies with distinct reward and information profiles.

## Question Design Standards

- Computational questions should have definite numerical answers.
- Include at least one question requiring backward induction on a decision tree.
- At least one question should compare policy rankings with and without epistemic value.
- Connect policy evaluation to Active Inference's expected free energy minimization explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
