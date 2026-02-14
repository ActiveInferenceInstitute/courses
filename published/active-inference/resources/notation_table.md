# Active Inference Notation Table

> **Quick Navigation**: [Curriculum Home](../README.md) | [Glossary](./glossary.md) | [Key References](./references.md) | [Cross-Course Map](./cross_course_map.md)

This table defines the **canonical notation** used across all 4 courses. All modules, labs, quizzes, and dashboards must use these symbols consistently. When in doubt, this table is the authoritative source.

---

## Core Variables

| Symbol | LaTeX | Name | Definition | First Introduced |
|---|---|---|---|---|
| `F` | `$F$` | Variational Free Energy (VFE) | Upper bound on observation surprisal `-ln p(o)`; minimized in perception/learning | M3: Perception |
| `G` | `$G$` | Expected Free Energy (EFE) | Functional of policies `π`; bounds expected future surprisal; drives action selection | M5: Action |
| `o` | `$o$` | Observations | Sensory data received by the agent | M1: Systems |
| `s` | `$s$` | Hidden states | Latent states of the generative model | M1: Systems |
| `a` | `$a$` | Actions | Actions taken by the agent on the environment | M2: Agents |
| `π` | `$\pi$` | Policy | Sequence of actions `(a_1, a_2, ..., a_T)` | M5: Action |
| `τ` | `$\tau$` | Time step | Discrete time index within a trial | M5: Action |
| `T` | `$T$` | Time horizon | Total number of time steps in planning | M8: Planning |
| `γ` | `$\gamma$` | Precision (policy) | Inverse temperature for policy selection; higher γ = more decisive | M4: Cognition |
| `β` | `$\beta$` | Precision (sensory) | Inverse variance of sensory noise; higher β = more reliable sensory data | M4: Cognition |
| `ω` | `$\omega$` | Precision (prior) | Inverse variance of prior beliefs; modulates top-down influence | M4: Cognition |

---

## Generative Model Matrices (Discrete State-Space)

| Symbol | LaTeX | Name | Dimensions | Definition | Code |
|---|---|---|---|---|---|
| **A** | `$\mathbf{A}$` | Likelihood matrix | `\|o\| × \|s\|` | `P(o_t \| s_t)` — maps hidden states to observations | `model.A` |
| **B** | `$\mathbf{B}$` | Transition matrix | `\|s\| × \|s\| × \|a\|` | `P(s_{t+1} \| s_t, a_t)` — state transitions under actions | `model.B` |
| **C** | `$\mathbf{C}$` | Preference vector | `\|o\| × T` | `ln P(o_t)` — log prior preferences over observations | `model.C` |
| **D** | `$\mathbf{D}$` | Prior state distribution | `\|s\|` | `P(s_0)` — prior beliefs about initial state | `model.D` |
| **E** | `$\mathbf{E}$` | Habit vector | `\|π\|` | `P(π)` — prior over policies (habit strength) | `model.E` |

### Matrix Relationships

```text
Generative Model:  p(o, s, π) = p(o|s) · p(s|π) · p(π)
                              = A · B^π · E

Perception:        q(s) ← argmin_q F[q, o]  (update beliefs using A, B)
Action:            π*   ← argmin_π G(π)      (select policy using A, B, C)
Learning:          A    ← update(pA, o, s)   (update likelihood from experience)
```

---

## Learned Parameters (Dirichlet Concentrations)

| Symbol | LaTeX | Name | Definition | Initialized As | Updated By |
|---|---|---|---|---|---|
| **pA** | `$\mathbf{p_A}$` | Learned likelihood | Dirichlet concentration parameters for A-matrix | Copy of A (or uniform) | Each observation |
| **pB** | `$\mathbf{p_B}$` | Learned transitions | Dirichlet concentration parameters for B-matrix | Copy of B (or uniform) | Each state transition |
| **pD** | `$\mathbf{p_D}$` | Learned prior | Dirichlet concentration parameters for D-vector | Copy of D (or uniform) | Each episode start |

---

## Information-Theoretic Quantities

| Symbol | LaTeX | Name | Formula | Used In |
|---|---|---|---|---|
| `D_KL` | `$D_{KL}$` | KL Divergence | `D_KL[q(s) \|\| p(s)] = E_q[ln q(s) - ln p(s)]` | VFE, EFE, risk |
| `H` | `$H$` | Entropy | `H[p] = -E_p[ln p]` | Ambiguity, uncertainty |
| `I` | `$I$` | Mutual Information | `I(X;Y) = H(X) - H(X\|Y)` | Communication, epistemic value |
| `S` | `$\mathfrak{S}$` | Surprisal | `S(o) = -ln p(o)` — negative log model evidence | VFE upper bound |
| `ln p(o)` | `$\ln p(o)$` | Log model evidence | Negative surprisal; `F ≥ -ln p(o)` | Model comparison |

