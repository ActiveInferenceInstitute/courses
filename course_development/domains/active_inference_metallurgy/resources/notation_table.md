# Notation Table: Active Inference for Metallurgy

> Standard symbols and notation used throughout the curriculum.
> This curriculum uses **moderate technical notation** — equations are present but always grounded in physical meaning.
> Where formal notation is introduced, it is always accompanied by a metallurgical parallel.

---

## Core Symbols

| Symbol / Concept | Plain English | Formal Meaning | Metallurgical Translation | First Introduced |
| --- | --- | --- | --- | --- |
| **System** | A thing with a boundary | An entity with internal and external states separated by a Markov blanket | A crystal, grain, phase region, or manufacturing process with defined boundaries | C1 M1 |
| **Agent** | Something that acts to achieve a state | A system that minimizes free energy through perception and action | An atom, defect, nucleus, or sensor-controller pair pursuing equilibrium or target properties | C1 M2 |
| **Prediction** | A guess about what will happen | Expected observation under the generative model | Phase diagram prediction, process model forecast, expected hardness | C1 M3 |
| **Prediction Error** | When reality ≠ expectation | Difference between predicted and actual observations | Off-target composition, unexpected phase fraction, process deviation | C1 M3 |
| **Surprise** | An unexpected outcome | Negative log probability of an observation under the model | Unexpected failure, anomalous microstructure, weld defect | C1 M3 |
| **Action** | Making something happen | Changing the world to match predictions | Phase transformation, deformation, heat treatment, quenching | C1 M5 |
| **Learning** | Getting better over time | Updating model parameters based on prediction error | Alloy database refinement, CALPHAD assessment, process optimization | C1 M6 |
| **G (Gibbs free energy)** | Energy available for work at constant T, P | G = H − TS | Governs phase stability, drives transformations | C1 M1 |
| **ΔG** | Free energy change | G_products − G_reactants | Driving force for phase transformation | C1 M5 |
| **ΔG*** | Critical nucleation barrier | (16π γ³) / (3 ΔG_v²) | Energy barrier a nucleus must overcome to grow | C3 M2 |
| **Markov Blanket** | Boundary between inside and outside | Statistical partition into internal, external, sensory, and active states | Grain boundary, phase interface, system boundary | C1 M1 |
| **Free Energy (Variational)** | Tension or misalignment | Upper bound on surprise; divergence between model and reality | Gap between predicted and actual microstructure or properties | C1 M1 |
| **Precision** | Confidence in a signal | Inverse variance of a probability distribution | Measurement resolution, instrument accuracy, model confidence | C1 M3 |
| **Expected Free Energy** | How good a plan looks | Combined pragmatic + epistemic value of a future action | Expected outcome of a processing route considering both properties and learning | C4 M8 |
| **D (Diffusivity)** | Rate of atomic migration | D = D₀ exp(−Q/RT) | Governs mass transport, homogenization, precipitation kinetics | C2 M7 |
| **Policy** | Plan of action | Sequence of actions selected to minimize EFE | Processing route: melt → cast → roll → heat treat → finish | C4 M8 |
| **Nested Systems** | Systems within systems | Hierarchical Markov blankets at multiple scales | Atoms → grains → phases → components → assemblies | C3 M1 |
| **Prior** | What we believe before new evidence | Prior probability distribution | Established phase diagram, handbook property value | C1 M4 |
| **Posterior** | Updated belief after new evidence | Posterior probability distribution | Revised phase boundary after new experimental data | C1 M4 |

---

## Diagrammatic Conventions

Throughout the curriculum, diagrams use these conventions:

| Element | Representation | Example |
| --- | --- | --- |
| Markov blanket boundary | Dashed border | Grain boundary diagram, phase interface |
| Information flow (sensory) | Arrow **into** the system | Heat flux, chemical potential gradient |
| Information flow (active) | Arrow **out of** the system | Latent heat release, diffusing species |
| Internal states | Nodes inside the boundary | Crystal structure, defect configuration |
| External states | Nodes outside the boundary | Temperature field, applied stress |
| Prediction error | Red highlighted gap | Expected vs. actual phase fraction |
| Free energy minimization | Downward-pointing arrow | ΔG driving transformation |

---

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Home](../README.md)
