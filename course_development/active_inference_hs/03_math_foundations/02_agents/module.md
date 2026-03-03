# Module 02: Agents — Agents as Dynamical Systems

## Learning Objectives

1. Describe an agent as a **dynamical system** with internal states, sensory inputs, and motor outputs.
2. Define a **Markov blanket** as the mathematical boundary between the agent and its environment.
3. Write a simple state-update equation for an agent that makes predictions and corrects errors.

## Introduction

An agent is anything that senses the world and acts on it. In mathematical terms, an agent is a dynamical system with a special structure: it has **internal states** (beliefs, memories, goals), **sensory states** (inputs from the environment), and **active states** (outputs that change the environment). The Markov blanket — the set of sensory and active states — is the mathematical boundary between the agent and everything else.

## Key Concepts

### 1. The Agent Equation

We can write the simplest possible agent as a state-update rule:

$$\hat{x}_{t+1} = \hat{x}_t + \alpha \cdot (o_t - \hat{o}_t)$$

Here, $\hat{x}_t$ is the agent's current belief (internal state), $o_t$ is what the agent actually senses (observation), $\hat{o}_t$ is what it *predicted* it would sense, and $\alpha$ is a **learning rate**. The difference $(o_t - \hat{o}_t)$ is the **prediction error**. This single equation captures the core of Active Inference: update your beliefs proportionally to your surprise.

### 2. Markov Blankets in Math

A **Markov blanket** of a variable $X$ is the set of variables that make $X$ conditionally independent of all other variables. If you know the blanket, you know everything $X$ can possibly "see." For an agent, the blanket is formed by the sensory inputs (what comes in) and the motor outputs (what goes out). Everything outside the blanket is hidden.

### 3. Prediction and Correction

Agents continuously cycle between two operations: (1) **prediction** — generating an expected observation from the current belief, and (2) **correction** — updating the belief when the prediction does not match reality. This predict-correct cycle is the mathematical heartbeat of Active Inference and is directly related to the Kalman filter from engineering.

## Applications

* **Spreadsheet Agent**: Students can build a simple agent in a spreadsheet. Column A = time step. Column B = true hidden state (e.g., temperature). Column C = noisy observation = B + random noise. Column D = agent's belief, updated using the equation above. Plot belief vs. reality and watch the agent track the true state.
* **Thermostat as Agent**: A thermostat has an internal state (set point = 72°F), a sensor (thermometer), and an actuator (heater/AC). It predicts the room should be 72°F. When the sensor reads 68°F, the prediction error is −4°F, and the thermostat acts (turns on the heater).

## Discussion Questions

1. In the agent equation, what happens if $\alpha = 0$? What about $\alpha = 1$? Which is a better agent?
2. Is a rock an agent? Why or why not? (Hint: does it have a Markov blanket with active states?)

## Summary

An agent is a dynamical system with a Markov blanket. It predicts its sensory inputs, detects prediction errors, and updates its internal states. The simple equation $\hat{x}_{t+1} = \hat{x}_t + \alpha (o_t - \hat{o}_t)$ captures this process.

## References

* Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
