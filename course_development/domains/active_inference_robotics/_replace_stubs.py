#!/usr/bin/env python3
"""Replace stub content in questions.md and lab.md files for the Active Inference Robotics course."""

import os

BASE = "/Users/4d/Documents/GitHub/courses/course_development/domains/active_inference_robotics"

SECTIONS = [
    "01_robotic_systems",
    "02_bio_inspired_design",
    "03_control_estimation",
    "04_autonomous_agents",
]

SUBMODULES = [
    "01_systems",
    "02_agents",
    "03_perception",
    "04_cognition",
    "05_action",
    "06_learning",
    "07_communication",
    "08_planning",
]

SPINE_LABELS = {
    "01_systems": "Systems",
    "02_agents": "Agents",
    "03_perception": "Perception",
    "04_cognition": "Cognition",
    "05_action": "Action",
    "06_learning": "Learning",
    "07_communication": "Communication",
    "08_planning": "Planning",
}

SECTION_LABELS = {
    "01_robotic_systems": "Robotic Systems",
    "02_bio_inspired_design": "Bio-Inspired Design",
    "03_control_estimation": "Control and Estimation",
    "04_autonomous_agents": "Autonomous Agents",
}

# ============================================================================
# QUESTIONS: 17 unique questions per (section, submodule) combination
# ============================================================================

# For each section + submodule pair, we generate questions that are:
# - Technically substantive
# - Reference real robots, tools, algorithms
# - Combine the section theme with the spine topic

