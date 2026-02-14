# Lab: Math Foundations Capstone -- From Sets to Free Energy

## Objective

Work through a sequence of mathematical exercises that build from basic set theory and probability to the core equations of Active Inference, demonstrating how each module's math connects to the next.

## Part 1: Sets and Graphs (Systems)

**Goal**: Represent a simple system using set notation and a graph.

Consider a weather system with states S = {sunny, cloudy, rainy}. Observations are O = {dry, wet}. Actions are A = {carry umbrella, no umbrella}.

1. Write the state space, observation space, and action space as sets.
2. Draw a graph with nodes for each state and edges showing possible transitions.
3. Write a transition matrix T where T(i,j) = P(next state = j | current state = i). Use reasonable probabilities.

{fill:textarea}

## Part 2: Probability and Bayes' Theorem (Agents through Cognition)

**Goal**: Apply Bayes' theorem to update beliefs.

You think there is a 30% chance it will rain today (prior: P(rain) = 0.3). You see dark clouds. When it rains, dark clouds appear 90% of the time: P(clouds | rain) = 0.9. When it does not rain, dark clouds appear 20% of the time: P(clouds | no rain) = 0.2.

1. Compute P(clouds) using the law of total probability.
2. Compute P(rain | clouds) using Bayes' theorem.
3. How much did seeing clouds change your belief? Is the posterior closer to 0 or 1 compared to the prior?

{fill:textarea}

## Part 3: Surprise and Free Energy (Action and Learning)

**Goal**: Compute surprise and variational free energy for a simple model.

Suppose your generative model predicts observation o with probability Q(o) = 0.8. The actual probability is P(o) = 0.5.

1. Compute the surprise of observation o under Q: -ln(Q(o)).
2. Compute the KL divergence between P and Q for this single observation.
3. Free energy F = E_Q[-ln P(o,s)] + entropy of Q. For a simplified case where there is one state, compute F.

{fill:textarea}

## Part 4: Expected Free Energy and Policy Selection (Planning)

**Goal**: Compare two policies using expected free energy.

An agent must choose between Policy A (go left) and Policy B (go right). For each policy, estimate:

| Component | Policy A | Policy B |
|-----------|----------|----------|
| Expected reward (pragmatic value) | 5 | 3 |
| Expected information gain (epistemic value) | 1 | 4 |
| Expected free energy G = -(reward + info gain) | | |

Which policy minimizes expected free energy? Under what circumstances would the agent prefer the other policy?

{fill:textarea}

## Summary

| Math Concept | Module Connection | Key Formula |
|-------------|------------------|-------------|
| Sets and graphs | Systems | S = {s1, s2, ...} |
| Probability distributions | Agents | P(x), sum to 1 |
| Conditional probability | Perception | P(A|B) = P(B|A)P(A)/P(B) |
| Bayes' theorem | Cognition | Posterior proportional to likelihood times prior |
| Surprise | Action | -ln P(o) |
| KL divergence | Learning | D_KL(Q || P) |
| Expected free energy | Planning | G = -E[reward + info gain] |
