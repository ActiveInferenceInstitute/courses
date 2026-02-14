# Practice Quiz: Action / Robotics (Research Methods)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Active Inference robot control replaces inverse kinematics with:
A) Random actions
B) Predictive inference — motor commands are generated to minimize prediction errors between predicted and desired proprioceptive states
C) Pre-programmed sequences
D) External commands

**2.** pymdp implements Active Inference for:
A) Continuous systems only
B) Discrete-state POMDPs — using A, B, C, D matrices for observation, transition, preferences, and prior beliefs
C) Only image processing
D) Hardware control only

**3.** Generalized coordinates of motion include:
A) Only position
B) Position, velocity, acceleration, and higher-order derivatives — enabling smooth trajectory planning
C) Only velocity
D) Only acceleration

**4.** RxInfer.jl is designed for:
A) Static analysis only
B) Real-time reactive message passing — suitable for robotics and streaming data applications
C) Only MATLAB users
D) Only visualization

**5.** Exploration in robot navigation under Active Inference emerges from:
A) Random walks
B) Epistemic value — the agent naturally moves toward uncertain regions to reduce model uncertainty
C) Pre-programmed routes
D) Human teleoperation

**6.** In multi-agent HRI, the robot models the human as:
A) A static object
B) Another Active Inference agent — predicting intentions, actions, and preferences through its generative model
C) A random variable
D) An obstacle

**7.** The "dark room problem" for robotics asks:
A) How robots navigate at night
B) If a robot minimizes surprise, why doesn't it stay still in a dark room? The answer is that its generative model includes homeostatic priors (e.g., battery level, task goals) that generate prediction errors requiring movement to resolve
C) Whether robots need light
D) How to power off robots

**8.** Factor graphs in Active Inference robotics enable:
A) Only discrete computations
B) Efficient real-time inference by factorizing the generative model into local computations — enabling distributed message passing that scales to complex, high-dimensional robotic systems
C) Only offline planning
D) Only simulation

## Part B: Short Answer

**1.** A robot arm reaches for an object but encounters an unexpected obstacle. Describe, step by step, how an Active Inference controller handles this perturbation differently from a classical PID controller. Which approach recovers more gracefully, and why? (200 words)

**2.** Compare the computational requirements of running Active Inference vs. deep reinforcement learning on a real-time robotic platform. What are the practical bottlenecks for each approach, and which is more feasible for current embedded hardware? (200 words)

## Part C: Essay Questions

**1.** Design a complete Active Inference robot for kitchen assistance. Specify: (a) the generative model (state space, observation model, transition model, preferences), (b) the implementation framework and justify your choice, (c) the control loop architecture, (d) how the robot handles uncertainty (noisy sensors, novel objects), (e) how it interacts with a human partner. (600 words)

**2.** Compare Active Inference robotics with: (a) classical control (PID), (b) model predictive control, and (c) deep reinforcement learning. For each: what problems does it handle well? What are its failure modes? Where does Active Inference provide unique value? (400 words)

**3.** Critically evaluate the "sim-to-real gap" for Active Inference robots. What changes when moving from simulation to hardware? How does the generative model need to be adapted? Is Active Inference more or less robust to the sim-to-real gap than reinforcement learning? (400 words)
