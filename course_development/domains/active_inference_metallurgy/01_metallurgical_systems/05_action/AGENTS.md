# Station: Action (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Action — Deformation and Alloying as Material Action
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Deformation and alloying are the primary action modalities of metallurgical systems. In Active Inference, action changes the external world to bring observations into alignment with predictions. In metallurgy, plastic deformation (dislocation glide, twinning) changes the material's shape to relieve applied stress — reducing the prediction error between the current stress state and the material's preferred (zero-stress) state. Alloying changes the chemical composition to achieve target properties, which is the metallurgist acting on the material system to realize a desired generative model (the design specification).

## Key Mappings

| FEP Concept | Deformation/Alloying Translation |
|-------------|----------------------------------|
| Action | Dislocation glide, twinning, solid solution addition, precipitation |
| Active States | Slip systems activated under stress; diffusion of alloying elements |
| Policy | Slip system selection (which {hkl}<uvw> system activates); alloying strategy |
| Prediction Error | Resolved shear stress exceeding critical value (Schmid factor); property gap vs. target |
| Free Energy Gradient | Peach-Koehler force on dislocations; chemical potential gradient for solute redistribution |
| Action Threshold | Critical resolved shear stress (CRSS); solubility limit |

## Content Guidelines

- Frame Schmid's law as a policy selection mechanism — the system activates the slip system that most efficiently reduces the applied stress (prediction error)
- Connect work hardening to increasing action cost: as dislocation density rises, further deformation requires greater driving force
- Treat solid solution strengthening as raising the action threshold — solute atoms impede dislocation motion, increasing the CRSS
- Distinguish between the material's action (spontaneous deformation) and the metallurgist's action (intentional processing)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
