# Lab: Bio-Inspired Navigation and Foraging

## Objective

Design navigation and foraging algorithms inspired by biological strategies. You will analyze how animals plan routes, forage optimally, and make decisions under uncertainty, then implement bio-inspired planning algorithms for autonomous robots.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Path Integration and Dead Reckoning

Analyze biological path integration (desert ant navigation) as Active Inference planning:

1. How does the desert ant maintain a home vector using optic flow and step counting?
2. Model this as a generative model that predicts position from self-motion cues.
3. How does the ant decide when to switch from exploration to homing?
4. Design a robotic path integration system inspired by ant navigation for GPS-denied environments.

{fill:textarea}

## Part 2: Optimal Foraging Theory

Apply optimal foraging theory to robotic task allocation:

1. The marginal value theorem: when should a robot leave a depleting resource patch? Frame as expected free energy evaluation.
2. Design a foraging policy where robots exploit known reward locations while exploring for new ones.
3. How does the explore-exploit trade-off in foraging map to pragmatic vs. epistemic value in Active Inference?

{fill:textarea}

## Part 3: Cognitive Maps and Spatial Planning

Compare biological cognitive maps with robotic planning:

1. How do rats use hippocampal replay to plan novel shortcuts they have never traveled?
2. Design a robotic planning system that uses experience replay to discover new routes.
3. How does the concept of a cognitive map differ from a metric map, and what are the planning implications?

{fill:textarea}

## Part 4: Bio-Inspired Planning Comparison

Compare planning strategies:

| Feature | Desert Ant | Honeybee | Rat | AI Robot Planner |
| --- | --- | --- | --- | --- |
| Spatial representation | {fill} | {fill} | {fill} | {fill} |
| Planning horizon | {fill} | {fill} | {fill} | {fill} |
| Optimality | {fill} | {fill} | {fill} | {fill} |
| Novel route discovery | {fill} | {fill} | {fill} | {fill} |

{fill:textarea}

## Summary Table

| Concept | Classical Robotics | Active Inference | Your Design |
| --- | --- | --- | --- |
| Core mechanism | {fill} | {fill} | {fill} |
| Uncertainty handling | {fill} | {fill} | {fill} |
| Adaptation | {fill} | {fill} | {fill} |
| Key advantage | {fill} | {fill} | {fill} |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- Pio-Lopez, L., Nizard, A., Friston, K., & Pezzulo, G. (2016). Active Inference and robot control. *Journal of the Royal Society Interface*, 13(122).
