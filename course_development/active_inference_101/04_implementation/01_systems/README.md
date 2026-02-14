# Module 01: Systems

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Setting Up the Active Inference Toolkit

Part of **Implementation & Simulation** -- this module sets up the Python environment and core data structures for implementing Active Inference agents.

## Learning Objectives

By the end of this module, students will be able to:

1. **Set up** a Python environment with NumPy, SciPy, matplotlib, and pymdp for Active Inference implementation
2. **Implement** core utility functions (normalize, log_stable, softmax, entropy, kl_divergence) in NumPy
3. **Construct** a GenerativeModel class encapsulating A, B, C, D matrices with proper validation
4. **Debug** common probability code errors: non-normalized distributions, shape mismatches, numerical instability
5. **Compare** the code data structures with their mathematical definitions from the Math Frameworks course

## Prerequisites

- Mathematical Frameworks Module 01: Systems (probability, generative models)
- Basic Python programming experience (variables, functions, arrays)

## Key Concepts

- **NumPy array**: The fundamental data structure for probability distributions and matrices
- **Normalization**: Ensuring probability vectors sum to 1
- **Log-stable computation**: Avoiding log(0) errors with epsilon offsets
- **Softmax function**: Converting log-probabilities to valid probability distributions
- **GenerativeModel class**: Python class encapsulating the POMDP components

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Setting Up the Active Inference Toolkit |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Building the Active Inference Toolkit in Python |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Heins, C. et al. (2022). pymdp: A Python library for active inference. *JOSS*, 7(73), 4098.
- NumPy documentation: <https://numpy.org/doc/>
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
