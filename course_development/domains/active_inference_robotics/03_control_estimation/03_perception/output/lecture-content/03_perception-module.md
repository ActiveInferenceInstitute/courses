# Module 03: Perception in Robotics — Sensor Processing for Control

## Learning Objectives

1. Define robotic **perception for control** as the extraction of task-relevant state information from raw sensor data.
2. Analyze how different sensor modalities (vision, LiDAR, tactile, force/torque) implement the observation model (A matrix) for control applications.
3. Apply the concept of **observation design** — choosing and configuring sensors to maximize the informativeness of observations for the control task.

## Introduction

Control requires perception — a robot cannot control what it cannot observe. But perception for control is different from perception in general: it is **task-directed**. A robot arm performing assembly doesn't need to understand the entire visual scene — it needs to know the position and orientation of the part it's assembling. A mobile robot doesn't need to identify every object — it needs to know where obstacles are and where traversable space is.

## Key Concepts

### 1. Sensor Modalities and Their A Matrices

Each sensor modality implements a different observation model:

- **Encoders** (joint position sensors): Simple, direct A matrix — the observation is a noisy linear function of the joint angle. High precision, low ambiguity.
- **IMU** (Inertial Measurement Unit): Provides acceleration and angular velocity. The A matrix involves integrating these to get position and orientation — introducing drift (accumulating noise). Moderate precision, needs fusion.
- **Camera**: Rich, high-dimensional observations (millions of pixels). The A matrix involves 3D-to-2D projection, lighting variation, and occlusion. High ambiguity — many different 3D scenes can produce similar 2D images.
- **LiDAR**: Provides direct distance measurements in a scan pattern. The A matrix is geometric (ray casting). Low ambiguity for geometry, but no color or texture information.
- **Force/Torque sensors**: Measure contact forces at end-effectors. The A matrix relates hidden contact states (friction, material stiffness, contact geometry) to observed force vectors.

### 2. Feature Extraction as Dimensionality Reduction

Raw sensor data is high-dimensional; control requires low-dimensional state estimates. Feature extraction bridges this gap:

- **Visual features**: Edges, corners, SIFT/ORB keypoints, deep-learned features — reduce a megapixel image to hundreds of task-relevant descriptors
- **Point cloud processing**: Down-sampling, plane fitting, object segmentation of LiDAR data — reduce millions of 3D points to geometric primitives
- **Tactile feature extraction**: Contact location, normal force, friction coefficient from distributed tactile arrays

In Active Inference terms, feature extraction is **model-based dimensionality reduction** — the generative model specifies which aspects of the observation are relevant for the current inference task, and the feature extractor computes sufficient statistics.

### 3. Observability and Sensor Selection

Not all states are observable from all sensors. **Observability analysis** determines which states can be estimated from the available observations:

- A camera alone cannot observe depth at a single frame (unobservable) — but with structure from motion (multiple frames + known motion), depth becomes observable
- An encoder alone cannot detect external contact forces — but combined with a dynamics model and motor current measurements, contact can be inferred
- **Sensor selection** is the engineering decision about which A matrices to implement — choosing sensors that make the task-relevant states observable

### 4. Active Perception for Control

When perception is insufficient for the current control task, the robot can take **epistemic actions** — actions chosen to improve state estimation:

- A robot arm unsure about an object's pose can rotate the object to bring distinguishing features into view
- A mobile robot unsure about its location can move to a landmark-rich area to improve localization
- A manipulation robot unsure about an object's weight can lift it slightly to generate diagnostic force observations

These are Active Inference epistemic actions — reducing expected ambiguity through deliberately informative behavior.

## Applications

- **Visual servoing**: A robot arm uses real-time camera feedback to align with a target — the controller directly minimizes visual prediction error (the difference between the observed and desired image features), bypassing explicit 3D state estimation entirely.
- **Tactile slip detection**: A gripper monitors shear force patterns to detect incipient slip — when the tactile prediction error exceeds a threshold (force pattern deviates from stable-grasp model), the controller increases grip force before the object falls.

## Conclusion

Perception for control transforms raw sensor data into task-relevant state estimates through sensor-specific A matrices, feature extraction, observability analysis, and active perception. The next module examines the cognitive processing that builds on these perceptual estimates.
