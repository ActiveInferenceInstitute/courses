# Glossary

> **Quick Navigation**: [Resources Home](./README.md) | [Notation Table](./notation_table.md) | [Curriculum Home](../README.md)

This glossary defines all technical terms used across the Active Inference for High School curriculum. Each entry includes a **student-friendly explanation** first, then the formal definition, and shows which courses use the term most.

---

## A

**Action** — Doing something to change the world around you. Formally, an action is a change to active states that influences external states through the Markov Blanket. *Used in: All courses, especially Life M5, Bio M5, Math M5, Tech M5.*

**Active States** — The part of a system's boundary that lets it push back on the world (like your muscles or voice). Formally, the component of the Markov Blanket that influences external states. Symbol: α. *Used in: All courses.*

**Agent** — Anything that senses its environment and acts on it — you, a dog, a robot, even a single cell. Formally, a system with a Markov Blanket that can be described as minimizing free energy. *Used in: All courses.*

**Ambiguity** — When the signals you're getting are noisy or unclear, making it hard to figure out what's really going on. Formally, the expected entropy of observations given states: E_q[H[p(o|s)]]. *Used in: Math M5, Tech M5.*

**Approximate Posterior** — Your brain's "best guess" about what's really happening, updated as new evidence comes in. Formally, the recognition density q(s) that approximates the true posterior p(s|o). Symbol: q(s). *Used in: Math M3, Tech M3.*

**Autopoiesis** — A system that makes and maintains itself — like a cell that builds its own membrane. Coined by Maturana and Varela. *Used in: Life M2, Bio M2.*

---

## B

**Bayes' Theorem** — A formula for updating your beliefs when you get new evidence. If you believe something, and then see evidence, Bayes' theorem tells you exactly how to change your belief. Formula: P(A|B) = P(B|A)·P(A)/P(B). *Used in: Math M4, Tech M4.*

**Belief** — What you think is true about the world, even if you're not 100% sure. In Active Inference, beliefs are probability distributions, not all-or-nothing. *Used in: All courses.*

**Boundary** — Where a system ends and its environment begins. In Active Inference, boundaries are defined statistically (by Markov Blankets), not just physically. *Used in: Life M1, Bio M1, Math M1.*

---

## C

**Conditional Independence** — Two things are conditionally independent if, once you know a third thing, learning about one tells you nothing new about the other. This is the mathematical basis of the Markov Blanket. *Used in: Math M1, Life M1.*

**Conditional Probability** — The probability of something happening, given that something else has already happened. Written as P(A|B). *Used in: Math M3.*

---

## D

**Deep Temporal Model** — A model that plans multiple steps into the future, like a chess player thinking several moves ahead. *Used in: Math M8, Tech M8.*

---

## E

**Entropy** — A measure of how uncertain or unpredictable something is. High entropy means lots of possible outcomes; low entropy means things are more predictable. Symbol: H. *Used in: Math M7.*

**Epistemic Value** — The value of learning something new, even if it doesn't help you right away. It's the "curiosity" component of decision-making. *Used in: Math M5, Tech M5.*

**Evidence** — Information that supports or contradicts a belief. In Bayesian terms, evidence is what you observe. *Used in: All courses.*

**Expected Free Energy (EFE)** — A prediction about how much prediction error you'll have in the future if you follow a certain plan. Low EFE means good plan. Symbol: G. *Used in: Math M5, Tech M5.*

**External States** — Everything outside a system's boundary that the system cannot directly access. Symbol: η. *Used in: All courses.*

---

## F

**Free Energy Principle (FEP)** — The big idea: any system that survives over time can be described as minimizing something called "free energy" — basically, keeping its predictions close to reality. Proposed by Karl Friston. *Used in: All courses.*

---

## G

**Generative Model** — Your brain's internal model of how the world works — it generates predictions about what you'll see, hear, and feel. Formally, a joint probability distribution p(o,s) over observations and hidden states. *Used in: All courses.*

**Generative Process** — The actual real world that generates the signals your senses receive. Distinguished from the Generative Model, which is the brain's approximation. *Used in: Life M1, Tech M1.*

---

## H

**Hidden States** — Things about the world you can't directly observe but have to infer. You can see a shadow but you have to guess the object casting it. *Used in: Math M3, Tech M3.*

**Homeostasis** — Your body's ability to maintain stable internal conditions (temperature, blood sugar, pH) despite changes in the environment. Active Inference sees homeostasis as a form of prediction. *Used in: Bio M1, Bio M2.*

---

## I

**Inference** — Figuring out what's probably true based on the evidence you have. In Active Inference, perception, action, and learning are all forms of inference. *Used in: All courses.*

**Information Gain** — How much you expect to learn from taking a particular action. It's why you explore: to reduce uncertainty. *Used in: Math M5, Tech M5.*

**Internal States** — Everything inside a system's boundary — the "guts" of the system, shielded from the outside except through the blanket. Symbol: μ. *Used in: All courses.*

---

## K

