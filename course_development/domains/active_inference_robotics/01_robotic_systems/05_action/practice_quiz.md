# Practice Quiz: Action in Robotic Systems

## Part A: Multiple Choice

1. In Active Inference, robotic action is fundamentally about:
A) Executing pre-programmed motion sequences without feedback
B) Changing the world to make sensory observations conform to the agent's predictions and preferences
C) Moving as fast as possible
D) Consuming maximum electrical power

**Answer: B** -- Action in Active Inference is the process of changing the environment so that sensory observations match the agent's preferred states. A robot reaches for an object not because it received a "reach" command, but because its generative model predicts (prefers) the sensory state of holding the object.

2. How does Active Inference differ from traditional PID control for a robot joint?
A) Active Inference cannot control robot joints
B) PID minimizes a setpoint error using fixed gains, while Active Inference minimizes free energy using precision-weighted prediction errors, unifying perception and control under one objective
C) PID is always superior to Active Inference
D) There is no difference whatsoever

**Answer: B** -- PID control uses fixed proportional, integral, and derivative gains to minimize error. Active Inference treats the setpoint as a preferred sensory state and adjusts actions to minimize variational free energy, naturally handling uncertainty and adapting precision weighting based on context.

3. Motor primitives in the Active Inference framework are best understood as:
A) The smallest physical components of a motor
B) Attractors in a dynamical generative model -- preferred trajectories that the agent's actions attempt to realize
C) Random motor commands
D) Factory default settings

**Answer: B** -- Motor primitives are encoded as attracting trajectories in the generative model. The robot "expects" its joints to follow a specific trajectory, and motor commands are generated to minimize the prediction error between expected and actual joint positions.

4. A robot arm performing compliant manipulation uses force feedback to adjust its grip. In Active Inference terms, this is:
A) A failure of the control system
B) Active inference on proprioceptive predictions -- the robot adjusts its actions to minimize the discrepancy between predicted and observed contact forces
C) The robot ignoring its sensors
D) An open-loop control strategy

**Answer: B** -- When the robot predicts a certain contact force but observes a different one, the prediction error drives action updates. Increasing grip force or reducing approach speed are actions that bring observed forces closer to the predicted (desired) profile.

5. What is the relationship between action and the active states of the Markov blanket?
A) Active states are the robot's internal computations
B) Active states are the sensory inputs to the robot
C) Active states are the channels through which the robot exerts physical influence on the world -- motors, grippers, propellers
D) Active states exist only in simulation

**Answer: C** -- Active states are the boundary states through which the robot's decisions become physical changes in the environment. Joint motors, gripper actuators, and propulsion systems are the hardware embodiment of the active component of the Markov blanket.

6. In a quadruped robot, central pattern generators (CPGs) produce rhythmic gait patterns. From an Active Inference perspective, CPGs are:
A) Unnecessary for locomotion
B) Dynamical generative models that produce periodic proprioceptive predictions, with sensory feedback modulating the pattern to maintain stable locomotion
C) Static lookup tables of joint angles
D) Only found in biological systems

**Answer: B** -- CPGs generate expected joint trajectories as periodic attractors. Ground contact feedback provides prediction errors that modulate the timing and amplitude of the gait cycle, allowing the robot to adapt to terrain variations without replanning the entire gait.

7. Why is Active Inference particularly well-suited for soft robot control?
A) Soft robots do not need any control at all
B) Soft robots have complex, nonlinear dynamics that are difficult to model precisely, and Active Inference's probabilistic approach naturally handles this uncertainty through precision-weighted prediction errors
C) Active Inference only works with rigid robots
D) Soft robots have simpler dynamics than rigid robots

**Answer: B** -- Soft robots have continuum mechanics, hysteresis, and viscoelastic properties that resist precise analytical modeling. Active Inference's probabilistic framework treats this modeling uncertainty as low precision on dynamical predictions, naturally adapting control to the actual observed behavior.

8. The concept of "action as fulfilling proprioceptive predictions" means:
A) The robot predicts what actions it will take and then does something different
B) The motor system generates commands that drive the body to states predicted by the generative model -- the predicted joint angle becomes the desired joint angle
C) Proprioception is irrelevant to action
D) The robot only uses visual feedback for control

**Answer: B** -- In Active Inference, the generative model generates proprioceptive predictions (expected joint angles, expected forces). The motor system acts as a reflex arc that generates whatever commands are needed to make the actual proprioceptive state match the predicted one.

9. A drone maintaining hover in gusty wind uses Active Inference control. When a gust displaces the drone, what happens?
A) The drone remains displaced permanently
B) The predicted sensory state (hover position) diverges from the observed state, creating prediction error that drives corrective motor commands to restore the preferred position
C) The drone turns off its motors
D) The drone updates its preferred position to wherever the gust moved it

**Answer: B** -- The drone's generative model predicts (prefers) the hover position. Wind displacement creates proprioceptive and inertial prediction errors. The active inference process generates corrective thrust commands that minimize these errors, returning the drone to its intended position.

10. Impedance control -- regulating the relationship between force and displacement at the end-effector -- maps to Active Inference as:
A) A concept unrelated to Active Inference
B) Setting the precision (stiffness) of proprioceptive predictions, where high precision yields stiff behavior and low precision yields compliant behavior
C) Maximizing free energy
D) Removing all sensors from the robot

**Answer: B** -- In Active Inference, the precision of proprioceptive predictions determines how strongly the agent acts to enforce them. High precision on position predictions yields stiff, position-tracking behavior. Low precision allows observed positions to deviate from predictions, yielding compliant behavior.

## Part B: Short Answer and Design Prompts

1. Design an Active Inference controller for a robot arm that must insert a peg into a hole with tight tolerances. Describe how the generative model encodes the desired trajectory, how force feedback modifies actions during contact, and how precision weighting shifts between position control (free space) and force control (contact).

2. Compare how a traditional computed-torque controller and an Active Inference controller would handle a sudden 2 kg payload increase on a manipulator's end-effector. What are the expected transient behaviors and adaptation mechanisms?

3. A bipedal robot trips on an obstacle. Describe the cascade of prediction errors across the generative model hierarchy and the corrective actions at each level -- from ankle torque reflexes to balance recovery stepping to high-level path replanning.

4. How would Active Inference handle the transition between free-space reaching and contact-rich manipulation (e.g., wiping a surface)? Describe the required changes in the generative model's preferred sensory states and precision allocations.

5. A swarm of drones must collectively carry a large payload. Design the action component of each drone's Active Inference model, including how individual force contributions are coordinated to maintain the payload's position and orientation.