QUESTIONS_DATA = {
    # ========================================================================
    # SECTION 1: ROBOTIC SYSTEMS
    # ========================================================================
    ("01_robotic_systems", "01_systems"): [
        "How does the Markov blanket of a UR5 industrial manipulator differ from that of a quadrotor drone? Identify the sensory and active states for each platform and explain how their physical form factors shape these boundaries.",
        "A ROS2-based mobile robot has separate nodes for lidar processing, odometry, path planning, and motor control. Explain how each node constitutes a nested system with its own Markov blanket, and describe the topic interfaces that connect them.",
        "Compare the system identification requirements for a differential-drive mobile robot versus a cable-driven parallel manipulator. How does the complexity of the generative model scale with the number of degrees of freedom?",
        "A warehouse robot must operate in environments ranging from -5C cold storage to 40C loading docks. How does temperature variation affect the system's Markov blanket (sensor drift, actuator performance) and what implications does this have for the generative model?",
        "Explain how the DDS (Data Distribution Service) Quality of Service policies in ROS2 (reliability, durability, deadline) formalize the information flow across Markov blanket boundaries in a robotic system.",
        "A humanoid robot has over 30 degrees of freedom. Discuss the engineering trade-offs between maintaining a single monolithic generative model versus decomposing the system into limb-level subsystems with separate Markov blankets.",
        "How does adding a force-torque sensor at a manipulator's wrist change the system's Markov blanket? What new sensory states become available, and how does this affect the accuracy-complexity trade-off in the generative model?",
        "Mars rovers like Curiosity operate with a 4-22 minute communication delay to Earth. How does this constraint affect the system architecture, and what does it imply about the rover's generative model depth and autonomy requirements?",
        "A soft robotic gripper has continuously deformable geometry rather than discrete joint states. How would you define the internal states and Markov blanket for a system whose physical boundary is itself compliant and variable?",
        "Compare the variational free energy implications of a robot using a 2D lidar (planar scan) versus a 3D lidar (point cloud). How does observation dimensionality affect the computational demands of free energy minimization?",
        "Explain how the concept of nested Markov blankets applies to a robotic surgery system like the da Vinci, where the surgeon, the teleoperator console, and the patient-side manipulator form a layered system.",
        "A swarm of 50 small ground robots must collectively map a disaster site. How do individual system boundaries compose into a collective system, and what role does communication play in defining the swarm's effective Markov blanket?",
        "How does the choice of onboard computing hardware (microcontroller vs. ARM SoC vs. GPU workstation) constrain the complexity of the generative model a robot can maintain in real time?",
        "Describe how system calibration (camera intrinsics, IMU biases, joint friction parameters) relates to setting the parameters of a robot's generative model. What happens to prediction error when calibration degrades over time?",
        "A legged robot transitions between walking on flat ground and climbing stairs. How does this environmental change require the robot to switch between different generative models, and what free energy signal triggers this switch?",
        "Explain how the concept of allostasis (maintaining viability across changing setpoints) applies to a robot that must manage its own battery level, thermal state, and task completion simultaneously.",
        "How would you design a system test that validates whether a robot's implemented architecture actually respects the Markov blanket boundaries specified in its design documents?",
    ],
    ("01_robotic_systems", "02_agents"): [
        "A Roomba vacuum cleaner and a Boston Dynamics Spot robot both navigate indoor environments. Compare their agency levels using Active Inference criteria: generative model depth, temporal horizon, and action repertoire.",
        "Explain how a robotic manipulator performing pick-and-place exhibits agency through expected free energy minimization. What constitutes its prior preferences, and how do these differ from a hardcoded waypoint sequence?",
        "How does morphological computation in a compliant robotic hand reduce the computational burden on the agent's generative model? Provide a concrete example involving grasping irregular objects.",
        "A self-driving car must decide between braking hard and swerving to avoid an obstacle. Frame this as an expected free energy evaluation over two policies, decomposing into pragmatic and epistemic components.",
        "Describe how a robotic agent's autonomy degrades when its communication link to a remote operator is lost. What minimal generative model must the robot maintain for safe autonomous operation?",
        "Compare reactive (subsumption architecture) and deliberative (STRIPS planning) agent architectures. How does Active Inference subsume both under a single framework with varying temporal depth?",
        "A surgical robot operates as a shared-autonomy agent where the surgeon retains high-level control. How do you define the agent boundaries when human and machine share the Markov blanket?",
        "How does the concept of epistemic foraging apply to a search-and-rescue robot that must decide whether to explore an unknown corridor or exploit a known path to a detected survivor?",
        "A robot arm in a collaborative assembly cell must infer the human worker's intent from observed motion. How does this intent inference fit into the Active Inference framework as hidden state estimation?",
        "Explain why a drone performing autonomous inspection of a wind turbine qualifies as a higher-agency system than a drone following GPS waypoints, even though both complete their tasks successfully.",
        "How does the precision (inverse variance) of sensory observations affect an agent's action selection? Give an example where a robot in fog must increase its reliance on proprioceptive versus visual observations.",
        "A multi-agent warehouse system assigns tasks to individual robots. Is the task allocator an agent? Discuss whether centralized coordination qualifies as agency under the Active Inference definition.",
        "Describe how a robot's generative model encodes preferences (desired observations) rather than explicit goal states. How does this differ from classical goal-directed planning in PDDL?",
        "A quadruped robot learning to walk on ice encounters unexpected slip. Trace the sequence: prediction error, belief update, policy re-evaluation, and action selection under Active Inference.",
        "How does the concept of a 'deep' generative model (hierarchical, with multiple temporal scales) relate to a robot's capacity for abstract reasoning about its task?",
        "Compare the agency of a thermostat, a PID-controlled robotic joint, and a full Active Inference agent controlling the same joint. What qualitative differences emerge at each level?",
        "A robot in a nuclear decommissioning scenario has severe constraints on the number of actions it can take (limited battery, radiation exposure). How does this action budget reshape its expected free energy landscape?",
    ],
    ("01_robotic_systems", "03_perception"): [
        "A mobile robot fuses lidar range data and wheel odometry for localization. Describe how Active Inference frames this sensor fusion as the combination of multiple likelihood functions within a single generative model.",
        "Explain the difference between passive perception (processing incoming sensor data) and active perception (moving the camera to reduce uncertainty). Provide a robotics example where active perception is essential.",
        "How does a Kalman filter relate to variational free energy minimization? Under what assumptions are the two approaches mathematically equivalent for robotic state estimation?",
        "A robot's lidar returns unexpected readings due to glass surfaces. Describe this scenario in terms of prediction error, and explain how the robot should update its generative model versus its beliefs about the environment.",
        "Compare the observation models for three sensor modalities on a mobile manipulator: 2D lidar (range-bearing), RGB camera (pixel intensity), and wrist force-torque sensor. How does each modality contribute differently to free energy minimization?",
        "How does sensor noise covariance (the R matrix in estimation theory) map to the concept of sensory precision in Active Inference? What happens to perception when a sensor degrades (increasing noise)?",
        "A drone uses visual odometry from a downward-facing camera for position estimation. In what flight conditions does this perception channel become unreliable, and how should the generative model's precision weighting adapt?",
        "Explain how SLAM (Simultaneous Localization and Mapping) can be cast as a perception problem under Active Inference, where both the robot's pose and the map are hidden states to be inferred.",
        "A robot detects an object that matches no template in its object recognition database. How does Active Inference handle this 'novel object' problem compared to a classical pattern-matching approach?",
        "Describe how attention mechanisms in biological vision relate to precision weighting in Active Inference. How could a robot implement selective attention to prioritize processing of task-relevant sensor data?",
        "A manipulator uses joint encoders and an external motion capture system. When these two perception channels disagree, how does the generative model resolve the conflict through precision-weighted prediction error minimization?",
        "How does the resolution and field of view of a lidar sensor affect the granularity of the robot's generative model? What is the relationship between sensor bandwidth and the temporal frequency of belief updates?",
        "A robot operating in a dusty construction site experiences gradual sensor degradation (lens fouling, lidar scattering). How can the robot detect this degradation through changes in its variational free energy?",
        "Compare top-down (model-driven) and bottom-up (data-driven) perception in robotics. How does Active Inference integrate both through the generative model's prior predictions and sensory likelihood?",
        "Explain how depth perception from a stereo camera pair involves an implicit generative model of 3D geometry. What are the hidden states, and what observations does each camera provide?",
        "A humanoid robot must perceive human facial expressions for social interaction. Discuss the challenges of building a generative model for social perception compared to geometric perception.",
        "How does the concept of perceptual inference at multiple hierarchical levels apply to a robot that processes raw pixels into features, features into objects, and objects into scene semantics?",
    ],
    ("01_robotic_systems", "04_cognition"): [
        "A robot maintaining a 3D occupancy grid of its environment performs continuous belief updates as new lidar scans arrive. Explain how this process is an instance of variational free energy minimization over a spatial generative model.",
        "Compare the computational requirements of belief propagation on a factor graph versus gradient-based variational inference for a mobile robot's localization problem. When would you choose each approach?",
        "How does a robot maintain beliefs about occluded objects (e.g., an item behind a shelf)? What role does the generative model's temporal dynamics play in propagating beliefs about hidden states?",
        "A robot operating at 100 Hz control frequency has limited CPU budget per cycle. Discuss the trade-off between generative model complexity and real-time performance, and how this trade-off relates to the free energy bound.",
        "Explain how a robot's cognitive architecture differs when using an onboard ARM processor versus offloading computation to a cloud GPU. What are the latency and reliability implications for the generative model?",
        "A manipulation robot must reason about the stability of a stack of objects it is building. What hidden states must the generative model track, and how does gravity impose constraints on the model's dynamics?",
        "How does the concept of cognitive load relate to variational free energy in robotic systems? When a robot encounters a highly novel environment, what happens to its free energy and computational demands?",
        "Describe how a task-level state machine (e.g., for assembly: locate part, grasp, align, insert) can be cast as a hierarchical generative model with discrete states at the top level and continuous states below.",
        "A service robot must track multiple humans moving through a room. How does the data association problem (which observation belongs to which person) fit into the Active Inference framework?",
        "Compare the generative models of a robot that uses a pre-built map (AMCL localization) versus one that builds a map on the fly (SLAM). How does the model complexity differ, and what are the free energy implications?",
        "How does a robot decide when its current generative model is insufficient and needs structural updating (model expansion)? What free energy signal indicates model inadequacy?",
        "A legged robot must reason about ground contact scheduling (gait patterns). Explain how discrete contact events interact with continuous body dynamics in a hybrid generative model.",
        "Discuss the role of working memory in robotic cognition. How does a robot's finite memory buffer for recent observations relate to the temporal depth of its generative model?",
        "An underwater robot operates in environments with no GPS and limited visual features. How must its cognitive architecture differ from a ground robot to maintain spatial awareness?",
        "Explain how a robot performing a long-horizon task (e.g., cooking a meal) maintains a plan representation that spans minutes while updating motor commands at millisecond timescales.",
        "How does the FPGA-based versus GPU-based computation affect the types of variational inference algorithms a robot can run in real time? Provide concrete latency comparisons.",
        "A robot encounters contradictory evidence: its map says a door is open but its camera sees a closed door. Describe the cognitive process of resolving this conflict through free energy minimization.",
    ],
    ("01_robotic_systems", "05_action"): [
        "Compare position control, velocity control, and impedance control for a manipulator arm. How does each control mode correspond to different forms of active inference with different precision structures?",
        "A robot must grasp an egg without breaking it. Explain how force control through Active Inference adjusts the precision of tactile predictions to achieve compliant grasping.",
        "How does the expected free energy decomposition (pragmatic + epistemic + risk) apply to a mobile robot choosing between a short path through a narrow gap and a longer path through open space?",
        "A quadrotor drone must maintain stable hover in gusty wind. Describe the action selection process as free energy minimization, identifying the prediction errors that drive motor commands.",
        "Explain how inverse kinematics can be framed as an inference problem under Active Inference: given a desired end-effector pose, infer the joint angles that minimize prediction error.",
        "Compare PID control and Active Inference control for a single revolute joint. Under what conditions do they produce equivalent behavior, and when does Active Inference provide advantages?",
        "A humanoid robot catches a thrown ball. Discuss the temporal constraints on action: how does the limited time window for interception affect the depth of the expected free energy evaluation?",
        "How do actuator limitations (torque saturation, bandwidth, backlash) constrain the set of policies available to an Active Inference agent? How should the generative model account for these limits?",
        "A cable-driven robot (like a tendon-driven hand) has coupled actuation where pulling one cable affects multiple joints. How does this coupling appear in the generative model's action-state mapping?",
        "Describe how a robot learns an impedance profile through interaction: starting stiff and gradually becoming compliant as its generative model of contact dynamics improves.",
        "A mobile robot navigating in a crowd must balance the pragmatic goal of reaching its destination with the risk of collision. How does expected free energy naturally encode safety constraints?",
        "Explain the relationship between a robot's action bandwidth (how fast it can change motor commands) and the temporal resolution of its generative model. What happens when these are mismatched?",
        "A surgical robot performing tissue retraction must apply precisely controlled forces. How does Active Inference handle the transition from free-space motion (position control) to contact (force control)?",
        "Compare open-loop trajectory execution with closed-loop Active Inference control. Under what conditions is open-loop execution acceptable, and what does this imply about the generative model's accuracy?",
        "How does a robot performing bimanual manipulation coordinate actions between its two arms? Describe the generative model that links the states and actions of both limbs.",
        "A legged robot must generate rhythmic walking patterns. Discuss whether Central Pattern Generators (CPGs) can be interpreted as a form of active inference with periodic prior preferences.",
        "Explain how a robotic gripper performing in-hand manipulation (rotating an object within the fingers) uses tactile prediction errors to drive fine motor adjustments.",
    ],
    ("01_robotic_systems", "06_learning"): [
        "A manipulator learns its own dynamics model from 100 random trajectories. Describe this system identification process as parameter learning in a generative model, specifying the prediction error that drives updates.",
        "Compare sim-to-real transfer with direct real-world learning for a quadruped robot learning to walk. How does each approach handle the accuracy-complexity trade-off in the generative model?",
        "How does domain randomization in simulation training relate to the Active Inference concept of learning robust generative models that minimize free energy across diverse conditions?",
        "A robot learns a visual grasping policy from demonstrations. Explain the difference between learning the generative model parameters (model-based) versus learning a direct policy mapping (model-free) from an Active Inference perspective.",
        "Describe the safety challenges of robotic learning: a robot exploring its joint limits could damage itself. How can prior preferences over observations encode safety constraints during learning?",
        "A mobile robot's odometry model degrades as its wheels wear. How does online adaptive learning detect and compensate for this gradual parameter drift?",
        "Compare Hebbian learning (correlation-based) with gradient-based learning (backpropagation) for updating a robot's sensory processing model. How does each relate to free energy gradient descent?",
        "A robot has learned to manipulate rigid objects but encounters a deformable object for the first time. How does structure learning (expanding the generative model) differ from parameter learning (adjusting existing weights)?",
        "Explain the exploration-exploitation trade-off in robotic learning through the epistemic and pragmatic components of expected free energy. How does a robot balance gathering information with achieving its task?",
        "How does the sample efficiency problem in robotics (real-world data is expensive) relate to the free energy principle's emphasis on using informative priors to constrain learning?",
        "A swarm of robots shares learned environment models with each other. Describe how this collective learning relates to distributed free energy minimization across a multi-agent system.",
        "Compare curriculum learning (progressively harder tasks) with random task presentation for a robot learning manipulation skills. How does task ordering affect the learning trajectory in generative model space?",
        "A robot's camera is replaced with a higher-resolution model. How must the perceptual learning process adapt the generative model's observation likelihood to the new sensor characteristics?",
        "Describe how meta-learning ('learning to learn') applies to a robot that must quickly adapt to new objects. What structural properties of the generative model enable fast few-shot adaptation?",
        "How does catastrophic forgetting affect a robot that learns new skills? Explain how Bayesian model updating through free energy minimization naturally mitigates forgetting through posterior preservation.",
        "A robot learns a reward function from human demonstrations (inverse reinforcement learning). How does this relate to learning prior preferences in the Active Inference framework?",
        "Compare the learning dynamics of a robot trained entirely in simulation versus one that fine-tunes a simulated model with real-world data. What free energy signals indicate when the sim model is insufficient?",
    ],
    ("01_robotic_systems", "07_communication"): [
        "Explain how ROS2 topics, services, and actions map to different types of communication across Markov blanket boundaries. Which communication pattern is appropriate for continuous sensor streams versus discrete task commands?",
        "A team of three robots must coordinate to transport a large object. How does communication enable the alignment of their generative models about the shared object state?",
        "Compare the communication requirements of a teleoperated robot (low autonomy, high bandwidth) versus a fully autonomous robot (high autonomy, low bandwidth). How does autonomy trade off against communication needs?",
        "How does DDS (Data Distribution Service) quality of service in ROS2 formalize the reliability and latency requirements of communication channels between robotic subsystems?",
        "A human operator provides verbal commands to a robot ('pick up the red cup'). Describe the chain of inference the robot must perform to ground this natural language command in its generative model.",
        "Explain how a robot performing shared workspace collaboration with a human uses implicit communication (observing human motion) to infer intent. How does this relate to Active Inference's generative model of other agents?",
        "A fleet of delivery robots communicates through a central server. What are the implications of server failure for the collective Markov blanket of the fleet?",
        "How does communication latency affect a robot's effective temporal horizon for planning? Give an example where delayed communication degrades coordinated behavior.",
        "A drone swarm uses only local peer-to-peer communication (no central coordinator). How does local information exchange lead to emergent collective behavior, and how does Active Inference frame this as distributed free energy minimization?",
        "Compare the information content of different robot-to-human communication modalities: visual displays, audio alerts, haptic feedback, and motion-based gestures. How does each modality affect the human's generative model of the robot's state?",
        "A robot must communicate uncertainty about its task progress to a human supervisor. What representation of uncertainty is most useful: confidence intervals, probability distributions, or simple traffic-light indicators?",
        "How does communication bandwidth limit the complexity of shared generative models in multi-robot systems? What compression strategies can robots use to communicate essential belief states efficiently?",
        "A manipulation robot and a mobile base must coordinate handoffs. Describe the communication protocol needed and how it ensures that both agents' generative models are synchronized at the handoff moment.",
        "Explain how semantic communication (transmitting meaning rather than raw data) relates to Active Inference's concept of generative model alignment between communicating agents.",
        "A robot operating in a GPS-denied environment receives position updates from a remote beacon. How does intermittent communication affect the robot's belief uncertainty and planning horizon?",
        "Compare centralized versus decentralized communication architectures for a team of exploration robots. How does the architecture choice affect collective free energy minimization?",
        "A robot must explain its decision-making to a non-technical human operator. How does generating an explanation relate to constructing a simplified generative model that the human can understand?",
    ],
    ("01_robotic_systems", "08_planning"): [
        "Compare RRT (Rapidly-exploring Random Tree) and A* search as planning algorithms. How does each explore the robot's configuration space, and how would an Active Inference approach evaluate trajectories differently?",
        "A robot must plan a manipulation sequence to assemble furniture from parts. Explain how task planning (symbolic) and motion planning (geometric) interact in a hierarchical generative model.",
        "How does the expected free energy decomposition into pragmatic, epistemic, and risk components map to real-world planning trade-offs for a mobile robot navigating an office?",
        "A drone planning an inspection route for a solar farm must balance coverage completeness with battery life. Frame this as an expected free energy optimization and identify the competing terms.",
        "Explain how planning depth (number of future timesteps considered) is constrained by computational budget in a real-time robotic system. How does Active Inference handle the tension between optimal and real-time planning?",
        "A robot plans a path through a dynamic environment where humans are walking. How does the generative model predict human motion, and how does uncertainty about future human positions affect the plan?",
        "Compare model-predictive control (MPC) with Active Inference planning. What are the structural similarities and differences in how they evaluate future action sequences?",
        "A legged robot must plan foothold placements on rough terrain. How does this discrete-continuous planning problem fit within the expected free energy framework?",
        "Explain how active perception planning (choosing where to look) and task execution planning can be unified under a single expected free energy objective.",
        "A warehouse robot must plan routes for 20 sequential pick-and-place tasks. How does the planning complexity scale, and what heuristics can reduce the computational burden while preserving solution quality?",
        "How does a robot replan when its current plan becomes infeasible (e.g., a door it planned to traverse is now locked)? Describe the free energy signal that triggers replanning.",
        "A manipulator planning a grasp must consider both the geometry of approach and the expected forces during contact. How does the generative model integrate kinematic and dynamic planning?",
        "Compare the planning capabilities of a robot with a 1-second lookahead versus a 10-second lookahead. What qualitative behavioral differences emerge from different temporal horizons?",
        "A search-and-rescue robot must plan under extreme uncertainty about the building layout. How does epistemic planning (information gathering) dominate over pragmatic planning (goal reaching) in early exploration?",
        "Explain how contingency planning (planning for multiple possible outcomes) is naturally encoded in the expected free energy framework through the evaluation of policies under model uncertainty.",
        "A multi-robot team must coordinate their plans to avoid conflicts (e.g., two robots trying to use the same narrow corridor). How does shared planning relate to the alignment of generative models?",
        "How does the concept of planning as inference (interpreting plans as posterior distributions over trajectories) change the way we think about robotic motion planning compared to classical optimization?",
    ],
    # ========================================================================
    # SECTION 2: BIO-INSPIRED DESIGN
    # ========================================================================
    ("02_bio_inspired_design", "01_systems"): [
        "Compare the Markov blanket of a biological organism (e.g., a honeybee) with that of a biomimetic drone. How do the sensory and active boundaries differ between biological and engineered systems?",
        "How do biological scaling laws (strength scales with cross-section, weight scales with volume) constrain the design of bio-inspired robotic systems at different sizes?",
        "An octopus distributes neural processing across its arms. How would you design a robot with distributed computation inspired by this architecture, and what are the Markov blanket implications?",
        "Compare centralized (mammalian brain) versus decentralized (insect ganglia) nervous system architectures for robotic control. How does each affect the generative model structure?",
        "How does the concept of homeostasis in biological systems translate to robotic system design? Give an example of a bio-inspired robot that maintains functional coherence through environmental variation.",
        "A gecko can climb vertical glass surfaces using van der Waals forces. How would you define the Markov blanket of a climbing robot inspired by gecko adhesion, especially at the foot-surface interface?",
        "Biological organisms evolve their body plans over generations. How does evolutionary optimization relate to the Active Inference principle that systems persist by minimizing surprise?",
        "Compare the sensory bandwidth of biological systems (e.g., compound eyes processing 200 frames/sec) with equivalent robotic sensors. What design lessons does biology offer for sensor placement and density?",
        "How does the concept of umwelt (species-specific perceptual world) from biology inform the design of task-specific robotic generative models?",
        "A biological fish uses its lateral line organ to sense water flow. Design a bio-inspired sensory system for an underwater robot and specify its role in the Markov blanket.",
        "Explain how modularity in biological body plans (segments in arthropods, vertebrae in mammals) inspires modular robotic design with nested Markov blankets.",
        "How does the energy efficiency of biological locomotion (e.g., running cockroach) compare to current robotic locomotion? What bio-inspired principles could reduce a robot's energy consumption?",
        "A plant exhibits tropism (growing toward light). Can a slowly actuated system like a plant-inspired robot be understood through Active Inference? What is its temporal scale?",
        "Compare the redundancy strategies of biological organisms (duplicate organs, distributed sensors) with robotic fault-tolerance approaches. How does redundancy affect the free energy landscape?",
        "How does the principle of morphological computation (body shape contributing to computation) apply to a snake robot whose locomotion gaits emerge from body-environment interaction?",
        "A biological immune system identifies and responds to novel pathogens. How might this inspire an anomaly detection and response system in a robotic platform?",
        "Discuss how the allometric scaling of brain size to body size in biology might inform the sizing of computational resources for robots of different scales.",
    ],
    ("02_bio_inspired_design", "02_agents"): [
        "Compare the agency of an ant (simple individual, complex colony behavior) with a single autonomous drone in a swarm. How does individual generative model simplicity enable collective intelligence?",
        "How does the concept of affordances (action possibilities offered by the environment) from ecological psychology apply to bio-inspired robotic agents?",
        "A predator-prey relationship involves two agents each trying to minimize their own free energy. Model a pursuit-evasion scenario between a robotic predator and prey using Active Inference.",
        "Biological agents exhibit habituation (reduced response to repeated stimuli). How would you implement habituation in a robotic agent's generative model, and what computational benefit does it provide?",
        "Compare the agency of a social insect (ant following pheromone trails) with a solitary predator (cat stalking prey). How do their generative models differ in depth and social complexity?",
        "A cuttlefish rapidly changes its body color for camouflage and communication. Design a bio-inspired robot that uses active camouflage, and explain how color change constitutes an active state in the Markov blanket.",
        "How does the concept of niche construction (organisms modifying their environment) relate to robotic agents that reshape their workspace to reduce future free energy?",
        "A biological agent's motivational states (hunger, fear, curiosity) drive behavior selection. How do these map to prior preferences and precision weighting in an Active Inference robotic agent?",
        "Compare the reactive escape behaviors of insects (triggered by specific stimuli) with the deliberative escape planning of mammals. How do these represent different generative model depths?",
        "How does embodied cognition (intelligence arising from body-environment interaction) challenge the traditional sense-plan-act paradigm in robotics?",
        "A spider builds a web that extends its sensory capabilities. How does this external structure change the spider's effective Markov blanket, and what robotics analog exists?",
        "Biological agents use internal clocks (circadian rhythms) to anticipate environmental changes. Design a robot that uses temporal prediction to pre-emptively adjust its behavior.",
        "Compare the learning speed of biological agents (a cat learns to hunt in weeks) with current robot learning (thousands of simulated episodes). What biological mechanisms enable faster learning?",
        "How does the concept of autopoiesis (self-producing systems) from biology relate to the Active Inference definition of agency in robotic systems?",
        "A parasitic organism manipulates its host's behavior. How does this multi-agent scenario, where one agent's actions modify another's generative model, inform adversarial robotics?",
        "Biological agents exhibit play behavior (exploration without immediate reward). How does play relate to epistemic foraging in Active Inference, and how could a robot benefit from play?",
        "Compare the agency spectrum from virus (minimal agency, environmental exploitation) to primate (high agency, tool use). Where do current robots fall on this spectrum, and what capabilities would move them higher?",
    ],
    ("02_bio_inspired_design", "03_perception"): [
        "A barn owl localizes prey by sound alone using interaural time and level differences. Design a bio-inspired acoustic localization system for a robot and specify its generative model.",
        "How does the fovea-periphery organization of the primate visual system inspire robotic camera systems with variable resolution? What are the Active Inference implications for attention and saccades?",
        "Bats use echolocation with frequency-modulated chirps. Compare this active sensing strategy with a robot using ultrasonic range sensors. How does the transmitted signal design affect the generative model?",
        "Biological vision adapts to light levels over 10 orders of magnitude. How should a robot's visual generative model handle dynamic range, and what bio-inspired mechanisms could help?",
        "Compare the predictive coding model of biological perception (top-down predictions matched against bottom-up signals) with a robot's sensor fusion pipeline. Where are the parallels strongest?",
        "A pit viper senses infrared radiation to detect warm-blooded prey. Design a multi-spectral perception system for a robot that combines visible and thermal cameras, specifying the generative model for each modality.",
        "How does biological proprioception (muscle spindles, Golgi tendon organs) compare to robotic joint sensing (encoders, strain gauges)? What information does biology capture that typical robots miss?",
        "The vestibular system provides biological organisms with gravity and acceleration sensing. How should an IMU-based perception system be designed to mimic this, and what generative model structure is appropriate?",
        "Insect compound eyes provide wide field of view with motion sensitivity. Design a bio-inspired perception system for a micro aerial vehicle using an array of low-resolution cameras.",
        "How does the concept of perceptual constancy (recognizing objects despite viewpoint changes) from biological vision apply to robotic object recognition? What generative model properties enable constancy?",
        "A star-nosed mole uses 22 tactile appendages to identify objects at extraordinary speed. How does this parallel tactile perception system inspire multi-finger robotic manipulation sensing?",
        "Biological organisms habituate to constant stimuli (e.g., ignoring background noise). How could a robot implement sensory habituation to reduce processing load, and what free energy principle underlies this?",
        "Compare the temporal resolution of biological perception (visual: ~50ms, auditory: ~1ms, tactile: ~10ms) with robotic sensor rates. How do these timescales affect the generative model's temporal structure?",
        "How does the McGurk effect (visual information altering auditory perception) in biology relate to multi-modal sensor fusion in robotics? What does it reveal about the generative model's cross-modal structure?",
        "A mantis shrimp perceives 16 color channels (versus 3 in humans). How would additional spectral channels in a robot's camera affect the dimensionality and informativeness of its observation model?",
        "Biological organisms perform gist perception (rapid scene categorization in ~100ms). Design a robotic fast scene classification system and describe its role in the hierarchical generative model.",
        "How does biological sensory adaptation (e.g., adjusting pupil size, gain control in neurons) inspire adaptive sensor management in robots operating in variable environments?",
    ],
    ("02_bio_inspired_design", "04_cognition"): [
        "Compare the hippocampal place cell system in mammals with SLAM algorithms in robots. How does the biological spatial memory system inspire more efficient robotic mapping?",
        "How does the prefrontal cortex's role in working memory and executive function inspire the design of cognitive architectures for robot task management?",
        "Biological cognitive maps represent not just spatial layout but also reward distributions and danger zones. How should a robot's generative model incorporate valence alongside geometry?",
        "Compare the speed-accuracy trade-off in biological decision making (fast heuristic vs. slow deliberate) with anytime planning algorithms in robotics.",
        "How does the cerebellum's role in forward models (predicting sensory consequences of motor commands) relate to the generative model in Active Inference robotic control?",
        "A crow uses tools to extract food. How does tool-use cognition (representing the tool as extending the body's action space) translate to a robot that must reason about grasped tools?",
        "Biological memory consolidation transfers information from hippocampus to cortex during sleep. How could a robot implement offline model consolidation to improve its generative model?",
        "Compare episodic memory (specific past events) and semantic memory (general knowledge) in biology. How should a robot's generative model represent both types of information?",
        "How does the biological concept of mental simulation (imagining future scenarios) relate to model-based planning in Active Inference? What neural substrates perform this simulation?",
        "A bird caching food must remember hundreds of hiding locations. How does this biological memory feat inspire efficient spatial memory systems in robots with limited onboard storage?",
        "Compare the cognitive flexibility of primates (adapting to novel tool configurations) with the brittleness of current robotic manipulation systems. What generative model properties enable flexibility?",
        "How does the mirror neuron system (understanding others' actions by simulating them internally) inform robotic understanding of human demonstrations through internal generative model replay?",
        "Biological organisms exhibit counterfactual reasoning ('what would happen if...'). How does this relate to policy evaluation in Active Inference, where the robot evaluates alternative action sequences?",
        "A dog learns which actions produce treats through classical and operant conditioning. How do these learning mechanisms map to updating prior preferences and model parameters in Active Inference?",
        "Compare the modularity of biological cognition (specialized brain regions for faces, language, spatial reasoning) with modular robotic cognitive architectures. Is specialization always beneficial?",
        "How does the concept of attention from neuroscience (selective enhancement of relevant information) map to precision weighting in a robot's hierarchical generative model?",
        "Biological organisms dream (neural replay during REM sleep). Could a robot benefit from 'dreaming' -- running its generative model forward without sensory input to consolidate learning?",
    ],
    ("02_bio_inspired_design", "05_action"): [
        "Compare muscle-tendon actuators in biological systems with electric motors in robots. How does the compliance and energy storage of biological actuators affect the generative model of action?",
        "A cheetah transitions between walking, trotting, and galloping gaits. How do discrete gait transitions emerge from continuous dynamics, and how should a legged robot's generative model represent this?",
        "How does the stretch reflex arc (monosynaptic spinal reflex) inspire low-latency reactive control in robotic systems? What is the relationship to Active Inference at different hierarchical levels?",
        "A bird adjusts its wing shape in real time during flight. Design a morphing-wing drone inspired by this, and describe how the action space includes both thrust and shape change.",
        "Compare the force-velocity characteristics of biological muscles with electric motors. How do these differences affect the generative model's prediction of action outcomes?",
        "An octopus coordinates 8 arms with effectively infinite degrees of freedom. How do biological organisms reduce this action space to manageable dimensions, and what lessons apply to hyper-redundant robots?",
        "How does Central Pattern Generator (CPG) theory from neuroscience inspire rhythmic locomotion controllers for legged and swimming robots? Can CPGs be cast as active inference?",
        "A human catching a ball performs rapid predictive reaching. How does the biological motor system generate this action before sensory feedback about the ball's trajectory is complete?",
        "Compare the energy efficiency of biological swimming (fish undulation) with robotic propulsion (propellers, thrusters). What bio-inspired actuation could improve underwater robot efficiency?",
        "How does the concept of motor primitives (building blocks of movement) from motor neuroscience relate to action libraries in robotic manipulation?",
        "A chameleon extends its tongue at 40 m/s to catch prey. What principles of elastic energy storage and release could improve the peak performance of robotic actuators?",
        "Biological organisms exhibit anticipatory postural adjustments before voluntary movement. How should a humanoid robot's control system implement similar anticipatory stabilization?",
        "Compare the parallel elastic actuation in biological joints (muscles + tendons + ligaments) with Series Elastic Actuators (SEAs) in robotics. How does compliance affect the free energy of action?",
        "How does the principle of minimum intervention (only correcting deviations that matter for the task) from biological motor control apply to Active Inference action selection in robots?",
        "A jumping spider calculates its leap trajectory before jumping. How does this pre-computed ballistic action relate to open-loop planning in Active Inference for fast robotic actions?",
        "Biological organisms exhibit motor babbling during development (random movements that learn body dynamics). How does this relate to exploration in the active inference framework for robot learning?",
        "Compare the dexterity of a human hand (27 degrees of freedom, rich tactile sensing) with robotic grippers. What bio-inspired design principles could bridge the dexterity gap?",
    ],
    ("02_bio_inspired_design", "06_learning"): [
        "Compare Hebbian learning ('neurons that fire together wire together') with backpropagation-based learning in neural networks. Which is more biologically plausible, and how does each relate to free energy minimization?",
        "How does synaptic plasticity (LTP and LTD) in biological neural networks inspire online learning algorithms for robotic generative models?",
        "A young animal learns to walk within hours of birth. What developmental learning mechanisms enable this rapid motor acquisition, and how could they accelerate robot learning?",
        "Compare one-shot learning in biological systems (a child learns 'giraffe' from one example) with the data-hungry learning of current robot vision systems. What structural priors enable biological efficiency?",
        "How does the reward prediction error signal in dopamine neurons relate to the prediction error in Active Inference? Are these the same computational quantity?",
        "A biological organism generalizes learned skills across contexts (e.g., grasping works for cups and bottles). How does this transfer learning relate to the structure of the generative model?",
        "Compare the role of sleep in biological memory consolidation with offline training in robotic learning. Could a robot implement a 'sleep' phase to improve its generative model?",
        "How does imitation learning in biological systems (mirror neurons, social learning) differ from learning from demonstration in robotics? What Active Inference account unifies them?",
        "A biological organism learns to avoid danger through negative reinforcement. How do aversive experiences update the prior preferences in an Active Inference generative model?",
        "Compare the developmental stages of biological motor learning (reflexes, babbling, coordinated movement, skilled performance) with staged robot learning curricula.",
        "How does neuromodulation (dopamine, serotonin, norepinephrine) affect learning rates and exploration in biological systems? What robotic analog could implement adaptive learning rate control?",
        "A biological organism exhibits savings (faster relearning of previously learned skills). How does this relate to the preservation of generative model structure even when parameters are forgotten?",
        "Compare associative learning (Pavlovian conditioning) with causal learning (understanding mechanisms). How do these different learning types produce different generative model structures?",
        "How does the critical period hypothesis (optimal windows for learning specific skills) from developmental biology inform the scheduling of learning phases in robotic training?",
        "A bird learning its species' song goes through a babbling phase followed by crystallization. Design a robot learning paradigm inspired by this two-phase developmental process.",
        "Compare the brain's ability to learn continuously without catastrophic forgetting with neural network challenges in continual learning. What biological mechanisms protect old memories?",
        "How does curiosity-driven exploration in biological organisms (novelty seeking, play) relate to the epistemic component of expected free energy in Active Inference?",
    ],
    ("02_bio_inspired_design", "07_communication"): [
        "Compare pheromone-based communication in ant colonies with stigmergic communication in robot swarms (leaving digital markers in the environment). How does each implement distributed generative model alignment?",
        "How does the waggle dance of honeybees (communicating food source location) inspire information sharing protocols in multi-robot foraging systems?",
        "A flock of birds maintains formation through local communication (each bird responding to nearest neighbors). How does this local coupling achieve global coordination, and what is the equivalent in robot swarms?",
        "Compare vocal communication in primates (rich semantics, learned) with simple signal communication in insects (fixed repertoire). How does communication complexity correlate with generative model depth?",
        "How do alarm calls in biological groups (vervet monkey alarm calls distinguish predator types) inspire threat classification and communication in multi-robot security systems?",
        "A school of fish changes direction simultaneously through pressure wave sensing. Design a robot swarm communication system inspired by this hydrodynamic signaling mechanism.",
        "Compare the bandwidth and latency of biological communication channels (chemical: slow/persistent, visual: fast/directional, auditory: fast/omnidirectional) with robotic equivalents.",
        "How does the concept of honest signaling from evolutionary biology (costly signals that reliably indicate quality) apply to trust and reliability in multi-robot communication?",
        "A symbiotic relationship (e.g., clownfish and anemone) involves two species communicating to mutual benefit. How does this model inter-species communication inspire heterogeneous robot team coordination?",
        "Biological organisms use body language and posture to communicate emotional states. How could a robot use its posture and movement dynamics to communicate its internal state to human collaborators?",
        "Compare the decentralized decision-making of ant colonies (emergent consensus through local interactions) with centralized robot task allocation. Under what conditions is each approach superior?",
        "How does the cocktail party problem (isolating one voice among many) from auditory neuroscience apply to a robot processing multiple simultaneous communication channels in a noisy environment?",
        "A wolf pack uses coordinated hunting strategies communicated through body position and gaze direction. Design a multi-robot hunting/herding strategy using similar implicit communication.",
        "Compare quorum sensing in bacteria (population-density-dependent gene expression) with threshold-based activation in robot swarms. How do both achieve population-level decision making?",
        "How does the concept of teaching in biological systems (a mother cat teaching kittens to hunt) inform the design of robot-to-robot skill transfer protocols?",
        "Biological organisms use deceptive communication (e.g., fireflies mimicking other species' signals). How should a robot's communication protocol account for potentially deceptive or corrupted messages?",
        "Compare the role of shared attention (two agents attending to the same object) in human-animal interaction with joint attention in human-robot interaction. How does shared attention align generative models?",
    ],
    ("02_bio_inspired_design", "08_planning"): [
        "Compare the navigation planning of a desert ant (path integration using polarized light) with GPS-based robot navigation. How does the ant's minimal computation achieve reliable homing?",
        "A squirrel plans cache locations for winter food storage months in advance. How does this long-horizon planning under uncertainty relate to Active Inference's expected free energy over extended time horizons?",
        "How does the concept of optimal foraging theory (biological organisms maximize energy gain per unit time) relate to planning in Active Inference for resource-gathering robots?",
        "Compare the territorial patrol patterns of biological organisms with coverage planning algorithms for surveillance robots. What bio-inspired heuristics improve coverage efficiency?",
        "A predator plans an ambush by predicting prey movement patterns. How does predictive modeling of other agents' behavior fit into the Active Inference planning framework?",
        "How do biological organisms plan routes through complex 3D environments (birds navigating through forests, fish through coral reefs)? What spatial representations enable this, and how do they map to robot planning?",
        "Compare the planning horizon of an insect (seconds) with that of a primate (months to years). How does brain size and structure constrain planning depth, and what parallels exist in robotic systems?",
        "A beaver builds a dam that reshapes its environment to reduce future survival uncertainty. How does this niche construction planning relate to Active Inference's concept of acting to minimize long-term free energy?",
        "How does the concept of satisficing (choosing a 'good enough' option rather than optimal) from behavioral biology apply to real-time robot planning under computational constraints?",
        "Compare migratory route planning in birds (innate + learned, adapted to conditions) with adaptive route planning in long-range autonomous vehicles.",
        "A mother bird plans a feeding schedule across multiple chicks. How does this resource allocation planning under competing demands relate to multi-objective planning in robotics?",
        "How does the concept of cognitive maps (Tolman's spatial representations in rats) relate to occupancy grids and topological maps used in robot navigation planning?",
        "Compare the planning strategies of solitary versus social foragers. How does group planning (coordinated search) outperform individual planning, and what does this imply for multi-robot systems?",
        "A biological organism uses landmarks for navigation planning. How does landmark-based planning in animals inspire visual place recognition in robot localization and planning?",
        "How does the concept of risk sensitivity from behavioral ecology (organisms prefer certain outcomes over uncertain ones of equal expected value) relate to the risk term in expected free energy?",
        "Compare the nest-building planning of different species (termites: decentralized, birds: individual craft). How does the planning architecture affect the resulting structure's complexity?",
        "A biological organism exhibits contingency planning (e.g., creating escape routes before exploring). How does maintaining multiple planned options relate to policy evaluation in Active Inference?",
    ],
    # ========================================================================
    # SECTION 3: CONTROL AND ESTIMATION
    # ========================================================================
    ("03_control_estimation", "01_systems"): [
        "Compare the state-space representation of a 2-DOF planar robot arm with that of a differential-drive mobile robot. How do the state dimensions and nonlinearities differ?",
        "How does the concept of observability from control theory (can all states be estimated from outputs?) relate to the informativeness of a robot's Markov blanket sensory states?",
        "A robot arm has 6 joints but only a wrist-mounted force sensor and joint encoders. Analyze the observability of end-effector contact forces. What additional sensors would make the system fully observable?",
        "Compare open-loop and closed-loop system architectures for a quadrotor drone. How does closing the loop with IMU feedback change the system's stability properties?",
        "How does the concept of controllability from control theory (can all states be driven to desired values?) relate to a robot's capacity for active inference through its actuators?",
        "A soft robot has infinite-dimensional state space (continuous deformation) but finite-dimensional actuation. How does this underactuation affect the system's controllability and estimation requirements?",
        "Compare the linearized system models used near operating points with nonlinear models required for large deviations. How does the operating regime affect control and estimation accuracy?",
        "How does discretization of continuous dynamics (zero-order hold, Runge-Kutta) affect the accuracy of a robot's state-space model? What sampling rate is needed for a given system bandwidth?",
        "A robot system has both fast dynamics (motor current loops at 10 kHz) and slow dynamics (arm motion at 100 Hz). How does time-scale separation simplify the system architecture?",
        "Compare the transfer function and state-space representations of a single robot joint. When is each representation more useful for control design and estimation?",
        "How does adding a flexible link (rather than a rigid one) to a robot arm change the system's state dimension and eigenstructure? What new modes must be estimated and controlled?",
        "A mobile robot has nonholonomic constraints (cannot move sideways). How do these constraints affect the system's state-space model and reachable set?",
        "Compare the system architectures of a position-controlled robot and a torque-controlled robot. How does the inner control loop's presence affect the outer loop's design?",
        "How does the condition number of a robot's Jacobian matrix relate to the system's sensitivity to perturbations near singular configurations?",
        "A cable-driven robot has complex tendon routing that couples multiple joints. How does this coupling appear in the system matrices, and what challenges does it create for estimation?",
        "Compare the system stability properties of a wheeled robot (marginally stable heading) with a bipedal robot (unstable balance). How does inherent stability affect control architecture requirements?",
        "How does model uncertainty (unknown mass, friction, compliance) affect the reliability of state-space-based control and estimation? What robust control approaches address this?",
    ],
    ("03_control_estimation", "02_agents"): [
        "Compare PID control and Linear Quadratic Regulator (LQR) design for a robotic joint. How do these classical agents differ in their implicit models of the system?",
        "How does the separation principle (design estimator and controller independently) from linear control theory relate to the Active Inference framework where perception and action are unified?",
        "A Kalman filter estimates a robot's state while a PID controller drives it to a target. Describe how replacing this dual-agent architecture with Active Inference unifies estimation and control.",
        "Compare the gain-scheduling approach (switching PID gains based on operating point) with an Active Inference agent that naturally adapts its precision weighting. Which is more robust to nonlinear dynamics?",
        "How does the concept of the certainty equivalence principle (act as if the estimate is certain) compare to Active Inference's explicit treatment of uncertainty in action selection?",
        "A robot manipulator uses a computed torque controller that requires an accurate dynamics model. How does model error propagate into control error, and how does Active Inference handle this differently?",
        "Compare a classical cascade control architecture (inner velocity loop, outer position loop) with a hierarchical Active Inference agent. How do the timescales of inference correspond to control loop rates?",
        "How does the concept of robust control (H-infinity design) relate to minimizing worst-case free energy across model uncertainties?",
        "A teleoperated robot has a human operator in the control loop. How do you model this human-in-the-loop system as an agent where both human and machine contribute to state estimation and control?",
        "Compare Model Reference Adaptive Control (MRAC) with Active Inference as approaches to controlling a robot with unknown parameters. What are the convergence guarantees of each?",
        "A mobile robot uses a navigation stack with separate localization, path planning, and trajectory tracking agents. How does this modular agent architecture compare to a monolithic Active Inference agent?",
        "How does the concept of internal model control (embedding a model of the plant in the controller) relate to the generative model in Active Inference?",
        "A robot arm must track a moving target while compensating for gravity. How does a feedforward gravity compensation term combine with feedback control, and how does Active Inference subsume both?",
        "Compare the agent architectures of a classical autopilot (PID loops for attitude, altitude, heading) with an Active Inference flight controller for a quadrotor.",
        "How does the concept of anti-windup (preventing integrator saturation) in PID control relate to the treatment of actuator constraints in Active Inference action selection?",
        "A visual servoing system uses image features directly in its control loop. How does this visual agent differ from a position-based agent that first estimates Cartesian pose?",
        "Compare the stability guarantees of Lyapunov-based control design with the free energy minimization criterion in Active Inference. Under what conditions do they provide equivalent stability?",
    ],
    ("03_control_estimation", "03_perception"): [
        "Derive the Kalman filter update equations and explain how they minimize the estimation error covariance. How does this relate to variational free energy minimization?",
        "Compare the Extended Kalman Filter (EKF) and Unscented Kalman Filter (UKF) for estimating the pose of a mobile robot. When does the UKF's sigma-point approach outperform the EKF's linearization?",
        "How does a particle filter handle multi-modal probability distributions that Kalman filters cannot represent? Give a robotic localization example where multi-modality arises.",
        "A robot uses LIDAR-based scan matching for localization. Describe the observation model and explain how the ICP (Iterative Closest Point) algorithm relates to maximum likelihood estimation.",
        "Compare the precision (inverse covariance) representation in Active Inference with the covariance representation in Kalman filtering. What are the computational trade-offs of each?",
        "How does the innovation sequence (difference between predicted and actual measurements) in a Kalman filter serve the same role as prediction error in Active Inference?",
        "A manipulator's joint encoders have quantization noise while its force sensor has Gaussian noise. How do these different noise models affect the estimation algorithm choice?",
        "Compare visual odometry (estimating motion from camera images) and wheel odometry (from encoders). How should a state estimator weight these sources when the robot drives on slippery terrain?",
        "How does the concept of observability Gramian quantify which states are most and least observable from available sensors? Give a robotic example where certain states are poorly observable.",
        "A robot operating in a GPS-denied underground mine uses IMU dead reckoning that drifts over time. How does loop closure detection (recognizing a previously visited location) correct accumulated drift?",
        "Compare batch estimation (processing all measurements at once) with recursive estimation (processing measurements sequentially). When is each approach appropriate in robotics?",
        "How does the information filter (the dual of the Kalman filter, operating on information matrix instead of covariance) relate to precision-weighted estimation in Active Inference?",
        "A stereo camera provides depth estimates that degrade with distance (depth uncertainty grows quadratically). How should the estimation algorithm adapt its precision weighting as a function of range?",
        "Compare the computational complexity of EKF-SLAM and graph-based SLAM. How does the choice of estimation approach scale with map size?",
        "How does sensor pre-integration (accumulating IMU measurements between keyframes) improve the efficiency of visual-inertial odometry? What is the free energy interpretation?",
        "A robot detects an outlier measurement (e.g., lidar return from a reflective surface). How does robust estimation (M-estimators, RANSAC) relate to adjusting precision weights in Active Inference?",
        "Compare the estimation challenges of a robot with accurate but sparse sensors (e.g., GPS at 1 Hz) versus noisy but dense sensors (e.g., IMU at 200 Hz). How does sensor fusion optimize the trade-off?",
    ],
    ("03_control_estimation", "04_cognition"): [
        "Compare system identification using least squares regression with Bayesian parameter estimation for learning a robot's dynamics model. How does the Bayesian approach provide uncertainty estimates that least squares does not?",
        "How does online recursive least squares (RLS) for system identification relate to continuous updating of a generative model's parameters in Active Inference?",
        "A robot arm's dynamics change when it picks up an unknown payload. How should the cognitive system detect this change and update the dynamics model in real time?",
        "Compare frequency-domain identification (Bode plots, transfer function fitting) with time-domain identification (state-space model fitting) for a robot joint. When is each approach more appropriate?",
        "How does the concept of persistent excitation (sufficiently rich input signals) from system identification theory relate to Active Inference's epistemic foraging (acting to reduce model uncertainty)?",
        "A mobile robot must learn both its kinematics (wheel radii, track width) and the floor surface properties (friction coefficients). How do these two identification problems interact?",
        "Compare the information content of different excitation trajectories for identifying a manipulator's inertial parameters. How should a robot design its identification experiments to maximize learning?",
        "How does the concept of model order selection (choosing the number of states in a state-space model) relate to the accuracy-complexity trade-off in Active Inference generative models?",
        "A robot operating in a structured environment must learn object properties (mass, friction, shape) through interaction. How does this manipulation-based system identification differ from standard trajectory-based identification?",
        "Compare gray-box identification (physics-informed model with unknown parameters) with black-box identification (neural network trained on data). What are the trade-offs for robotic applications?",
        "How does the concept of structural identifiability (can parameters be uniquely determined from input-output data?) constrain the generative model design in robotics?",
        "A robot learns that its dynamics model is wrong (large persistent prediction errors). How does the system decide between parameter re-estimation and structural model change?",
        "Compare the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) for model selection in robotic system identification. How do these relate to variational free energy?",
        "How does the concept of forgetting factors in recursive estimation (exponential weighting of recent data) handle non-stationary system parameters like gradually wearing robot joints?",
        "A fleet of identical robots can share identification data. How does pooling data from multiple robots improve parameter estimation, and what assumptions must hold for this to be valid?",
        "Compare the computational requirements of offline batch identification versus online adaptive identification for a real-time robotic system. What are the real-time constraints?",
        "How does the concept of dual control (simultaneously identifying the system and controlling it) relate to the unified perception-action framework of Active Inference?",
    ],
    ("03_control_estimation", "05_action"): [
        "Derive the LQR (Linear Quadratic Regulator) control law for a 2-DOF robot arm and explain how the cost function weights shape the resulting behavior. How does this relate to prior preferences in Active Inference?",
        "Compare computed torque control (inverse dynamics) with impedance control for a manipulator interacting with the environment. When is each approach appropriate, and how does Active Inference generalize both?",
        "How does Model Predictive Control (MPC) optimize over a finite horizon of future actions? Compare MPC's receding horizon approach with Active Inference's expected free energy evaluation.",
        "A robot performing contact-rich assembly tasks must switch between free-space motion and constrained motion. How does hybrid control (combining continuous and discrete modes) handle this transition?",
        "Compare the stability guarantees of a Lyapunov-based controller with the optimality of an LQR controller for a robotic joint. How does Active Inference balance stability and optimality?",
        "How does the concept of passivity-based control (ensuring the system dissipates energy) relate to the free energy principle's constraint that systems must remain within viable bounds?",
        "A quadrotor must perform aggressive aerobatic maneuvers that push it far from hover equilibrium. How do nonlinear control approaches (feedback linearization, backstepping) handle this compared to Active Inference?",
        "Compare the tracking performance of a PID controller tuned with Ziegler-Nichols versus one optimized via expected free energy minimization. What systematic advantages does the Active Inference approach offer?",
        "How does actuator saturation (maximum torque limits) affect optimal control design? How should the Active Inference generative model incorporate these hard constraints?",
        "A robotic hand performing in-hand manipulation must coordinate multiple fingers with contact constraints. How does the high-dimensional action space challenge both classical optimal control and Active Inference?",
        "Compare the control architectures for a hydraulic excavator (high force, low bandwidth) and an electric manipulator (moderate force, high bandwidth). How do actuator dynamics affect the control design?",
        "How does the concept of null-space control in redundant manipulators (using extra DOF for secondary objectives) relate to the pragmatic-epistemic decomposition in Active Inference?",
        "A robot walking on uneven terrain must simultaneously maintain balance and make forward progress. How does the control hierarchy handle these competing objectives?",
        "Compare feedforward and feedback control contributions in a robot performing a fast point-to-point motion. How does the ratio depend on model accuracy and disturbance characteristics?",
        "How does iterative learning control (ILC, improving trajectory tracking over repeated trials) relate to parameter learning in Active Inference? What convergence properties does each guarantee?",
        "A soft robot actuated by pneumatic chambers has nonlinear pressure-volume dynamics. How does this nonlinear actuation challenge the control design compared to electric motor actuation?",
        "Compare the concept of stochastic optimal control (minimizing expected cost under noise) with Active Inference's treatment of action selection under uncertainty. Are they mathematically equivalent?",
    ],
    ("03_control_estimation", "06_learning"): [
        "Compare Model Reference Adaptive Control (MRAC) with recursive least squares parameter estimation as approaches to learning a robot's unknown dynamics online. What stability guarantees does each provide?",
        "How does the concept of persistent excitation ensure convergence in adaptive control? What happens to parameter estimates when the robot executes repetitive trajectories that lack excitation?",
        "A robot arm's joint friction changes with temperature. Design an adaptive controller that estimates friction parameters online and adjusts the control law accordingly.",
        "Compare direct adaptive control (adjusting control gains directly) with indirect adaptive control (identifying the plant, then computing control gains). How does Active Inference relate to each?",
        "How does the concept of certainty equivalence in adaptive control (using estimated parameters as if they were certain) compare to Active Inference's explicit treatment of parameter uncertainty?",
        "A mobile robot learns its wheel radii by comparing commanded and actual velocities during operation. How does this online calibration affect localization accuracy over time?",
        "Compare the L1 adaptive controller's transient performance guarantees with those of classical adaptive controllers. How does fast adaptation relate to precision weighting in Active Inference?",
        "How does the concept of parameter projection (constraining parameters to a known feasible set) in adaptive control relate to informative priors in Bayesian estimation?",
        "A robot operating in variable gravity (e.g., space applications) must adapt its dynamics model to changing gravitational conditions. How does the adaptive estimation detect and respond to this environmental change?",
        "Compare the convergence rates of gradient-based parameter estimation versus natural gradient methods for learning robot dynamics. How does the Fisher information matrix affect convergence?",
        "How does the concept of self-tuning regulators (simultaneously identifying and controlling) relate to the dual estimation-control problem in Active Inference?",
        "A manipulator's cable drive system experiences cable stretch over time. Design a learning algorithm that detects and compensates for this slow degradation.",
        "Compare the sample complexity of model-based adaptive control (learning a parametric model) with model-free reinforcement learning for a simple robotic task. What are the data efficiency trade-offs?",
        "How does the concept of integral action (ensuring zero steady-state error) in classical control relate to the learning of bias parameters in a generative model?",
        "A robot fleet shares learned models through federated learning. How does distributed parameter estimation compare to centralized estimation, and what privacy-accuracy trade-offs arise?",
        "Compare the stability analysis of adaptive control systems (Lyapunov-based) with the convergence analysis of variational inference algorithms. What mathematical tools do they share?",
        "How does the concept of meta-learning (learning hyperparameters of the learning algorithm itself) relate to tuning the learning rate and precision dynamics in Active Inference?",
    ],
    ("03_control_estimation", "07_communication"): [
        "How does the Smith predictor handle communication delay in a networked control system? What assumptions about the plant model are required, and how does Active Inference handle delay differently?",
        "Compare event-triggered control (transmitting only when a threshold is exceeded) with time-triggered control (transmitting at fixed intervals) for a networked robotic system. How does each affect free energy?",
        "A robot arm is controlled over a WiFi link with variable latency (5-50ms). How does this jitter affect the control loop stability, and what estimation techniques compensate for it?",
        "How does the concept of networked control systems (NCS) theory extend classical control to account for communication constraints? What new stability conditions arise?",
        "Compare the communication requirements of centralized estimation (one estimator for all robots) versus distributed estimation (each robot estimates locally) in a multi-robot system.",
        "A consensus algorithm allows multiple robots to agree on a shared estimate (e.g., target location). How does the convergence rate depend on the communication graph topology?",
        "How does quantization of control signals (sending discrete commands over a digital link) affect the precision of robotic control? What is the minimum bit rate needed for a given control performance?",
        "A robot transmits compressed sensor data to a remote estimator. How does lossy compression affect estimation accuracy, and how should the estimator's precision weighting adapt?",
        "Compare the communication architectures for cooperative manipulation (two arms holding one object) versus cooperative transport (two mobile robots carrying one object). How do the estimation requirements differ?",
        "How does the concept of co-design (jointly optimizing the controller and communication protocol) improve performance over separate design in networked robotic systems?",
        "A multi-robot SLAM system must communicate map information. Compare map merging approaches (exchanging raw scans, feature maps, or pose graphs) and their bandwidth implications.",
        "How does the concept of observability over networks (can each robot's state be estimated given the communication graph?) extend classical observability theory?",
        "A robotic system uses predictive communication (sending predicted future states rather than current states) to compensate for communication delay. How does this relate to the generative model's temporal predictions?",
        "Compare the resilience of star, mesh, and ring communication topologies for a multi-robot team to single-link failures. How does topology affect collective estimation performance?",
        "How does the concept of distributed Kalman filtering (each node runs a local filter and exchanges estimates) compare to centralized fusion? What are the conditions for equivalent performance?",
        "A human operator supervises a team of robots through a bandwidth-limited interface. What information should the robots communicate to maximize the operator's situational awareness?",
        "Compare the communication efficiency of gossip protocols (random pairwise exchanges) with flooding protocols (broadcast to all) for distributing state estimates in a robot swarm.",
    ],
    ("03_control_estimation", "08_planning"): [
        "Compare Model Predictive Control (MPC) with explicit dynamic programming for path planning. How does MPC's receding horizon approach handle the curse of dimensionality?",
        "How does the concept of reachability analysis (computing all states achievable from current state under control constraints) inform safe planning for robotic systems?",
        "A quadrotor must plan a trajectory through a cluttered environment while satisfying dynamic constraints (maximum acceleration, angular rate). How does trajectory optimization handle these coupled constraints?",
        "Compare time-optimal and energy-optimal trajectory planning for a robot arm performing a pick-and-place task. How does the cost function choice affect the resulting trajectory shape?",
        "How does the concept of tube-based MPC (planning a nominal trajectory with a tube of allowed deviations) relate to the risk term in expected free energy?",
        "A legged robot must plan footstep sequences and body trajectories simultaneously. How does this hybrid planning problem (discrete footsteps, continuous body motion) challenge standard MPC?",
        "Compare the planning horizons needed for different robotic tasks: lane keeping (short), overtaking (medium), and highway merging (long). How does the required horizon scale with task complexity?",
        "How does the concept of explicit MPC (pre-computing the control law offline as a piecewise affine function) trade online computation for offline computation? When is this approach practical?",
        "A robotic manipulator plans a trajectory that must avoid joint limits, workspace obstacles, and singularities simultaneously. How do these different constraint types affect the planning algorithm?",
        "Compare the planning performance of Sequential Quadratic Programming (SQP) with Interior Point methods for trajectory optimization. What are the convergence properties of each?",
        "How does the concept of funnel-based planning (ensuring the system stays within a verified safe region around the planned trajectory) provide formal safety guarantees?",
        "A fleet of mobile robots must plan coordinated paths to avoid collisions with each other. How does multi-agent trajectory optimization scale with the number of robots?",
        "Compare offline trajectory planning (computing the full trajectory before execution) with online replanning (updating the trajectory during execution). What triggers replanning?",
        "How does the concept of chance-constrained optimization (satisfying constraints with a specified probability) handle uncertain obstacle locations in robot planning?",
        "A spacecraft must plan fuel-optimal trajectories with limited thrust. How does the combination of free-fall dynamics and impulsive control affect the planning problem structure?",
        "Compare gradient-based trajectory optimization with sampling-based planning (MPPI, CEM) for a robot navigating in a dynamic environment. When does each approach excel?",
        "How does the concept of information-theoretic planning (choosing actions that maximize information gain) relate to the epistemic component of expected free energy in Active Inference?",
    ],
    # ========================================================================
    # SECTION 4: AUTONOMOUS AGENTS
    # ========================================================================
    ("04_autonomous_agents", "01_systems"): [
        "Compare the system architectures of a self-driving car (Apollo/Autoware) and a fully autonomous drone (PX4). How do their Markov blanket structures differ in sensor suites, computation, and actuation?",
        "How does the concept of operational design domain (ODD) from autonomous driving constrain the generative model's scope? What happens when the system encounters conditions outside its ODD?",
        "A fully autonomous mobile robot must manage its own power consumption, thermal state, and sensor health. How does this self-monitoring extend the system's Markov blanket to include internal health states?",
        "Compare the autonomy levels (SAE L1-L5 for vehicles, NIST autonomy levels for robots) and map each level to the depth and sophistication of the underlying generative model.",
        "How does the concept of graceful degradation apply to an autonomous robot whose lidar fails mid-mission? What system architecture supports continued operation with reduced capability?",
        "A Mars rover operates with zero real-time human intervention. How does its system architecture differ from an Earth-based robot that can rely on cloud computation and human oversight?",
        "Compare the system architectures of an autonomous underwater vehicle (AUV) and an autonomous surface vessel (ASV). How do environmental constraints (pressure, communication, GPS) shape each system?",
        "How does the concept of system-of-systems engineering apply to an autonomous warehouse where multiple robots, conveyors, and human workers form an integrated autonomous operation?",
        "A fully autonomous surgical robot must maintain sterility, instrument tracking, and tissue safety simultaneously. How does this safety-critical system architecture constrain the generative model design?",
        "Compare the redundancy requirements of autonomous systems in different domains: aviation (triple-redundant), automotive (dual-redundant), and consumer robotics (no redundancy). How does redundancy affect system cost and reliability?",
        "How does the concept of runtime monitoring (checking safety invariants during execution) complement the generative model's predictions in an autonomous system?",
        "A swarm of 100 autonomous drones must collectively monitor a forest fire. How does the system architecture scale from individual drone autonomy to swarm-level coordination?",
        "Compare the boot-up and self-test procedures of an autonomous robot with the concept of system initialization and prior belief setting in Active Inference.",
        "How does the concept of digital twins (virtual replicas of physical systems) support the design and validation of autonomous robotic system architectures?",
        "A fully autonomous agricultural robot must operate 24/7 in varying weather conditions (rain, wind, darkness). How does environmental robustness affect the system architecture requirements?",
        "Compare the system architectures needed for autonomous exploration (unknown environments) versus autonomous operation in known environments (e.g., a factory). How does prior knowledge affect architecture choices?",
        "How does the concept of V&V (verification and validation) for autonomous systems differ from traditional robotics V&V? What additional challenges does full autonomy introduce?",
    ],
    ("04_autonomous_agents", "02_agents"): [
        "Compare the BDI (Beliefs, Desires, Intentions) agent architecture from AI with the Active Inference agent architecture. How does each represent goals, beliefs, and action selection?",
        "How does the concept of bounded rationality (agents with limited computation making satisficing decisions) apply to autonomous robots that must act in real time?",
        "A self-driving car must handle an ethical dilemma (unavoidable accident scenario). How does the Active Inference framework encode preferences that address ethical considerations?",
        "Compare the agent architectures of a fully autonomous drone delivery system versus a semi-autonomous surgical robot. How does the level of human oversight affect the agent design?",
        "How does the concept of meta-cognition (reasoning about one's own reasoning process) apply to an autonomous agent that must decide when to ask for human help?",
        "A rescue robot must balance its own safety against the urgency of reaching trapped survivors. How does the expected free energy framework handle this conflict between self-preservation and task completion?",
        "Compare reactive autonomy (behavior trees, subsumption) with deliberative autonomy (PDDL planning) for a household service robot. When does each approach fail?",
        "How does the concept of multi-agent reinforcement learning relate to Active Inference in a team of autonomous robots that must learn cooperative strategies?",
        "A autonomous agent operating in a social environment (e.g., hospital robot) must model human norms and expectations. How does the generative model encode social rules?",
        "Compare the agent design of a competitive autonomous racing car with a cooperative autonomous warehouse robot. How do the expected free energy landscapes differ?",
        "How does the concept of intention recognition (inferring what another agent plans to do) apply to an autonomous vehicle predicting pedestrian behavior at a crosswalk?",
        "A fully autonomous robot operating for months without maintenance must decide when to seek repairs. How does self-monitoring of degradation fit into the Active Inference agent framework?",
        "Compare the adaptability of a hand-designed behavior tree with a learned neural network policy for an autonomous manipulation agent. What are the robustness-interpretability trade-offs?",
        "How does the concept of theory of mind (modeling other agents' beliefs and intentions) enable an autonomous robot to cooperate effectively with humans and other robots?",
        "A competitive multi-agent scenario (e.g., robot soccer) requires agents that model opponents. How does the depth of opponent modeling affect strategic performance?",
        "Compare the concept of autonomy as self-evidencing (Active Inference) with autonomy as reward maximization (reinforcement learning). Under what conditions are these equivalent?",
        "How does the concept of moral agency apply to autonomous robots? Should a robot that causes harm be considered a moral agent, and how does the Active Inference framework inform this question?",
    ],
    ("04_autonomous_agents", "03_perception"): [
        "Compare the perception pipeline of an autonomous vehicle (camera, lidar, radar fusion) with that of an autonomous drone (monocular camera, IMU). How do sensor constraints affect the perception architecture?",
        "How does the concept of semantic segmentation (labeling each pixel with a class) contribute to an autonomous robot's generative model of the environment?",
        "A autonomous robot must detect and classify objects it has never seen before (open-set recognition). How does the generative model handle novel observations that fall outside trained categories?",
        "Compare end-to-end perception (raw images to driving commands) with modular perception (detection, tracking, prediction, planning) for autonomous vehicles. What are the interpretability trade-offs?",
        "How does the concept of domain adaptation apply when an autonomous robot trained in simulation must perceive real-world scenes? What perception pipeline changes are needed?",
        "A autonomous underwater robot operates in turbid water with near-zero visibility. How must the perception pipeline adapt when the primary visual modality is unavailable?",
        "Compare the perception requirements for autonomous highway driving (structured, high-speed) versus autonomous off-road driving (unstructured, variable terrain). How do the generative models differ?",
        "How does the concept of 3D object detection from point clouds (PointNet, VoxelNet) relate to the generative model's observation likelihood for lidar-equipped autonomous systems?",
        "A autonomous drone performing package delivery must detect landing zones, obstacles, and humans from an aerial perspective. How does the top-down viewpoint affect the perception generative model?",
        "Compare temporal perception approaches: tracking-by-detection (independent detections linked over time) versus end-to-end temporal models (recurrent networks processing video). Which aligns better with Active Inference?",
        "How does the concept of self-supervised learning for perception (e.g., predicting next frame from current frame) relate to learning the generative model's temporal dynamics?",
        "A autonomous robot operating at night must use infrared cameras and radar. How does the shift from visual to non-visual sensing change the structure of the generative model?",
        "Compare the perception challenges of a ground robot (2D navigation, 3D obstacles) with a flying robot (full 3D navigation). How does the dimensionality of the required world model differ?",
        "How does the concept of uncertainty estimation in deep learning (Monte Carlo dropout, ensemble methods) provide the precision estimates needed for Active Inference perception?",
        "A autonomous agricultural robot must perceive and classify plant health status from visual appearance. How does this application-specific perception differ from general object recognition?",
        "Compare the latency requirements of perception for different autonomous applications: autonomous driving (50ms), drone racing (10ms), and household robotics (200ms). How does latency constrain the perception architecture?",
        "How does the concept of multi-task perception (jointly detecting objects, estimating depth, and segmenting scenes from a single model) reduce computational cost while improving the generative model's coherence?",
    ],
    ("04_autonomous_agents", "04_cognition"): [
        "Compare scene graph representations (objects, attributes, relationships) with occupancy grids as world models for autonomous robots. When is each representation more appropriate?",
        "How does the concept of a world model in model-based reinforcement learning relate to the generative model in Active Inference? Are they formally equivalent?",
        "A autonomous robot must maintain long-term memory of its environment (semantic map that persists across sessions). How does this long-term cognitive representation support efficient planning?",
        "Compare the cognitive architectures SOAR, ACT-R, and Active Inference as frameworks for autonomous robot intelligence. What does each emphasize, and where do they agree?",
        "How does the concept of situation awareness (perceiving, comprehending, and projecting future states) from human factors engineering map to the Active Inference cognitive process?",
        "A autonomous robot encounters a novel object that blocks its path. Trace the cognitive process from detection through classification, physics reasoning, and action planning.",
        "Compare symbolic reasoning (logic-based, PDDL planning) with neural reasoning (learned world models) for autonomous robots. How does Active Inference bridge symbolic and subsymbolic cognition?",
        "How does the concept of causal reasoning (understanding cause-effect relationships) enhance an autonomous robot's generative model beyond mere correlation-based prediction?",
        "A autonomous construction robot must reason about structural stability as it builds. How does the cognitive system incorporate physics simulation into its generative model?",
        "Compare the cognitive load of an autonomous robot operating in a static environment versus a dynamic environment with moving agents. How does scene complexity affect computational requirements?",
        "How does the concept of abstraction hierarchies (representing the world at multiple levels of detail) support efficient cognition for autonomous robots with limited computation?",
        "A autonomous robot must explain its decisions to a human auditor (explainable AI). How does the structure of the generative model support generating human-understandable explanations?",
        "Compare the cognitive requirements of reactive autonomy (respond to current situation) versus proactive autonomy (anticipate and prepare for future situations). What generative model depth enables proactive behavior?",
        "How does the concept of common sense reasoning (implicit knowledge about physics, social norms, object properties) apply to autonomous robots? How would you encode common sense in a generative model?",
        "A autonomous robot operating over months develops an increasingly rich world model. How does the cognitive system manage model complexity to prevent computational overload?",
        "Compare the cognitive architecture of a single autonomous robot with that of a multi-robot system that shares cognition through communication. How does distributed cognition differ from individual cognition?",
        "How does the concept of abductive reasoning (inference to the best explanation) relate to the Active Inference cognitive process when an autonomous robot encounters surprising observations?",
    ],
    ("04_autonomous_agents", "05_action"): [
        "Compare end-to-end learned policies (sensory input to motor output) with structured action pipelines (perception, planning, control) for autonomous robot manipulation. What are the safety implications?",
        "How does the concept of safe reinforcement learning (learning policies that satisfy safety constraints) relate to Active Inference's treatment of prior preferences as safety bounds?",
        "A autonomous mobile manipulator must coordinate base movement with arm manipulation during a pick-and-place task. How does the whole-body action space challenge the expected free energy computation?",
        "Compare the action strategies of an autonomous racing drone (aggressive, near-limit dynamics) with an autonomous inspection drone (conservative, prioritizing stability). How do the prior preferences differ?",
        "How does the concept of skill primitives (reusable building blocks of action) enable hierarchical action composition in autonomous manipulation systems?",
        "A autonomous legged robot must traverse a debris field with uncertain footing. How does the action selection balance between cautious exploration and efficient locomotion?",
        "Compare the action spaces of a traditional industrial robot (pre-programmed trajectories) with a fully autonomous manipulation system (learned, adaptive actions). What capability gap exists?",
        "How does the concept of sim-to-real policy transfer affect the reliability of autonomous robot actions? What domain randomization strategies improve transfer robustness?",
        "A autonomous underwater robot must perform precision manipulation in currents. How do environmental disturbances affect the action selection and what adaptive mechanisms compensate?",
        "Compare the action complexity of autonomous navigation (2D position + heading) with autonomous manipulation (6D pose + grasp configuration). How does dimensionality affect the planning and control architecture?",
        "How does the concept of behavior cloning (learning actions from human demonstrations) relate to inheriting prior preferences from an expert's generative model?",
        "A autonomous surgical robot must perform actions with sub-millimeter precision. How do the precision requirements constrain the action generation architecture compared to warehouse robotics?",
        "Compare the emergency stop protocols of different autonomous systems (vehicle: brake hard, drone: auto-land, manipulator: hold position). How does each relate to the system's safety prior preferences?",
        "How does the concept of contact-implicit trajectory optimization (planning through contact/no-contact transitions) enable autonomous manipulation of objects with complex geometries?",
        "A autonomous robot performing long-duration operations must manage action fatigue (actuator heating, battery depletion). How does action resource management factor into the expected free energy computation?",
        "Compare the action generation approaches for autonomous grasping: analytical (grasp quality metrics) versus learned (neural network predicting grasp poses). What are the reliability trade-offs?",
        "How does the concept of recovery actions (returning to a known safe state after failure) complement the Active Inference framework's focus on minimizing expected free energy?",
    ],
    ("04_autonomous_agents", "06_learning"): [
        "Compare online reinforcement learning with offline reinforcement learning for training autonomous robot policies. What are the safety and efficiency trade-offs?",
        "How does the concept of curriculum learning (gradually increasing task difficulty) accelerate learning for autonomous manipulation systems? Design a curriculum for a deformable object manipulation task.",
        "A autonomous robot deployed in a new environment must learn quickly with minimal interactions. Compare few-shot learning, meta-learning, and transfer learning approaches for this rapid adaptation.",
        "Compare model-based reinforcement learning (learning a dynamics model, then planning through it) with model-free reinforcement learning (directly learning a value function or policy). How does Active Inference relate to each?",
        "How does the concept of reward shaping affect the learning speed and final performance of an autonomous navigation agent? What are the risks of poorly designed reward functions?",
        "A autonomous robot fleet learns collectively: each robot contributes experience to a shared model. How does federated learning apply to multi-robot systems while preserving operational privacy?",
        "Compare the learning approaches for autonomous driving: imitation learning (from human demonstrations), reinforcement learning (from simulation), and Active Inference (from generative model updating).",
        "How does the concept of continual learning (learning new tasks without forgetting old ones) challenge autonomous robots that operate in evolving environments?",
        "A autonomous manipulation robot must learn to handle novel objects not seen during training. How does zero-shot generalization differ from few-shot adaptation in the Active Inference framework?",
        "Compare the data efficiency of learning from simulation (unlimited cheap data) versus real-world interaction (limited expensive data). How does the sim-to-real gap affect the learned generative model?",
        "How does the concept of intrinsic motivation (curiosity-driven exploration without extrinsic reward) enable autonomous robots to discover useful skills in open-ended environments?",
        "A autonomous robot learning a complex assembly task from video demonstrations must extract the relevant action sequence from visual observation. How does this observational learning relate to updating the generative model?",
        "Compare the learning stability of on-policy methods (PPO, TRPO) with off-policy methods (SAC, TD3) for autonomous robot control. What does each assume about the data distribution?",
        "How does the concept of safe exploration (ensuring the robot does not damage itself or the environment during learning) constrain the epistemic foraging component of expected free energy?",
        "A autonomous robot operating for years in the same environment should become increasingly efficient. How does the learning system balance exploitation of known strategies with exploration of potentially better ones?",
        "Compare the learning architectures for single-task autonomy (one specific task learned well) versus multi-task autonomy (generalist robot capable of many tasks). What generative model structure supports each?",
        "How does the concept of self-play (an agent learning by competing against itself) apply to autonomous multi-robot scenarios where each robot improves by interacting with learning teammates?",
    ],
    ("04_autonomous_agents", "07_communication"): [
        "Compare Vehicle-to-Everything (V2X) communication in autonomous driving with Robot-to-Robot communication in warehouse automation. How do the latency and reliability requirements differ?",
        "How does the concept of intention broadcasting (announcing planned actions to nearby agents) prevent conflicts in multi-autonomous-robot environments? How does this relate to generative model alignment?",
        "A autonomous robot must communicate with a non-expert human using natural language. How does the robot translate its internal belief states into human-understandable explanations?",
        "Compare the communication requirements of leader-follower formation control versus consensus-based formation control for autonomous drone swarms.",
        "How does the concept of trust calibration apply to human-robot interaction with autonomous systems? How should the robot communicate its confidence level to build appropriate trust?",
        "A team of autonomous exploration robots discovers a hazard. How does the team's communication protocol ensure all members update their generative models with this critical information?",
        "Compare the communication architectures for autonomous robot teams in structured indoor environments (WiFi infrastructure) versus outdoor field environments (ad-hoc mesh networks).",
        "How does the concept of shared mental models from human teamwork apply to multi-autonomous-robot coordination? What information must be communicated to maintain model alignment?",
        "A autonomous robot interacting with elderly users must adapt its communication style (speed, vocabulary, modality). How does the robot learn a model of the user's communication preferences?",
        "Compare the privacy implications of different communication architectures: centralized (all data to cloud), distributed (peer-to-peer), and federated (local processing, shared summaries).",
        "How does the concept of pragmatic communication (communicating only what the receiver needs to know) reduce bandwidth requirements in multi-robot autonomous systems?",
        "A autonomous delivery robot must negotiate right-of-way with human pedestrians using only non-verbal cues (motion, lights, sounds). Design a communication protocol for this interaction.",
        "Compare the communication overhead of cooperative mapping (each robot contributes to a shared map) versus independent mapping (each robot builds its own map). When is sharing worth the communication cost?",
        "How does the concept of communication as active inference (choosing what to communicate to minimize collective free energy) differ from communication as information exchange?",
        "A autonomous robot fleet operates in an environment where communication can be intercepted. How should the communication protocol ensure security while maintaining real-time coordination?",
        "Compare the human-robot communication challenges of a autonomous vehicle (brief, critical interactions with pedestrians) versus a autonomous home robot (extended, nuanced interactions with residents).",
        "How does the concept of adaptive communication (adjusting message content and frequency based on task urgency and channel quality) improve the efficiency of multi-robot autonomous systems?",
    ],
    ("04_autonomous_agents", "08_planning"): [
        "Compare the planning architectures of autonomous driving (behavior planning + motion planning + trajectory tracking) with autonomous drone delivery (mission planning + path planning + flight control).",
        "How does the concept of hierarchical task planning (decomposing a complex mission into subtasks) relate to hierarchical generative models in Active Inference?",
        "A autonomous robot must plan under deep uncertainty about its environment (e.g., first exploration of an unknown building). How does the balance between epistemic and pragmatic planning shift during exploration?",
        "Compare Monte Carlo Tree Search (MCTS) planning with Model Predictive Path Integral (MPPI) control for autonomous systems. How does each handle stochasticity and branching futures?",
        "How does the concept of anytime planning (providing a usable plan at any time, improving with more computation) benefit autonomous robots that face unpredictable computational budgets?",
        "A team of autonomous robots must coordinate their plans to achieve a collective goal (e.g., multi-robot construction). How does multi-agent planning scale, and what simplifications make it tractable?",
        "Compare the planning horizons of different autonomous applications: industrial manipulation (seconds), autonomous driving (minutes), and space mission planning (years). How does the planning architecture adapt to each timescale?",
        "How does the concept of contingent planning (branching plans that depend on future observations) handle the irreducible uncertainty in autonomous robot operations?",
        "A autonomous robot must plan a sequence of actions that includes irreversible steps (e.g., cutting material). How does irreversibility affect the expected free energy evaluation and risk assessment?",
        "Compare sampling-based motion planning (RRT*, PRM*) with optimization-based planning (TrajOpt, CHOMP) for autonomous manipulation in cluttered environments.",
        "How does the concept of temporal logic specifications (LTL formulas expressing mission requirements) integrate with Active Inference planning to ensure autonomous robots satisfy complex mission constraints?",
        "A autonomous robot re-plans its trajectory every 100ms. How does the computational budget constrain the planning depth and resolution, and what warm-starting strategies improve efficiency?",
        "Compare the planning approaches for autonomous navigation in structured environments (road networks) versus unstructured environments (off-road terrain). How do prior map availability and terrain uncertainty affect the planning algorithm?",
        "How does the concept of social-aware planning (accounting for the comfort and expectations of nearby humans) extend the Active Inference framework's prior preferences for autonomous service robots?",
        "A autonomous exploration robot must decide between revisiting previously mapped areas (to improve map quality) and exploring new areas (to expand map coverage). Frame this as an epistemic planning trade-off.",
        "Compare the planning complexity of single-robot task and motion planning (TAMP) with multi-robot TAMP. What decomposition strategies make multi-robot TAMP tractable?",
        "How does the concept of adversarial planning (planning against an opponent who is also planning) apply to autonomous robots in competitive scenarios such as robot soccer or multi-agent pursuit?",
    ],
}

