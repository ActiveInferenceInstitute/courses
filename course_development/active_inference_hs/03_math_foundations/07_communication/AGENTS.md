# Station: Communication (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- information theory, entropy, and divergence measures
- **Topics**: Information Content (Surprisal), Entropy, KL Divergence, Mutual Information
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with surprisal of everyday events before introducing the log formula.
- Use base-2 logarithms consistently so answers are in bits.
- Entropy comparisons should use fair vs. biased distributions.
- KL divergence should be shown to be asymmetric through explicit computation.

## Active Inference Integration

- Surprisal (-log P(o)) is the quantity that free energy bounds from above.
- Entropy measures the uncertainty in an agent's beliefs about hidden states.
- KL divergence between approximate and true posteriors is a core component of variational free energy.
- Mutual information quantifies epistemic value -- the information gain from making an observation.

## Lab Design Principles

- Surprisal exercises should contrast rare vs. common events.
- Entropy comparisons should use 2-outcome distributions (coins) for simplicity.
- KL divergence should use 3-outcome distributions and compute both directions.
- Mutual information should use a 2x2 joint probability table.

## Question Design Standards

- Computational questions should have definite numerical answers (may need calculator for logs).
- Include at least one question computing surprisal for everyday events.
- At least one question should compute entropy and identify which distribution is more uncertain.
- Connect KL divergence and mutual information to Active Inference explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
