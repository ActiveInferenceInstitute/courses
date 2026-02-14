# Module 04: Cognition in 101

## Learning Objectives

1.  Define **Cognition** within the context of 101.
2.  Analyze how Cognition interacts with other components of the Active Inference framework.
3.  Apply specific constraints of 101 to the formal definition of Cognition.

## Introduction

This module explores **Cognition**. In the **101** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Cognition is a critical component of the 8-part Active Inference spine, bridging the gap between Mathematical Frameworks and course synthesis.

This final unit brings everything together through implementation. Having established the conceptual foundations (Cognitive Science), the neural substrates (Computational Neuroscience), and the formal mathematics (Mathematical Frameworks), students now build working Active Inference agents in code. The focus is on translating theory into practice: writing generative models, implementing belief updating, and running simulations that demonstrate perception, decision-making, learning, and planning. Students will use Python-based toolkits and will see firsthand how the equations from Unit 3 produce intelligent behavior when run on a computer.

The eight modules in this unit walk through the full implementation pipeline. You will implement system boundaries and state spaces, define agent architectures with explicit generative models, code perceptual inference loops, build cognitive evaluation of competing hypotheses, implement action selection via expected free energy, add learning through parameter updates, enable multi-agent communication through shared models, and cap the course with a planning module that evaluates policies over temporal horizons. By the end, you will have a complete, working Active Inference agent.

## Key Concepts

### 1. Cognition as a Markov Blanket Boundary
How does Cognition define the boundary between the agent and the environment?

### 2. Generative Models of Cognition
What parameters involved in Cognition must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Cognition drive the perception-action loop?

## Applications

In 101, we see Cognition manifest in:
*   **Specific Example 1**: Implementing a simple Active Inference agent that navigates a grid world. The agent maintains a categorical generative model over its position and the locations of rewards. At each time step, it evaluates a set of policies (move up, down, left, right, or stay) by computing the expected free energy for each, which balances the pragmatic value of reaching the reward (exploiting what it knows) against the epistemic value of visiting unobserved cells (exploring to reduce uncertainty). Students implement the belief update equations in Python, using NumPy arrays for the state-transition matrices and observation likelihoods, and can visualize how the agent's posterior beliefs about its location evolve over time. This exercise connects the mathematical formalism of Unit 3 to observable, debuggable behavior.
*   **Specific Example 2**: Building a predictive coding network for handwritten digit recognition using the MNIST dataset. Students implement a two-layer hierarchical generative model where the top layer encodes digit identity (0-9) and the bottom layer generates pixel intensities. Cognition in this context is the inference process: given a handwritten image, the network iteratively passes prediction errors upward and predictions downward until it converges on a digit classification. Students compare the network's performance and internal dynamics with a standard feedforward classifier, observing how the Active Inference approach naturally handles occluded or noisy digits by leveraging its generative model to "fill in" missing information.

## Conclusion

Understanding Cognition allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