# ============================================================================
# SECTION-LEVEL QUESTIONS (4 section-level question files)
# ============================================================================

# Section-level questions are about the section theme broadly

SECTION_QUESTIONS = {
    "01_robotic_systems": {
        "topic": "Systems",
        "questions": [
            "How does the ROS2 middleware architecture formalize system boundaries through its node-topic-service communication model? Describe how DDS Quality of Service policies enforce Markov blanket properties.",
            "Compare the system architecture of a UR5 manipulator performing assembly with a Clearpath Jackal navigating a warehouse. How do their Markov blankets differ in sensor suites, actuator types, and computational layers?",
            "A mobile manipulation platform has a wheeled base, a 6-DOF arm, and a vision system. Identify the nested Markov blankets at the joint, subsystem, and platform levels, and explain the interfaces between them.",
            "How does the choice of communication middleware (ROS2/DDS, MQTT, custom UDP) affect the information flow across system boundaries in a multi-robot warehouse? What bandwidth and latency constraints matter?",
            "Explain how system identification calibrates a robot's generative model. Design a calibration experiment for a differential-drive robot that estimates wheel radii, track width, and IMU biases.",
            "A robot operates reliably in a structured factory but fails in an unstructured outdoor environment. Use the free energy framework to explain this failure in terms of the accuracy-complexity trade-off.",
            "Compare the real-time computational requirements of state estimation on an ARM Cortex-M (microcontroller) versus an NVIDIA Jetson (GPU SoC). How does hardware constrain the generative model complexity?",
            "How does the concept of digital twins support the validation of robotic system architectures before physical deployment? Describe the relationship between the digital twin and the robot's generative model.",
            "A robot's lidar sensor degrades over 6 months due to lens contamination. How does the system detect this degradation through free energy monitoring, and what automated responses are appropriate?",
            "Explain how the concept of graceful degradation applies to a robot that loses one of its three cameras. How should the system architecture support continued operation with reduced sensor capability?",
            "Compare the system architectures of an industrial manipulator cell (fixed, controlled environment) and a field service robot (mobile, uncontrolled environment). How does environmental predictability affect architecture design?",
            "How does the concept of functional safety (IEC 61508, ISO 13849) constrain the system architecture of collaborative robots? What Markov blanket properties ensure safe human-robot interaction?",
            "A space robot operates with 20-minute communication delays. How must the system architecture balance onboard autonomy with ground-based oversight? What generative model depth is needed?",
            "Describe how time-scale separation in robotic systems (motor control at kHz, perception at 30Hz, planning at 1Hz) enables modular design. How do these timescales map to levels of the generative model?",
            "How does adding a tactile sensor array to a gripper change the system's information-theoretic capacity? Quantify the additional bandwidth and its implications for the generative model.",
            "Compare the fault-tolerance strategies of redundant sensor configurations (triple-redundant IMU) versus diverse sensor configurations (IMU + visual odometry + wheel encoders). Which provides better robustness?",
            "Explain how a robot's power system (battery, power distribution, thermal management) constitutes a subsystem with its own Markov blanket that interacts with the computational and mechanical subsystems.",
        ],
    },
    "02_bio_inspired_design": {
        "topic": "Agents",
        "questions": [
            "Compare the sensory systems of a honeybee (compound eyes, antennae, mechanoreceptors) with the sensor suite of a micro aerial vehicle. What bio-inspired sensor placement principles emerge?",
            "How does the octopus's distributed nervous system (two-thirds of neurons in the arms) inspire decentralized control architectures for hyper-redundant robotic manipulators?",
            "A gecko climbs vertical surfaces using van der Waals adhesion. Design a bio-inspired climbing robot and specify how the adhesion mechanism defines the active states of its Markov blanket.",
            "Compare the energy efficiency of biological locomotion (running cockroach: 15 J/kg/m) with wheeled robot locomotion (mobile robot: 5 J/kg/m). What bio-inspired design principles could improve legged robot efficiency?",
            "How does the concept of allometric scaling (brain size vs. body size) from biology inform the computational resource allocation for robots at different scales?",
            "A biological fish senses water flow through its lateral line organ. Design a bio-inspired flow sensor array for an underwater robot and describe its role in the generative model.",
            "Compare the morphological computation in a compliant robotic hand (passive adaptation to object shape) with rigid-fingered grasping. How does body compliance reduce generative model complexity?",
            "How does the biological immune system's ability to detect novel threats inspire anomaly detection systems in autonomous robots?",
            "A bird caching food exhibits planning behavior (storing food for future use). How does this biological example of future-oriented behavior relate to expected free energy minimization?",
            "Compare the sensory bandwidth of biological compound eyes (~200 frames/sec, wide FOV) with standard robotic cameras (~30 fps, narrow FOV). What perceptual advantages does the biological design offer?",
            "How does the concept of umwelt (species-specific perceptual world) inform the design of task-specific generative models for specialized robots?",
            "A biological predator-prey arms race drives increasing sophistication in both sensing and evasion. How does this coevolutionary dynamic apply to adversarial robotic scenarios?",
            "Compare the redundancy strategies of biological organisms (bilateral symmetry, redundant organs) with fault-tolerance approaches in robotic systems. Which provides better resilience?",
            "How does the stretch reflex arc (monosynaptic spinal reflex, ~1ms latency) inspire hierarchical control architectures with fast local loops and slower cortical oversight?",
            "A plant exhibits tropism (growing toward resources) on a timescale of hours. How does Active Inference apply to systems with very slow dynamics and long temporal horizons?",
            "Compare the communication strategies of social insects (chemical pheromones) and social mammals (vocalizations, body language) for informing multi-robot communication design.",
            "How does the concept of developmental robotics (robots that grow and mature like biological organisms) challenge the traditional approach of designing fixed robotic systems?",
        ],
    },
    "03_control_estimation": {
        "topic": "Systems",
        "questions": [
            "Compare the state-space representation of a single flexible-joint robot arm with that of a rigid-arm model. How does joint flexibility introduce additional states and what estimation challenges arise?",
            "How does the separation principle from linear control theory (independent estimator and controller design) relate to Active Inference where perception and action are coupled?",
            "A Kalman filter estimates a mobile robot's pose while a PID controller tracks waypoints. Describe how Active Inference unifies these two subsystems under a single free energy objective.",
            "Compare the stability analysis approaches: Lyapunov stability for classical controllers versus free energy bounds for Active Inference controllers. Under what conditions do they yield equivalent guarantees?",
            "How does Model Predictive Control handle state and input constraints? Compare the MPC constraint satisfaction mechanism with the Active Inference treatment of prior preferences as soft constraints.",
            "A manipulator must transition from free-space motion to constrained contact during assembly. How do hybrid control approaches handle this discrete mode switch, and what is the Active Inference equivalent?",
            "Compare the Extended Kalman Filter and the Unscented Kalman Filter for estimating a quadrotor's state during aggressive maneuvers. When does the EKF's linearization assumption fail?",
            "How does the concept of persistent excitation from adaptive control theory relate to epistemic foraging in Active Inference? Both ensure sufficient information for parameter learning.",
            "A robot's dynamics change when it picks up an unknown object. Compare Model Reference Adaptive Control with Active Inference for online adaptation to this payload change.",
            "How does the information filter (inverse covariance form of the Kalman filter) relate to precision-weighted estimation in Active Inference? What computational advantages does each provide?",
            "Compare the computational complexity of batch SLAM (process all measurements at once) with incremental SLAM (process measurements sequentially). How does the choice affect real-time operation?",
            "A consensus algorithm enables multiple robots to agree on a shared state estimate. How does the communication graph topology affect convergence speed and estimate quality?",
            "How does the concept of robust control (H-infinity methods) handle model uncertainty compared to Active Inference's approach of maintaining distributions over model parameters?",
            "Compare computed torque control with impedance control for a robot interacting with humans. How does each approach handle the uncertainty of human motion and compliance?",
            "A network of robots estimates a common target's position using distributed Kalman filtering. How do communication delays and packet losses affect the estimation quality?",
            "How does the concept of dual control (simultaneously learning the system model and controlling it optimally) relate to the unified inference-action framework of Active Inference?",
            "Compare the trajectory optimization approaches of Sequential Quadratic Programming and Model Predictive Path Integral control. What are the convergence and real-time performance characteristics of each?",
        ],
    },
    "04_autonomous_agents": {
        "topic": "Systems",
        "questions": [
            "Compare the autonomy architectures of a Level 4 self-driving vehicle (limited ODD) with a Level 5 vehicle (unrestricted ODD). How does the generative model's scope differ between these levels?",
            "How does the concept of operational design domain (ODD) from autonomous driving constrain what an autonomous robot can safely do? What happens at ODD boundaries?",
            "A fully autonomous Mars rover must operate for months without human intervention. How does the system architecture balance computation, communication, and onboard autonomy?",
            "Compare the BDI (Beliefs, Desires, Intentions) agent framework with Active Inference as architectures for autonomous robot decision making. What does each framework emphasize?",
            "How does the concept of graceful degradation apply when an autonomous robot loses a sensor mid-mission? Design a degradation hierarchy that maintains safety while reducing capability.",
            "A autonomous drone delivery system must handle wind, rain, GPS denial, and airspace conflicts. How does the system architecture layer these challenges across perception, planning, and control?",
            "Compare the safety certification requirements for autonomous systems in different domains: aviation (DO-178C), automotive (ISO 26262), and medical (IEC 62304). How do these standards constrain system design?",
            "How does the concept of runtime monitoring (checking system invariants during execution) complement the generative model's predictions for ensuring safe autonomous operation?",
            "A team of autonomous robots must coordinate to search a collapsed building. How does the multi-agent planning architecture handle communication loss and individual robot failures?",
            "Compare the perception pipelines of autonomous driving (camera + lidar + radar fusion) versus autonomous manipulation (RGB-D camera + tactile sensing). How do the fusion architectures differ?",
            "How does the concept of explainable autonomy help humans trust and oversee autonomous robots? What information must the robot communicate about its decision process?",
            "A autonomous agricultural robot operates 24/7 across seasons. How does the system architecture handle long-term changes in the environment (crop growth, weather patterns, equipment wear)?",
            "Compare the planning approaches for single-robot autonomy (self-contained planning) versus multi-robot autonomy (coordinated planning). What communication and computation trade-offs arise?",
            "How does the concept of continual learning enable autonomous robots to improve their generative models over operational lifetime? What safeguards prevent learned degradation?",
            "A autonomous robot must operate in a human-shared environment following social norms. How does the generative model encode and enforce social constraints on behavior?",
            "Compare the action architectures for autonomous driving (steering, throttle, brake) versus autonomous manipulation (joint torques, gripper commands). How does the action space dimensionality affect planning?",
            "How does the concept of digital twins support the development, testing, and monitoring of autonomous robotic systems throughout their lifecycle?",
        ],
    },
}


