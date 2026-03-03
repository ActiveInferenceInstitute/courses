# Module 04: Cognition — Conditionals, Logic, and Decision-Making

## Learning Objectives

1. Use **if-elif-else** statements to implement decision logic in code.
2. Build a decision tree in code that makes choices based on multiple inputs.
3. Understand that conditionals are the code version of the brain's "hypothesis testing."

## Introduction

Cognition is thinking — and in code, thinking happens through **conditionals** (if-else statements) and **logic** (and, or, not). Every time your program checks a condition and chooses a path, it is performing a tiny act of cognition. This module levels up your conditionals from simple checks to complex, multi-factor decision trees.

## Key Concepts

### 1. If-Elif-Else as Hypothesis Testing

```python
if sky == "dark" and stars_visible:
    hypothesis = "nighttime"
elif sky == "dark" and not stars_visible:
    hypothesis = "cloudy night or eclipse"
elif sky == "light":
    hypothesis = "daytime"
else:
    hypothesis = "uncertain"
```

Each branch is a **hypothesis** — a guess about the state of the world. The code checks conditions (evidence) and selects the hypothesis that best fits. This is exactly what Active Inference calls inference: choosing the explanation that minimizes prediction error.

### 2. Nested Decisions

Real thinking involves chains of decisions. A game's NPC (non-player character) might follow nested logic:

```python
if player_nearby:
    if player_is_enemy:
        if my_health > 50:
            action = "attack"
        else:
            action = "flee"
    else:
        action = "greet"
else:
    action = "patrol"
```

Each level of nesting adds nuance to the NPC's "cognition." More branches = a richer model of the world.

### 3. Truth Tables and Boolean Logic

Computers think in True/False. The operators `and`, `or`, `not` combine conditions:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

Boolean logic is the foundation of all digital cognition — from a simple `if` statement to the deepest neural network.

## Activities

### 🧙 Activity 1: NPC Brain

Design the decision logic for an NPC in a game. Your NPC should make at least 3 levels of nested decisions based on: player proximity, player behavior (friendly/hostile), time of day, and NPC's health. Write the code and test it with different scenarios.

### 📋 Activity 2: 20 Questions Bot

Write a program that plays "20 Questions." The bot asks yes/no questions (using `input()`) and narrows down the possibilities using if-else branches. How many questions does it need to guess correctly? (Hint: with optimal questions, you can distinguish 1 million objects in just 20 questions!)

## Summary

Conditionals are the code version of cognition. Each `if` branch is a hypothesis, and the code selects the branch that best matches the evidence. Boolean logic (and, or, not) is the fundamental language of computational thinking.

## References

* Matthes, E. (2019). *Python Crash Course*. Chapter 5.
