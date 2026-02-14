# Station: Perception (Microstructural Evolution)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Topics**: Perception — Microscopy and EBSD as Perceptual Systems
- **Lab Style**: Image Analysis Lab
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Microscopy is perception at the microstructural scale. The microscopist selects an imaging modality (optical, SEM, TEM), sample preparation protocol, and imaging parameters to resolve specific microstructural features. This is active perception: choosing the sensory modality and parameters that maximize the information gained about the hidden microstructural state. EBSD (Electron Backscatter Diffraction) is a particularly rich perceptual system — it generates orientation maps that reveal grain structure, misorientation distributions, and texture, enabling the microscopist to infer the processing history encoded in the microstructure.

## Key Mappings

| FEP Concept | Microscopy Perception Translation |
|-------------|----------------------------------|
| Sensory Data | Micrograph, EBSD orientation map, TEM diffraction pattern |
| Generative Model | Expected microstructure given processing history (grain size, phase distribution, texture) |
| Perceptual Inference | Stereological measurement, grain size analysis, phase fraction quantification |
| Active Perception | Choosing magnification, imaging mode, etchant, or detector to resolve specific features |
| Precision | Spatial resolution (optical: ~1 um, SEM: ~10 nm, TEM: ~0.1 nm), angular resolution of EBSD |
| Multi-Modal Perception | Combining optical microscopy + SEM/EDS + EBSD + TEM for comprehensive microstructural inference |

## Content Guidelines

- Frame sample preparation (grinding, polishing, etching) as a prerequisite perception step that reveals hidden microstructural information
- Treat EBSD scan parameter selection (step size, accelerating voltage, tilt angle) as active sensing optimization
- Connect image segmentation and stereological analysis to perceptual inference — extracting quantitative features from raw sensory data
- Emphasize that each microscopy modality provides a different view of the same underlying microstructural reality, and combining modalities reduces overall uncertainty

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
