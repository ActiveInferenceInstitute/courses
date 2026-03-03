# Module 01: Systems — Mathematical Modeling of Systems

## Learning Objectives

1. Represent a real-world system as a set of **state variables**, **parameters**, and **update rules**.
2. Distinguish between **open systems** (exchange energy/information with the environment) and **closed systems**.
3. Connect the concept of a system's **boundary** to the mathematical idea of a Markov blanket.

## Introduction

In the Everyday Life and Biology & Health units, you learned to *recognize* systems everywhere — in your school, your body, and your social life. Now we put numbers on things. A mathematical model is a translation of a real system into variables and equations. This is the foundation of all science, engineering, and data science.

Consider a simple population model: $P_{t+1} = r \cdot P_t \cdot (1 - P_t / K)$. Here, $P_t$ is the current population (a **state variable**), $r$ is the growth rate (a **parameter**), and $K$ is the carrying capacity (a **constraint** — it acts like a boundary on how big the population can get). This single equation captures the prediction-correction loop of Active Inference: the population "predicts" exponential growth, but the carrying capacity provides a corrective signal, pulling the population back toward equilibrium.

## Key Concepts

### 1. State Variables and State Space

A **state variable** is any quantity that describes the current condition of a system. Temperature, position, population size, bank balance — all are state variables. The set of all possible values forms the **state space**. A system's trajectory through state space is like a path through a map.

### 2. Parameters and Constraints

**Parameters** are values that shape the system's behavior but do not change during the model's run (like the growth rate $r$). **Constraints** are boundaries on what the system can do. In Active Inference, the Markov blanket *is* the constraint: it determines which external information the system can access.

### 3. Equilibria and Attractors

An **equilibrium** is a state where the system stays put. A **stable equilibrium** (an attractor) means the system returns there after a perturbation — like body temperature returning to 98.6°F. Attractors are the mathematical expression of the idea that living systems resist surprise.

## Applications

* **Algebra**: A system of linear equations ($2x + 3y = 12$, $x - y = 1$) constrains the values of $x$ and $y$. The solution set is the system's equilibrium. Adding a third equation (new evidence!) further narrows the possibilities — just like sensory data reduces an agent's uncertainty.
* **Population Ecology**: The logistic equation above models a self-regulating population. Students can simulate it in a spreadsheet and watch how different values of $r$ produce stability, oscillation, or chaos.

## Discussion Questions

1. What are the state variables in your school's cafeteria system? What are the constraints?
2. Can a system have more than one equilibrium? Give an example.

## Summary

Mathematical modeling translates real systems into state variables, parameters, and rules. Equilibria and attractors describe how systems resist surprise. This mathematical toolkit underlies all of Active Inference.

## References

* Strogatz, S. (2015). *Nonlinear Dynamics and Chaos*. Chapter 1.
