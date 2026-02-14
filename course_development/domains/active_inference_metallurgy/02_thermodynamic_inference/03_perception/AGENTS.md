# Station: Perception (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Perception — Thermal Analysis and Calorimetric Sensing
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Thermal analysis instruments (DSC, DTA, dilatometry) are perception systems that detect phase transformations through their thermal or dimensional signatures. A DSC measures heat flow as a function of temperature — each exothermic or endothermic peak is sensory evidence of a phase transformation event. The metallurgist interprets these peaks through a generative model (expected transformation temperatures from the phase diagram) and updates beliefs about the actual transformation behavior. When the observed peak temperature deviates from the predicted equilibrium temperature, this prediction error carries information about transformation kinetics, undercooling, or heating rate effects.

## Key Mappings

| FEP Concept | Thermal Analysis Translation |
|-------------|----------------------------|
| Sensory Data | DSC heat flow curve, DTA temperature difference, dilatometry length change |
| Generative Model | Phase diagram predicting transformation temperatures at given composition |
| Prediction Error | Deviation between observed and predicted transformation temperature |
| Perceptual Inference | Identifying transformation onset, peak, and endpoint from thermal trace |
| Precision | Instrument sensitivity (mW resolution), heating rate, sample mass |
| Active Perception | Varying heating/cooling rate to resolve overlapping transformations |

## Content Guidelines

- Frame DSC baseline subtraction as separating signal (transformation enthalpy) from noise (instrument drift, heat capacity background)
- Treat heating rate variation as active sensing — slower rates give better temperature resolution but lose kinetic information
- Connect transformation enthalpy measurement to quantifying the Gibbs energy change (the thermodynamic prediction error that drove the transformation)
- Emphasize that dilatometry senses phase transformations through volume change, providing a complementary perceptual modality to calorimetric sensing

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
