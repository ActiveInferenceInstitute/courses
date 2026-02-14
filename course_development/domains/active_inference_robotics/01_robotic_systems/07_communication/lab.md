# Lab: Multi-Robot Communication and Coordination

## Objective

Design communication protocols for a multi-robot team, framing inter-robot communication as generative model alignment through shared prediction errors. You will analyze how robots can share beliefs, coordinate actions, and achieve consensus using Active Inference principles.

## Prerequisites

- Understanding of Active Inference agents from Modules 02 and 05
- Familiarity with basic networking concepts (publish-subscribe, message passing)
- Module 06: Learning (how shared experience accelerates adaptation)

## Part 1: Communication as Generative Model Alignment

Consider a team of three warehouse robots that must coordinate to avoid collisions and distribute pick tasks efficiently.

1. Each robot maintains its own generative model of the warehouse. What information should robots share to align their models?
   - Position beliefs (where am I?)
   - Task status (what am I doing?)
   - Environmental updates (obstacle detected at location X)
   - Model parameters (learned friction coefficients)

2. Frame inter-robot communication as prediction error sharing: Robot A sends a message to Robot B. In what sense is this message a prediction error that updates Robot B's generative model?

3. What is the Active Inference interpretation of a communication failure (lost message, delayed transmission)?

{fill:textarea}

## Part 2: ROS2 Topic Architecture Design

Design a ROS2-compatible message-passing architecture for the multi-robot team:

1. Define the topic structure:
   - `/robot_i/belief/pose` -- robot i's belief about its own pose
   - `/robot_i/belief/task_status` -- current task state
   - `/shared/environment_updates` -- map updates from any robot
   - `/shared/coordination` -- task allocation and conflict resolution

2. For each topic, specify: message type, publication rate, and which robots subscribe.
3. How does this architecture map to the Markov blanket structure of the multi-agent system? Each robot has its own blanket, and communication channels form the sensory/active states between robot blankets.

{fill:textarea}

## Part 3: Consensus as Collective Free Energy Minimization

Design a consensus algorithm where robots agree on a shared world model:

1. Each robot has a belief about the location of a movable obstacle: Robot A believes (3.0, 2.0), Robot B believes (3.2, 1.8), Robot C believes (2.9, 2.1).
2. Define a consensus update rule based on precision-weighted averaging:
   - mu_consensus = sum(Pi_i * mu_i) / sum(Pi_i)
   - Where Pi_i is robot i's confidence in its estimate
3. Trace three rounds of consensus updates. Do the robots converge? What happens if one robot has much higher precision than the others?
4. How does this relate to minimizing the collective free energy of the multi-agent system?

{fill:textarea}

## Part 4: Communication Bandwidth and Information Content

Analyze the trade-off between communication bandwidth and coordination quality:

| Communication Level | Bandwidth | Information Shared | Coordination Quality |
| --- | --- | --- | --- |
| No communication | 0 | Nothing | {fill} |
| Position only | Low | Pose estimates | {fill} |
| Beliefs + uncertainty | Medium | Poses + covariances | {fill} |
| Full generative model | High | All parameters + beliefs | {fill} |

1. For each level, describe a scenario where coordination succeeds or fails.
2. What is the minimum communication needed to avoid collisions?
3. Frame bandwidth constraints as a cost term in the expected free energy of communication actions.

{fill:textarea}

## Part 5: Distributed Active Inference Pseudocode

Write pseudocode for a distributed Active Inference loop where each robot runs locally but communicates with neighbors:

```
function distributed_AIF_step(robot_id, belief, neighbors):
    # 1. Local perception-action cycle
    observation = sense()
    belief = update_belief(observation, model)
    action = select_action(belief, preferences)

    # 2. Communication: send belief summary to neighbors
    for neighbor in neighbors:
        send(robot_id, belief.summary(), neighbor)

    # 3. Receive and integrate neighbor beliefs
    for message in receive_all():
        belief = integrate_neighbor_belief(belief, message)

    # 4. Coordination: adjust action if conflict detected
    if collision_predicted(belief, neighbor_beliefs):
        action = resolve_conflict(action, neighbor_beliefs)

    execute(action)
    return belief
```

{fill:textarea}

## Summary Table

| Communication Aspect | Classical Multi-Robot | Active Inference Multi-Robot |
| --- | --- | --- |
| Message content | State estimates | Beliefs + precisions (prediction errors) |
| Coordination mechanism | Centralized planner or auction | Collective free energy minimization |
| Conflict resolution | Priority rules | Precision-weighted consensus |
| Adaptation to failures | Timeout + fallback | Reduced precision for silent agents |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Friston, K., & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Ren, W., & Beard, R. W. (2008). *Distributed Consensus in Multi-vehicle Cooperative Control*. Springer.
