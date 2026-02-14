# Module 05: Action — Robotics and Embodied Active Inference

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Apply Active Inference to **robot control** — designing sensorimotor agents that act through prediction.
2. Analyze the software tools (**pymdp, SPM, RxInfer.jl**) for implementing Active Inference.
3. Evaluate the advantages of Active Inference robotics over classical and RL-based approaches.

## Key Concepts

### 1. Embodied Active Inference

Active Inference naturally extends to robotics because motor control IS active inference — acting to fulfill proprioceptive predictions:

**The control loop**: The robot has a generative model predicting sensory consequences of actions. Motor commands are generated to minimize the difference between predicted and desired proprioceptive states. This replaces classical inverse kinematics with predictive inference.

**Advantages**: No need for separate perception and control modules — both emerge from the same generative model. The robot inherently handles uncertainty, adapts to perturbations, and explores informative states.

### 2. Software Implementation Frameworks

**pymdp (Python)**: Open-source Python package for discrete-state Active Inference (POMDPs). Features:

- Define A (observation), B (transition), C (preferences), D (prior beliefs) matrices
- Policy evaluation via expected free energy G(π)
- Belief updating via variational message passing
- Customizable for any discrete task

**SPM/spm_MDP_VB (MATLAB)**: The original implementation in the Statistical Parametric Mapping toolkit. Implements discrete POMDP models with hierarchical and deep temporal extensions.

**RxInfer.jl (Julia)**: Reactive message passing framework for real-time Active Inference. Uses factor graphs and variational message passing, scales to continuous state spaces. Designed for robotics and real-time applications.

### 3. Continuous State-Space Active Inference

For robotics, continuous state-space models are essential:

**Generalized coordinates of motion**: States include position, velocity, acceleration, and higher-order derivatives: x̃ = (x, x', x'', ...). This enables smooth trajectory planning and execution.

**Free energy in generalized coordinates**: F = ε^T Π ε / 2, where ε are prediction errors in generalized coordinates and Π is the precision matrix. Minimizing F with respect to action produces motor commands.

**Attractor dynamics**: Desired behavior is encoded as an attractor in generalized coordinate space. The control law drives the system toward this attractor while minimizing prediction errors.

### 4. Robot Experiment Design

**Navigation tasks**: Robot navigates an environment, building a map (generative model) through exploratory behavior (epistemic foraging). Active Inference naturally balances exploration (reducing map uncertainty) and exploitation (reaching goal locations).

**Manipulation tasks**: Robot grasps objects, with the generative model predicting visual and tactile consequences of grip actions. Precision weighting determines how much to rely on vision vs. touch.

**Human-robot interaction**: The robot models the human partner as another Active Inference agent, predicting their intentions and actions. This enables coordination and collaborative behavior.

### 5. Implementation Workflow

1. **Define generative model**: Specify state space, observation model, transition model, preferences
2. **Implement in chosen framework**: Code A, B, C, D matrices (discrete) or generative equations (continuous)
3. **Simulation**: Test in simulation (Gazebo, MuJoCo, or custom)
4. **Parameter tuning**: Adjust precision parameters for stable behavior
5. **Hardware deployment**: Transfer to physical robot with real-time inference loop
6. **Validation**: Compare behavior to theoretical predictions and alternative controllers

### 6. Experimental Paradigms for Motor Active Inference

Rigorous empirical testing of motor Active Inference requires specific experimental paradigms:

**Force-field perturbation**: Subjects reach to targets while a robotic manipulandum applies unexpected force perturbations. Motor adaptation (recovering straight reaches over trials) is modeled as updating the B-matrix (transition model). The rate of adaptation, after-effects, and savings (faster re-learning) constrain the model's learning parameters. Active Inference predicts that adaptation rate depends on the precision of proprioceptive prediction errors — high precision → fast adaptation, which can be tested by manipulating sensory reliability (e.g., adding noise to visual feedback).

**Visuomotor rotation**: Subjects adapt to a rotated mapping between hand movement and cursor position. Active Inference predicts dual-rate adaptation (fast and slow processes) corresponding to different levels of the generative model hierarchy — fast processes update at the sensory level (recalibrating visuomotor mapping), while slow processes update at the structural level (learning a new visuomotor relationship).

**TMS and motor predictions**: Transcranial magnetic stimulation applied to motor cortex during movement planning reveals the time course of motor prediction formation. Motor-evoked potential amplitudes change *before* movement onset, reflecting the descending proprioceptive prediction. TMS can also disrupt the cerebellar forward model, selectively impairing motor prediction without affecting motor execution.

**EMG decomposition**: High-density surface EMG can decompose motor unit recruitment patterns during Active Inference-predicted movements, testing whether spinal reflex arcs (alpha motor neurons) fulfill predictions generated by motor cortex. Time-frequency analysis of EMG distinguishes prediction-driven (smooth, anticipatory) from error-driven (reactive, corrective) motor commands.

> **Clinical Application — Neurorehabilitation**: Active Inference provides principled guidelines for rehabilitation design: (1) recalibrate the generative model (not just strengthen muscles), (2) manipulate prediction error precision (augmented feedback, error amplification), and (3) use the cerebellum's learning rule (error-dependent, timing-sensitive practice). Brain-computer interfaces guided by Active Inference can close the sensorimotor loop for paralyzed patients by providing artificial prediction error signals.

> **Cross-Track Connection — Philosophical Foundations (Module 05)**: The experimental paradigms here operationalize the pragmatist principle of "learning by doing" — each perturbation study tests how the organism updates its generative model through active engagement with a changing environment.

## Summary

Active Inference provides a unified framework for robot perception, action, and learning. Software tools (pymdp, SPM, RxInfer.jl) implement both discrete and continuous models. Experimental paradigms — force-field perturbation, visuomotor rotation, TMS, and EMG decomposition — provide rigorous methods for testing motor Active Inference predictions. Robot experiments test the embodied predictions of Active Inference, from navigation and manipulation to human-robot interaction. Neurorehabilitation benefits from Active Inference's principled approach to motor relearning.

## Further Reading

- Lanillos, P. et al. (2021). Active inference in robotics and artificial agents: Survey and challenges. *arXiv preprint* arXiv:2112.01871.
- Fountas, Z. et al. (2020). Deep active inference agents using Monte-Carlo methods. *NeurIPS 2020*.
- Heins, C. et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *JOSS*, 7(73), 4098.
- Shadmehr, R. & Mussa-Ivaldi, F. A. (1994). Adaptive representation of dynamics during learning of a motor task. *Journal of Neuroscience*, 14(5), 3208-3224.
- Bestmann, S. & Duque, J. (2016). Transcranial magnetic stimulation. *The Neuroscientist*, 22(4), 392-405.
