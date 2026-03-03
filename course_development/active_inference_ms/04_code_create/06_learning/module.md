# Module 06: Learning — Variables, Memory, and Improvement Over Time

## Learning Objectives

1. Use **variables** to store information that changes over time (the agent's "memory").
2. Write code that **improves** its behavior based on past results (simple parameter adjustment).
3. Connect code variables to Active Inference: variables are the agent's beliefs, and updating them is learning.

## Introduction

Learning in code happens when a program changes its behavior based on experience. The simplest form of learning is updating a variable. Every time your bot tries something, succeeds or fails, and adjusts a number — that is learning. This module shows you how to build programs that genuinely improve over time.

## Key Concepts

### 1. Variables as Memory

Variables are your code's memory. They store what the agent knows, believes, and has experienced:

```python
times_hit_wall = 0
successful_routes = []
best_score = 0
```

These variables accumulate experience. A program with no variables has no memory — it makes the same mistakes forever. A program with variables can learn.

### 2. Learning by Counting

The simplest learning algorithm: count what works and do more of it.

```python
action_scores = {"left": 0, "right": 0, "forward": 0}

# After each action, update the score
if action_result == "success":
    action_scores[chosen_action] += 1

# Choose the action with the highest score
best_action = max(action_scores, key=action_scores.get)
```

This is a **frequency-based learner**: it learns which action succeeds most often. Over time, it gets better!

### 3. Learning Rate: How Fast to Adapt

Should your program change its behavior quickly after one result, or slowly after many results? This is the **learning rate** problem.

```python
learning_rate = 0.1
estimate = estimate + learning_rate * (new_observation - estimate)
```

- High learning rate (0.9): Adapts fast but is jumpy and unstable
- Low learning rate (0.01): Adapts slowly but smoothly

This tradeoff is at the heart of Active Inference: how much should you trust new evidence versus your existing beliefs?

## Activities

### 📈 Activity 1: Training a Bot

Create a bot that starts by choosing random directions in a maze. After each run, it records which directions led to dead ends. Over 50 runs, the bot should find shorter and shorter paths. Plot the number of steps per run. Does the graph go down?

### 🎯 Activity 2: Guess My Number (Learning Edition)

Write a program that tries to guess a hidden number between 1 and 100. After each guess, the user says "higher" or "lower." The program uses a learning variable to narrow its range. How many guesses does it need? (Optimal: 7!)

## Summary

Learning in code means updating variables based on experience. Counting successes, adjusting estimates, and tuning learning rates are all forms of computational learning that mirror how Active Inference agents update their generative models.

## References

- Briggs, J. (2013). *Python for Kids*. Chapter 12.
