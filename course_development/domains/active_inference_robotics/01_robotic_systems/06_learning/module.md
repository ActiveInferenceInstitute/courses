# Robotic Learning: Updating Generative Models Through Experience

## Executive Summary

Learning in robotics is the process by which a robot improves its generative model through interaction with the world. In Active Inference, learning corresponds to updating the parameters and structure of the generative model to reduce long-term prediction error — making the robot's internal model a better approximation of the true dynamics of its body and environment. This module examines how robots learn dynamics models from manipulation experience, adapt perception models to new visual conditions, and tune control policies through trial and error. Unlike offline machine learning, robotic learning must contend with real-time constraints, physical safety requirements, and the cost of acquiring data through actual physical interaction.

## Learning Objectives

1. Define robotic learning as parameter and structure updates to the generative model driven by accumulated prediction errors.
2. Distinguish between parameter learning (adjusting existing model weights) and structure learning (changing the model architecture).
3. Analyze the accuracy-complexity trade-off in robotic model learning and its relationship to variational free energy.
4. Evaluate the challenges unique to robotic learning: sample efficiency, safety constraints, and sim-to-real transfer.
5. Connect robotic learning paradigms (supervised, reinforcement, self-supervised) to Active Inference's free energy minimization.

## Introduction

The previous module on Action examined how robots translate beliefs into physical forces. But what happens when those actions produce unexpected outcomes — when the object slips from the gripper, when the mobile base skids on a wet floor, when the visual detector misidentifies a part? These prediction errors are not just problems to be corrected in the moment; they are learning signals that can improve the robot's generative model for future interactions. In the next module on Communication, we will see how learned knowledge can be shared between robots; here, we focus on the individual robot's learning process.

## Key Concepts

### 1. Learning as Free Energy Minimization Over Long Timescales

In Active Inference, perception updates beliefs about hidden states on a fast timescale (milliseconds to seconds), while learning updates the parameters of the generative model on a slower timescale (minutes to hours to days). Both processes minimize variational free energy, but at different levels of the model hierarchy.

When a UR5 manipulator repeatedly fails to grasp objects at the expected location, the immediate perceptual response is to update the belief about the object's current position. But if the offset is systematic — the camera is slightly miscalibrated — then perceptual correction alone is insufficient. The robot needs to learn a new value for the camera extrinsic calibration parameter, adjusting the generative model so that future predictions from camera observations are more accurate. This parameter update is learning: it changes the model itself, not just the current state estimate.

The variational free energy framework provides a natural objective for learning. Parameters should be updated to reduce the average prediction error across many observations, subject to a complexity penalty that prevents overfitting. A dynamics model with too many parameters might perfectly fit the training data (low accuracy term) but fail on novel situations because it has memorized noise (high complexity term). The free energy objective balances these, guiding the robot toward models that are accurate and parsimonious.

### 2. Parameter Learning in Dynamics Models

Dynamics models — predicting how the world evolves given the robot's actions — are central to robotic control and planning. Learning the parameters of these models from experience is one of the most important forms of robotic learning.

For a manipulator, the dynamics model includes the mass, inertia, and friction parameters of each link and joint. Classical system identification estimates these from carefully designed excitation trajectories. But in Active Inference, learning can be continuous: every motion the robot makes generates prediction errors between expected and actual joint torques, and these errors can be used to incrementally refine the dynamics parameters through gradient descent on the variational free energy.

For a mobile robot, the dynamics model includes wheel radius, track width, and surface friction coefficients. These parameters change over time — tires wear, floors are waxed, payloads change. An Active Inference robot continuously monitors its prediction errors (the difference between commanded and actual velocities) and updates its dynamics parameters accordingly. If the robot suddenly finds itself slipping on a wet floor, the increased prediction errors drive rapid updates to the friction parameter, which in turn causes the controller to command more conservative velocities.

### 3. Learning Perception Models

The observation model — predicting what sensory data the robot should receive given the world state — also requires learning and adaptation.

A visual object detector trained in one lighting condition may fail when deployed in another. Active Inference frames this as increased prediction error at the observation level: the model predicts one pattern of pixel intensities, but the actual image is systematically different. Learning reduces this error by updating the observation model parameters. Fine-tuning a neural network object detector on images from the deployment environment is parameter learning in the observation model. Training a new detector from scratch for a novel object class is structure learning — adding new states and observation mappings to the generative model.

Self-supervised learning is particularly natural for robotic perception. A robot that grasps objects learns to associate visual features with grasp success and failure. An object that looks graspable (low prediction error on the observation model) but consistently slips from the gripper (high prediction error on the action outcome model) generates a learning signal that updates the visual model to better predict grasp affordances. This learning loop — act, observe outcome, update model — is exactly the perception-action-learning cycle that Active Inference prescribes.

### 4. Sim-to-Real Transfer and Domain Adaptation

One of the major challenges in robotic learning is data efficiency. Physical robot interactions are slow, expensive, and potentially damaging. Simulation offers unlimited, safe, fast data generation — but simulated environments inevitably differ from reality. Sim-to-real transfer addresses this gap.

In Active Inference terms, sim-to-real transfer is a model adaptation problem. The generative model learned in simulation has systematic prediction errors when applied to the real world — the simulated physics does not perfectly match real physics, the rendered images do not match real camera images. The robot must learn to correct these discrepancies, either by fine-tuning the entire model on real-world data or by learning a "residual" model that captures the sim-to-real gap.

