# Station: Perception (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Perception — X-Ray Diffraction and Spectroscopic Sensing
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Characterization techniques are the sensory modalities of metallurgical inference. X-ray diffraction (XRD) generates sensory data (diffraction patterns) that the metallurgist inverts through a generative model (Bragg's law, structure factors) to infer hidden states (crystal structure, lattice parameters, phase fractions). Energy-dispersive spectroscopy (EDS) and X-ray photoelectron spectroscopy (XPS) perform chemical perception — sensing elemental composition as evidence for updating beliefs about alloy stoichiometry. Every measurement is an act of perceptual inference: raw signal in, updated belief out.

## Key Mappings

| FEP Concept | Characterization Translation |
|-------------|----------------------------|
| Sensory Data | XRD pattern, EDS spectrum, XPS binding energy peaks |
| Generative Model | Bragg's law, structure factor calculations, characteristic X-ray emission lines |
| Perceptual Inference | Rietveld refinement (fitting model to diffraction data to infer crystal structure) |
| Prediction Error | Residual between measured and calculated diffraction pattern (R-factor) |
| Precision | Instrument resolution, signal-to-noise ratio, counting statistics |
| Active Perception | Choosing scan range, step size, dwell time to resolve specific structural features |

## Content Guidelines

- Frame Rietveld refinement explicitly as variational inference: iteratively updating model parameters to minimize the weighted residual (prediction error)
- Connect instrument precision (detector resolution, beam quality) to the precision weighting of sensory signals in Active Inference
- Treat wavelength-dispersive spectroscopy (WDS) vs. EDS as different precision regimes for the same underlying chemical perception task
- Emphasize that Bragg's law is a generative model — it predicts where peaks should appear given a crystal structure hypothesis

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
