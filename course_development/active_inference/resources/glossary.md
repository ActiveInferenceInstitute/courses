# Active Inference Glossary

> **Quick Navigation**: [Curriculum Home](../README.md) | [Notation Table](./notation_table.md) | [Key References](./references.md) | [Cross-Course Map](./cross_course_map.md)

Canonical definitions for all key terms used across the Active Inference curriculum. All 4 courses use these definitions consistently. Terms are organized alphabetically.

---

## A

- **Active Inference** — A corollary of the Free Energy Principle stating that organisms act to minimize expected free energy, unifying perception, action, learning, and planning under a single imperative. All behavior can be cast as inference about the causes of sensory data and the selection of actions that minimize expected surprise.

- **Active States (α)** — Blanket states that influence but are not directly influenced by external states. Formalize the concept of 'action' in the Markov Blanket partition. Examples: muscle contractions, secretory activity, gene expression changes.

- **Affordance** — An action possibility specified by the relationship between an agent's generative model and its environment. In Active Inference, affordances are encoded as policies that reduce expected free energy. Originally introduced by J.J. Gibson in ecological psychology.

- **Allostasis** — The process of achieving physiological stability through predictive regulation, anticipating bodily needs before they arise. Distinguished from homeostasis (reactive regulation). In Active Inference, allostatic regulation is interoceptive inference — the brain predicts and preemptively corrects deviations from set-points.

- **Ambiguity** — A component of Expected Free Energy representing the expected entropy of observations given states: `E_q[H[p(o|s)]]`. High ambiguity means the agent cannot clearly observe the state it would be in. Drives epistemic action (exploration).

- **Attracting Set** — A region in state space toward which a system tends to evolve over time. Under the FEP, living systems occupy characteristic attracting sets defined by their phenotype. Also called an attractor.

- **Autopoiesis** — The capacity of a system to produce and maintain itself, particularly its own boundary. Coined by Maturana and Varela (1972). In Active Inference, autopoiesis is formalized through the self-evidencing dynamics of Markov Blankets. A cell producing its own membrane is the canonical example.

## B

- **Bayesian Mechanics** — The interpretation of internal state dynamics as performing approximate Bayesian inference on external states. Formalizes the relationship between the particular partition and variational inference. Developed by Da Costa, Friston, and colleagues.

- **Bayesian Model Reduction (BMR)** — A method for scoring simpler models against a current model without re-fitting data. Implements Occam's razor by analytically comparing the evidence for reduced models, enabling efficient structure learning and pruning of unnecessary parameters. In neuroscience, proposed as the computational function of sleep.

- **Belief** — In Active Inference, a probability distribution `q(s)` encoded in internal states. Not a conscious propositional attitude, but a physical quantity characterizing the system's statistical relation to its environment. Distinguished from colloquial usage.

- **Belief Propagation** — A message-passing algorithm for performing inference on factor graphs. In Active Inference, prediction errors (bottom-up messages) and predictions (top-down messages) are passed through the cortical hierarchy. Each message updates local beliefs to minimize free energy.

- **Blanket States (b)** — The union of sensory and active states that statistically separate internal from external states: `b = (σ, α)`. Named after the Markov Blanket concept from Bayesian network theory (Pearl, 1988).

## C

- **Concentration Parameters** — Parameters of a Dirichlet distribution used for learning (`pA`, `pB`, `pD`). Increase monotonically with experience, encoding learned contingencies. Higher concentrations yield sharper (more confident) distributions. The effective learning rate decreases as concentrations grow, implementing a natural schedule from fast initial learning to slow fine-tuning.

- **Complexity** — In the VFE decomposition: `D_KL[q(s) || p(s)]`, the KL divergence between posterior and prior beliefs. Penalizes deviation from prior expectations. Balances accuracy in Bayesian inference.

- **Conditional Independence** — A probabilistic relationship where two sets of variables become independent once a third set is known. The defining property of a Markov Blanket: internal states are conditionally independent of external states given blanket states (`μ ⊥ η | b`).

## D

- **d-separation** — A graphical criterion for determining conditional independence in directed acyclic graphs (DAGs). Used to identify Markov Blankets: a node's Markov Blanket consists of its parents, children, and co-parents. In the FEP, d-separation provides the formal basis for the particular partition.

