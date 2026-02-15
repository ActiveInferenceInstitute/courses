# Lab: Bayes' Theorem -- Updating Beliefs with Evidence

## Objective

Apply **Bayes' theorem** to update beliefs when new evidence arrives. This is the core mathematical operation of cognition in Active Inference: combining what you already believe (prior) with what you observe (likelihood) to form a new belief (posterior).

## Prerequisites

- Completed Math Foundations: Perception module (conditional probability, likelihood)
- Comfort with fraction multiplication and division

## Part 1: Bayes' Theorem by Counting

**Goal**: Derive Bayes' theorem from a concrete counting scenario.

A class of 100 students: 30 study regularly, 70 do not. Of those who study, 90% pass the exam. Of those who do not study, 40% pass.

1. Fill in the table:

| | Pass | Fail | Total |
|--|------|------|-------|
| Study | ? | ? | 30 |
| No Study | ? | ? | 70 |
| Total | ? | ? | 100 |

2. P(Study | Pass) = (students who study AND pass) / (total who pass) = ?
3. Now compute the same answer using Bayes' formula: P(Study | Pass) = P(Pass | Study) * P(Study) / P(Pass) = ?
4. Verify both methods give the same answer.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Bayes' Theorem Formula

**Goal**: Practice the formula P(H|D) = P(D|H) * P(H) / P(D).

A disease affects 1 in 1000 people. A test is 99% accurate (detects disease when present) and has a 5% false positive rate.

1. P(disease) = 0.001, P(no disease) = 0.999
2. P(positive | disease) = 0.99
3. P(positive | no disease) = 0.05
4. P(positive) = P(pos|disease)*P(disease) + P(pos|no disease)*P(no disease) = ?
5. P(disease | positive) = P(pos|disease)*P(disease) / P(positive) = ?
6. Were you surprised by how low P(disease | positive) is? Why does this happen?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Sequential Updating

**Goal**: Apply Bayes' theorem multiple times as new evidence arrives.

You think a coin might be fair (P(heads) = 0.5) or biased (P(heads) = 0.8). Your prior: P(fair) = 0.7, P(biased) = 0.3.

1. You flip and get heads. Compute P(fair | heads) using Bayes' theorem.
2. Now use your answer from step 1 as the new prior. You flip again and get heads. Compute P(fair | heads, heads).
3. One more flip: tails. Compute the new posterior.
4. How did your belief shift across three updates? In Active Inference, this sequential updating IS cognition.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Prior Strength

**Goal**: Explore how strong vs. weak priors affect belief updating.

Use the same coin scenario, but compare two agents:
- Agent A (strong prior): P(fair) = 0.95
- Agent B (weak prior): P(fair) = 0.50

Both observe 3 heads in a row.

1. Compute P(fair | 3 heads) for Agent A.
2. Compute P(fair | 3 heads) for Agent B.
3. Which agent shifts their belief more? Why?
4. In Active Inference, prior strength relates to **precision** -- how confident the agent is in its existing model.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Bayes' theorem | P(H\|D) = P(D\|H)*P(H)/P(D) | Updates prior belief with evidence |
| Prior | P(H) | Belief before observing data |
| Posterior | P(H\|D) | Belief after observing data |
| Evidence / marginal likelihood | P(D) | Total probability of the data |
| Sequential updating | Prior -> Posterior -> new Prior | Repeated application of Bayes' rule |
