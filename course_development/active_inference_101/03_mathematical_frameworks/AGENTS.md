# Course AGENTS: Mathematical Frameworks

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: Mathematical Frameworks
- **Number**: 3
- **Perspective**: Probability, information theory, variational methods
- **Lab Type**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible. Full mathematical notation. Python/NumPy. Textbook-quality.

## Content Guidelines

This course develops the mathematical foundations of Active Inference, moving from probability theory through information theory to variational methods. All content should:

1. **Build mathematics incrementally**: Start from probability basics (random variables, Bayes' theorem) and develop toward variational free energy and expected free energy. No step should assume mathematical knowledge beyond introductory calculus and linear algebra.
2. **Connect every equation to intuition**: Every mathematical expression should be accompanied by a plain-language explanation and a concrete example. The goal is for students to understand both the formalism and its meaning.
3. **Define mathematical notation precisely**:
   - **P(o, s)**: Joint probability of observations and hidden states -- the generative model
   - **q(s)**: The approximate posterior -- the agent's best guess about hidden states
   - **F[q]**: Variational free energy -- the quantity the agent minimizes
   - **G(pi)**: Expected free energy of policy pi -- the quantity guiding action selection
   - **D_KL(q || p)**: KL divergence -- the information-theoretic distance between two distributions
4. **Use the POMDP framework**: Partially Observable Markov Decision Processes provide the concrete mathematical scaffolding for Active Inference. All modules should reference the A, B, C, D matrices.
5. **Include worked examples**: Every new concept should include a fully worked numerical example that students can follow step by step.

## Lab Design Principles

Labs in this course are **problem set** format:

- Provide structured mathematical problems with increasing difficulty
- Include numerical exercises that can be solved by hand or with a calculator
- Use `{fill:textarea}` for showing work and explaining reasoning
- Connect each problem to the Active Inference concepts from the module

## Question Standards

- Questions should test mathematical reasoning, not just formula recall
- Include derivation questions ("show that...") alongside computation questions
- Require students to interpret mathematical results in terms of Active Inference concepts

## References

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.
