# Lab: Multi-Agent Active Inference and Shared Generative Models

> **Learning Goal:** Analyze multi-agent scenarios using Active Inference, exploring coordination, communication, and collective intelligence.

## Part 1: Recursive Modeling Depth

**Exercise**: Consider a conversation between two people (A and B) discussing a controversial topic:

| ToM Level | A's Model | Effect on Behavior |
|-----------|-----------|-------------------|
| Level 0 | A has beliefs about the topic | A states opinions directly |
| Level 1 | A models B's beliefs about the topic | A adjusts message based on B's likely knowledge |
| Level 2 | A models B's model of A's beliefs | A anticipates B's response to A's statement, and pre-addresses objections |
| Level 3 | A models B's model of A's model of B | A considers how B will react to A's anticipation of B's objection |

1. At what level does the recursion become practically useful vs. computationally intractable?
2. How does autism (proposed as reduced ToM depth) affect conversational dynamics?
3. How does Machiavellianism (proposed as deep ToM used for self-serving purposes) use deep recursion?

{fill:textarea}

## Part 2: Game Theory as Active Inference

> **Learning Goal:** Recast classical games in Active Inference terms.

**Exercise**: Analyze the Prisoner's Dilemma using Active Inference:

Two agents each choose: Cooperate (C) or Defect (D). Payoffs: CC=(3,3), CD=(0,5), DC=(5,0), DD=(1,1).

**Standard game theory**: Nash equilibrium = (D, D) — both defect.

**Active Inference reformulation**:

1. Each agent has a generative model of the other agent's likely action
2. Expected free energy for Cooperate = G(C) depends on the predicted probability that the other cooperates
3. Expected free energy for Defect = G(D) depends on the same prediction

If Agent A believes (with high precision) that B will cooperate → A's best policy is Defect (exploiting trust)
If Agent A is uncertain → EFE may favor Cooperate (epistemic value of maintaining relationship)

**Key question**: Under what conditions does cooperation emerge?

- When agents have repeated interactions (iterated PD) — long-term model updating favors cooperation
- When agents' C vectors include social preferences (prosocial preferences)
- When reputation mechanisms provide additional observations about trustworthiness

{fill:textarea}

## Part 3: Shared Model Formation

> **Learning Goal:** Trace how shared generative models form through communication.

**Exercise**: Model the formation of a scientific consensus:

1. **Initial state**: 20 scientists, each with their own generative model of a phenomenon. Models differ significantly.
2. **Communication**: Scientists publish papers (signals encoding their beliefs + evidence)
3. **Model updating**: Each scientist updates their model based on received papers (weighted by precision of the evidence and credibility of the source)
4. **Convergence**: Over multiple rounds, models converge → shared generative model emerges

Map this process:

| Round | Communication Event | Effect on Model Diversity | Collective Free Energy |
|-------|-------------------|--------------------------|----------------------|
| 1 | Initial hypotheses published | High diversity, high collective F | Maximum (conflicting models) |
| 2 | Experimental results shared | Diversity decreases for well-supported views | Decreasing |
| 3 | Review papers synthesize | Further convergence, outliers identified | Declining |
| N | Consensus forms | Low diversity on core claims, ongoing debate at frontiers | Near minimum |

What happens when evidence dramatically contradicts the consensus? (Paradigm shift = collective model revision)

{fill:textarea}

## Part 4: Stigmergic Communication

> **Learning Goal:** Analyze indirect communication through environment modification.

**Exercise**: Model an ant colony foraging task using stigmergy:

1. **Individual agent**: Each ant minimizes free energy given local sensory information (pheromone concentration, food detection)
2. **Active states**: Lay pheromone (strength proportional to food quality), move in direction of pheromone gradient
3. **Collective behavior**: Pheromone trails form between nest and food sources. Shorter paths accumulate more pheromone (faster round-trip). Longer paths lose pheromone to evaporation.
4. **Emergent optimization**: The colony converges on the shortest path — without any ant knowing the global map.

How does this implement: (a) collective inference about food locations, (b) model updating through environmental modification, (c) Bayesian model selection (short path wins)?

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: Multi-agent Active Inference treats human communication as mutual model alignment. But is genuine understanding more than model alignment? When two people deeply understand each other, is something happening beyond having similar generative models?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Recursive analysis | Theory of Mind levels |
| 2 | Game-theoretic reasoning | EFE in strategic interactions |
| 3 | Process tracing | Shared model formation |
| 4 | Collective behavior | Stigmergic communication |
| 5 | Philosophical reflection | Understanding vs. alignment |
