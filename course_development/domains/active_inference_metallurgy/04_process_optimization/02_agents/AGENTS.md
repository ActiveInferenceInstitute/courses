# Station: Agents (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Agents — Sensors and Controllers as Process Agents
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Industrial sensors and controllers form agent pairs that implement Active Inference at the process level. A thermocouple (sensory state) measures furnace temperature, the PLC controller (internal model) compares this to the setpoint (preferred state), and the heating element (active state) adjusts power output to minimize the deviation (prediction error). This sensor-controller-actuator triad is the canonical Active Inference agent architecture in manufacturing. Multi-sensor fusion combines data from thermocouples, pyrometers, load cells, and flow meters to form a richer perceptual model of the process state, while multi-actuator coordination enables more precise process control.

## Key Mappings

| FEP Concept | Sensor/Controller Translation |
|-------------|------------------------------|
| Agent | Sensor-controller-actuator triad (e.g., thermocouple + PID controller + heating element) |
| Sensory States | Sensor readings: temperature, pressure, force, flow rate, position |
| Internal Model | Controller setpoint, PID gains, feedforward model |
| Prediction Error | Deviation between measured process variable and setpoint |
| Active States | Actuator output: heater power, valve position, motor speed, laser power |
| Multi-Agent Coordination | Cascade control, supervisory control, multi-loop coordination |

## Content Guidelines

- Frame PID control as a minimal Active Inference agent: the proportional term responds to current prediction error, the integral term accumulates past errors (learning), and the derivative term anticipates future errors (planning)
- Treat sensor fusion as multi-modal perception — combining heterogeneous sensor data into a unified process state estimate
- Connect model predictive control (MPC) to planning under a generative model — the controller simulates future process trajectories to select the optimal control action
- Emphasize that the human operator is also a process agent, with the HMI (human-machine interface) as their sensory channel and the control panel as their action interface

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
