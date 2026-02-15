# Lab: Optimization and Expected Value

## Objective

Practice **optimization** -- finding the best choice among alternatives -- using **expected value** calculations. In Active Inference, action selection means choosing the policy that minimizes expected free energy, which combines expected value with information gain.

## Prerequisites

- Completed Math Foundations: Cognition module (Bayes' theorem)
- Comfort with multiplication and weighted averages

## Part 1: Expected Value of Actions

**Goal**: Compute expected values to compare different action choices.

You are deciding how to spend 2 hours before a test. Three study strategies:

| Strategy | P(A grade) | P(B grade) | P(C grade) |
|----------|-----------|-----------|-----------|
| Review notes | 0.3 | 0.5 | 0.2 |
| Practice problems | 0.5 | 0.3 | 0.2 |
| Study group | 0.4 | 0.4 | 0.2 |

Assign values: A = 4 points, B = 3 points, C = 2 points.

1. E[review notes] = 0.3(4) + 0.5(3) + 0.2(2) = ?
2. E[practice problems] = ?
3. E[study group] = ?
4. Which strategy has the highest expected value?
5. Would you always choose the highest expected value option? What might matter besides the average?

{fill:textarea}

## Part 2: Minimizing Expected Loss

**Goal**: Reframe optimization as minimizing a cost rather than maximizing a reward.

An agent wants an A on the test. Define "loss" as the gap between desired and actual grade:

| Outcome | Loss (gap from A) |
|---------|-------------------|
| A | 0 |
| B | 1 |
| C | 2 |

1. E[loss for review notes] = 0.3(0) + 0.5(1) + 0.2(2) = ?
2. E[loss for practice problems] = ?
3. E[loss for study group] = ?
4. Does minimizing expected loss give the same best strategy as maximizing expected value?
5. In Active Inference, the agent minimizes **expected free energy** -- which is a type of expected loss relative to preferred outcomes.

{fill:textarea}

## Part 3: The Explore-Exploit Tradeoff

**Goal**: See how information gain competes with expected reward.

You know Strategy A has E[grade] = 3.1 (from Part 1). A new Strategy D is untested -- you have no data.

1. If you pick Strategy D, what is your expected grade? (You do not know -- that is the point.)
2. What do you gain by trying Strategy D even if it might be worse? (Information!)
3. Suppose after trying Strategy D once, you learn E[grade for D] = 3.5. Was exploring worth it?
4. In Active Inference, **epistemic value** (information gain) is added to **pragmatic value** (expected reward). An agent that only exploits never discovers better strategies.

{fill:textarea}

## Part 4: Gradient Descent (Intuitive)

**Goal**: Understand optimization as repeatedly taking small steps toward improvement.

Imagine you are on a hilly landscape in the dark and want to reach the lowest point.

1. Strategy: At each step, feel which direction slopes downward and take a small step that way. This is **gradient descent**.
2. Suppose your "height" at position x is f(x) = (x - 3)^2. Compute f(0), f(1), f(2), f(3), f(4).
3. Starting at x = 0, which direction reduces f(x)? Take a step of size 1 in that direction.
4. Repeat until you reach the minimum. How many steps did it take?
5. In Active Inference, the agent adjusts its actions to "descend" the free energy landscape, always moving toward states that match its preferences.

{fill:textarea}

## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Expected value | E[X] = sum(x_i * p_i) | Probability-weighted average outcome |
| Expected loss | E[L] = sum(loss_i * p_i) | Probability-weighted average cost |
| Optimization | argmin / argmax | Finding the action that minimizes cost or maximizes reward |
| Explore-exploit | Epistemic vs pragmatic value | Tradeoff between gaining information and maximizing reward |
| Gradient descent | x_new = x - step * slope | Iterative optimization by following the downhill direction |
