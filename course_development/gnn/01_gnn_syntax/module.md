# GNN Syntax: Reading a Generative Model as Plain Text

## Introduction

Every Active Inference model in this curriculum is, at bottom, a set of
commitments: which states exist, how they produce observations, how they change,
and what the agent prefers. Writing those commitments down once, in a form that
humans can read and software can check, is the job of **Generalized Notation
Notation (GNN)**.

GNN is a plain-text, Markdown-based notation for specifying generative models.
It was introduced by Smékal and Friedman (2023) as an *interlingua* for Active
Inference: a single specification that can be rendered into multiple
implementation frameworks instead of being written three times as prose,
diagrams, and code. The authors call this the **triple play**: one plain-text
model, expressed as text, as a graphical model, and as an executable
simulation.

This lesson teaches you to read a GNN file section by section, using a real
exemplar from the GNN project's own exemplar corpus — the
[Static Perception Model](./models/static_perception.md), the simplest complete
specification in the corpus. You will then see where each section goes as the
specification travels through the GNN processing pipeline, and which exemplars
match which level of this curriculum.

> **This track is supplementary.** It is not one of the fourteen 8-topic spiral
> courses. It is a skills track that supports them: the Core curriculum's
> Computer Science unit builds its own `active_inference` library, and this
> track shows the notation layer above such implementations.

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. **Explain** what GNN is and why an implementation-agnostic notation for
   generative models is useful (the triple play).
2. **Identify** the required sections of a GNN file and state what each one
   declares.
3. **Read** a complete GNN exemplar — the Static Perception Model — and explain
   each variable, connection, and parameter in it.
4. **Compute** the perception update the exemplar describes for a concrete
   observation, by hand.
5. **Describe** what the GNN pipeline does with a specification at steps 3, 5,
   11, and 12, and **map** the shipped exemplars to course levels.

---

## Key Terms

| Term | Definition |
|------|------------|
| **Generalized Notation Notation (GNN)** | A plain-text notation for specifying Active Inference generative models, organized into named sections such as state space, connections, and initial parameterization (Smékal & Friedman, 2023). |
| **Generative model** | The agent's internal model of how hidden states cause observations and how states evolve. |
| **State space block** | The GNN section that declares every variable with its dimensions and type, for example `A[2,2,type=float]`. |
| **Likelihood matrix `A`** | The matrix `A[o,s] = P(o | s)`: the probability of observation `o` given hidden state `s`. |
| **Transition matrix `B`** | The tensor describing how hidden states evolve, `B[next_state, previous_state, action]` when actions are declared. |
| **Prior `D`** | The initial belief over hidden states before any observation. |
| **Preference vector `C`** | The agent's preferences over observations, used when planning is required. |
| **Ontology annotation** | The GNN section that asserts what each variable *means* in the model's vocabulary (`A=LikelihoodMatrix`), separating a symbol from its interpretation. |
| **Triple play** | The GNN goal of moving one specification between plain text, graphical, and executable computational forms. |

---

## Core Concepts

### 1. Why a notation for generative models?

Active Inference research models are usually communicated through a mixture of
prose, equations, pseudo-code, and figures. Each channel is useful, but none of
them is *checkable*: a reader cannot run the prose, and a reader of the code
cannot easily see which part of the math it implements.

