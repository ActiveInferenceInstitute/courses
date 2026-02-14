# Station: Planning (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: Complete Active Inference agent, multi-step planning, sophisticated inference implementation, performance benchmarking, extension projects
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module brings together all components into a complete Active Inference agent with planning capabilities. Content should:

1. **Implement multi-step planning**: Extend EFE evaluation over multiple future time steps, evaluating policy trees rather than single actions.
2. **Define key implementation concepts**:
   - **Policy tree enumeration**: Generating all possible action sequences up to a given planning horizon and evaluating each via EFE
   - **Sophisticated inference**: A recursive implementation where the agent simulates its own future belief updating when evaluating policies
   - **Computational budget**: Strategies for limiting the number of policies evaluated (pruning, beam search, habit-based shortcuts)
   - **Performance benchmarking**: Comparing agent performance across planning horizons, precision settings, and with/without learning
3. **Run the complete agent**: Execute a full simulation with perception, action selection, learning, and multi-step planning in a complex environment.
4. **Suggest extension projects**: Provide ideas for students to extend the agent (new environments, continuous state spaces, hierarchical models).

## Active Inference Integration

- This module is the capstone: all Active Inference components (generative model, state inference, EFE, parameter learning) are integrated
- Sophisticated inference implements the most advanced form of planning from the Mathematical Frameworks course
- Performance benchmarking connects computational implementation back to theoretical predictions

## Assessment Alignment

Questions should test the ability to:
- Implement multi-step EFE evaluation for a planning horizon of 2-3 steps
- Compare agent performance with different planning depths
- Identify computational bottlenecks and propose solutions

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