Domain randomization — systematically varying simulation parameters (friction, lighting, camera noise) during training — forces the learned model to be robust across a range of conditions. In Active Inference terms, this is learning a model with appropriate complexity: rather than overfitting to one specific simulation, the model captures the invariant structure that transfers to reality. The residual prediction errors that remain after sim-to-real transfer drive continued learning in the real environment, progressively closing the gap between the model and reality.

### 5. Safety Constraints on Robotic Learning

Unlike learning in virtual environments, robotic learning in the physical world carries real risks. A robot that explores aggressively to learn its dynamics model might collide with objects, damage itself, or injure nearby humans. Safety constraints are essential in robotic learning.

Active Inference provides a natural framework for safe exploration through the expected free energy objective. The expected free energy includes a risk term — the probability of visiting states that are far from the agent's preferred (safe) states. This risk term penalizes exploratory actions that might lead to dangerous configurations (joint limits, excessive contact forces, proximity to humans) while still allowing the epistemic term to drive learning-oriented exploration in safe regions of the state space.

In practice, this manifests as constrained exploration strategies. A manipulator learning its payload capacity might explore with small, gradually increasing loads rather than immediately attempting the maximum load. A mobile robot learning to navigate a new environment might first explore open areas before venturing into narrow corridors. These cautious exploration patterns emerge from the expected free energy objective when the preference model encodes appropriate safety margins.

## Active Inference Connection

Learning in Active Inference is the slow minimization of variational free energy with respect to model parameters, as opposed to the fast minimization with respect to hidden states (perception) and actions (control). This three-timescale optimization — fast perception, medium-speed action, slow learning — mirrors the hierarchy of adaptation in robotic systems. Critically, Active Inference provides a unified objective for all three timescales, eliminating the need for separate loss functions for perception, control, and learning. The same prediction error that drives perceptual updates and action corrections also drives model learning, ensuring that the robot's generative model improves wherever its predictions are most inaccurate.

## Applications

### Case Study 1: Online Dynamics Learning for UR5 Manipulation

A UR5 manipulator tasked with handling objects of unknown mass demonstrates online dynamics learning. The robot's generative model initially assumes the end-effector is unloaded. When the robot grasps a 2 kg object, the actual joint torques required to execute a trajectory differ significantly from the predicted torques — the prediction error spikes. The learning algorithm (recursive least squares on the dynamics parameters) incrementally updates the estimated payload mass, center of gravity, and inertia tensor over the next several motion cycles. Within five repetitions, the prediction error returns to baseline, and the robot's motions become smooth and accurate for the new payload. When the robot releases the object and grasps a different one, the learning process repeats, adapting to the new payload parameters. This continuous adaptation is parameter learning under the Active Inference framework — the same prediction errors that drive joint-level control also drive model parameter updates on a slower timescale.

### Case Study 2: Visual Model Adaptation for Mobile Robot Navigation

A Clearpath Jackal robot trained to navigate using visual features in a well-lit laboratory is deployed in a dimly lit warehouse. The visual odometry system, which tracks feature points across camera frames, initially fails — prediction errors spike because the observation model (trained on bright, high-contrast images) cannot accurately predict the dark, low-contrast warehouse images. A self-supervised adaptation procedure runs overnight: the robot drives slowly through the warehouse, collecting paired data from its camera (high prediction error) and its lidar (low prediction error, since lidar is unaffected by lighting). Using the lidar-derived motion estimates as ground truth, the visual model's parameters are updated to handle the new lighting conditions. After adaptation, visual odometry prediction errors drop to acceptable levels, and the robot can navigate using vision alone. This is observation model learning driven by cross-modal prediction error — the lidar provides a reliable reference signal that enables the visual model to learn.

## Cross-References

- **Module 3 (Perception)**: The perceptual prediction errors that serve as learning signals
- **Module 5 (Action)**: The action outcomes that generate experience data for learning
- **Module 4 (Cognition)**: How learned model improvements enhance cognitive capabilities
- **Module 8 (Planning)**: How more accurate learned models enable better planning

## Summary

| Concept | Definition | Robotics Example |
|---------|-----------|-----------------|
| Parameter Learning | Updating model weights to reduce prediction error | Estimating payload mass from joint torque errors |
| Structure Learning | Changing the model architecture to represent new entities or relationships | Adding a new object class to a visual detector |
| Accuracy-Complexity Trade-off | Balancing model fit against model simplicity | Domain randomization preventing simulation overfitting |
| Sim-to-Real Transfer | Adapting a simulation-trained model to the real world | Fine-tuning a grasp policy on a physical UR5 after training in simulation |
| Safe Exploration | Learning through experience while respecting physical safety constraints | Gradually increasing payload exploration within torque limits |
| Self-Supervised Learning | Learning from prediction errors between different sensory modalities | Using lidar to supervise visual odometry adaptation |

## References

1. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
2. Nguyen-Tuong, D., & Peters, J. (2011). Model learning for robot control: A survey. *Cognitive Processing*, 12(4), 319-340.
3. Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. *IROS*.
4. Brunke, L., et al. (2022). Safe learning in robotics: From learning-based control to safe reinforcement learning. *Annual Review of Control, Robotics, and Autonomous Systems*, 5, 411-444.
