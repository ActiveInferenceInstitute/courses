# Module 02: Agents in Comedy

## Learning Objectives

1. Model Abbott and Costello as distinct inference agents with competing **generative models**.
2. Distinguish between the straight man's high-precision priors and the comic's volatile model.
3. Formalize the audience as a third inference agent that tracks both performers' beliefs.

## Introduction

Every comedy routine has at least two agents. In "Who's on First?", they are magnificent: Abbott, the straight man, radiating implacable certainty; Costello, the comic, spiraling through escalating bewilderment. But they are not just characters — they are *inference engines*. Each maintains a generative model of the world, takes actions based on that model, and processes observations from the environment. The tragedy (and the comedy) is that they are running incompatible models on identical observations.

In Active Inference, an **agent** is any entity bounded by a Markov blanket that maintains beliefs about hidden states and acts to minimize its expected free energy. Abbott is an agent. Costello is an agent. And sitting out in the dark, watching both, the audience is a third agent — the one that holds the whole system in its inferential gaze.

## Key Concepts

### 1. Abbott as High-Precision Agent

Abbott knows the players' names. Who is on first. What is on second. I Don't Know is on third. His generative model has extremely high **precision** — the inverse variance of his beliefs. When Abbott says "Who's on first," he is not asking a question. He is stating a fact with maximum confidence.

In Active Inference terms, Abbott's prior belief P(name = "Who" | position = first base) has precision approaching infinity. This means his model is essentially non-negotiable. No amount of counter-evidence from Costello will cause Abbott to revise his belief. This is not stubbornness — it is an agent whose model is correct and whose precision is appropriately high.

Abbott's high precision serves a critical comedic function: he is the **fixed point** of the routine. Without a stable reference, Costello's confusion would have no contrast. The straight man's immovability is what makes the comic's volatility legible.

### 2. Costello as Volatile-Model Agent

Costello enters the exchange with a perfectly reasonable generative model: words mean what they usually mean. "Who" is a question word. "What" is a question word. "I Don't Know" is an expression of ignorance. His model has moderate precision — he is reasonably confident in his understanding of English.

But every observation he receives at the Markov blanket (every answer Abbott gives) is *consistent with his model and simultaneously wrong*. When Abbott says "Who's on first," Costello's model parses this as a question — "Who is on first?" — and generates an appropriate response: "That's what I want to find out."

Costello's precision fluctuates wildly. Sometimes he seems to almost grasp the situation (his precision on the name-interpretation rises), but then another confusing exchange crashes it back down. He is an agent trapped in a region of belief space where the likelihood mapping is degenerate: the same observations are consistent with two incompatible hypotheses, and his model cannot disambiguate.

### 3. The Audience as Meta-Inference Agent

The audience is the most sophisticated inference agent in the system. They track:

- **Abbott's internal state**: They know (or quickly infer) that "Who" is a name. They model Abbott as a high-precision agent who is stating facts.
- **Costello's internal state**: They infer that Costello interprets "Who" as a question. They model Costello as a confused agent with a wrong but reasonable model.
- **The gap**: The audience holds both models simultaneously. They can see the mismatch that neither performer (within the fiction of the routine) can see. This is **theory of mind** operating at full capacity — maintaining multiple, conflicting models of other agents.

The audience's laughter occurs when the gap between the two agents' models becomes salient — when a specific exchange makes the incompatibility vivid. The audience is not surprised by the routine's existence (they chose to watch it); they are surprised by the *specific local form* the incompatibility takes in each exchange.

## Applications

- **Straight Man / Comic as Precision Contrast**: The straight-man/comic dynamic is one of the oldest structures in comedy, from vaudeville to modern sitcoms. In every case, it maps to a precision contrast: one agent holds high-precision priors (the "normal" one), and the other has volatile or miscalibrated priors (the "funny" one). The comedy arises from the prediction errors generated at the interface between these precision profiles.

- **Solo Performers as Multi-Agent Systems**: A stand-up comedian performing alone is still a multi-agent system. They are simultaneously the narrator (high precision, telling the story) and the characters they portray (varying precision, sometimes confused). The comedian switches between agentive roles, and the audience tracks all of them.

## Conclusion

Abbott and Costello are not just performing a routine — they are running competing inference engines on the same sensory data. Abbott's engine is precise and correct; Costello's is reasonable and wrong. The audience runs a meta-inference engine that tracks both. The comedy is an emergent property of this multi-agent system: it arises not from any single agent's state, but from the *relations* between their models. In the next module, we examine how perception works in this system — how the phoneme sequence "Who" is parsed by different agents with different models.
