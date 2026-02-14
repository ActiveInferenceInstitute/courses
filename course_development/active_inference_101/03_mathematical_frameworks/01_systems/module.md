# Module 01: Systems — Probability and Generative Models

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Review **probability basics**: random variables, probability distributions, conditional probability, Bayes' theorem.
2. Define a **generative model** mathematically: a joint distribution P(observations, hidden states).
3. Explain why generative models are the mathematical formalization of "systems" in Active Inference.

## Introduction

The Cognitive Science and Computational Neuroscience units introduced Active Inference conceptually and neurally. Now we develop the *mathematics*. Don't worry — we'll build up from basics. This module starts with probability theory and generative models.

## Key Concepts

### 1. Random Variables and Probability Distributions

A **random variable** is a quantity whose value is uncertain. We describe uncertainty with **probability distributions**:

- **Discrete**: P(X = x) for each possible value (e.g., rolling a die: P(X = 3) = 1/6)
- **Continuous**: p(x) — a probability density function (e.g., human height follows a bell curve)

Key properties:

- All probabilities are between 0 and 1
- Total probability sums/integrates to 1

### 2. Joint, Marginal, and Conditional Probability

For two random variables X and Y:

- **Joint**: P(X, Y) — probability of X *and* Y occurring together
- **Marginal**: P(X) = Σ_Y P(X, Y) — probability of X regardless of Y
- **Conditional**: P(X | Y) — probability of X *given* that Y is known

**Example**: X = "it's raining," Y = "you see dark clouds"

- P(rain, clouds) = probability of both
- P(rain) = total probability of rain
- P(rain | clouds) = probability of rain given you see clouds (higher than P(rain) alone!)

### 3. Bayes' Theorem — The Update Rule

**Bayes' theorem** is the mathematical engine of Active Inference:

**P(s | o) = P(o | s) × P(s) / P(o)**

Where:

- **P(s | o)**: Posterior — what we believe about hidden state *s* after observing *o*
- **P(o | s)**: Likelihood — how probable observation *o* is given state *s*
- **P(s)**: Prior — what we believed before observing anything
- **P(o)**: Evidence — how probable the observation is overall (normalizing constant)

**Everyday example**: You hear a scratching sound (o). Was it your cat (s₁) or a burglar (s₂)?

- Prior: P(cat) = 0.95, P(burglar) = 0.05 (cats scratch more often)
- Likelihood: P(scratch | cat) = 0.8, P(scratch | burglar) = 0.3
- Posterior: P(cat | scratch) ≈ 0.98 — even more certain it's the cat

### 4. Generative Models — The Core Formalism

A **generative model** is a joint probability distribution that specifies how hidden states generate observations:

**P(o, s) = P(o | s) × P(s)**

This says: "The world (state s) generates observations (o) according to likelihood P(o | s), and states have prior probability P(s)."

The generative model is the mathematical version of the brain's "model of the world" from the Cognitive Science unit. It contains:

- What states exist (hidden states s)
- How states generate observations (likelihood)
- What the agent expects in advance (prior)

### 5. From Static to Dynamic: Adding Time

Real systems change over time. We extend the generative model:

**P(o₁:T, s₁:T) = P(s₁) × Π_t P(s_t | s_{t-1}) × Π_t P(o_t | s_t)**

This is a **Hidden Markov Model (HMM)** — the simplest dynamic generative model:

- P(s₁): Initial state distribution
- P(s_t | s_{t-1}): Transition dynamics (how states evolve)
- P(o_t | s_t): Observation model (how states generate data)

## Summary

Probability theory provides the language for Active Inference. Generative models — joint distributions over observations and hidden states — formalize the brain's model of the world. Bayes' theorem explains how agents update beliefs when new data arrives. Hidden Markov Models extend this to dynamic systems.

## Further Reading

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. (Chapter 2)
- MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press. (Chapter 2)
