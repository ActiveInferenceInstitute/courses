# Practice Quiz: Robotic Systems (Unit Overview)

## Part A: Multiple Choice

1. The Active Inference framework views a robot as:
A) A collection of independent components with no unifying principle
B) A system that maintains its functional coherence by minimizing variational free energy through continuous sensing and acting across its Markov blanket
C) A purely mechanical device with no information processing
D) An entity that maximizes entropy in its environment

**Answer: B** -- Active Inference provides a unified framework where the robot is understood as a system that persists by maintaining accurate predictions about its environment and acting to fulfill those predictions, with the Markov blanket defining the boundary between robot and world.

2. Which of the following correctly describes the relationship between the eight modules in the Active Inference spine?
A) They are completely independent topics with no interconnection
B) They form a linked sequence: Systems provide boundaries for Agents, which use Perception to feed Cognition, which drives Action, improved through Learning, coordinated through Communication, and directed by Planning
C) Only the first and last modules matter
D) They should be studied in random order

**Answer: B** -- The eight modules form an integrated cycle where each module builds on and feeds into the others. Understanding this interconnection is essential for grasping how robotic systems implement the full Active Inference perception-cognition-action loop.

3. A UR5 robot arm picking objects from a conveyor belt simultaneously involves which modules?
A) Only Action
B) Perception (detecting objects), Cognition (tracking object positions and deciding which to pick), Action (moving the arm and grasping), and Planning (sequencing picks for efficiency)
C) Only Systems and Communication
D) None of the modules apply to industrial robots

**Answer: B** -- Even a seemingly simple pick-and-place task engages multiple Active Inference modules simultaneously. The robot must perceive object positions, maintain cognitive state about which objects remain, plan optimal pick sequences, and execute precise actions.

4. In the robotic systems unit, the Markov blanket formalism is applied at which levels?
A) Only at the level of the entire robot
B) At multiple nested levels: individual sensors, software nodes, subsystems, the full robot, and even multi-robot teams
C) Only at the quantum level
D) Only at the social level

**Answer: B** -- The Markov blanket applies recursively. A single joint has a blanket (encoder sensing, motor acting). A ROS2 node has a blanket (subscriptions and publications). The full robot has a blanket (all sensors and actuators). This nested structure enables modular, hierarchical system design.

5. What makes Active Inference a unifying framework for robotics?
A) It uses the most expensive hardware
B) It provides a single objective function -- variational free energy minimization -- that encompasses perception (state estimation), action (control), learning (model updating), planning (policy evaluation), and communication (model alignment) as different aspects of the same optimization
C) It eliminates the need for engineering
D) It only applies to humanoid robots

**Answer: B** -- Rather than requiring separate theoretical frameworks for perception, control, planning, and learning, Active Inference derives all of these capabilities from a single principle: minimize the divergence between the agent's generative model and its sensory observations, through both belief updates and actions.

6. A robotic system that fails at the perception level will:
A) Still function perfectly at all other levels
B) Propagate errors to cognition (incorrect state estimates), action (responses to phantom states), planning (strategies based on false beliefs), and communication (sharing incorrect information)
C) Only affect the perception module
D) Automatically correct itself without any intervention

**Answer: B** -- The Active Inference modules are tightly coupled. Perceptual failures cascade through the system: if the robot misperceives an obstacle's location, its cognitive state is wrong, its planned path is inappropriate, its actions are misdirected, and any shared information with other agents is misleading.

7. The concept of "generative model" in robotic systems refers to:
A) A 3D printer that generates physical models
B) The internal model that predicts sensory observations given the robot's actions and the state of the world, encompassing dynamics, observation, and preference models
C) A marketing model for selling robots
D) The robot's physical appearance

**Answer: B** -- The generative model is the core computational structure in Active Inference: it encodes the robot's beliefs about how the world works (dynamics model), how world states produce observations (observation model), and what states the robot prefers (preference model).

8. Sensor fusion, motor control, SLAM, and task planning are traditionally treated as separate subfields in robotics. Active Inference unifies them by:
A) Ignoring their differences
B) Showing that each is a specific instance of free energy minimization operating on different components of the generative model at different temporal scales
C) Replacing them with a single algorithm that handles everything without specialization
D) Declaring them all obsolete

**Answer: B** -- Sensor fusion minimizes free energy with respect to hidden states (perception). Motor control minimizes free energy with respect to actions. SLAM simultaneously minimizes with respect to pose and map states. Task planning evaluates expected free energy over policy space. Each is a facet of the same objective.

9. The concept of robotic system "persistence" in Active Inference means:
A) The robot never runs out of battery
B) The robot continues to function as intended despite environmental variability by maintaining its generative model within viable bounds through perception and action
C) The robot is physically indestructible
D) The robot never stops moving

**Answer: B** -- A robot persists when it reliably achieves its task despite variation in object positions, lighting, terrain, and other environmental factors. This persistence emerges from the robot's ability to minimize free energy -- keeping its model calibrated and its actions effective across conditions.

10. Which real-world robotic platform best illustrates the full Active Inference spine?
A) A simple on/off switch
B) An autonomous mobile manipulator that senses its environment (perception), maintains situation awareness (cognition), moves and grasps (action), improves with experience (learning), coordinates with humans (communication), and sequences multi-step tasks (planning) -- all organized as a coherent system with well-defined Markov blankets
C) A passive thermometer
D) A fixed security camera

**Answer: B** -- An autonomous mobile manipulator engages all eight modules of the Active Inference spine in integrated operation. Its nested Markov blankets (navigation, manipulation, perception subsystems) form a coherent system that exemplifies the full framework.

## Part B: Short Answer and Design Prompts

1. Choose a specific robotic platform (e.g., Boston Dynamics Spot, a DJI agricultural drone, a Fetch mobile manipulator) and map its subsystems to the eight modules of the Active Inference spine. For each module, identify the specific hardware and software components that implement that function.

2. Describe a scenario where failures in three different modules (e.g., perception, planning, and communication) cascade to produce a system-level failure. How could an Active Inference approach detect and recover from such cascading failures?

3. Compare how a traditional sense-plan-act pipeline and an Active Inference architecture would handle a dynamic manipulation task where objects move unpredictably. What are the advantages of the unified free energy approach?

4. Design the system architecture for an Active Inference-based autonomous forklift. Define the nested Markov blankets, the generative model at each level, and the interfaces between subsystems. How do the eight modules manifest in this specific platform?

5. How does the Active Inference framework change the way we approach robotic system testing and validation? Compare testing a robot designed as a traditional control system versus testing one designed as an Active Inference agent.
