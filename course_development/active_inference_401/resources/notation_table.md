# Notation Table: Active Inference 401: Advanced PhD Seminar

> Canonical symbols and notation used throughout the curriculum.
> All modules must use these symbols consistently.

## Variational and Free Energy Quantities

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| $F$ | Variational Free Energy | `$F$` | $F = D_{KL}[q(s) \| p(s)] - \mathbb{E}_{q(s)}[\ln p(o \mid s)]$; upper bound on surprisal |
| $G$ | Expected Free Energy | `$G$` | $G(\pi) = \mathbb{E}_{q(o,s \mid \pi)}[\ln q(s \mid \pi) - \ln p(o, s)]$; decomposes into Risk + Ambiguity |
| $\tilde{F}$ | Generalized Free Energy | `$\tilde{F}$` | Combines VFE and EFE under a single variational functional |
| $\mathbb{F}$ | Free energy functional (path integral) | `$\mathbb{F}$` | Path integral formulation over state trajectories |
| $D_{KL}$ | Kullback-Leibler Divergence | `$D_{KL}$` | $D_{KL}[q \| p] = \mathbb{E}_q[\ln q - \ln p]$; always $\geq 0$ (Gibbs' inequality) |
| $\mathcal{L}$ | ELBO / Negative VFE | `$\mathcal{L}$` | $\mathcal{L} = -F = \ln p(o) - D_{KL}[q(s) \| p(s \mid o)]$ |

## Generative Model Components

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| $p(o,s)$ | Generative model (joint) | `$p(o,s)$` | Joint distribution over observations $o$ and hidden states $s$ |
| $p(o \mid s)$ | Likelihood | `$p(o \mid s)$` | Maps hidden states to predicted observations |
| $p(s' \mid s, a)$ | Transition model | `$p(s' \mid s, a)$` | State dynamics conditioned on action |
| $q(s)$ | Approximate posterior | `$q(s)$` | Variational approximation to $p(s \mid o)$ (recognition density) |
| $\pi$ | Policy | `$\pi$` | Sequence of actions $\pi = (a_1, \ldots, a_T)$ |
| $\gamma$ | Policy precision | `$\gamma$` | Inverse temperature for policy selection: $p(\pi) = \sigma(\gamma \cdot G(\pi))$ |

## POMDP Matrices (Discrete State-Space)

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| **A** | Likelihood matrix | `$\mathbf{A}$` | $A_{ij} = p(o_i \mid s_j)$; categorical observation model |
| **B** | Transition matrix | `$\mathbf{B}$` | $B_{ij}^{(a)} = p(s_i' \mid s_j, a)$; action-conditioned state transitions |
| **C** | Preference vector | `$\mathbf{C}$` | $C_i = \ln p(o_i)$; log prior preferences over observations |
| **D** | Prior over initial states | `$\mathbf{D}$` | $D_i = p(s_i^{(0)})$; initial state distribution |
| **E** | Habit vector | `$\mathbf{E}$` | $E_\pi = p(\pi)$; prior over policies before EFE evaluation |

## Markov Blanket and Partition States

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| $\eta$ | External states | `$\eta$` | States outside the Markov blanket; hidden from internal states |
| $\mu$ | Internal states | `$\mu$` | States inside the blanket; parameterize beliefs about $\eta$ |
| $s$ | Sensory states | `$s$` | Blanket states influenced by $\eta$ but not $\mu$ |
| $a$ | Active states | `$a$` | Blanket states influenced by $\mu$ but not $\eta$ |
| $b = (s, a)$ | Blanket states | `$b$` | Union of sensory and active states |
| $p = (\mu, b)$ | Particular states | `$p$` | Internal + blanket states; constitutes the "agent" |

## Dynamical and Geometric Quantities

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| $\Gamma$ | Fisher information metric | `$\Gamma$` | Riemannian metric on $\mathcal{M}$; $\Gamma_{ij} = \mathbb{E}[\partial_i \ln p \cdot \partial_j \ln p]$ |
| $Q$ | Solenoidal flow matrix | `$Q$` | Antisymmetric ($Q = -Q^T$); generates non-dissipative flow |
| $f_\mu$ | Flow of internal states | `$f_\mu$` | $f_\mu = (Q_{\mu\mu} - \Gamma_{\mu\mu}) \nabla_\mu F$ |
| $p^*(\cdot)$ | NESS density | `$p^*(\cdot)$` | Non-equilibrium steady-state distribution; $\partial_t p^* = 0$ |
| $\mathcal{M}$ | Statistical manifold | `$\mathcal{M}$` | Space of probability distributions with Fisher metric |

## Information-Theoretic Quantities

| Symbol | Meaning | LaTeX | Definition |
| ------ | ------- | ----- | ---------- |
| $H[p]$ | Shannon entropy | `$H[p]$` | $H[p] = -\mathbb{E}_p[\ln p]$ |
| $I(X;Y)$ | Mutual information | `$I(X;Y)$` | $I(X;Y) = D_{KL}[p(x,y) \| p(x)p(y)]$ |
| $\mathfrak{s}(o)$ | Surprisal | `$\mathfrak{s}(o)$` | $\mathfrak{s}(o) = -\ln p(o)$; self-information |
| $\ln p(o \mid m)$ | Log model evidence | `$\ln p(o \mid m)$` | Marginal likelihood under model $m$ |

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Home](../README.md)