- **Dark Room Problem** — The objection that if organisms minimize surprise, they should seek maximally predictable environments (a dark, empty room). Active Inference resolves this through the generative model: organisms have prior expectations about the states they should occupy (encoded in C-vector preferences), and a dark room violates those expectations.

- **Deep Temporal Model** — A generative model that extends over multiple future time steps, enabling evaluation of policies with delayed consequences. The temporal depth T determines the planning horizon. Deeper models enable more foresighted behavior but incur exponential computational cost.

- **Dirichlet Distribution** — A distribution over probability vectors (simplices). Used in Active Inference for learning model parameters (A, B, D matrices). The conjugate prior for categorical distributions. Parameterized by concentration parameters that grow with experience.

- **D_KL (KL Divergence)** — Kullback-Leibler divergence: a non-symmetric measure of the difference between two probability distributions. `D_KL[q||p] = E_q[ln q - ln p]`. Always non-negative. Zero only when q = p.

## E

- **Efference Copy** — A copy of a motor command sent to sensory areas to predict the sensory consequences of self-generated movement. In Active Inference, efference copies are not separate signals but are inherent in the generative model's predictions: the same model that generates motor commands also predicts their sensory effects.

- **ELBO (Evidence Lower Bound)** — The negative variational free energy: `-F = ln p(o) - D_KL[q(s)||p(s|o)]`. Since `D_KL ≥ 0`, `-F ≤ ln p(o)`, so negative VFE is a lower bound on log model evidence. Maximizing the ELBO is equivalent to minimizing VFE.

- **Embodied Cognition** — The thesis that cognition is shaped by and dependent on the body, not confined to the brain. Active Inference naturally accommodates embodiment through interoceptive inference and the body-schema in the generative model.

- **Enactivism** — The view that cognition is constituted by the agent's active engagement with its environment, not by passive representation. Originated with Varela, Thompson, and Rosch (1991). Active Inference is compatible with enactivism through its emphasis on action as inference.

- **Epistemic Value** — The expected information gain from a policy: the reduction in uncertainty about hidden states. One of two components of Expected Free Energy (alongside pragmatic value). Drives curiosity, exploration, and information-seeking behavior.

- **Ergodicity** — A property of dynamical systems whereby time averages equal ensemble averages. Under the FEP, biological systems maintain a characteristic non-equilibrium steady state (NESS) that is approximately ergodic over their lifetime.

- **Expected Free Energy (G)** — The expected free energy of a policy `π` (sequence of future actions), guiding action selection. Unlike VFE (which minimizes surprise of *past* observations), EFE minimizes *expected future* surprise. `G(π) = risk + ambiguity`. Decomposes into **pragmatic value** (divergence from preferred outcomes) and **epistemic value** (expected information gain).

- **Extended Mind** — The thesis (Clark & Chalmers, 1998) that cognitive processes can extend beyond the brain and body to include external artifacts (notebooks, smartphones). In Active Inference, the question becomes whether the external artifact falls within the agent's Markov Blanket — whether it participates in the relevant conditional independence structure.

- **External States (η)** — States outside the Markov Blanket that influence sensory states but are not directly accessible to the agent. The "hidden" world that the agent must infer.

## F

- **Factor Graph** — A bipartite graph representing the factorization structure of a joint probability distribution. In Active Inference, factor graphs provide the computational architecture for message passing and belief propagation. Each factor node corresponds to a conditional distribution (A, B, C, D).

- **Fokker-Planck Equation** — A partial differential equation describing the time evolution of the probability density of a stochastic process. In the FEP, the Fokker-Planck equation corresponding to the Langevin dynamics defines the NESS density, from which the free energy functional is derived.

- **Free Energy Principle (FEP)** — The principle that any self-organizing system at non-equilibrium steady state can be described as minimizing variational free energy (or its path integral, free action). Proposed by Karl Friston. Applies to any system with a Markov Blanket that persists over time.

## G

- **Generalized Coordinates** — An extended state description including position, velocity, acceleration, and higher-order derivatives. Used in continuous-time Active Inference to handle temporal dynamics.

- **Generative Model** — A probabilistic model of how observations are generated from hidden causes. Specified by matrices `A, B, C, D, E` in discrete state-spaces. The agent's "model of the world" that generates predictions. Distinguished from the generative process.

- **Generative Process** — The actual process that generates the agent's observations. The "real world" that the generative model attempts to capture. The generative process is never directly accessible; only observations are.