**KL Divergence** — A measure of how different two probability distributions are. It's always ≥ 0 and equals 0 only when the distributions are identical. Symbol: D_KL. *Used in: Math M3.*

---

## L

**Likelihood** — How probable an observation is, given a particular state of the world. "If it's raining, how likely am I to see wet pavement?" Written as P(observation|state). Matrix: **A**. *Used in: Math M3, Tech M3.*

---

## M

**Markov Blanket** — The statistical boundary that separates a system from its environment. It consists of sensory states (influenced by the outside) and active states (influencing the outside). Named after Andrey Markov. *Used in: All courses.*

**Mental Model** — See Generative Model. An informal term for the brain's internal representation of how the world works. *Used in: Life courses.*

**Mutual Information** — How much knowing one thing tells you about another thing. If knowing the weather tells you a lot about what people are wearing, the mutual information between weather and clothing is high. *Used in: Math M7.*

---

## N

**Non-Equilibrium Steady State (NESS)** — A stable pattern that persists even though energy and matter are constantly flowing through it — like a whirlpool or a living cell. *Used in: Life M1, Math M1.*

---

## O

**Observation** — What you actually perceive — the data your senses give you. In the math, observations are denoted by `o`. *Used in: All courses.*

---

## P

**Perception** — The process of figuring out what's happening in the world based on sensory signals. In Active Inference, perception IS inference — your brain is constantly guessing and updating. *Used in: All courses.*

**Policy** — A plan: a sequence of actions you might take. In Active Inference, you choose the policy that minimizes expected free energy. Symbol: π. *Used in: Math M5, Tech M5.*

**Posterior** — Your updated belief after seeing evidence. Before evidence: "prior." After evidence: "posterior." *Used in: Math M4.*

**Pragmatic Value** — The value of getting outcomes you actually want. It's the "reward" component of decision-making, complementing epistemic value. *Used in: Math M5, Tech M5.*

**Precision** — How much you trust a signal. High precision means the signal is clear and reliable; low precision means it's noisy. Formally, the inverse of variance. *Used in: Bio M4, Math M4.*

**Prediction** — What your brain expects to happen next, based on its model of the world. *Used in: All courses.*

**Prediction Error** — The difference between what you predicted and what actually happened. Your brain uses prediction errors to update its model. See also: Surprisal. *Used in: All courses.*

**Predictive Coding** — A theory of brain function: the brain sends predictions downward through its hierarchy, and only the prediction errors (surprises) get sent upward. *Used in: Bio M3.*

**Prior** — What you believe before seeing any evidence. Your starting assumption. *Used in: Math M4.*

**Probability** — A number between 0 and 1 that represents how likely something is. 0 = impossible, 1 = certain. *Used in: Math M1.*

---

## R

**Recognition Density** — See Approximate Posterior. The brain's best guess about hidden states, written as q(s). *Used in: Math M3.*

**Risk** — In Active Inference, the expected divergence between predicted outcomes and preferred outcomes. High risk means you expect things to go badly. *Used in: Math M5.*

---

## S

**Self-Organization** — When order emerges on its own from simple interactions, without anyone being in charge. Examples: flocking birds, snowflakes, traffic jams. *Used in: Life M1, Bio M1.*

**Sensory States** — The part of a system's boundary that receives information from the outside world (like your eyes, ears, or a thermometer's sensor). Symbol: σ. *Used in: All courses.*

**Surprise** — See Prediction Error. Technically, surprisal is −ln p(o), the negative log probability of an observation. Something with low probability is very surprising. *Used in: All courses.*

**System** — Anything with an identifiable boundary between inside and outside — a cell, a person, a school, a city. In Active Inference, systems are defined by their Markov Blankets. *Used in: All courses.*

---

## T

**Transition Matrix** — A table showing how likely each state is to change into each other state. Matrix: **B**. *Used in: Math M2, Tech M3.*

---

## U

**Updating** — Changing your beliefs based on new evidence. This is the core process in Active Inference: predict, observe, compare, update. *Used in: All courses.*

---

## V

**Variational Free Energy (VFE)** — A number that measures how wrong your brain's current model is. The brain tries to minimize this — either by updating beliefs (perception) or by acting on the world (action). Symbol: F. *Used in: Math M3, Tech M3.*

---

## Per-Course Term Emphasis

| Term | Everyday Life | Biology & Health | Math Foundations | Technology & AI |
| --- | :---: | :---: | :---: | :---: |
| Prediction / Surprise | ★★★ | ★★★ | ★★ | ★★ |
| Markov Blanket | ★★ | ★★ | ★★★ | ★★★ |
| Homeostasis | ★ | ★★★ | ★ | ★ |
| Bayes' Theorem | ★ | ★ | ★★★ | ★★ |
| Generative Model | ★★ | ★★ | ★★★ | ★★★ |
| Policy / EFE | ★ | ★ | ★★★ | ★★★ |
| Precision | ★★ | ★★★ | ★★ | ★★ |
| Predictive Coding | ★ | ★★★ | ★★ | ★ |
