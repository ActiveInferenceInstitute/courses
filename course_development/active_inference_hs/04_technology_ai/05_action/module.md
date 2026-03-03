# Module 05: Action — Robotics and Embodied AI

## Learning Objectives

1. Describe the **sense-plan-act** architecture of a physical robot.
2. Explain how **actuators** (motors, servos) implement actions selected by the robot's control algorithm.
3. Connect the robotics control loop to the Active Inference predict-correct-act cycle.

## Introduction

A robot is Active Inference made physical. Unlike a chatbot that only manipulates text, a robot manipulates the *physical world*: it picks up objects, navigates rooms, and assembles products. This module explores how robots turn computational decisions into physical actions — and the unique challenges that embodiment creates.

## Key Concepts

### 1. The Robotics Control Loop

Every robot runs a tight loop:

1. **Sense**: Read sensors (LIDAR, cameras, force sensors, encoders)
2. **Plan**: Run the control algorithm (compare sensor data to goals)
3. **Act**: Send commands to actuators (motors, grippers, speakers)
4. **Repeat**: At 10-1000 Hz

This is the Active Inference perception-action loop implemented in hardware.

### 2. Degrees of Freedom

A **degree of freedom (DOF)** is one independent axis of motion. Your arm has 7 DOF (shoulder: 3, elbow: 1, wrist: 3). An industrial robot arm typically has 6 DOF. A self-driving car has effectively 2 (steering angle and speed). More DOF = more flexibility, but also more parameters the controller must manage.

### 3. Sim-to-Real Transfer

Training a robot in the real world is slow and expensive (robots break!). Modern robotics trains in a **simulation environment** first, then transfers the learned policy to the real robot. The gap between simulation and reality creates prediction errors that the robot must adapt to — this is the "sim-to-real" problem, and it maps directly onto Active Inference's concept of model mismatch.

## Applications

* **Warehouse Robots**: Amazon's Kiva robots navigate warehouses using a grid-based coordinate system. Each robot predicts traffic patterns and adjusts its path to avoid collisions.
* **Surgical Robots**: The Da Vinci surgical system translates a surgeon's hand movements into micro-precise robotic actions. The robot's control system must maintain sub-millimeter accuracy while compensating for tissue deformation (prediction errors from unexpected material properties).

## Discussion Questions

1. A self-driving car's steering controller and a brain controlling your arm both implement the same predict-correct loop. What is one key difference?
2. Why is the "sim-to-real" gap a problem? How might Active Inference help a robot adapt to reality faster?

## Summary

Robots turn computational decisions into physical actions through actuators. The robotics control loop (sense-plan-act) is the embodied version of Active Inference. Sim-to-real transfer highlights the challenge of model mismatch between simulated and real environments.

## References

* Siciliano, B. et al. (2009). *Robotics: Modelling, Planning and Control*. Chapter 1.