---

## Markov Blanket Partition

| Symbol | LaTeX | Name | Definition | Analogy |
|---|---|---|---|---|
| `η` | `$\eta$` | External states | States outside the Markov Blanket | The world beyond the organism |
| `μ` | `$\mu$` | Internal states | States inside the Markov Blanket | The brain/body interior |
| `σ` | `$\sigma$` | Sensory states | Blanket states influenced by external states | Receptors, sensory organs |
| `α` | `$\alpha$` | Active states | Blanket states that influence external states | Muscles, effectors |
| `b = (σ, α)` | `$b = (\sigma, \alpha)$` | Blanket states | Union of sensory and active states | The membrane, skin, interface |

### Conditional Independence Structure

```text
External (η) ──→ Sensory (σ) ──→ Internal (μ)
                                      │
                                      ↓
External (η) ←── Active (α) ←── Internal (μ)

Key property: μ ⊥ η | b  (internal independent of external, given blanket)
```

---

## Free Energy Decompositions

### Variational Free Energy (VFE)

```text
F = E_q[ln q(s) - ln p(o,s)]

Decomposition 1 (Divergence + Surprisal):
  F = D_KL[q(s) || p(s|o)] + S(o)
  F = D_KL[q(s) || p(s|o)] - ln p(o)

Decomposition 2 (Complexity - Accuracy):
  F = D_KL[q(s) || p(s)]   -  E_q[ln p(o|s)]
      ├── Complexity ──┤      ├── Accuracy ──┤

Decomposition 3 (Energy - Entropy):
  F = E_q[-ln p(o,s)]  -  H[q(s)]
      ├── Energy ──┤      ├── Entropy ──┤
```

### Expected Free Energy (EFE)

```text
G(π) = E_q[F_τ | π]

Decomposition (Risk + Ambiguity):
  G(π) = -E_q[ln p(o_τ | C)]  +  E_q[H[p(o_τ | s_τ)]]
          ├── Risk ──────────┤    ├── Ambiguity ──────┤
          (Pragmatic value)        (Epistemic value)

Risk:      D_KL[q(o_τ|π) || p(o_τ|C)]  — distance from preferences
Ambiguity: E_q[H[p(o|s)]]              — expected imprecision of observations
```

### Policy Selection

```text
P(π) = σ(-γ · G(π))    (softmax of negative EFE)
     = exp(-γ · G(π)) / Σ_π' exp(-γ · G(π'))
```

---

## Temporal Notation

| Symbol | Meaning | Example |
|---|---|---|
| `x_t` | Value of x at time t | `s_t` = hidden state at time t |
| `x_{1:T}` | Sequence from t=1 to T | `o_{1:T}` = all observations |
| `x^π` | Conditioned on policy π | `q(s_t^π)` = beliefs under policy π |
| `x_τ` | Future time step (planning) | `G(π) = Σ_τ G_τ(π)` |

---

## Conventions

- **Bold uppercase** (`**A**`) for matrices
- **Bold lowercase** (`**c**`) for vectors
- **Italic lowercase** (`*s*`) for scalar variables
- **Greek letters** for precision and time parameters
- Subscript `_t` for time-indexed variables
- Superscript `^π` for policy-conditioned quantities
- Tilde `~` for generalized coordinates (continuous-time models)
- Hat `^` for estimated or inferred quantities

---

## Usage in Each Course

| Course | Primary Symbols Used | Depth | Typical Presentation |
|---|---|---|---|
| Philosophy | `F`, `G`, Markov Blanket (`η, μ, σ, α`), `S` | Conceptual definitions | Prose with occasional formulas |
| Cognitive Science | `F`, `G`, precision (`γ, β`), `D_KL`, prediction error | Neural correlates | Diagrams, experimental paradigms |
| Mathematics | All symbols — full derivation | Formal proofs | Equations, derivations, proofs |
| Computer Science | `A, B, C, D, E`, `pA, pB`, `G(π)`, `γ` | Implementation in `active_inference` library | Code blocks, API calls |

---

## Quick Reference Card

```text
PERCEPTION:  minimize F  w.r.t. internal states μ  →  update beliefs q(s)
ACTION:      minimize G  w.r.t. active states α   →  select policy π
LEARNING:    minimize F  w.r.t. parameters θ      →  update A, B, D
PLANNING:    evaluate G  over future time steps    →  deep temporal inference
```
