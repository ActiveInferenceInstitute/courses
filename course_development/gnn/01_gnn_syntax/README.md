# Module 01: GNN Syntax

> **Quick Navigation**: [Track Home](../README.md) | [Curriculum Home](../../README.md) | [Models](./models/README.md)

## Reading a Generative Model as Plain Text

Part of the **GNN Syntax Track** — this module introduces Generalized Notation
Notation (GNN) and walks through a complete, real exemplar from the GNN
exemplar corpus.

## Learning Objectives

By the end of this module, students will be able to:

1. **Explain** why an implementation-agnostic notation for generative models is
   useful (the "triple play" of text, graph, and executable forms)
2. **Identify** every required section of a GNN file and state what it declares
3. **Read** the Static Perception Model exemplar and explain each variable,
   connection, and parameter
4. **Compute** the perception update the exemplar describes for concrete
   observations
5. **Map** the shipped exemplars to course levels and describe what each level
   adds

## Prerequisites

- For the guided reading: comfort with fractions and percentages (middle school
  level and up)
- For the hand computation: Bayes' rule in the form `posterior ∝ prior × likelihood`
- For the pipeline lab: a local checkout of the
  [GNN repository](https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation)

## Key Concepts

- **GNN**: a plain-text notation for generative models, organized into named
  sections
- **State space block**: declares each variable with dimensions and type
- **Initial parameterization**: the numeric values the model starts from
- **Ontology annotation**: declares what each symbol means in this model
- **Triple play**: one specification, read as text, drawn as a graph, and
  executed as code
- **Pipeline steps 3, 5, 11, 12**: parse, type-check, render, execute

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lesson: GNN Syntax — Reading a Generative Model as Plain Text |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (7 multiple choice + 3 short answer) |
| [lab.md](./lab.md) | Lab: Reading and Running a GNN Specification |
| [models/](./models/README.md) | Five GNN exemplars copied from GNN v5.0.3, mapped to course levels |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Smékal, J., & Friedman, D. A. (2023). *Generalized Notation Notation for
  Active Inference Models.* Zenodo. <https://zenodo.org/records/7803328>
- Active InferAnt Stream 014.1, *Generalized Notation Notation: From Plaintext
  to Triple Play* (2025). <https://www.youtube.com/watch?v=3tYOBVIOLyU>
- Active InferAnt Stream 014.2, *Generalized Notation Notation for Generative
  Model Supply Chains* (2025). <https://www.youtube.com/watch?v=Y3-FMoaEZYE>

## Resources

- [GNN exemplar index](https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation/blob/main/input/gnn_files/INDEX.md) — the full corpus this module samples from
- [Core curriculum notation table](../../active_inference/resources/notation_table.md) — the A–E matrix conventions used across courses
- [Core curriculum glossary](../../active_inference/resources/glossary.md)
