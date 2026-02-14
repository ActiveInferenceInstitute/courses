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

- **感覚減衰 (Gansoku Kemizu)** — 自己生成された感覚信号の精度（信頼性重み付け）の低下、行動中に見られる。これは、運動予測が感覚的証拠を上回らせ、運動を駆動するために必要である。統合失調症で見られ、制御の幻覚に寄与する。

- **感覚状態 (σ)** — 外部の状態に影響を受けるが、直接影響を与えない包摂的な状態。 ‘感覚’または‘観察’という概念を具体化する。例：網膜活性化、内耳刺激。

- **線維曲面流 (Shin’i Kyūmen Flow)** — 吸引集合のNESS密度を循環するダイナミクスの成分で、確率密度が変化しない。散逸（勾配）流とは区別される。線維曲面流は詳細平衡を破り、生体システムの特徴である。

- **高度な推論 (Kōdō na Sūren)** — Active Inferenceの拡張で、エージェントが行動と観察の結果として自身の信念が将来どのように変化するかをモデル化する。メタ認知的な計画やより深い先見を可能にする。Fristonら（2021）によって導入された。

- **驚き (Kyōki)** — 生成モデルの下での観察の負の対数確率： `S(o) = -ln p(o)`。長期的平均の驚きを最小化することは、変分フリーエネルギーを最小化することに相当する。口語的な驚きの感覚とは異なる。

## T

- **心の理論 (Kokoro no iritsu)** — 他者の心理状態（信念、欲求、意図）を属性する能力。Active Inferenceにおいて、メンタル化は他者の生成モデルの隠れた状態に関する推論である。

- **転移エントロピー (Ten’i Entoropii)** — 情報の流れを測る方向性の指標： `T_{X→Y} = I(Y_future; X_past | Y_past)`。相関情報とは異なり、転移エントロピーは不均衡な因果的影響を捉える。Active Inferenceにおいて、社会的相互作用における誰がリードし、誰が追従するかを定量化するために使用される。

- **T-迷路 (T-Meiryuu)** — Active Inferenceにおける標準的なベンチマーク環境で、開始位置、ヒントの場所、2つの報酬腕で構成される。エージェントは報酬が格納されている腕を学習するためにヒントを訪れる必要がある。EFEにおける認識（ヒントを訪れること）と実践（報酬に向かうこと）の価値のバランスをテストする。

## V

- **変分フリーエネルギー (Henbun-teki Furi Enerugii)** — 驚き（負の対数証拠）の範囲を定める情報理論的な量： `F ≥ -ln p(o)`。 `F = E_q[ln q(s) - ln p(o,s)]`で定義される。信念 `q(s)`に関してFを最小化することは、**知覚**に対応し、パラメータに関してFを最小化することは、**学習**に対応する。

---

## 迅速な用語検索（コース別）

| 用語 (Yōgo) | 哲学 (Hotoke) | 認知科学 (Kōni Gakuryō) | 数学 (Sūgakyu) | コンピュータ科学 (Konpyūta Gakuryō) |
|---|---|---|---|---|
| マルコフ被覆 (Marukuho Hiko) | システム境界（哲学的） (Shisutemu Kyōbō - Hotoke-teki) | 皮質列の境界 (Kishitsu Ren no Kyōbō) | 条件独立性パーティション (Jōten dokyutshusei pātishon) | エージェント-環境インターフェース (Ējento - Kankyou Intāfēsu) |
| 生成モデル (Seisei Moderu) | ワールドモデル、暗黙の理論 (Wārudo Moderu, Ankumu no Riron) | 脳の予測モデル (Noun no Yosoku Moderu) | 共同分布 p(o,s) (Kyōyū bushi p(o,s)) | A, B, C, D, E行列 (A, B, C, D, E ryokyu) |
| フリーエネルギー (Furi Enerugii) | 驚き限界、自己証拠 (Kyōki Genkai, Jiko Shōko) | 予測誤差信号 (Yosoku Gusasu Shinō) | 変分関数 F (Henbun kansu F) | 最小化する目的関数 (Shinlizuka suru mokushukan) |
| 精度 (Jūtei) | 信頼性、注目度 (Shinrisu, Shimeitō) | 注意/ゲインモジュレーション (Chūi/Gain Modyūreshon) | 逆分散 β, γ (Inku Bisan β, γ) | softmaxにおけるγパラメータ (softmax ni okeru γ parāmēsu) |
| ポリシー (Porithii) | 計画、意図、目的 (Keikaku, Ito, Mokuteki) | モーターコマンドシーケンス (Mōtā Komandu Shīkensu) | 行動シーケンス (a₁,...,aₜ) (Kōdō Shīkensu) | B行列のスライスへのインデックス (B ryokyu no suraisu e no indeksu) |
| 予測誤差 (Yosoku Gusasu) | 違反した期待 (Hanien shita Kitai) | 神経的なミスマッチ信号 (Shinai Teki no Misumatchu Shinō) | ε = o - E_q[o] (Epsilon = o - E_q[o]) | 信頼度更新後の余剰 (Shin'itutsu kinka gohou no yosō) |
| 学習 (Gakushū) | モデルの再構成 (Moderu no Saikōseki) | シナプティックプラスチック性 (Shinaputikku Purashikkusei) | パラメータの勾配降下 (Paramēsu no Kakubai Kōchaku) | Dirichlet更新 (Dirikutu update) |
| 驚き (Kyōki) | 存在論的脅威 (Sonzai-ronteki Kyōi) | 神経的な驚き信号 (Shinai Teki no Kyōki Shinō) | -ln p(o) (Negai-n arushi o) | 負の対数証拠 (Funoi tai shōko shōko) |
| 暗室問題 (Anshitsu Mondai) | なぜ私たちは隠れないのか？ (Naze Watashitachi wa Kakurenai no ka?) | なぜ生物が探索するのか？ (Naze seibutsu ga tansaku suru no ka?) | Cベクトルが偏性を解決する (C bēkutoru ga hensei o kaiketsu suru) | 非特異的なCの偏好 (Hi-toki-i nakana C no henkō) |
| 高度な推論 (Kōdō na Sūren) | メタ認知、先見 (Metakōni, Senken) | PFCの再帰的計画 (PFC no Sai keitoku kikai) | EFEの再帰的探索 (EFE no Sai keitoku tansaku) | 1より大きい時間的T (1 yori ooki no jikinto T) |

---