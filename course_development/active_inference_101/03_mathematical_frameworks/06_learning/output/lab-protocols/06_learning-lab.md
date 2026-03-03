# Lab: Parameter and Structure Learning

> **Learning Goal:** Compute Dirichlet updates and analyze Bayesian Model Reduction.

## Part 1: Dirichlet Updating

**Exercise**: An agent starts with a uniform prior over a 3-outcome observation:
α_prior = [1, 1, 1] (total count = 3)

After 10 trials, it observes: outcome 1 (6 times), outcome 2 (3 times), outcome 3 (1 time)

1. Compute α_posterior = α_prior + counts = ?
2. Expected probabilities (mean of Dirichlet) = α_i / Σα_i for each outcome
3. Now imagine 100 more observations with the same proportions. Compute the new α and probabilities.
4. How much did the probabilities change between step 2 and step 3? Why?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Learning Rate Decay

> **Learning Goal:** See how the learning rate decreases naturally.

**Exercise**: Track the effective learning rate (1/(total_count + 1)) after each batch:

| Experience Level | Total α count | Learning rate | Effect of 1 new observation |
|-----------------|---------------|---------------|---------------------------|
| Novice (10 observations) | | | |
| Intermediate (100 observations) | | | |
| Expert (1000 observations) | | | |

What pattern do you see? How does this match the intuition that experts are "harder to convince"?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Bayesian Model Reduction

> **Learning Goal:** Compare models of different complexity.

**Scenario**: You've learned that a friend is either at home, at work, or at the gym on weekdays. After 100 observations:

- Home: 5 times
- Work: 92 times
- Gym: 3 times

1. Full model (3 states): What is the approximate likelihood (model evidence)?
2. Reduced model (2 states: work/not-work): What is lost by collapsing home and gym into "not-work"?
3. Reduced model (1 state: always-work): What is lost? Is this model too simple?
4. Which model does BMR prefer and why?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: A vs. B Matrix Learning

> **Learning Goal:** Compare learning observation model vs. transition model.

**Exercise**: Consider an agent learning about a new environment:

| What it learns | Which matrix | Example | How long to learn? |
|---------------|-------------|---------|-------------------|
| "Red lights mean stop" | | | |
| "Pressing the button turns on the light" | | | |
| "Rain clouds produce rain" | | | |
| "Studying leads to good grades" | | | |

For each, indicate whether it updates the A matrix (observations) or B matrix (transitions), and estimate relative difficulty of learning.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 150 words, reflect: The mathematical framework shows that learning rate decreases automatically with experience. Is this always adaptive, or can it become maladaptive? Think about situations where an "expert" should update their beliefs rapidly but can't.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Dirichlet computation | Parameter updating with counts |
| 2 | Rate analysis | Learning rate decay |
| 3 | Model comparison | BMR and model complexity |
| 4 | Matrix classification | A vs. B matrix learning |
| 5 | Critical reflection | When slow learning fails |
