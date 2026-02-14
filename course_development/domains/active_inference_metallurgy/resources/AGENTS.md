# Resources — Agent Guidelines

> **Quick Navigation**: [Resources README](./README.md) | [Course AGENTS](../AGENTS.md)

## Overview

The resources directory provides shared reference materials that ensure consistency across all 32 modules of the Active Inference for Metallurgy curriculum. These resources serve as the canonical source of truth for notation, terminology, references, and cross-course linkages.

## Conventions

- All shared resources must use consistent terminology as defined in `glossary.md`
- All notation must follow `notation_table.md`
- References must follow APA format as established in `references.md`
- Cross-course links must reference specific module paths, not generic placeholders

## Resource Maintenance Rules

1. **Glossary entries** must include both the Active Inference definition and the metallurgical translation. Every term used in module content should have a glossary entry.
2. **Notation table** entries must specify the symbol, its meaning in both the FEP framework and in thermodynamics/metallurgy, and the units where applicable.
3. **References** should prioritize foundational texts: Friston (2010) for FEP, Porter & Easterling for phase transformations, Callister & Rethwisch for materials science fundamentals, and Parr et al. (2022) for Active Inference.
4. **Cross-course map** entries should identify the specific Active Inference concept, the module where it appears, and the parallel treatment in other domain courses (e.g., robotics, organizations).
5. **Learning pathways** should offer at least three routes: (a) the linear sequence through all four units, (b) a thermodynamics-first pathway for physical metallurgists, and (c) a process-first pathway for manufacturing engineers.

## Thermodynamic-Inferential Dual Notation

When a symbol appears in both thermodynamic and inferential contexts, the glossary and notation table must clearly distinguish them:

| Symbol | Thermodynamic Meaning | Inferential Meaning |
|--------|----------------------|---------------------|
| F | Helmholtz free energy (J) | Variational free energy (nats) |
| G | Gibbs free energy (J) | Generative model |
| mu | Chemical potential (J/mol) | Mean of variational distribution |
| sigma | Stress (MPa) | Standard deviation of belief distribution |
| S | Entropy (J/K) | Surprise (-log p(y)) |