GNN's proposal is to make the specification itself a first-class artifact: a
structured plain-text file that declares the model, from which other
representations are derived. Smékal and Friedman (2023) motivate this as a way
to "bridge and respect gaps among different modeling approaches," so that
models specified once can be compared, rendered, and executed across
frameworks. The same idea is the theme of the Institute's two Active InferAnt
Stream episodes on GNN — [Episode 014.1, "From Plaintext to Triple
Play"](../../youtube/active-inferant-stream/17_active-inferant-stream-014-1-generalized-notation-notation/module.md)
and [Episode 014.2, "Generative Model Supply
Chains"](../../youtube/active-inferant-stream/18_active-inferant-stream-014-2-generalized-notation-notation/module.md).

### 2. The anatomy of a GNN file

A GNN file is a Markdown document with a fixed sequence of `##` sections. The
exemplar corpus uses this structure:

| Section | What it declares |
|---------|------------------|
| `GNNSection` | The model family tag (for example `ActInfPOMDP`). |
| `GNNVersionAndFlags` | The notation version (`GNN v1`). |
| `ModelName` | A short, unique name for the model. |
| `ModelAnnotation` | Free-text description of what the model demonstrates. |
| `StateSpaceBlock` | Every variable, with dimensions and type: `A[2,2,type=float]`. |
| `Connections` | Which variables influence which (`D>s`, `s-A`, `A-o`). |
| `InitialParameterization` | The numeric values the matrices start from. |
| `Equations` | The inference or update equations the model implies. |
| `Time` | Whether the model is static or dynamic, and its time horizon. |
| `ActInfOntologyAnnotation` | What each symbol means: `A=LikelihoodMatrix`. |
| `ModelParameters` | Counts and conventions (number of states, tensor order). |
| `Footer`, `Signature` | Provenance line and a signature placeholder. |

Two conventions deserve attention. First, the **state space block separates
declaration from value**: dimensions and types live in the block, numbers live
in the initial parameterization, so a reader can see the *shape* of a model
before its arithmetic. Second, the **ontology annotation separates a symbol
from its meaning**. The letter `A` is not welded to "likelihood matrix"; the
file asserts that for this model, `A` means `LikelihoodMatrix`. That is what
makes localization and multi-model comparison possible — the notation is stable
while the interpretation is declared.

### 3. A real exemplar, in full

Here is the complete Static Perception Model from the GNN v5.0.3 exemplar
corpus, reproduced unmodified from
[`models/static_perception.md`](./models/static_perception.md):

```markdown
# GNN Example: Static Perception Model

# GNN Version: 1.0

# Simplest possible GNN model: perception with a minimal action/transition component
# (action/transition added for POMDP/pymdp rendering compatibility)

## GNNSection

ActInfPOMDP

## GNNVersionAndFlags

GNN v1

## ModelName

Static Perception Model

## ModelAnnotation

The simplest Active Inference model demonstrating pure perception:

- 2 hidden states mapped to 2 observations via a likelihood matrix A
- Prior D encodes initial beliefs over hidden states
- Minimal 2-action transition component B so the model is a complete POMDP
  for optional compatibility; perception itself requires no action planning
- Suitable as a minimal baseline and for testing perception-only inference

## StateSpaceBlock

# Generative model parameters

A[2,2,type=float]    # Likelihood matrix: P(observation | hidden state)
B[2,2,2,type=float]  # Transition matrix: B[next_state, previous_state, actions]
C[2,type=float]      # Preference vector over observations
D[2,1,type=float]    # Prior belief over hidden states

# Hidden state

s[2,1,type=float]    # Hidden state (posterior belief)

# Observation

o[2,1,type=int]      # Observation (one-hot encoded)

# Action

u[1,type=int]        # Action taken

## Connections

D>s
s-A
A-o
s-B
B>u
u>s

## InitialParameterization

# Asymmetric sensor: P(o=0|s=0)=0.9; P(o=1|s=1)=0.8

A={
  (0.9, 0.2),
  (0.1, 0.8)
}

# Minimal transitions: action 0 = stay, action 1 = flip state. The transition tensor B is stored as (next_state, previous_state, action); per-action slices are column-stochastic: rows are next states, columns are previous states, and each column sums to 1 over next states.

B={
  ( (0.95, 0.05), (0.05, 0.95) ),
  ( (0.05, 0.95), (0.95, 0.05) )
}

# Neutral preference over observations

C={(0.0, 0.0)}

# Uniform prior over hidden states

D={(0.5, 0.5)}

## Equations

A[o,s] = P(o | s). For the single observation o, Bayesian perception is
q(s) = D[s] A[o,s] / sum_j D[j] A[o,j]. Equivalently, for one-hot o,
q = softmax(log D + log(A^T o)). A is a likelihood, not a posterior Q(s|o).

The optional transition component uses B[next,previous,action]. Action 0
stays with probability 0.95; action 1 flips with probability 0.95.
For a chosen action u, the predicted next-state belief is
q_next = B[:,:,u] q.

An actual next state is sampled according to
P(s_next | s,u) = B[:,s,u].
Neutral C does not make
active planning necessary for this static perception baseline.

## Time

Static

## ActInfOntologyAnnotation

A=LikelihoodMatrix
B=TransitionMatrix
C=PreferenceVector
D=Prior
s=HiddenState
o=Observation
u=Action

## ModelParameters
b_tensor_order: next_state_previous_state_action

num_hidden_states: 2
num_obs: 2
num_actions: 2
num_timesteps: 5

## Footer

Static Perception Model v1 - GNN Representation.
Simplest possible Active Inference model.
Minimal action/transition component added for POMDP/pymdp compatibility.

## Signature

Cryptographic signature goes here
```

Read the file in the order it is written: the annotation says what the model
demonstrates; the state space block says what exists; the connections say what
influences what; the initial parameterization says where the numbers start; the
equations say what the model computes; the ontology annotation says what the
symbols mean. Nothing in the file is implementation-specific. There is no
Python, no Julia, and no framework import.

### 4. From plain text to executable: the processing pipeline

The GNN project ships a 25-step processing pipeline (steps 0–24) that consumes
specifications like the one above. Four steps carry the specification from text
to a running simulation:

| Step | Module | What it does with the spec |
|------|--------|----------------------------|
| 3 | `gnn` | Discovers and parses every model file, writing parsed artifacts. |
| 5 | `type_checker` | Checks declared dimensions, types, and consistency; estimates resources. |
| 11 | `render` | Generates framework code (PyMDP, JAX, RxInfer.jl, and others) from the parsed spec. |
| 12 | `execute` | Runs the rendered scripts and records execution results. |

A minimal run over a folder of specifications:

```bash
python src/gnn/main.py --target-dir input/gnn_files/basics --only-steps "3,5,11,12"
```

Steps 3 and 5 are pure text processing: they require no simulator. Step 11 and
step 12 depend on which frameworks the local environment provides, and a
framework that cannot represent a model reports `unsupported` rather than
producing a wrong simulation. That distinction — checked, rendered, executed —
is exactly the triple play the notation was designed for.

### 5. Which model for which course level

The five exemplars shipped with this lesson are mapped to levels of the
curriculum. The mapping is by *conceptual demand*, not by age label alone:

| Level | Exemplar | Why this model |
|-------|----------|----------------|
| Elementary / Family | *(none shipped)* | These levels work with stories, drawings, and movement; GNN is a text notation and is not introduced. |
| Middle school (guided) | [`static_perception.md`](./models/static_perception.md) | Reading a 2×2 table of fractions; perception as inference. |
| High school | [`dynamic_perception.md`](./models/dynamic_perception.md) | Adds time: beliefs update as observations arrive. |
| College 101 | [`simple_mdp.md`](./models/simple_mdp.md) | Adds decisions: a minimal Markov decision process with actions. |
| Core curriculum | [`actinf_pomdp_agent.md`](./models/actinf_pomdp_agent.md) | The canonical full Active Inference agent with A–E matrices. |
| Advanced 401 | [`dirichlet_likelihood_learning.md`](./models/dirichlet_likelihood_learning.md) | Adds learning: Dirichlet concentration updates of parameters. |

Each file is a verbatim copy from the GNN v5.0.3 exemplar corpus at commit
`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`; provenance and verification
commands are in [`models/README.md`](./models/README.md).

---

## Examples

### Example 1: Reading the likelihood matrix

The Static Perception Model declares `A[2,2,type=float]` and gives:

```text
A={
  (0.9, 0.2),
  (0.1, 0.8)
}
```

The model's equations fix the convention: `A[o,s] = P(o | s)`. So the rows are
observations and the columns are hidden states:

- `P(o = 0 | s = 0) = 0.9` and `P(o = 1 | s = 0) = 0.1` (column 0 sums to 1)
- `P(o = 0 | s = 1) = 0.2` and `P(o = 1 | s = 1) = 0.8` (column 1 sums to 1)

The sensor is asymmetric: it is more reliable when the state is 0 than when the
state is 1. That asymmetry is a property of the *model*, stated in one place,
rather than a detail buried in an implementation.

### Example 2: Computing the perception update by hand

Suppose the agent has the uniform prior `D = (0.5, 0.5)` and observes `o = 0`.
The exemplar's equation gives:

```text
q(s) = D[s] · A[o,s] / Σ_j D[j] · A[o,j]
```

Numerator for `s = 0`: `0.5 × 0.9 = 0.45`. Numerator for `s = 1`:
`0.5 × 0.2 = 0.10`. The denominator is `0.45 + 0.10 = 0.55`. So:

- `q(s = 0) = 0.45 / 0.55 ≈ 0.818`
- `q(s = 1) = 0.10 / 0.55 ≈ 0.182`

After seeing `o = 0`, the agent believes state 0 with probability about 0.818.
Repeating with `o = 1` gives `q ≈ (0.111, 0.889)`. This is the entire content of
"perception" in the simplest model: a prior, a likelihood, and Bayes' rule.
Everything else in Active Inference — transitions, actions, policies, learning —
is added to this motif one piece at a time.

### Example 3: What the pipeline adds

Point the GNN pipeline at the models folder and the same file yields:

- **Parsed artifacts** (step 3): a machine-readable version of every section.
- **Type-check output** (step 5): dimensions, types, and resource estimates.
- **Rendered code** (step 11): framework scripts parameterized by the spec.
- **Execution results** (step 12): simulation output for supported frameworks.

You can compare the rendered code back against the spec: the `A` matrix in the
generated script must be the `A` matrix in the file. That traceability from
declaration to execution is what makes the notation useful for education as
well as research — a student can see *why* a simulation behaves as it does.

---

## Summary

- GNN is a plain-text notation for generative models, designed so that one
  specification can be read as text, drawn as a graph, and executed as code
  (Smékal & Friedman, 2023).
- A GNN file separates declaration (state space), structure (connections),
  values (initial parameterization), meaning (ontology annotation), and
  computation (equations).
- The Static Perception Model is the minimal complete exemplar: a 2×2
  likelihood, a uniform prior, and Bayes' rule, plus a minimal transition
  component for framework compatibility.
- The pipeline turns specifications into checked, rendered, and executed
  artifacts in steps 3, 5, 11, and 12.
- This track ships five verbatim exemplars mapped to course levels, from a
  guided middle-school reading to parameter learning at the 401 level.

---

## References

1. Smékal, J., & Friedman, D. A. (2023). *Generalized Notation Notation for
   Active Inference Models.* Zenodo.
   <https://zenodo.org/records/7803328>
2. Active Inference Institute. *Generalized_Notation_Notation* (GNN) repository,
   release v5.0.3, commit `8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`.
   <https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation>
3. Active InferAnt Stream 014.1, *Generalized Notation Notation: From Plaintext
   to Triple Play* (2025).
   <https://www.youtube.com/watch?v=3tYOBVIOLyU>
4. Active InferAnt Stream 014.2, *Generalized Notation Notation for Generative
   Model Supply Chains* (2025).
   <https://www.youtube.com/watch?v=Y3-FMoaEZYE>
5. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free
   Energy Principle in Mind, Brain, and Behavior.* MIT Press. (For the A–E
   matrix conventions used across the curriculum.)
6. See also the Core curriculum's
   [Notation Table](../../active_inference/resources/notation_table.md) for the
   symbols used in its modules.

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
