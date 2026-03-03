# Research Methods — Module 05: Action — Study Questions

## Recall and Comprehension

1. How does Active Inference replace classical inverse kinematics for robot control?
2. What are the advantages of a unified perception-action framework in robotics?
3. Describe pymdp's core data structures. What are A, B, C, D matrices?
4. How does RxInfer.jl differ from pymdp? What applications does each serve best?
5. What are generalized coordinates of motion? Why are they needed for continuous control?

## Analysis and Application

1. How is free energy computed in generalized coordinates? How does this differ from the discrete POMDP case?
2. What are attractor dynamics? How do they encode desired behavior in the continuous Active Inference framework?
3. How does a robot balance exploration and exploitation during navigation? What role does the epistemic term in EFE play?
4. How does precision weighting determine the balance between visual and tactile feedback during manipulation? Under what conditions should tactile precision dominate?
5. How can a robot model a human partner as another Active Inference agent? What is the minimal model complexity needed for effective human-robot interaction?
6. What is the implementation workflow from generative model definition to hardware deployment? What are the bottleneck steps?
7. What challenges arise when transferring an Active Inference controller from simulation to real hardware (sim-to-real)? How does domain randomization help?

## Research Design

1. How does Active Inference handle unexpected perturbations during robot manipulation? Design an experiment to measure recovery from a sudden 10N force perturbation.
2. Compare Active Inference control with PID control for a reaching task. Specify: (a) state space, (b) action space, (c) performance metrics, (d) conditions under which each framework is expected to win.
3. Compare Active Inference control with model-based RL for navigation. Under what conditions (partial observability, novel environments, multi-objective) does each approach have theoretical advantages?
4. What is deep active inference? How do neural networks approximate the generative model? What are the training challenges (mode collapse, local minima)?
5. How do you validate that a robot is "truly" performing Active Inference vs. implementing a control law that happens to produce similar behavior?

## Critical Evaluation

1. What precision parameters must be tuned for stable robot behavior? Is this different from gain tuning in PID — or is Active Inference robotics just "PID with extra steps"?
2. How does Active Inference handle sensor noise and actuator uncertainty? Compare with Kalman filter approaches — when are they equivalent?
3. Design a robot experiment that demonstrates Active Inference's advantage over classical control in a scenario requiring **both** perception and action adaptation (e.g., grasping novel objects with unknown mass).
4. A robotics paper claims their Active Inference controller achieves "zero-shot transfer" to a new task. What must be true about the generative model for this to work? What are the failure modes?
5. How does the computational cost of Active Inference planning scale with action space and planning horizon? At what point does it become intractable, and what approximations are used?
6. Critically evaluate: Is there an in-principle advantage to Active Inference robotics over well-tuned model-predictive control (MPC), or is the advantage primarily conceptual/unifying?
