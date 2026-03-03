# Module 04: Cognition — Probability, Entropy, and Decision-Making

## Learning Objectives

1. Calculate **probability distributions** and interpret them as beliefs about the world.
2. Define **entropy** as a measure of uncertainty and connect it to the concept of "surprise."
3. Explain how an Active Inference agent uses its beliefs to make decisions under uncertainty.

## Introduction

Cognition is thinking — and thinking, mathematically, is the manipulation of probability distributions. When you believe "it will probably rain today," your brain is assigning a high probability to rain and a low probability to sun. This module introduces the mathematics of belief: probability distributions, entropy, and how agents use these tools to make intelligent decisions under uncertainty.

## Key Concepts

### 1. Probability Distributions as Beliefs

A **probability distribution** assigns a number between 0 and 1 to each possible outcome. For a coin: $P(\text{heads}) = 0.5$, $P(\text{tails}) = 0.5$. For today's weather, your brain might assign: $P(\text{rain}) = 0.7$, $P(\text{sun}) = 0.2$, $P(\text{snow}) = 0.1$. These numbers represent your *belief state* — they are your brain's generative model of what will happen.

### 2. Entropy: Measuring Uncertainty

**Shannon entropy** measures how uncertain a probability distribution is:

$$H = -\sum_i P(x_i) \log_2 P(x_i)$$

A fair coin has maximum entropy ($H = 1$ bit): you are maximally uncertain. A rigged coin ($P(\text{heads}) = 0.99$) has low entropy: you are very confident. Agents in Active Inference are driven to reduce entropy — to move from "I have no idea" to "I am very confident."

### 3. The Exploration-Exploitation Trade-off

When choosing what to do, an agent balances two drives: **exploitation** (choose the option you *know* is rewarding) and **exploration** (choose the option you are uncertain about, to *learn* more). In Active Inference, this trade-off emerges naturally from the Expected Free Energy: the agent simultaneously seeks reward (pragmatic value) and information (epistemic value).

## Applications

* **Guessing Game**: A friend picks a number between 1 and 100. You ask yes/no questions. The optimal strategy (binary search: "Is it above 50?") maximizes entropy reduction — each question cuts your uncertainty in half. In $\log_2(100) ≈ 7$ questions, you can always find the number.
* **Exam Strategy**: You have 60 minutes and 3 essay questions to answer. How do you allocate time? An Active Inference agent would explore (read all questions briefly) before exploiting (invest deep time in the question it can answer best).

## Discussion Questions

1. Which has higher entropy: the roll of a fair 6-sided die or the outcome of a basketball game between the #1 and #100 ranked teams? Why?
2. When should a student explore (try new study strategies) versus exploit (stick with what works)?

## Summary

Cognition is the manipulation of beliefs, and beliefs are probability distributions. Entropy measures uncertainty. Active Inference agents reduce entropy by gathering information and making smart decisions that balance exploration and exploitation.

## References

* Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory*. Chapter 2.
