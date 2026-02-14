# Station: Systems (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: Python environment setup, NumPy arrays, probability distributions in code, generative model class, model validation
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module sets up the computational toolkit for Active Inference implementation. Content should:

1. **Provide complete environment setup**: Python installation, virtual environment creation, package installation (NumPy, SciPy, matplotlib, pymdp). Assume students have basic Python experience.
2. **Define key implementation concepts**:
   - **NumPy array**: The fundamental data structure for representing probability distributions and matrices in Active Inference code
   - **Normalization**: Ensuring probability vectors sum to 1 using `x / x.sum()`
   - **Log-stable computation**: Using `np.log(x + eps)` to avoid log(0) = -inf errors
   - **Softmax function**: Converting log-probabilities to probabilities: `exp(x - max(x)) / sum(exp(x - max(x)))`
3. **Build core utility functions**: normalize, log_stable, softmax, entropy, kl_divergence. These are reused throughout the course.
4. **Implement the GenerativeModel class**: A clean Python class encapsulating A, B, C, D matrices with methods for likelihood and transition queries.

## Active Inference Integration

- The code structures directly mirror the mathematical formalism from the Mathematical Frameworks course
- Each NumPy array corresponds to a specific component of the POMDP generative model
- The validation functions ensure the model satisfies the constraints required for valid Active Inference

## Assessment Alignment

Questions should test the ability to:
- Write correct NumPy code for basic probability operations (normalization, softmax, KL divergence)
- Construct a valid GenerativeModel object for a simple scenario
- Debug common errors in probability code (non-normalized distributions, shape mismatches)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