- **Generalized Synchrony** — A state where the dynamics of two coupled systems become statistically dependent through mutual observation. In Active Inference, formalizes communication and social interaction as coupled inference.

## H

- **Hierarchical Gaussian Filter (HGF)** — A generative model with cascading Gaussian levels where each level's volatility (variance) is controlled by the level above. Used to model learning under uncertainty about uncertainty. Developed by Mathys et al. (2011, 2014).

- **Hierarchical Generative Model** — A generative model with multiple levels of abstraction. Higher levels generate priors for lower levels, implementing predictive coding. Each level encodes regularities at a different temporal and spatial scale.

## I

- **Interoception** — Perception of internal bodily states (heart rate, gut distension, blood glucose). In Active Inference, interoception is inference about internal physiological states, contributing to emotion and the sense of self. The insular cortex is the primary cortical hub for interoceptive inference.

- **Internal States (μ)** — States inside the Markov Blanket that are statistically separated from external states by the blanket. Encode the agent's beliefs (recognition density) about external states.

## K

- **KL Divergence** — See D_KL.

## L

- **Langevin Equation** — A stochastic differential equation: `dx = f(x)dt + σdW`. Describes the dynamics of a system under deterministic flow f(x) and random fluctuations σdW. The FEP derives its formalism from Langevin dynamics on Markov-blanketed systems.

- **Lewis Signaling Game** — A game-theoretic model of communication where a sender observes a hidden state and emits a signal, and a receiver observes only the signal and must select the correct action. Used in computational Active Inference to demonstrate emergent communication between agents.

- **Life-Mind Continuity Thesis** — The claim that the fundamental organizational principles of mind are continuous with those of life. Under the FEP, all living systems perform inference; the difference between bacteria and humans is the complexity of the generative model, not the fundamental mechanism.

## M

- **Markov Blanket** — A set of states that renders internal states conditionally independent of external states: `μ ⊥ η | b`. Consists of sensory states σ and active states α. The formal definition of a system boundary in the FEP. Named after the concept in Bayesian networks (Pearl, 1988).

- **Message Passing** — An algorithm for performing inference on graphical models. In Active Inference, belief propagation passes predictions (top-down) and prediction errors (bottom-up) through a hierarchical generative model.

- **Mismatch Negativity (MMN)** — An event-related potential observed 100-250 ms after an unexpected auditory stimulus. In predictive coding, MMN reflects the precision-weighted prediction error generated when an observation violates the brain's predictive model.

- **Motor Inference** — The generation of movement through proprioceptive predictions. The motor cortex specifies desired proprioceptive states; spinal reflex arcs fulfill these predictions by adjusting muscle tension. Action is self-fulfilling proprioceptive prediction.

- **Mutual Information** — A symmetric measure of statistical dependence: `I(X;Y) = H(X) - H(X|Y)`. In Active Inference communication models, MI between signals and states measures the informativeness of an emergent communication protocol.

## N

- **Niche Construction** — The process by which organisms modify their environment to make it more predictable. In Active Inference, a form of active inference operating on external states. Examples: beaver dams, spider webs, human cultural institutions.

- **Non-Equilibrium Steady State (NESS)** — A stable state maintained far from thermodynamic equilibrium through the continuous exchange of energy and matter with the environment. Living systems are NESS systems. Distinguished from equilibrium (death/dissipation). The NESS density defines the attracting set of a living system.

## P

- **Particular Partition** — The specific decomposition of a system's state space into internal (μ), external (η), sensory (σ), and active (α) states. Defines the fundamental architecture of an Active Inference agent.

- **Policy (π)** — A sequence of actions `(a_1, a_2, ..., a_T)`. Evaluated by Expected Free Energy `G(π)`. Selected via softmax: `P(π) ∝ exp(-γ·G(π))`.

- **Pragmatic Value** — The expected utility (negative risk) of a policy: `−D_KL[q(o|π) || p(o|C)]`. One of two components of EFE. Drives goal-directed, exploitative behavior.

- **Precision** — The inverse variance of a probability distribution: `β = 1/σ²`. In Active Inference, precision modulates the gain on prediction errors. High precision = high reliability = high attention. Modulated by neuromodulators (dopamine, acetylcholine).

- **Prediction Error** — The difference between predicted and actual sensory input: `ε = o - E_q[o]`. In predictive coding, prediction errors are precision-weighted and passed upward in the cortical hierarchy.

