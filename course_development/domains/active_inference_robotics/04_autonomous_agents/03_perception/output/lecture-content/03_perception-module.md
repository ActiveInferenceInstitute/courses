# Module 03: Perception in Robotics — Autonomous Sensing

## Learning Objectives

1. Define **autonomous perception** as the capacity of a robot to build and maintain a comprehensive world model from its own sensor data without human labeling or supervision.
2. Analyze how **SLAM, object detection, and semantic segmentation** implement the perception component of autonomous Active Inference.
3. Apply the concept of **perceptual robustness** to understand failure modes of autonomous perception systems.

## Introduction

An autonomous robot perceives the world not through a single sensor or a single algorithm, but through a **multi-modal, multi-scale perceptual system** that constructs and maintains a rich internal model of the environment. This model must support navigation (where am I, where can I go?), interaction (what objects are here, what can I do with them?), and prediction (what will happen next?).

## Key Concepts

### 1. SLAM: Simultaneous Localization and Mapping

**SLAM** is the canonical perception problem of autonomous robotics — building a map of an unknown environment while simultaneously tracking the robot's position within that map:

- **Visual SLAM**: Uses camera images to extract features (ORB-SLAM, LSD-SLAM), track them across frames, and triangulate 3D structure
- **LiDAR SLAM**: Uses laser scans to match geometric features and build 3D point cloud maps
- **Graph SLAM**: Represents the pose history as a graph and optimizes the entire trajectory when loop closures are detected

In Active Inference terms, SLAM is joint inference over the hidden state (robot pose) and model parameters (map) — simultaneously estimating where you are and what the world looks like, using the consistency between observations across time as the binding constraint.

### 2. Object Detection and Recognition

Autonomous robots must identify and classify objects in their environment:

- **Detection**: Where in the sensor data is there an object? (bounding boxes, segmentation masks)
- **Recognition**: What kind of object is it? (car, person, chair, obstacle)
- **Pose estimation**: Where is the object in 3D space, and what is its orientation?

Modern deep learning approaches (YOLO, Mask R-CNN, PointNet) implement high-dimensional likelihood models — the A matrix mapping from hidden object properties (type, position, orientation) to pixel patterns or point cloud features, learned from large datasets.

### 3. Semantic Mapping

**Semantic mapping** extends SLAM by labeling the geometric map with semantic categories:

- The map contains not just "there is a surface at coordinates (x, y, z)" but "this surface is a sidewalk (traversable), this is a wall (non-traversable), this is a door (openable)"
- Semantic labels provide **affordance information** directly — the map tells the planner what actions are available at each location
- Active Inference interpretation: semantic mapping enriches the generative model with categorical hidden states that support richer policy evaluation

### 4. Perceptual Failure Modes

Autonomous perception systems fail in predictable ways:

- **Adversarial conditions**: Sun glare, fog, heavy rain, snow degrade visual and LiDAR perception — precision drops, uncertainty grows
- **Out-of-distribution objects**: The perception model was trained on specific object categories; novel objects (an overturned shopping cart, a large bird, a construction sign) may be misclassified or missed entirely
- **Sensor degradation**: Lens fouling, mechanical misalignment, electromagnetic interference reduce sensor quality
- **Perceptual aliasing**: Two different locations look identical to the sensors (identical corridors, repeated architectural features), causing the agent to confuse its position

Robust autonomous systems detect perceptual failure through **meta-perceptual monitoring** — tracking the confidence of their own perceptual estimates and triggering conservative behavior when confidence drops.

## Applications

- **Last-mile delivery robot**: A sidewalk delivery robot uses visual-inertial SLAM for localization, semantic segmentation to distinguish sidewalk from street from grass, and pedestrian detection to avoid collisions — all integrated into a single perception pipeline that feeds the navigation planner.
- **Underwater inspection**: An autonomous underwater vehicle inspecting bridge pilings uses sonar SLAM (visual perception is degraded by turbidity) combined with learned defect detection — identifying cracks, corrosion, and biofouling from sonar returns.

## Conclusion

Autonomous perception — SLAM, object recognition, semantic mapping, and robustness monitoring — provides the foundation for self-governing robotic action. The perceptual system constructs and maintains the generative model that all other components (cognition, action, planning) depend on. The next module examines autonomous cognition.
