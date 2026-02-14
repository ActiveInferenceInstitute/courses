# Station: Systems (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Systems — Manufacturing Process as Inference System
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

A manufacturing process (furnace, rolling mill, AM build chamber) is a bounded inference system. The furnace walls, chamber atmosphere, and temperature controls define the Markov blanket that separates the process interior (internal states: material temperature, phase fractions, stress distribution) from the external environment (ambient conditions, upstream supply chain, downstream requirements). The process boundary mediates all energy and material exchange. Each process unit can be treated as an autonomous inference system within the larger manufacturing chain, with inputs (raw material, energy) and outputs (processed material, waste heat) crossing the Markov blanket.

## Key Mappings

| FEP Concept | Manufacturing System Translation |
|-------------|----------------------------------|
| Markov Blanket | Furnace walls, build chamber, rolling stand housing, weld pool boundary |
| Internal States | Material temperature profile, phase fraction evolution, residual stress |
| External States | Ambient temperature, incoming material composition, energy supply |
| System Identity | Process unit maintaining its operating envelope despite disturbances |
| Nested Systems | Sensor < process unit < production line < factory (ISA-95 hierarchy) |
| System Boundary Integrity | Process containment, atmosphere control, thermal insulation |

## Content Guidelines

- Frame each process unit as maintaining its own steady state (the process equivalent of self-organization) despite disturbances from raw material variability, ambient conditions, and equipment wear
- Treat the ISA-95 manufacturing hierarchy as nested Markov blankets: each level infers and acts at its characteristic timescale
- Connect process boundaries to energy and mass balance equations — the Markov blanket conditions correspond to conservation laws at the process boundary
- Emphasize that additive manufacturing (LPBF, DED) represents a particularly clean example: the melt pool is a highly localized inference system with precisely defined boundaries

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
