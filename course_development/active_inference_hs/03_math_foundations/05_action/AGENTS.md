# Station: Action (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- expected value, optimization, and gradient descent
- **Topics**: Expected Value of Actions, Expected Loss, Explore-Exploit Tradeoff, Gradient Descent
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with decision tables students can compute by hand (study strategies, games).
- Show optimization from two perspectives: maximizing reward AND minimizing loss.
- Introduce the explore-exploit tradeoff as a natural tension in decision-making.
- Use the parabola f(x) = (x-3)^2 for an intuitive introduction to gradient descent.

## Active Inference Integration

- Action selection in Active Inference minimizes expected free energy.
- Expected free energy combines pragmatic value (expected reward) and epistemic value (information gain).
- The explore-exploit tradeoff emerges naturally from the expected free energy functional.
- Gradient descent is analogous to how agents iteratively adjust actions to reduce free energy.

## Lab Design Principles

- Decision tables should have 3 options and 3 outcomes for manageable computation.
- Expected loss exercises should mirror expected value exercises to show duality.
- Explore-exploit should use a concrete scenario (unknown strategy vs. known strategy).
- Gradient descent should use a simple quadratic so students can compute each step by hand.

## Question Design Standards

- Computational questions should have definite numerical answers.
- Include at least one question comparing maximizing reward vs. minimizing loss.
- At least one question should require reasoning about information gain vs. immediate reward.
- Connect expected free energy to Active Inference action selection explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
