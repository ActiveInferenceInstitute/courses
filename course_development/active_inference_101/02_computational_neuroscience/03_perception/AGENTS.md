# Station: Perception (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Predictive coding in cortex, mismatch negativity, repetition suppression, neural precision, sensory cortex hierarchy
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module grounds predictive processing in neural circuitry. Content should:

1. **Present predictive coding as a neural algorithm**: The brain implements Bayesian inference through a specific neural architecture where predictions flow top-down and prediction errors flow bottom-up through cortical layers.
2. **Define key terms precisely**:
   - **Predictive coding**: A neural implementation where cortical areas generate predictions about input from the level below and receive prediction errors when those predictions fail
   - **Mismatch negativity (MMN)**: An ERP component generated when a stimulus violates a predicted pattern, serving as neural evidence for predictive coding
   - **Repetition suppression**: Decreased neural response to repeated stimuli, reflecting successful prediction and reduced prediction error
   - **Neural precision**: The gain (amplification) applied to prediction error units, modulated by neuromodulators
3. **Use electrophysiology evidence**: Cite EEG (MMN, P300), fMRI (repetition suppression), and single-unit recording studies.
4. **Connect precision to neuromodulation**: Acetylcholine boosts sensory precision; dopamine boosts prior precision.

## Active Inference Integration

- Predictive coding is the canonical neural process theory of Active Inference (Rao & Ballard, 1999; Friston, 2005)
- Prediction error minimization is implemented through recurrent message passing in cortical hierarchies
- Precision weighting maps onto gain modulation of prediction error units via neuromodulators

## Assessment Alignment

Questions should test the ability to:
- Explain mismatch negativity as evidence for predictive coding
- Describe the neural circuit for a single level of predictive coding (predictions down, errors up)
- Predict the effect of manipulating neuromodulators on perceptual inference

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
