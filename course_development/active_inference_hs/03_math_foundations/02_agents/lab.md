# Lab: Random Variables and Probability Distributions

## Objective

Learn to represent an agent's beliefs and preferences using **probability distributions**, and practice computing basic probabilities that underpin the Active Inference framework.

## Prerequisites

- Completed Math Foundations: Systems module
- Basic arithmetic with fractions and decimals

## Part 1: Discrete Probability Distributions

**Goal**: Build and analyze probability distributions over agent states.

A student agent has beliefs about tomorrow's weather. Define a random variable X = {sunny, cloudy, rainy} with probabilities:

1. Assign probabilities: P(sunny) = 0.5, P(cloudy) = 0.3, P(rainy) = 0.2.
2. Verify they sum to 1.
3. What is the most likely state (the mode)?
4. Draw a bar chart of this distribution.

{fill:textarea}

## Part 2: Joint and Marginal Probabilities

**Goal**: Work with two random variables simultaneously.

Let X = weather = {sunny, rainy} and Y = mood = {happy, sad}. The joint distribution is:

| | happy | sad |
|--|-------|-----|
| sunny | 0.4 | 0.1 |
| rainy | 0.1 | 0.4 |

1. Compute P(sunny) and P(rainy) by summing rows.
2. Compute P(happy) and P(sad) by summing columns.
3. Are X and Y independent? Check: P(sunny, happy) = P(sunny) * P(happy)?

{fill:textarea}

## Part 3: Expected Value

**Goal**: Compute expected values as a measure of what an agent "expects."

A game pays $10 if you roll a 6 on a fair die, $0 otherwise.

1. P(win) = ? , P(lose) = ?
2. E[payout] = P(win) * $10 + P(lose) * $0 = ?
3. Would you pay $2 to play? Why?
4. How does expected value connect to policy evaluation in Active Inference?

{fill:textarea}

## Part 4: Preferred Distributions

**Goal**: Represent agent preferences as a probability distribution.

Define a preferred distribution P*(grade) = {A: 0.7, B: 0.2, C: 0.1} and actual P(grade) = {A: 0.3, B: 0.4, C: 0.3}.

1. Where are the biggest mismatches?
2. What actions could reduce the gap between P and P*?
3. In Active Inference, this gap is related to free energy. The agent acts to make P closer to P*.

{fill:textarea}

## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Random variable | X | Variable whose value is determined by chance |
| Probability distribution | P(X) | Assigns probabilities summing to 1 |
| Joint distribution | P(X, Y) | Probability over two variables |
| Expected value | E[X] | Probability-weighted average |
| Preferred distribution | P*(X) | Target distribution the agent acts to achieve |