def write_questions_file(filepath, title, q1, q2, q3, new_questions):
    """Write a complete questions.md file preserving the first 3 questions and replacing 4-20."""
    lines = [f"# Study Questions: {title}\n"]
    lines.append(f"1.  {q1}\n")
    lines.append(f"2.  {q2}\n")
    lines.append(f"3.  {q3}\n")
    for i, q in enumerate(new_questions, start=4):
        lines.append(f"{i}.  {q}\n")
    lines.append("")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))


def process_questions():
    """Process all questions.md files."""
    count = 0

    # Process submodule-level questions
    for section in SECTIONS:
        for submodule in SUBMODULES:
            filepath = os.path.join(BASE, section, submodule, "questions.md")
            if not os.path.exists(filepath):
                continue

            # Read existing file to get first 3 questions
            with open(filepath, "r") as f:
                content = f.read()

            lines = content.strip().split("\n")
            title_line = lines[0]  # e.g., "# Study Questions: Systems"
            # Extract the topic from the title
            if ":" in title_line:
                title = title_line.split(":", 1)[1].strip()
            else:
                title = SPINE_LABELS.get(submodule, submodule)

            # Extract Q1, Q2, Q3
            q1 = q2 = q3 = ""
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("1."):
                    q1 = stripped[2:].strip()
                    if q1.startswith(" "):
                        q1 = q1.strip()
                elif stripped.startswith("2."):
                    q2 = stripped[2:].strip()
                    if q2.startswith(" "):
                        q2 = q2.strip()
                elif stripped.startswith("3."):
                    q3 = stripped[2:].strip()
                    if q3.startswith(" "):
                        q3 = q3.strip()

            key = (section, submodule)
            if key in QUESTIONS_DATA:
                new_qs = QUESTIONS_DATA[key]
                write_questions_file(filepath, title, q1, q2, q3, new_qs)
                count += 1
                print(f"  Updated: {section}/{submodule}/questions.md")
            else:
                print(f"  MISSING DATA: {section}/{submodule}")

    # Process section-level questions
    for section in SECTIONS:
        filepath = os.path.join(BASE, section, "questions.md")
        if not os.path.exists(filepath):
            continue

        with open(filepath, "r") as f:
            content = f.read()

        lines = content.strip().split("\n")
        title_line = lines[0]
        if ":" in title_line:
            title = title_line.split(":", 1)[1].strip()
        else:
            title = SECTION_LABELS.get(section, section)

        q1 = q2 = q3 = ""
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("1."):
                q1 = stripped[2:].strip()
                if q1.startswith(" "):
                    q1 = q1.strip()
            elif stripped.startswith("2."):
                q2 = stripped[2:].strip()
                if q2.startswith(" "):
                    q2 = q2.strip()
            elif stripped.startswith("3."):
                q3 = stripped[2:].strip()
                if q3.startswith(" "):
                    q3 = q3.strip()

        if section in SECTION_QUESTIONS:
            new_qs = SECTION_QUESTIONS[section]["questions"]
            write_questions_file(filepath, title, q1, q2, q3, new_qs)
            count += 1
            print(f"  Updated: {section}/questions.md (section-level)")
        else:
            print(f"  MISSING SECTION DATA: {section}")

    print(f"\nTotal questions.md files updated: {count}")


if __name__ == "__main__":
    print("=== Processing questions.md files ===")
    process_questions()
    print("\nDone!")
