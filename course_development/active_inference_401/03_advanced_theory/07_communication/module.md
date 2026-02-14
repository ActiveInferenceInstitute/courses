# Module 07: Communication — Multi-Agent Active Inference and Shared Generative Models

> **Course**: Active Inference 401 | **Unit**: Advanced Theory | **Audience**: Graduate students / researchers

## Learning Objectives

1. Analyze the formal framework for **multi-agent Active Inference** — how interacting agents form complex adaptive systems.
2. Evaluate the concept of **shared generative models** — how agents align their models through communication.
3. Examine **collective intelligence** — how group-level inference emerges from individual interactions.

## Key Concepts

### 1. Multi-Agent Active Inference: The Setup

When multiple Active Inference agents interact, each agent's environment includes the other agents. This creates a complex system where each agent is simultaneously:

**Observing** other agents' behavior (sensory states)
**Predicting** other agents' hidden states (beliefs, intentions)
**Acting** on the environment (which includes other agents)

**Recursive modeling**: Agent A models agent B, but agent B's behavior depends on B's model of A. This creates recursive generative models: A has a model of B's model of A. The depth of this recursion determines the sophistication of social cognition (Theory of Mind levels).

**Formal structure**: For N agents, each agent i has:

- Internal states μᵢ parameterizing beliefs qᵢ(η) about the environment
- Active states aᵢ affecting the shared environment
- Sensory states sᵢ carrying information about the shared environment AND other agents' actions

### 2. Shared Generative Models

When agents communicate, their generative models can become aligned:

**Model alignment through communication**: When agent A communicates belief b to agent B, B's generative model is updated to incorporate A's perspective. Over time, repeated communication leads to **shared priors** — common beliefs about the world that both agents hold.

**Cultural generative models**: In human societies, cultural norms, narratives, and institutions function as shared generative models. These models are maintained through ritualized communication (education, media, ritual) and updated through collective experience (social movements, elections, crises).

**Consensus as free energy minimization**: A group of agents reaches consensus when their collective free energy is minimized — when all agents' generative models are mutually consistent. Disagreement = high collective free energy. Consensus = low collective free energy.

### 3. Active Inference Game Theory

Multi-agent scenarios can be analyzed using game-theoretic tools within Active Inference:

**Nash equilibrium recast**: A Nash equilibrium (no agent can improve their payoff by unilaterally changing strategy) corresponds to a joint policy vector π* where no agent can reduce their expected free energy by changing their policy:

∀i: G_i(πᵢ*, π₋ᵢ*) ≤ G_i(πᵢ, π₋ᵢ*) for all πᵢ

**Cooperation as EFE minimization**: Cooperation emerges when agents' generative models include the welfare of other agents in their preferences (C vector). An altruistic agent has preferences that include minimizing others' free energy.

**Signaling**: Communication signals are actions designed to reduce uncertainty in the receiver. The sender acts to produce observations that minimize the receiver's expected free energy — selecting signals that are both informative (high epistemic value) and relevant (high pragmatic value for the receiver).

### 4. Generalized Synchrony and Coupling

When agents interact over time, their dynamics become coupled:

**Generalized synchrony**: Two coupled Active Inference agents may achieve generalized synchrony — their internal states become correlated, not because they share the same observations, but because they are each modeling the other. This is the formal basis for "being on the same wavelength."

**Coupled oscillators**: When Active Inference agents have oscillatory dynamics (as neural systems do), coupling produces phase synchronization, frequency locking, and other coordination phenomena. This connects Active Inference to dynamical systems theory of coordination (Haken, Kelso).

**Stigmergy**: Indirect communication through environment modification. Agent A modifies the environment; Agent B observes the modification and infers A's intentions. This is the mechanism used by ant colonies (pheromone trails) and is formalized as Active Inference where the environment serves as a communication channel.

### 5. Collective Intelligence

When many agents interact, group-level properties emerge:

**Swarm intelligence**: Simple agents following Active Inference individually can produce complex, seemingly intelligent group behavior. Each agent minimizes its own free energy given local information; the aggregate produces global coordination (e.g., flocking, schooling, swarming).

**Social institutions as collective models**: Institutions (governments, markets, scientific communities) are mechanisms for maintaining and updating shared generative models at scale. Their structures (hierarchies, voting mechanisms, peer review) implement specific forms of collective belief updating.

**Cultural evolution as model selection**: Over long timescales, cultural groups whose shared generative models better predict the environment outcompete groups with worse models. This is Bayesian Model Selection at the cultural level.

## Summary

Multi-agent Active Inference formalizes how interacting agents create complex adaptive systems. Shared generative models emerge through communication and are maintained by cultural institutions. Game-theoretic scenarios are recast in free energy terms. Coupled agents achieve generalized synchrony. Collective intelligence emerges from individual free energy minimization with mutual modeling.

## Further Reading

- Friston, K. & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Ramstead, M. J. D. et al. (2019). A tale of two densities: active inference is enactive inference. *Adaptive Behavior*, 28(4), 225-239.
- Veissière, S. P. L. et al. (2020). Thinking through other minds: A variational approach to cognition and culture. *Behavioral and Brain Sciences*, 43, e90.
