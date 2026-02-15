# Lab: Updating Estimates -- Learning from Data

## Objective

Practice **parameter updating** -- mathematically adjusting a model's estimates as new data arrives. In Active Inference, learning means updating the parameters of the generative model to better predict future observations.

## Prerequisites

- Completed Math Foundations: Action module (expected value, optimization)
- Comfort with averages and basic algebra

## Part 1: Running Average as Learning

**Goal**: See how the average updates incrementally as each new data point arrives.

A student takes quizzes each week. Scores: 70, 80, 75, 90, 85.

1. After quiz 1, the estimate of their "true ability" = 70.
2. After quiz 2, estimate = (70 + 80) / 2 = ?
3. After quiz 3, estimate = ?
4. Continue through all 5 quizzes.
5. Plot the running average over time. How does it stabilize?
6. The running average is a simple **learning rule**: the model's parameter (estimated ability) updates with each new observation.

{fill:textarea}

## Part 2: Weighted Updates -- Learning Rate

**Goal**: Explore how a learning rate controls the speed of updating.

Instead of a simple average, use the update rule: new_estimate = old_estimate + alpha * (observation - old_estimate), where alpha is the learning rate.

Start with estimate = 70. Use the same quiz scores: 70, 80, 75, 90, 85.

1. With alpha = 0.5: After quiz 2 (score 80), new_estimate = 70 + 0.5 * (80 - 70) = ?
2. Continue updating with alpha = 0.5 for all 5 quizzes.
3. Now repeat with alpha = 0.1 for all 5 quizzes.
4. Compare the two sequences. Which learning rate adapts faster? Which is more stable?
5. In Active Inference, the learning rate relates to **precision** -- how much weight the agent gives new data vs. existing beliefs.

{fill:textarea}

## Part 3: Curve Fitting as Learning

**Goal**: Fit a line to data and see learning as minimizing prediction error.

Data points: (1, 3), (2, 5), (3, 6), (4, 9), (5, 10).

1. Plot these points on graph paper.
2. Draw a line that looks like a good fit. Record your estimated slope (m) and intercept (b).
3. For your line y = mx + b, compute the prediction at each x value.
4. Compute the **prediction error** at each point: (actual y) - (predicted y).
5. Compute the sum of squared errors: sum of (error)^2.
6. A better-fitting line has lower total squared error. In Active Inference, learning minimizes **prediction error** -- the gap between what the model predicts and what actually happens.

{fill:textarea}

## Part 4: Overfitting vs. Generalization

**Goal**: Understand why simpler models can be better than complex ones.

Using the same 5 data points:

1. A straight line (y = mx + b) has 2 parameters. It fits reasonably but not perfectly.
2. A curve passing through all 5 points exactly has 5 parameters. It has zero training error.
3. Imagine a 6th data point at x = 6. Which model would you trust more to predict it? Why?
4. The straight line **generalizes** better despite having higher training error.
5. In Active Inference, free energy = prediction error + complexity. The complexity term penalizes overly complex models, favoring simpler generative models that generalize.

{fill:textarea}

## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Running average | x_bar = sum(x_i) / n | Simple estimate updated with each data point |
| Learning rate | alpha | Controls how much each new observation shifts the estimate |
| Prediction error | y - y_hat | Difference between actual and predicted values |
| Sum of squared errors | sum((y_i - y_hat_i)^2) | Total prediction error across all data points |
| Overfitting | -- | Model memorizes training data but fails on new data |
| Generalization | -- | Model performs well on unseen data |