- **Predictive Coding** — A neural implementation of variational inference where each cortical level generates predictions for the level below. Prediction errors flow upward; predictions flow downward. Implements VFE minimization. First demonstrated computationally by Rao & Ballard (1999).

## R

- **Recognition Density** — The approximate posterior `q(s)` over hidden states. The agent's best guess about the current state of the world, parameterized by internal states μ.

- **Risk** — The KL divergence between predicted and preferred outcomes: `D_KL[q(o|π) || p(o|C)]`. A component of pragmatic value in EFE. Measures how far predicted outcomes deviate from preferences.

## S

- **Self-Evidencing** — The process by which a system gathers evidence for its own existence (its generative model). Under the FEP, all living systems are self-evidencing: by persisting, they confirm the model that defines them. Conceptualized by Hohwy (2016).

- **Sensory Attenuation** — The reduction in precision (reliability weighting) of self-generated sensory signals during action. Necessary to allow motor predictions to override sensory evidence and drive movement. Disrupted in schizophrenia, contributing to delusions of control.

- **Sensory States (σ)** — Blanket states that are influenced by external states but do not directly influence them. Formalize the concept of 'sensation' or 'observation'. Examples: retinal activation, cochlear stimulation.

- **Solenoidal Flow** — The component of dynamics on the NESS density that circulates around the attracting set without changing the probability density. Distinguished from dissipative (gradient) flow. Solenoidal flow breaks detailed balance and is characteristic of living systems.

- **Sophisticated Inference** — An extension of Active Inference where the agent models how its own beliefs will change in the future as a result of actions and observations. Enables meta-cognitive planning and deeper foresight. Introduced by Friston et al. (2021).

- **Surprisal (S)** — The negative log probability of an observation under the generative model: `S(o) = -ln p(o)`. Minimizing long-run average surprisal ≈ minimizing variational free energy. Not the same as the colloquial feeling of surprise.

## T

- **Theory of Mind** — The ability to attribute mental states (beliefs, desires, intentions) to others. In Active Inference, mentalizing is inference about the hidden states of another agent's generative model.

- **Transfer Entropy** — A directed measure of information flow: `T_{X→Y} = I(Y_future; X_past | Y_past)`. Unlike mutual information, transfer entropy captures asymmetric causal influence. Used in Active Inference to quantify who is leading and who is following in social interaction.

- **T-Maze** — A standard benchmark environment in Active Inference consisting of a start position, a cue location, and two reward arms. The agent must visit the cue to learn which arm contains the reward. Tests the balance between epistemic (visiting the cue) and pragmatic (going to the reward) value in EFE.

## V

- **Variational Free Energy (F)** — An information-theoretic quantity that bounds the surprisal (negative log evidence) of observations: `F ≥ -ln p(o)`. Defined as `F = E_q[ln q(s) - ln p(o,s)]`. Minimizing F w.r.t. beliefs `q(s)` corresponds to **perception**; minimizing F w.r.t. parameters corresponds to **learning**.

---

## Quick Term Lookup by Course

| Term | Philosophy | CogSci | Math | CS |
|---|---|---|---|---|
| Markov Blanket | System boundary (philosophical) | Neural boundary (cortical columns) | Conditional independence partition | Agent-environment interface |
| Generative Model | World-model, implicit theory | Brain's predictive model | Joint distribution p(o,s) | A, B, C, D, E matrices |
| Free Energy | Surprise bound, self-evidencing | Prediction error signal | Variational functional F | Objective function to minimize |
| Precision | Reliability, salience | Attention/gain modulation | Inverse variance β, γ | γ parameter in softmax |
| Policy | Plan, intention, purpose | Motor command sequence | Action sequence (a₁,...,aₜ) | Index into B-matrix slices |
| Prediction Error | Violated expectation | Neural mismatch signal | ε = o - E_q[o] | Residual after belief update |
| Learning | Model restructuring | Synaptic plasticity | Parameter gradient descent | pA/pB Dirichlet updates |
| Surprisal | Existential threat | Neural surprise signal | -ln p(o) | Negative log evidence |
| Dark Room Problem | Why don't we hide? | Why do organisms explore? | C-vector resolves degeneracy | Non-trivial C preferences |
| Sophisticated Inference | Meta-cognition, foresight | PFC recursive planning | Recursive EFE, tree search | Deep temporal `T > 1` |
