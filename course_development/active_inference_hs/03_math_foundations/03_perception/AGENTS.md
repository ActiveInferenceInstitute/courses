# Station: Perception (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- conditional probability, likelihood functions, and evidence weighting
- **Topics**: Conditional Probability, Likelihood, Likelihood Ratios, Generative Model Tables, Backward Inference
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with concrete counting problems (students in clubs) before introducing P(A|B) notation.
- Clearly distinguish P(A|B) from P(B|A) -- this confusion is the base rate fallacy.
- Use likelihood ratio as an intuitive bridge: "which hypothesis does the evidence support more?"
- Always have students verify rows of conditional probability tables sum to 1.

## Active Inference Integration

- Perception is the process of inferring hidden states from observations.
- The generative model specifies P(observation | hidden state) -- a conditional probability table.
- Likelihood measures how well the model's predictions match actual observations.
- Perception as inference sets up Bayes' theorem (next module).

## Lab Design Principles

- Include Venn diagram exercises to visualize conditional probability.
- Use 2-hypothesis problems (Bag A vs Bag B) for likelihood comparisons.
- Conditional probability tables should have rows summing to 1.
- Build toward backward inference (observation to cause) without requiring full Bayes.

## Question Design Standards

- Computational questions should have definite numerical answers.
- Include at least one question testing P(A|B) vs. P(B|A) distinction.
- At least one question should use a likelihood ratio.
- Connect generative model tables to Active Inference perception explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
