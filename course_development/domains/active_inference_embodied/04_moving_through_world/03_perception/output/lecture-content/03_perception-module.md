# Module 03: Perception in Embodied Cognition — Perceiving While Moving

## Learning Objectives

1. Define **perception during locomotion** as a dynamically modulated inference process that adapts to the demands of ongoing movement.
2. Analyze how **optic flow, haptic ground contact, and auditory spatial cues** contribute to world perception during active movement.
3. Apply the Active Inference framework to explain how movement enhances perception and perception guides movement.

## Introduction

Perception while moving is fundamentally different from perception while stationary. The visual field flows, the vestibular system signals acceleration, footfalls generate tactile and auditory feedback, and proprioceptive signals change continuously. The moving agent doesn't merely process this torrent of information — it *uses* its own movement as a perceptual tool, actively generating diagnostic sensory flows that reveal environmental structure.

## Key Concepts

### 1. Motion Parallax and Depth Perception

Self-movement generates **motion parallax** — nearby objects appear to move faster across the visual field than distant objects:

- This provides robust depth information without stereo vision or prior knowledge of object size
- The agent can actively modulate parallax information by changing speed or head position — lateral head movements during locomotion (visible in many bird species) are epistemic actions that enhance depth inference
- In Active Inference, motion parallax is exploited by a generative model that predicts visual flow speed as a function of distance and self-velocity — deviations from predicted flow speed generate prediction errors that update the depth estimate

### 2. Haptic Ground Perception

Each footfall provides a rich stream of haptic information:

- **Surface compliance**: Hard concrete vs. soft sand vs. springy turf produce different force-displacement profiles — the foot "reads" the surface through mechanical interaction
- **Surface texture**: Gritty, smooth, slippery, or sticky surfaces generate distinctive tactile patterns at the foot-ground interface
- **Structural integrity**: An experienced hiker can assess whether a rock is stable through the subtle yielding (or lack thereof) felt during initial weight loading — a haptic prediction error of "more give than expected" signals instability

The moving agent builds a terrain model from sequential footfall observations — each step is a percept that updates the spatial model of surface properties along the path.

### 3. Auditory Spatial Perception

Sound provides spatial information that complements vision during movement:

- **Echolocation**: Footfall echoes in enclosed spaces provide information about room size, wall distance, and ceiling height — blind pedestrians exploit this actively
- **Surface identification**: The sound of footfalls on different surfaces (the click of tile, the crunch of gravel, the silence of carpet) provides auditory observation of surface type
- **Source localization**: Moving toward or away from a sound source changes its intensity, timing, and spectral properties — the agent's movement modulates the auditory observation, enabling active auditory inference

### 4. Perceptual-Motor Coupling

Perception and movement are not sequential (perceive THEN act) but **coupled** (perceive WHILE acting, act WHILE perceiving):

- Visual fixation during walking is not random — the eyes land on the surface approximately two steps ahead, providing predictive terrain information for foot placement planning
- Head stabilization during locomotion (the vestibulo-ocular reflex) ensures that visual perception remains stable despite body oscillation — an active stabilization that enables high-quality visual inference during movement
- Gait modification based on visual perception (stepping over obstacles, navigating around puddles) demonstrates continuous perceptual-motor coupling

## Applications

- **Blind navigation training**: Orientation and mobility training for blind individuals systematically develops non-visual perceptual skills — using echolocation, haptic ground reading, and auditory spatial cues to build a navigational generative model that supports independent mobility.
- **Trail running perception**: A trail runner perceives the trail through continuous perceptual-motor coupling — visual terrain scanning (2-3 steps ahead), haptic foot feedback (surface traction), and peripheral motion detection (branch movement signaling wildlife) are all integrated in real time, with movement speed modulating the required perceptual processing rate.

## Conclusion

Perception during movement is enriched by the sensory consequences of self-motion — optic flow, haptic ground contact, auditory spatial cues, and the continuous coupling between perception and action. The next module examines cognition during world-engaged movement.
