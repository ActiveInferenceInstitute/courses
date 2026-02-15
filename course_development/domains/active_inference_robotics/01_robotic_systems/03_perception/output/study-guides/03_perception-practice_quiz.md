# Practice Quiz: Perception in Robotic Systems

## Part A: Multiple Choice

1. In Active Inference, robotic perception is best understood as:
A) Passive data recording from sensors
B) Active Bayesian inference -- inverting a generative model to infer world states from sensory observations
C) Simply converting analog signals to digital values
D) Transmitting raw sensor data to a cloud server

**Answer: B** -- Perception is generative model inversion: given observations, the robot infers the most probable world state. This is fundamentally Bayesian -- combining prior beliefs with sensor likelihoods to produce posterior beliefs about the environment.

2. A Velodyne VLP-16 lidar produces approximately 300,000 points per second. What makes lidar well-suited for Kalman-filter-based fusion?
A) Its high cost
B) Its well-characterized, approximately Gaussian noise model and precise range measurements
C) Its ability to measure temperature
D) Its inability to detect obstacles

**Answer: B** -- Lidar's noise model is well-characterized and approximately Gaussian (typically +/- 3 cm), making it naturally compatible with Kalman filter assumptions. Its direct range measurements provide precise geometric information about the environment.

3. Why do IMU-based orientation estimates drift over time?
A) The IMU battery runs out
B) Small biases in the gyroscope integrate into growing orientation errors
C) The accelerometer measures color instead of acceleration
D) Drift is a feature, not a bug

**Answer: B** -- Gyroscope biases, even when very small, accumulate through integration over time. This is why IMUs must be fused with other sensors (lidar, visual odometry) that provide absolute reference corrections.

4. Sensor fusion in Active Inference is accomplished by:
A) Physically connecting sensors with wires
B) Combining multiple sensor likelihood functions with a prior using Bayes' rule, weighted by each sensor's precision
C) Choosing the single best sensor and ignoring others
D) Averaging all sensor readings equally regardless of reliability

**Answer: B** -- Each sensor provides a likelihood function over the world state. Bayes' rule combines these likelihoods, weighted by their precision (inverse variance), with a dynamics prior. Sensors with higher precision exert more influence on the fused estimate.

5. Active perception (epistemic foraging) in robotics refers to:
A) Perceiving only when the battery is fully charged
B) Selecting actions specifically to reduce perceptual uncertainty before committing to task execution
C) Using only active sensors like lidar, never passive sensors like cameras
D) Perceiving the environment only once at startup

**Answer: B** -- An Active Inference agent selects actions to reduce uncertainty when the epistemic term of expected free energy dominates. For example, a manipulator moves its wrist camera closer to an object to reduce depth uncertainty before attempting a grasp.

6. Perceptual aliasing occurs when:
A) A sensor produces readings above its maximum range
B) Different world states produce identical sensory observations, making them indistinguishable
C) Two sensors are manufactured by the same company
D) The robot has too many sensors

**Answer: B** -- A robot navigating a corridor with identical-looking intersections cannot distinguish its location from visual appearance alone. The generative model maps multiple distinct positions to the same observation, requiring additional modalities or temporal context to resolve.

7. When a mobile robot drives from a smooth floor onto gravel, how should precision weighting change?
A) All sensors should be weighted equally regardless of conditions
B) Wheel odometry precision drops (more slip), so lidar should receive higher weighting
C) Lidar precision drops, so odometry should receive higher weighting
D) Both sensors should be turned off

**Answer: B** -- On gravel, wheel slip increases odometry noise, reducing its precision. The Kalman filter (or Active Inference agent) should automatically downweight odometry and upweight lidar scan matching, which remains accurate regardless of terrain.

8. What causes model mismatch failures in robotic perception?
A) Using too many sensors simultaneously
B) The world deviating from the generative model's assumptions -- e.g., a static-world model encountering moving objects
C) Having perfectly calibrated sensors
D) Using the most expensive sensors available

**Answer: B** -- A lidar navigation system that models the world as static will misinterpret moving objects (people, forklifts) as jumps in the robot's own position, because the prediction errors violate the model's stationarity assumption.

9. In the expected free energy decomposition, what drives a robot to gather information before acting?
A) The pragmatic term (achieving preferred outcomes)
B) The epistemic term (reducing uncertainty about hidden states)
C) The robot's preference for expensive sensors
D) External commands from a human operator

**Answer: B** -- When uncertainty is high, the epistemic term dominates expected free energy, driving the agent to explore and gather information. This provides a principled mechanism for balancing exploration (reducing uncertainty) and exploitation (achieving goals).

10. An Extended Kalman Filter (EKF) used for robot localization is, from an Active Inference perspective:
A) Completely unrelated to free energy minimization
B) A specific approximation scheme for variational free energy minimization using Gaussian posteriors and linearized dynamics
C) Superior to Active Inference in all respects
D) Only applicable to biological systems

**Answer: B** -- The EKF approximates the posterior with a Gaussian distribution and propagates it through linearized dynamics. This is a specific case of variational inference where the approximate posterior family is Gaussian -- a particular scheme for minimizing variational free energy.

## Part B: Short Answer and Design Prompts

1. Design a sensor suite for an agricultural robot that must navigate between rows of crops, identify ripe fruit, and avoid irrigation equipment. For each sensor, describe its generative model (what it predicts) and its characteristic noise properties.

2. A mobile robot's lidar-based localization system works well in a structured office but fails in a large, featureless parking garage. Using Active Inference concepts, explain why the failure occurs and propose a multi-sensor solution.

3. Explain how a robot arm performing bin picking could use active perception (epistemic foraging) to resolve ambiguity about overlapping objects. What sequence of camera viewpoints would minimize expected free energy?

4. Compare factor graph optimization (as used in SLAM systems) with the Extended Kalman Filter as approximation methods for variational free energy minimization. What are the strengths and limitations of each?

5. How would an Active Inference robot handle sensor degradation -- for example, a camera becoming partially occluded by mud during outdoor operation? Describe the expected behavior in terms of precision weighting and model updating.
