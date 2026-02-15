# Station: Cognition (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- Bayes' theorem, prior-posterior updating, and precision
- **Topics**: Bayes' Theorem, Prior and Posterior Distributions, Sequential Updating, Prior Strength and Precision
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with counting tables before introducing the Bayes formula.
- Use the medical test example to illustrate the base rate fallacy.
- Show sequential updating as repeated Bayes applications where posterior becomes the next prior.
- Connect prior strength to the Active Inference concept of precision.

## Active Inference Integration

- Cognition is belief updating: combining priors with likelihoods to form posteriors.
- Bayes' theorem is the core mathematical operation of the generative model.
- Sequential updating shows how agents continuously revise beliefs as data arrives.
- Precision (inverse variance) determines how much weight new evidence gets vs. existing beliefs.

## Lab Design Principles

- Include a counting-table derivation so students see Bayes emerge from simple arithmetic.
- The medical test problem should produce a surprising result (low posterior despite 99% test accuracy).
- Sequential updating exercises should have 3+ rounds to show cumulative belief shift.
- Prior strength comparison should use two agents with different priors observing the same data.

## Question Design Standards

- Computational questions should have definite numerical answers.
- Include at least one question that requires computing P(D) via the law of total probability.
- At least one question should involve sequential (multi-step) updating.
- Connect precision and prior strength to Active Inference explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
