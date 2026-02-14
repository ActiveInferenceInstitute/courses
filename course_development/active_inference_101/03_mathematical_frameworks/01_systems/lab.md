# Lab: Probability and Generative Models

> **Learning Goal:** Build intuition for probabilistic reasoning and generative model construction.

## Part 1: Bayesian Reasoning Practice

**Exercise**: For each scenario, identify the prior, likelihood, and compute the posterior using Bayes' theorem.

1. **Medical test**: A disease affects 1% of the population (prior). A test has 95% sensitivity (P(positive | disease) = 0.95) and 90% specificity (P(negative | no disease) = 0.90). You test positive. What's the probability you actually have the disease?

2. **Email spam**: 40% of your emails are spam (prior). P(contains "free" | spam) = 0.8, P(contains "free" | not spam) = 0.1. An email contains the word "free." What's the probability it's spam?

Show your calculations step by step.

{fill:textarea}

## Part 2: Building Generative Models

> **Learning Goal:** Construct a simple generative model from scratch.

**Exercise**: Build a generative model for weather and clothing:

- Hidden state s ∈ {sunny, rainy}
- Observation o ∈ {umbrella, sunglasses, jacket}

1. Define P(s) — the prior on weather states
2. Define P(o | s) — the likelihood of each observation given each weather state
3. Verify: Does your model make intuitive sense? (P(umbrella | rainy) should be high)
4. Use Bayes' theorem: If you observe someone carrying an umbrella, what's the posterior P(s | umbrella)?

{fill:textarea}

## Part 3: Hidden Markov Model

> **Learning Goal:** Extend static models to dynamic sequences.

**Scenario**: A simple weather HMM:

- States: {sunny, rainy}
- Transition: P(sunny → sunny) = 0.7, P(sunny → rainy) = 0.3, P(rainy → rainy) = 0.6, P(rainy → sunny) = 0.4
- Observation: P(umbrella | rainy) = 0.9, P(umbrella | sunny) = 0.2

Day 1: You observe an umbrella. Day 2: You observe sunglasses. Day 3: You observe an umbrella.

1. What's the most likely weather sequence?
2. How does the inference at each step depend on the previous day?

{fill:textarea}

## Part 4: Connecting Math to Concepts

> **Learning Goal:** Bridge mathematical formalism to cognitive science concepts.

**Exercise**: Map each mathematical object to its cognitive science equivalent:

| Math | Cognitive Science |
|------|------------------|
| P(s) — prior | |
| P(o \| s) — likelihood | |
| P(s \| o) — posterior | |
| s — hidden state | |
| o — observation | |
| P(s_t \| s_{t-1}) — transition | |

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: Why is it useful to formalize intuitive concepts (like "belief" and "surprise") in mathematical language? What do we gain and what do we lose?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Bayesian computation | Prior × Likelihood → Posterior |
| 2 | Model building | Generative model construction |
| 3 | Temporal reasoning | Hidden Markov Models |
| 4 | Concept mapping | Math ↔ Cognitive science bridge |
| 5 | Epistemological reflection | Value of formalization |
