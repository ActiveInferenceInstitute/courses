# Practice Quiz: Learning in Robotic Systems

## Part A: Multiple Choice

1. In Active Inference, learning in a robotic system is best described as:
A) Downloading new software updates from the manufacturer
B) Updating the parameters of the generative model to reduce long-term prediction error -- changing the model itself, not just beliefs about current states
C) Memorizing a fixed set of sensor readings
D) Increasing the robot's processing speed

**Answer: B** -- Learning is distinct from perception (which updates beliefs about hidden states) in that it updates the parameters of the generative model itself. After learning, the robot has a structurally different model that makes better predictions about its body and environment.

2. A robot arm learns the mass of a new tool attached to its end-effector by observing the torques needed during several movements. This is an example of:
A) Perceptual inference (state estimation)
B) Parameter learning -- updating the robot's body model (proprioceptive generative model) based on accumulated prediction errors
C) Planning
D) Communication

**Answer: B** -- The robot starts with an inaccurate mass parameter in its dynamics model. Repeated movements produce systematic prediction errors (predicted torques differ from required torques). Over multiple trials, the mass parameter is updated to minimize these errors -- this is parameter learning.

3. The exploration-exploitation dilemma in robot learning is resolved in Active Inference by:
A) Always exploring and never exploiting
B) Always exploiting and never exploring
C) The expected free energy objective, which automatically balances epistemic value (information gain from exploration) with pragmatic value (task achievement from exploitation)
D) Flipping a coin to decide

**Answer: C** -- Expected free energy decomposes into epistemic and pragmatic terms. When model uncertainty is high, the epistemic term drives exploration. As the model improves, the pragmatic term dominates, shifting behavior toward task exploitation. This transition is automatic and principled.

4. Sim-to-real transfer in robot learning involves:
A) Moving a robot from one room to another
B) Training a generative model in simulation and deploying it on a physical robot, where the real world reveals model inaccuracies through prediction errors
C) Simulating that the robot has already learned
D) Transferring the robot's battery to a simulator

**Answer: B** -- Models trained in simulation often have systematic prediction errors when deployed on real hardware due to the reality gap (unmodeled friction, sensor noise, dynamic effects). Active Inference provides a natural framework for adapting the simulated model through real-world prediction error minimization.

5. What distinguishes structure learning from parameter learning in robotics?
A) There is no distinction
B) Parameter learning adjusts existing model weights, while structure learning changes the topology of the generative model -- adding new variables, states, or causal relationships
C) Structure learning is only relevant for buildings, not robots
D) Parameter learning requires more data than structure learning

**Answer: B** -- Parameter learning tunes existing model parameters (e.g., link masses, friction coefficients). Structure learning changes the model architecture itself -- for example, a robot discovering that an object in its workspace is articulated (has a joint) rather than rigid, requiring a new state variable in the generative model.

6. A mobile robot learns a navigation policy through repeated trials in a warehouse. After learning, what has changed in its Active Inference model?
A) Only the robot's hardware
B) The habit strengths (policy priors) in the generative model -- frequently successful policies acquire higher prior probability, making them more likely to be selected in similar future situations
C) The warehouse layout itself
D) The robot's serial number

**Answer: B** -- Through experience, the robot's prior beliefs about which policies are effective become more accurate. Policies that consistently led to low free energy acquire stronger priors, enabling faster and more reliable action selection in familiar contexts.

7. Curiosity-driven learning in a robot exploring a novel environment is explained by Active Inference as:
A) Random motion with no purpose
B) Seeking states with high expected information gain -- moving to locations where the robot's generative model is most uncertain, thereby maximally reducing model uncertainty per action
C) Avoiding all novel stimuli
D) Learning only from human demonstrations

**Answer: B** -- The epistemic component of expected free energy drives the robot toward states where its model is most uncertain. Observing these states provides maximum information gain, efficiently improving the generative model across the state space.

8. A robot learning to grasp objects of different shapes adapts its grasp strategy over time. In terms of the generative model, what is being updated?
A) Only the robot's color sensors
B) The mapping between observed object features (visual shape, estimated size) and the grasp parameters (finger positions, approach angle, grip force) that minimize expected free energy
C) The robot's serial communication protocol
D) The ambient room temperature model

**Answer: B** -- The robot learns a generative model that relates visual object features to the proprioceptive and tactile outcomes of different grasp strategies. Over trials, the model parameters are refined so that the robot can predict which grasp approach will succeed for each object category.

9. Why is learning rate (the speed of parameter updates) important in robotic Active Inference?
A) It only affects the robot's travel speed
B) Too fast and the model overfits to noise or recent experiences; too slow and the model fails to adapt to genuine changes -- the learning rate governs the balance between stability and plasticity
C) Learning rate is irrelevant in Active Inference
D) Higher learning rates always produce better results

**Answer: B** -- This is the stability-plasticity dilemma. In Active Inference, the learning rate corresponds to the relative precision assigned to new observations versus existing model parameters. High precision on new data yields fast but potentially unstable learning; low precision yields slow but robust learning.

10. Domain randomization in simulation-based robot training is analogous to which Active Inference concept?
A) Minimizing the complexity term of free energy -- the robot learns a model that is robust to parameter variation, implicitly encoding broad prior distributions over environmental conditions
B) Maximizing surprise
C) Eliminating all model parameters
D) Training on a single, perfectly accurate simulation

**Answer: A** -- Domain randomization exposes the learner to many variations of physics parameters, textures, and dynamics. The resulting model encodes broad priors, reducing complexity and improving generalization -- mirroring how free energy minimization penalizes overly specific models.

## Part B: Short Answer and Design Prompts

1. Design a learning curriculum for a robot arm that must learn to manipulate five different tool types (screwdriver, wrench, pliers, hammer, paintbrush). How would you structure the learning progression using Active Inference principles? What would the generative model learn at each stage?

2. A quadruped robot is deployed in a new environment with terrain types it has never encountered (e.g., ice, deep sand). Describe how Active Inference drives the robot to learn appropriate gait parameters for each terrain. What prediction errors drive the learning, and what parameters are updated?

3. Explain the difference between a robot that has learned to navigate a specific building and a robot that has learned to navigate buildings in general. How does the structure of the generative model differ, and what kind of learning produced each?

4. How could a team of robots share learned generative model parameters so that one robot's experience benefits others? Describe an Active Inference framework for multi-robot collaborative learning in a warehouse setting.

5. A robot's learned manipulation model suddenly produces high prediction errors after a mechanical component degrades (e.g., a joint develops increased friction). Describe how the robot would detect this change, distinguish it from environmental change, and adapt its model.
