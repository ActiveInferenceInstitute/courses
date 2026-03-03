# Module 03: Perception — Computer Vision and Sensor Fusion

## Learning Objectives

1. Explain how a computer "sees" using **pixel arrays**, **feature extraction**, and **convolutional neural networks (CNNs)**.
2. Define **sensor fusion** as the combination of multiple data streams to reduce uncertainty.
3. Connect computer vision to Active Inference: sensory processing as Bayesian inference on images.

## Introduction

How does a self-driving car "see" a stop sign? How does your phone unlock with your face? Computer vision is the technology of giving machines the ability to interpret visual information. This module explores how machines perceive — and how their perception systems mirror the Active Inference framework.

## Key Concepts

### 1. Images as Data

A digital image is a grid of numbers. A 1080p photo is 1920 × 1080 pixels, each with three color values (Red, Green, Blue). That is over 6 million numbers. The challenge of perception is: how do you transform 6 million raw numbers into the useful statement "there is a stop sign 30 meters ahead"?

### 2. Feature Extraction and CNNs

A **Convolutional Neural Network (CNN)** solves this by learning a hierarchy of features:

- **Layer 1**: Detects edges (horizontal, vertical, diagonal lines)
- **Layer 2**: Combines edges into textures and shapes (corners, curves)
- **Layer 3**: Combines shapes into objects (a red octagon = stop sign)

This hierarchy mirrors the brain's visual cortex: V1 detects edges, V2 detects textures, V4 detects shapes, and IT detects objects. In Active Inference terms, each layer generates predictions of what the layer below will send, and the difference is the prediction error signal that drives learning.

### 3. Sensor Fusion

A self-driving car does not rely on cameras alone. It fuses data from:

- **Cameras** (visual detail, color, read signs)
- **LIDAR** (precise 3D distance measurements)
- **Radar** (detects objects in fog and rain)
- **GPS** (global position)
- **IMU** (acceleration and rotation)

Each sensor provides a *different view* of the same world. **Sensor fusion** combines them using Bayesian inference: sensors with high precision (low noise) are weighted more heavily. This is exactly how Active Inference weights high-precision sensory channels.

## Applications

- **Face Recognition**: Your phone's Face ID uses a structured light sensor to project 30,000 infrared dots on your face, building a 3D map. It compares this map to its stored model. If the prediction error is below a threshold, it unlocks.
- **Medical Imaging**: AI-powered radiology uses CNNs trained on millions of X-rays. The AI detects patterns (tumors, fractures) that are too subtle for the human eye — but it can also make confident false alarms if its training data was biased.

## Discussion Questions

1. Why might a self-driving car's camera-based perception fail in heavy rain, even though its LIDAR works fine? How does sensor fusion help?
2. Face recognition AI has been shown to have higher error rates on certain skin tones. How does biased training data create biased generative models?

## Summary

Computer perception transforms raw sensor data into meaningful representations through feature hierarchies. CNNs process images the way the visual cortex does. Sensor fusion combines multiple data streams using Bayesian inference. These technologies implement Active Inference principles at scale.

## References

- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. Chapter 9.
