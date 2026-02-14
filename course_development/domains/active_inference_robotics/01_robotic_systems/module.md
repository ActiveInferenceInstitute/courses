# Unit 01: Robotic Systems — Overview

## Executive Summary

This unit establishes the foundational concepts of robotic systems through the lens of Active Inference. Robots are physical agents that must maintain their structural and functional integrity while operating in uncertain, dynamic environments. The Free Energy Principle provides a unifying framework for understanding how robotic hardware architectures, sensor suites, actuator configurations, and software stacks work together to form coherent systems that sense, act, and persist. From industrial manipulators like the UR5 to mobile platforms running ROS2, every robotic system can be analyzed as a collection of nested Markov blankets that separate internal computational states from the external physical world. This unit covers the eight core aspects of Active Inference as they apply to foundational robotics: system boundaries, agent architectures, perception pipelines, cognitive processing, action generation, learning mechanisms, communication protocols, and planning frameworks.

## Learning Objectives

1. Characterize a robotic system as a hierarchical composition of Markov blankets spanning hardware, software, and environmental interfaces.
2. Identify how sensors (lidar, IMU, joint encoders, cameras) constitute the sensory states of a robot's Markov blanket.
3. Analyze how actuators (servo motors, pneumatic cylinders, grippers) constitute the active states through which robots modify their environment.
4. Apply the variational free energy framework to understand how robotic control architectures maintain stable operation under uncertainty.
5. Map the eight Active Inference modules to concrete robotics subsystems and engineering practices.

## Unit Structure

This unit progresses through eight modules, each examining a core Active Inference concept as it manifests in robotic systems engineering:

### Module 1: Systems
Establishes the robot as a system with identifiable boundaries. Examines how hardware architecture, from the UR5 manipulator's kinematic chain to a mobile robot's chassis and sensor payload, defines the physical Markov blanket. Introduces nested system decomposition in ROS2 node architectures.

### Module 2: Agents
Defines what it means for a robot to be an agent — an entity that acts to minimize surprise. Covers the distinction between reactive controllers, deliberative planners, and hybrid architectures. Examines how agency emerges from the interaction of sensors, processors, and actuators.

### Module 3: Perception
Explores how robots construct internal models of their environment from raw sensor data. Covers lidar point cloud processing, IMU fusion, visual feature extraction, and proprioceptive state estimation through joint encoders. Frames perception as approximate Bayesian inference.

### Module 4: Cognition
Addresses the computational processes by which robots maintain and update their generative models. Covers belief propagation on factor graphs, probabilistic state estimation, and the role of onboard computing architectures (CPU, GPU, FPGA) in supporting real-time inference.

### Module 5: Action
Examines how robots generate motor commands to minimize expected free energy. Covers joint-space and task-space control, torque computation, trajectory generation, and the relationship between action and active inference's concept of active states.

### Module 6: Learning
Explores how robots update their generative models through experience. Covers parameter learning in dynamics models, structure learning for task adaptation, and the relationship between model complexity and generalization in robotic manipulation.

### Module 7: Communication
Addresses how robots exchange information with other systems, human operators, and each other. Covers ROS2 topic/service architectures, human-robot interaction modalities, and how communication extends the effective Markov blanket of a robotic system.

### Module 8: Planning
Examines how robots select action sequences by evaluating expected free energy over future time horizons. Covers motion planning algorithms, task planning, and the relationship between planning depth, computational resources, and plan quality.

## Key Themes Across the Unit

**Hardware-Software Co-Design**: Robotic systems cannot be understood by examining hardware or software alone. The physical configuration of sensors and actuators constrains what generative models are possible, while the computational architecture determines how quickly and accurately those models can be updated.

**Real-Time Constraints**: Unlike many AI systems that can process data in batch, robots must close the perception-action loop within strict timing deadlines. A manipulator moving at speed must update its state estimate and compute control signals within milliseconds. This real-time requirement shapes every aspect of robotic Active Inference.

**Embodiment**: Robots are physically embedded in the world they model. Their bodies are not incidental but constitutive of their cognitive capabilities. The compliance of a gripper, the field of view of a camera, and the bandwidth of a communication link all shape the robot's generative model and the policies available to it.

## Cross-References

- **Unit 02 (Bio-Inspired Design)**: Biological organisms provide existence proofs for many robotic system architectures
- **Unit 03 (Control and Estimation)**: The mathematical foundations of state estimation and control that underpin robotic Active Inference
- **Unit 04 (Autonomous Agents)**: How the single-robot principles from this unit scale to multi-robot and fully autonomous systems

## References

1. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
2. Siciliano, B., & Khatib, O. (Eds.). (2016). *Springer Handbook of Robotics* (2nd ed.). Springer.
3. Macenski, S., et al. (2022). Robot Operating System 2: Design, architecture, and uses in the wild. *Science Robotics*, 7(66).
4. Lanillos, P., et al. (2021). Active Inference in robotics and artificial agents: Survey and challenges. *arXiv preprint arXiv:2112.01871*.
