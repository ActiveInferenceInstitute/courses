# Station: Planning (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Planning — TTT and CCT Diagram Planning
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

TTT (Time-Temperature-Transformation) and CCT (Continuous Cooling Transformation) diagrams are policy maps for heat treatment planning. Each cooling trajectory through temperature-time space represents a different policy, and the resulting microstructure is the policy outcome. The metallurgist plans by evaluating counterfactual cooling paths: "If I quench to this temperature and hold for this duration, what phases will form?" This is planning as inference — using the generative model (transformation kinetics) to simulate future outcomes and select the policy that achieves the desired microstructure. Hardenability (Jominy) testing provides empirical calibration of these planned policies.

## Key Mappings

| FEP Concept | TTT/CCT Planning Translation |
|-------------|------------------------------|
| Policy Space | Set of all possible cooling trajectories through T-t space |
| Policy Evaluation | Predicting phase fractions for a given cooling path using TTT/CCT overlay |
| Expected Free Energy | Predicted microstructure quality + remaining uncertainty about transformation kinetics |
| Planning Horizon | Cooling path duration; number of isothermal hold steps |
| Counterfactual | "What microstructure would result from a different cooling rate?" |
| Optimal Policy | Cooling path that produces the target hardness/microstructure (e.g., full martensite, tempered bainite) |

## Content Guidelines

- Frame the TTT diagram as a map of the policy landscape — each point represents a transformation state achievable by a specific policy
- Treat Jominy hardenability testing as empirical policy evaluation — the end-quench test samples a continuous range of cooling rates in a single experiment
- Connect continuous cooling transformation to policy execution under real-world constraints (finite heat transfer, non-isothermal paths)
- Emphasize that multi-step heat treatments (e.g., austempering, Q&P) are sequential policies where each step's outcome constrains the next step's options

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
