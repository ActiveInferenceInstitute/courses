# Section 04: Computational Active Inference

## Learning Objectives

1. Build a complete Active Inference agent with A, B, C, D, and E matrices using the `active_inference` library, distinguishing the generative process (environment) from the generative model (agent's beliefs).
2. Implement state estimation through variational belief updating, policy selection through expected free energy computation, and online parameter learning through Dirichlet concentration updates.
3. Design and run multi-agent simulations where agents observe and influence each other, demonstrating emergent communication and coupled inference.
4. Construct deep temporal models for planning over extended time horizons using sophisticated inference and recursive belief updating.

## Introduction

Computational Active Inference translates the philosophical concepts, neural mechanisms, and mathematical equations of the preceding sections into running code. This section implements every component of the Active Inference framework in Python, using a custom `active_inference` library inspired by pymdp. Students build agents from scratch — defining generative models, running belief updates, selecting policies, learning parameters, communicating with other agents, and planning over extended horizons.

The fundamental insight that drives this entire section is the distinction between the **generative process** (the real causal structure of the environment, encoded in `DiscreteEnvironment`) and the **generative model** (the agent's approximation, encoded in `GenerativeModel` with A, B, C, D, and E matrices). The mismatch between these two is what drives perception, action, and learning. If the model perfectly matched the process, free energy would be zero and the agent would have nothing left to learn.

## Key Concepts

### 1. The A-E Matrix Framework

The discrete-state Active Inference agent is specified by five matrices: **A** (likelihood — how hidden states generate observations), **B** (transitions — how states evolve under each action), **C** (preferences — which observations the agent prefers), **D** (initial state prior — what the agent believes about its starting state), and **E** (habits — a prior over policies independent of expected free energy). Together, these five matrices define the agent's complete generative model and fully determine its behavior.

### 2. Variational Belief Updating

Perception in Active Inference is implemented as fixed-point iteration over the recognition density. Given an observation and the current belief about states, the agent alternates between computing the expected log-likelihood under current beliefs and updating beliefs to reduce free energy. This process converges to an approximate posterior that balances prior expectations against sensory evidence, weighted by their respective precisions.

### 3. Expected Free Energy and Policy Selection

The agent evaluates candidate policies by computing the expected free energy G for each one. G decomposes into risk (how far predicted outcomes deviate from preferences encoded in C) and ambiguity (how much information the action is expected to reveal). The softmax function converts these G values into a probability distribution over policies, with the precision parameter gamma controlling the exploration-exploitation balance.

### 4. Parameter Learning and Model Structure

Beyond updating beliefs about states (perception), Active Inference agents can update beliefs about their model's parameters. Dirichlet concentration parameters pA and pB accumulate evidence about the true likelihood and transition matrices, enabling online learning. Bayesian Model Reduction provides a principled method for pruning unnecessary model complexity, effectively implementing Occam's razor.

## Applications

* **The T-Maze Benchmark**: The canonical T-maze task provides a concrete demonstration of exploration-exploitation tradeoff. One arm of the maze contains a reward and the other a punishment, with a cue location that reveals which arm is correct. Computing expected free energy for "go to cue" versus "go directly to arm" policies shows how epistemic value (information gain) drives the agent to seek information before committing — the computational equivalent of curiosity.

* **Multi-Agent Signaling Games**: Two Active Inference agents can be coupled such that one agent's actions become another's observations. In signaling games, agents develop emergent communication protocols — one agent learns to signal which state it observes, and the other learns to interpret those signals. This demonstrates how communication arises naturally from coupled free energy minimization without requiring explicit language design.

## Conclusion

The Computational section closes the loop of the Active Inference curriculum. Every concept introduced philosophically (Section 01), grounded neurally (Section 02), and derived mathematically (Section 03) is here rendered as executable Python code. The custom `active_inference` library with its 56 exports, 253 tests, and 28 visualization functions provides a complete toolkit for building, running, and analyzing Active Inference agents. Students completing this section will be able to implement any discrete-state Active Inference problem from specification to simulation.
