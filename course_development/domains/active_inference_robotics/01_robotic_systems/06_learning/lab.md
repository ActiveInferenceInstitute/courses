# Lab: Adaptive Robotics and Online Learning

## Objective

Design and analyze learning mechanisms for a robot that must adapt its generative model parameters online. You will compare fixed-model controllers with adaptive controllers, explore sim-to-real transfer challenges, and design a learning architecture that updates model parameters while maintaining stable control.

## Prerequisites

- Understanding of generative models and free energy from Modules 03-05
- Familiarity with parameter estimation concepts
- Basic understanding of gradient-based optimization

## Part 1: Parameter Learning Scenario

A robot arm has learned its dynamics model in simulation but is now deployed on physical hardware where:
- Joint friction coefficients differ by 20-40% from simulation
- Link masses have manufacturing tolerances of +/- 5%
- Motor torque constants vary due to temperature

1. Identify which generative model parameters need to be updated for sim-to-real transfer.
2. For each parameter, specify: what observations would reveal the mismatch? What prediction errors would signal that learning is needed?
3. How does the free energy signal (high free energy = poor model fit) serve as a natural learning trigger?

{fill:textarea}

## Part 2: Online Parameter Adaptation

Design an online learning algorithm that updates the robot's dynamics model during operation:

1. **Learning rule**: Define the parameter update as gradient descent on free energy:
   - theta_{t+1} = theta_t - eta * dF/dtheta
   - Where theta includes friction coefficients, mass parameters, and motor constants

2. **Learning rate selection**: What determines the optimal learning rate? How does precision (confidence in current parameters) affect the learning rate?
3. **Stability constraint**: How do you ensure that parameter updates do not destabilize the controller? Describe at least two safeguards.

{fill:textarea}

## Part 3: Sim-to-Real Transfer Analysis

Compare three approaches to sim-to-real transfer:

| Approach | Description | Advantages | Limitations |
| --- | --- | --- | --- |
| Domain randomization | Train with varied simulation parameters | {fill} | {fill} |
| System identification | Measure physical parameters directly | {fill} | {fill} |
| Active Inference adaptation | Online free energy minimization | {fill} | {fill} |

For each approach, describe how it handles a specific sim-to-real gap: the simulated floor has friction coefficient 0.8, but the real floor has coefficient 0.4.

{fill:textarea}

## Part 4: Hierarchical Learning

Robots must learn at multiple timescales. Design a hierarchical learning architecture:

1. **Fast adaptation** (milliseconds): Precision updates -- adjusting confidence in sensor readings based on recent reliability.
2. **Medium adaptation** (seconds-minutes): Parameter updates -- adjusting dynamics model parameters (friction, mass, motor constants).
3. **Slow adaptation** (hours-days): Structure learning -- changing the model architecture itself (adding new state variables, changing model topology).

For each timescale, specify: what is being learned, what drives the learning, and what are the risks of learning too fast or too slow.

{fill:textarea}

## Part 5: Lifelong Learning Architecture

Design a pseudocode architecture for a robot that learns continuously throughout its operational lifetime:

```
function lifelong_learning_loop():
    while operational:
        # 1. Perceive and act (standard AIF loop)
        observation = sense()
        belief = update_belief(observation, model)
        action = select_action(belief, preferences)
        execute(action)

        # 2. Monitor free energy (learning signal)
        F = compute_free_energy(belief, observation, model)

        # 3. Fast adaptation: update precisions
        if F > threshold_fast:
            update_precisions(observation_history)

        # 4. Medium adaptation: update parameters
        if F > threshold_medium over window:
            update_parameters(gradient_F, learning_rate)

        # 5. Slow adaptation: consider model structure
        if F > threshold_slow over long_window:
            propose_model_revision()

        # 6. Consolidation: periodic review
        if time_for_consolidation:
            consolidate_learned_parameters()
```

{fill:textarea}

## Summary Table

| Learning Type | Timescale | What Changes | Free Energy Signal | Robotics Example |
| --- | --- | --- | --- | --- |
| Precision updating | Milliseconds | Sensor confidence | Prediction error variance | {fill} |
| Parameter learning | Seconds-minutes | Model parameters | Persistent prediction errors | {fill} |
| Structure learning | Hours-days | Model architecture | Irreducible free energy | {fill} |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Nguyen, S. M., & Oudeyer, P. Y. (2013). Active choice of teachers, learning strategies and goals for a socially guided intrinsic motivation learner. *Paladyn*, 3(3), 136-146.
- Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. *IEEE IROS*.
