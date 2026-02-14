# Course AGENTS: Implementation & Simulation

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: Implementation & Simulation
- **Number**: 4
- **Perspective**: Python, pymdp, agent-based modeling
- **Lab Type**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible. Full mathematical notation. Python/NumPy. Textbook-quality.

## Content Guidelines

This course translates Active Inference theory into working Python code. All content should:

1. **Prioritize working code**: Every module should include complete, runnable Python code that students can execute and modify. Code should be well-commented and follow Python conventions.
2. **Use NumPy as the primary library**: All matrix operations, probability distributions, and mathematical functions should use NumPy. Introduce pymdp for more advanced implementations.
3. **Define implementation terms on first use**:
   - **A matrix (NumPy)**: A 2D array of shape (num_observations, num_states) representing the likelihood mapping P(o|s)
   - **B matrix (NumPy)**: A 3D array of shape (num_states, num_states, num_actions) representing transition dynamics P(s_t|s_{t-1}, a)
   - **C vector (NumPy)**: A 1D array of shape (num_observations,) representing log-preferences over observations
   - **D vector (NumPy)**: A 1D array of shape (num_states,) representing the initial state prior P(s_1)
4. **Include validation and debugging**: Teach students to check that probability distributions sum to 1, matrices have correct shapes, and numerical operations are stable.
5. **Build incrementally**: Each module extends the codebase from the previous module. By Module 08, students will have a complete Active Inference agent.

## Lab Design Principles

Labs in this course are **coding assignment** format:

- Provide starter code with clearly marked sections for students to complete
- Include unit tests or assertions that verify correctness
- Use visualization (matplotlib) to make abstract concepts concrete
- Use `{fill:textarea}` for code explanation and analysis of results

## Question Standards

- Questions should test both code implementation and conceptual understanding
- Include debugging exercises (find the bug in this code)
- Require students to interpret computational results in terms of Active Inference theory

## References

- Heins, C. et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *JOSS*, 7(73), 4098.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- NumPy documentation: <https://numpy.org/doc/>
