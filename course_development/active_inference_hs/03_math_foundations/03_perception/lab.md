# Lab: Conditional Probability and Likelihood

## Objective

Practice computing **conditional probabilities** and **likelihoods** -- the mathematical tools an agent uses to update beliefs when new evidence arrives. These calculations are the building blocks of perception in Active Inference.

## Prerequisites

- Completed Math Foundations: Agents module (probability distributions)
- Comfort with fractions and basic probability notation

## Part 1: Conditional Probability

**Goal**: Compute P(A|B) -- the probability of A given that B has occurred.

A school has 200 students. Of these, 120 play sports, 80 are in band, and 40 do both.

1. Draw a Venn diagram showing Sports, Band, and the overlap.
2. P(Sports) = ?
3. P(Band) = ?
4. P(Sports | Band) = P(Sports AND Band) / P(Band) = ?
5. P(Band | Sports) = P(Sports AND Band) / P(Sports) = ?
6. Is P(Sports | Band) the same as P(Band | Sports)? Why does this matter?

{fill:textarea}

## Part 2: Likelihood vs. Probability

**Goal**: Distinguish between P(data | hypothesis) and P(hypothesis | data).

A bag has either 7 red and 3 blue marbles (Bag A) or 3 red and 7 blue (Bag B). You draw one marble and it is red.

1. P(red | Bag A) = ? This is the **likelihood** of Bag A.
2. P(red | Bag B) = ? This is the **likelihood** of Bag B.
3. Which bag is the drawn marble more likely to have come from?
4. The likelihood ratio is P(red | A) / P(red | B) = ? What does this number tell you?
5. In Active Inference, the generative model predicts observations. The likelihood measures how well a prediction matches what was actually observed.

{fill:textarea}

## Part 3: Conditional Probability Tables

**Goal**: Read and compute from a full conditional probability table.

A weather app's prediction model:

| Actual Weather | P(app says sunny) | P(app says rainy) |
|----------------|-------------------|-------------------|
| Sunny          | 0.9               | 0.1               |
| Rainy          | 0.3               | 0.7               |

Each row is a conditional distribution P(app prediction | actual weather).

1. Verify each row sums to 1.
2. If it is actually sunny, what is the probability the app gets it wrong?
3. If it is actually rainy, what is the probability the app gets it right?
4. Which weather condition does the app predict more accurately?
5. In Active Inference, this table is part of the **generative model** -- it describes how hidden states (actual weather) generate observations (app predictions).

{fill:textarea}

## Part 4: From Observation to Belief

**Goal**: Use conditional probability to reason backward from observation to cause.

Suppose P(sunny) = 0.6 and P(rainy) = 0.4 (your prior beliefs). The app says "rainy." Using the table from Part 3:

1. P(app says rainy | sunny) = ?
2. P(app says rainy | rainy) = ?
3. P(app says rainy) = P(rainy|sunny)*P(sunny) + P(rainy|rainy)*P(rainy) = ?
4. Without doing full Bayes yet, which hypothesis (sunny or rainy) does the "rainy" prediction support more?
5. This reasoning -- from observations back to hidden causes -- is **perception** in Active Inference.

{fill:textarea}

## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Conditional probability | P(A\|B) | Probability of A given B has occurred |
| Likelihood | P(data\|hypothesis) | How probable the data is under a hypothesis |
| Likelihood ratio | P(D\|H1) / P(D\|H2) | Relative support for two hypotheses |
| Generative model | P(observation\|state) | How hidden states produce observations |
| Prior | P(hypothesis) | Belief before seeing evidence |
