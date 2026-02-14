# Lab: Swarm Communication and Collective Behavior

## Objective

Design multi-robot communication systems inspired by biological swarm intelligence. You will analyze how biological collectives (ant colonies, bee swarms, fish schools) coordinate without centralized control and design robotic swarm behaviors that exploit stigmergic communication and Active Inference principles.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Ant Colony Optimization

Analyze ant foraging as distributed Active Inference:

1. How do pheromone trails implement stigmergic communication (indirect coordination through environment modification)?
2. Model pheromone deposition as an action that modifies the environment's generative model for other ants.
3. Design a robotic pheromone system using virtual markers (e.g., shared map annotations) for warehouse robots.
4. How does pheromone evaporation implement forgetting / precision decay?

{fill:textarea}

## Part 2: Honeybee Waggle Dance

The honeybee waggle dance communicates food source location. Design a robotic equivalent:

1. What information does the waggle dance encode (direction, distance, quality)?
2. How is this a form of belief sharing that aligns generative models across the hive?
3. Design a communication protocol where robots share location-quality estimates for task sites.
4. How does the dance's imprecision (noisy communication) affect collective decision-making?

{fill:textarea}

## Part 3: Fish Schooling and Flocking

Design a flocking controller inspired by fish schooling:

1. Implement the three classic rules: separation, alignment, cohesion.
2. Frame each rule as minimizing prediction errors relative to social prior preferences.
3. How does each individual's generative model of its neighbors enable collective behavior without global coordination?
4. Design a robot swarm that exhibits emergent obstacle avoidance through local interaction rules only.

{fill:textarea}

## Part 4: Bio-Inspired Communication Comparison

Compare biological and robotic communication strategies:

| Feature | Ant Pheromones | Bee Dance | Fish Schooling | Robotic Swarm |
| --- | --- | --- | --- | --- |
| Communication channel | {fill} | {fill} | {fill} | {fill} |
| Information bandwidth | {fill} | {fill} | {fill} | {fill} |
| Range | {fill} | {fill} | {fill} | {fill} |
| Robustness to failure | {fill} | {fill} | {fill} | {fill} |

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
