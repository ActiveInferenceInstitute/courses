# Module 02: Agents — Programming a Simple Bot

## Learning Objectives

1. Define an **agent** in code: something that has sensors (inputs), a brain (decision logic), and actuators (outputs).
2. Write a simple rule-based bot that senses its environment and acts.
3. Understand that improving the bot's rules is like updating its "model of the world."

## Introduction

An agent is any entity that senses its world and takes action. In code, an agent is a program that reads input, decides what to do, and produces output — in a loop. In this module, you will build your very first software agent: a simple bot that navigates a grid world.

## Key Concepts

### 1. The Bot Architecture

Every bot (agent) has three parts:

```
SENSE → DECIDE → ACT → (repeat)
```

- **Sense**: Read data from the environment (check what is in the cell ahead)
- **Decide**: Choose an action based on rules ("if wall ahead, turn right")
- **Act**: Execute the chosen action (move forward, turn, or stop)

### 2. A Simple Python Bot

```python
def bot_step(world, position, direction):
    # SENSE
    ahead = world[position + direction]

    # DECIDE
    if ahead == "wall":
        direction = turn_right(direction)  # Can't go forward
    elif ahead == "food":
        action = "eat"
    else:
        action = "move_forward"

    # ACT
    return execute_action(action, position, direction)
```

This 10-line function is a complete agent! It senses (reads the grid), decides (checks for walls and food), and acts (moves or turns).

### 3. Improving the Bot = Updating the Model

Your first bot might be dumb: it turns right at every wall and gets stuck in circles. What if you add a rule: "if I have turned right 3 times in a row, try turning left"? That is updating the bot's model of the world. The better the rules, the fewer "surprises" (dead ends, loops) the bot encounters. This is Active Inference: the bot is adjusting its behavior to minimize prediction errors.

## Activities

### 🤖 Activity 1: Build a Grid Bot

Using Scratch, Python, or any language you know, create a simple bot that navigates a 10×10 grid. The grid has walls, open spaces, and a goal (treasure). Your bot should:

1. Start in the top-left corner
2. Try to reach the treasure
3. Avoid walls

How many steps does your bot take? Can you improve its rules to find the treasure faster?

### 📊 Activity 2: Bot vs. Bot

Have two classmates build their own bots for the same grid. Race them! The bot that reaches the treasure in fewer steps has a better "model."

## Summary

An agent in code is a sense-decide-act loop. A simple bot can navigate a world using rules. Improving the rules (the model) reduces surprise and makes the bot smarter. This is the foundation of all AI.

## References

- Briggs, J. (2013). *Python for Kids*. Chapter 16.
