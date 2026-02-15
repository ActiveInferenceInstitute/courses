# Lab: Information Theory -- Bits, Entropy, and Shared Knowledge

## Objective

Practice computing **information content**, **entropy**, and **mutual information** -- the mathematical tools that quantify how much communication reduces an agent's uncertainty. In Active Inference, surprisal and entropy are central to the free energy calculation.

## Prerequisites

- Completed Math Foundations: Learning module (prediction error, model updating)
- Comfort with logarithms (base 2) and probability

## Part 1: Information Content (Surprisal)

**Goal**: Compute how much information a single message carries.

The information content of an event with probability p is: I = -log2(p) bits.

1. A fair coin lands heads: I = -log2(0.5) = ? bits.
2. A fair die lands on 6: I = -log2(1/6) = ? bits.
3. "School is cancelled" (P = 0.01): I = ? bits.
4. "The sun rose today" (P = 0.99): I = ? bits.
5. Which event carries more information? Why does rare = more informative?
6. In Active Inference, this quantity is called **surprisal** -- it measures how unexpected an observation is under the generative model.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Entropy

**Goal**: Compute the average information content of a probability distribution.

Entropy: H(X) = -sum(p_i * log2(p_i)) -- the expected surprisal.

Distribution A (fair coin): P(H) = 0.5, P(T) = 0.5.
Distribution B (biased coin): P(H) = 0.9, P(T) = 0.1.

1. H(A) = -(0.5 * log2(0.5) + 0.5 * log2(0.5)) = ? bits.
2. H(B) = -(0.9 * log2(0.9) + 0.1 * log2(0.1)) = ? bits.
3. Which distribution has higher entropy? Why?
4. A certain outcome (P = 1) has H = 0 bits. A maximally uncertain distribution (all outcomes equally likely) has maximum entropy. Why does this make sense?
5. In Active Inference, minimizing free energy involves reducing the entropy of beliefs about hidden states.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: KL Divergence

**Goal**: Measure the "distance" between two probability distributions.

KL(P || Q) = sum(p_i * log2(p_i / q_i)) -- how much P differs from Q.

Let P = {0.7, 0.2, 0.1} (your beliefs about tomorrow: sunny, cloudy, rainy).
Let Q = {0.4, 0.3, 0.3} (the weather forecast).

1. KL(P || Q) = 0.7*log2(0.7/0.4) + 0.2*log2(0.2/0.3) + 0.1*log2(0.1/0.3) = ?
2. Is KL divergence symmetric? Compute KL(Q || P) and compare.
3. KL divergence is always >= 0. When does it equal 0?
4. In Active Inference, variational free energy includes a KL divergence between the agent's approximate beliefs and the true posterior -- the agent acts to minimize this gap.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Mutual Information

**Goal**: Quantify how much knowing one variable tells you about another.

Consider weather (X) and umbrella-carrying (Y):

| | Umbrella | No umbrella |
|--|----------|-------------|
| Rainy | 0.35 | 0.05 |
| Sunny | 0.10 | 0.50 |

1. Compute H(X) -- the entropy of the weather marginal.
2. Compute H(X | Y = umbrella) -- the entropy of weather given you see an umbrella.
3. Does knowing about the umbrella reduce your uncertainty about weather?
4. Mutual information I(X;Y) = H(X) - H(X|Y). This measures how much one variable **communicates** about the other.
5. In Active Inference, agents seek observations with high mutual information -- they look where they expect to learn the most.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Information content / surprisal | I = -log2(p) | Bits of information in a single event |
| Entropy | H(X) = -sum(p_i * log2(p_i)) | Average information content of a distribution |
| KL divergence | KL(P \|\| Q) | How much distribution P differs from Q |
| Mutual information | I(X;Y) = H(X) - H(X\|Y) | How much knowing Y reduces uncertainty about X |
