# Module 05: Action — Functions, Loops, and Making Things Happen

## Learning Objectives

1. Use **functions** to organize actions into reusable, named blocks of code.
2. Use **loops** (for, while) to repeat actions efficiently.
3. Connect functions and loops to the Active Inference sense-decide-act cycle.

## Introduction

Action is the part of Active Inference where the agent *does* something — it changes the world. In code, actions are functions and loops: the building blocks that make things happen. This module teaches you to write better functions and loops, and to see them as the "motor system" of your code agents.

## Key Concepts

### 1. Functions as Actions

A function is a named action. Instead of writing the same code over and over, you write it once and *call* it:

```python
def move_forward(player, distance):
    player.x += distance
    print(f"Moved to {player.x}")

def turn_left(player):
    player.direction = rotate(player.direction, -90)
    print(f"Facing {player.direction}")
```

Each function is a discrete **action** your agent can take. The function name is the action's label. The parameters customize the action.

### 2. Loops as Repeated Actions

A `while` loop is an action repeated until a condition is met. This is the core of the Active Inference loop:

```python
while not at_goal:
    observation = sense(world, player)         # Sense
    decision = decide(observation, player)     # Decide
    at_goal = act(decision, player, world)     # Act
```

The loop keeps running — sense, decide, act — until the agent reaches its goal. Every game, every robot, every AI runs a loop like this.

### 3. Side Effects: Actions Change the World

A function that only calculates something (like `add(3, 4)`) is pure computation. But a function that changes a variable, moves a character, or writes to a file has a **side effect** — it changes the world. In Active Inference, every action is a side effect: the agent acts on the environment to make it match its predictions.

## Activities

### 🚀 Activity 1: Action Library

Create a library of at least 5 functions for a game character: `move_forward()`, `turn_left()`, `turn_right()`, `pick_up(item)`, `drop(item)`. Write a main loop that lets the user type commands ("forward", "left", "pick up key") and calls the right function.

### 🔄 Activity 2: The 100-Step Challenge

Write a program where a bot must reach a treasure in a 20×20 grid. The bot can move forward, turn left, or turn right. Challenge: can your bot reach the treasure in fewer than 100 steps? Optimize your action loop!

## Summary

Functions are named actions. Loops repeat the sense-decide-act cycle. Side effects are how code agents change the world. Well-organized functions and efficient loops are the "muscles" of your code — the tools that turn decisions into results.

## References

* Matthes, E. (2019). *Python Crash Course*. Chapters 8-9.
