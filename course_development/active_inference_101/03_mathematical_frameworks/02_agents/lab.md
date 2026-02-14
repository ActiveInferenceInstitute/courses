# Lab: Variational Inference

> **Learning Goal:** Build intuition for approximate inference through worked examples and conceptual exercises.

## Part 1: Why Exact Inference Fails

**Exercise**: Consider a simple model with 3 binary hidden states (s₁, s₂, s₃).

1. List all possible state combinations (there should be 2³ = 8).
2. Now consider 10 binary states: How many combinations? 20 states? 50 states?
3. If evaluating each combination takes 1 nanosecond, how long would it take to evaluate all combinations for 50 binary states?
4. Why does this demonstrate the need for approximate inference?

{fill:textarea}

## Part 2: KL Divergence Computation

> **Learning Goal:** Compute and interpret KL divergence for simple distributions.

**Exercise**: Consider two discrete distributions over outcomes {A, B, C}:

- P = {0.5, 0.3, 0.2}
- Q₁ = {0.4, 0.35, 0.25}
- Q₂ = {0.1, 0.1, 0.8}

1. Compute D_KL[Q₁ || P] = Σ Q₁(x) × log(Q₁(x)/P(x))
2. Compute D_KL[Q₂ || P]
3. Which approximation (Q₁ or Q₂) is closer to P? Does this match your intuition?

{fill:textarea}

## Part 3: The ELBO Decomposition

> **Learning Goal:** Understand accuracy vs. complexity in model fitting.

**Scenario**: Two students build models to predict exam scores:

- Student A's model: "Everyone gets a B" (simple but inaccurate)
- Student B's model: "Score depends on study hours, GPA, sleep, mood, day of week, horoscope, weather, shirt color..." (accurate on training data but overly complex)

1. Which model has higher accuracy? Which has lower complexity?
2. Which model would the ELBO prefer? Why?
3. What would an optimal model look like?

{fill:textarea}

## Part 4: Connecting Free Energy to Cognition

> **Learning Goal:** Map mathematical quantities to cognitive concepts.

| Mathematical Quantity | Cognitive Equivalent |
|----------------------|---------------------|
| q(s) | |
| P(s \| o) | |
| F (free energy) | |
| D_KL[q \|\| p] | |
| Accuracy term | |
| Complexity term | |

Fill in the cognitive equivalents (hint: beliefs, perfect inference, surprise, error, fit, simplicity).

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: The brain can't perform exact Bayesian inference, so it approximates. Does this mean our beliefs are always "wrong" to some degree? Is approximate inference a limitation or an advantage?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Exponential growth analysis | Intractability of exact inference |
| 2 | KL divergence computation | Measuring distribution closeness |
| 3 | Trade-off analysis | ELBO accuracy-complexity balance |
| 4 | Concept mapping | Math ↔ Cognition bridge |
| 5 | Epistemological reflection | Approximate vs. exact inference |
