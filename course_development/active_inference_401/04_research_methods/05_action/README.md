# Module 05: Action

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Robotics and Embodied Active Inference

Part of **Research Methods**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Robotics and Embodied Active Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Implementing Active Inference Agents in Simulation and Hardware |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Apply** Active Inference to robot control, implementing a sensorimotor agent that acts through proprioceptive prediction fulfillment rather than classical command-based control, demonstrating reaching, grasping, or navigation behaviors
2. **Analyze** the software tools available for Active Inference research (pymdp for discrete state spaces, SPM for continuous models, RxInfer.jl for scalable message passing), comparing their architectures, capabilities, and appropriate use cases
3. **Evaluate** the advantages of Active Inference robotics over classical control and reinforcement learning approaches, identifying specific tasks where the Active Inference formulation provides superior generalization, sample efficiency, or robustness to perturbation
4. **Design** and implement an embodied Active Inference agent for a novel task, specifying the generative model (state space, likelihood, transition dynamics, preferences), inference algorithm, and evaluation metrics

## Prerequisites

- Graduate-level robotics or control theory (state estimation, PID control, model predictive control)
- Proficiency in at least one Active Inference toolkit (pymdp, SPM, or RxInfer.jl)
- Experience with simulation environments (OpenAI Gym, MuJoCo, or ROS)

## Key References

- Lanillos, P. et al. (2021). Active inference in robotics and artificial agents: Survey and challenges. *arXiv:2112.01871*.
- Heins, C. et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software*, 7(73), 4098.
- Pio-Lopez, L. et al. (2016). Active inference and robot control: A case study. *Journal of the Royal Society Interface*, 13(122), 20160616.
- Millidge, B. et al. (2021). Whence the expected free energy? *Neural Computation*, 33(2), 447--482.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
