# Lab: Autonomous Navigation and Mission Planning

## Objective

Design and compare path planning algorithms for an autonomous mobile robot, framing navigation as expected free energy minimization over future trajectories. You will implement a planning algorithm that balances goal-seeking (pragmatic value) with information-gathering (epistemic value), and design a hierarchical mission planning system.

## Prerequisites

- Understanding of world models from Module 04 (maps, SLAM)
- Familiarity with path planning concepts (A*, RRT, potential fields)
- Module 05: Action (how planned actions are executed)

## Part 1: Planning as Expected Free Energy Minimization

A mobile robot must navigate from a start position to a goal position in a partially known environment.

1. Define the planning problem:
   - State space: robot pose (x, y, theta)
   - Action space: discrete set of motion primitives (forward, turn left, turn right, backward)
   - Observations: LIDAR scans providing partial environment information
   - Goal: reach target position (10.0, 8.0) while avoiding obstacles

2. For each candidate trajectory (sequence of actions), compute:
   - **Pragmatic value**: Expected proximity to goal position (how close will I get?)
   - **Epistemic value**: Expected information gain about unknown map regions (what will I learn?)
   - **Expected free energy**: G = pragmatic_value + epistemic_value

3. How does a robot choose between a short known path and a slightly longer path through unexplored territory?

{fill:textarea}

## Part 2: Classical vs. Active Inference Planning

Compare three planning approaches for the same navigation task:

| Feature | A* Search | RRT (Rapidly-exploring Random Tree) | Active Inference Planning |
| --- | --- | --- | --- |
| Objective | {fill} | {fill} | {fill} |
| Uncertainty handling | {fill} | {fill} | {fill} |
| Exploration strategy | {fill} | {fill} | {fill} |
| Replanning trigger | {fill} | {fill} | {fill} |
| Computational cost | {fill} | {fill} | {fill} |

1. When would A* outperform Active Inference planning? When would AI planning be superior?
2. How does Active Inference planning naturally handle the exploration-exploitation trade-off?

{fill:textarea}

## Part 3: Hierarchical Mission Planning

Design a two-level mission planning system for a delivery robot:

**High-level planner** (task level):
- Plans a sequence of locations to visit: pick-up station -> aisle 3 -> packing station B
- Operates on a topological map (graph of places)
- Timescale: decisions every 10-30 seconds

**Low-level planner** (navigation level):
- Plans collision-free paths between locations
- Operates on a metric map (occupancy grid)
- Timescale: replans every 0.5-2 seconds

1. How do the two levels communicate? Frame this as top-down prior preferences (high level sets goals) and bottom-up evidence (low level reports feasibility).
2. What happens when the low-level planner discovers that a planned path is blocked? How does this information propagate to the high-level planner?

{fill:textarea}

## Part 4: Planning Under Uncertainty

Design a scenario with three types of uncertainty and show how Active Inference planning handles each:

1. **State uncertainty**: The robot is unsure of its exact position (localization error). How does this affect planned trajectories? (Hint: plans that pass through feature-rich areas reduce state uncertainty.)
2. **Map uncertainty**: A corridor might be blocked. Design a plan that includes a contingency branch.
3. **Goal uncertainty**: The robot receives an ambiguous delivery instruction. How does it plan actions to clarify the goal (e.g., ask for confirmation, inspect the label)?

For each type, write the expected free energy decomposition showing which term (pragmatic or epistemic) dominates.

{fill:textarea}

## Part 5: Planning Algorithm Pseudocode

Write pseudocode for an Active Inference path planner:

```
function plan_trajectory(belief, goal, world_model, horizon):
    candidate_policies = generate_candidate_trajectories(belief, horizon)

    for each policy in candidate_policies:
        G = 0  # expected free energy
        current_belief = belief
        for t in range(horizon):
            # Predict future beliefs under this policy
            predicted_belief = predict(current_belief, policy[t], world_model)
            predicted_observation = expected_observation(predicted_belief, world_model)

            # Pragmatic value: distance to goal preferences
            G += pragmatic_value(predicted_observation, goal)

            # Epistemic value: expected uncertainty reduction
            G += epistemic_value(current_belief, predicted_belief)

            current_belief = predicted_belief

    best_policy = argmin(G)  # lowest expected free energy
    return best_policy[0]  # return first action
```

{fill:textarea}

## Summary Table

| Planning Aspect | Classical Approach | Active Inference Approach |
| --- | --- | --- |
| Objective | Minimize cost (distance, time) | Minimize expected free energy |
| Exploration | Separate exploration phase | Integrated via epistemic value |
| Uncertainty | Handled post-hoc or ignored | Core part of objective |
| Replanning | Triggered by failure | Continuous (beliefs update, plans update) |
| Hierarchy | Separate planners | Nested generative models |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Kaplan, R., & Friston, K. (2018). Planning and navigation as active inference. *Biological Cybernetics*, 112(4), 323-343.
- LaValle, S. M. (2006). *Planning Algorithms*. Cambridge University Press.
