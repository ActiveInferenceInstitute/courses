# Lab: Deriving the Core Equations of Active Inference

## Objective

Construct step-by-step derivations of the central mathematical results of Active Inference, verify key properties through worked examples, and develop fluency with the notation and manipulations required throughout the curriculum.

## Prerequisites

* Calculus: partial derivatives, gradients, chain rule
* Probability: Bayes' theorem, conditional probability, expectations
* Linear algebra: matrix multiplication, transpose, inverse (basics)
* Comfort with summation notation and logarithms

## Procedure

### Part 1: The Free Energy Bound (25 minutes)

Starting from Bayes' theorem p(s|o) = p(o|s)p(s) / p(o), derive the variational free energy:

**Step 1**: Define the recognition density q(s) as an approximation to the true posterior p(s|o).

**Step 2**: Write the KL divergence D_KL(q(s) || p(s|o)) and expand using the definition of KL divergence.

**Step 3**: Substitute Bayes' theorem to eliminate p(s|o) and rearrange to isolate -ln p(o).

**Step 4**: Identify F = E_q[ln q(s) - ln p(o,s)] and confirm that F = D_KL(q || p(s|o)) - ln p(o).

**Step 5**: Since D_KL >= 0, conclude that F >= -ln p(o).

**Step 6**: Decompose F into complexity - accuracy: F = D_KL(q(s) || p(s)) - E_q[ln p(o|s)].

Verify: For a Gaussian generative model p(o|s) = N(s, sigma^2) with prior p(s) = N(0, 1) and q(s) = N(mu, v), compute F explicitly as a function of mu and v. Find the optimal mu and v by setting dF/dmu = 0 and dF/dv = 0.

### Part 2: Expected Free Energy Decomposition (20 minutes)

For a discrete-state agent with policy pi:

**Step 1**: Define G(pi) = E_q(o,s|pi) [ln q(s|pi) - ln p(o, s)].

**Step 2**: Add and subtract ln p(o|C) where C encodes preferred outcomes.

**Step 3**: Show that G(pi) = E_q[D_KL(q(s|o,pi) || q(s|pi))] + E_q[D_KL(q(o|pi) || p(o|C))].

**Step 4**: Identify the first term as negative epistemic value (ambiguity) and the second as risk.

**Step 5**: Work through a numerical example with a 2-state, 2-observation system. Compute G for two policies and verify that the policy with higher epistemic value has lower G when the agent is uncertain.

### Part 3: Dirichlet Parameter Learning (15 minutes)

**Step 1**: Define a Dirichlet prior Dir(a_0) over the columns of the likelihood matrix A.

**Step 2**: After observing outcome o_j in state s_k, update the concentration parameter: a_jk := a_jk + 1.

**Step 3**: Compute the expected likelihood matrix E[A] = a_jk / sum_j(a_jk) for each column.

**Step 4**: Show that as data accumulates, E[A] converges to the maximum likelihood estimate, while the precision of the Dirichlet increases (the agent becomes more confident).

**Step 5**: Compute a numerical example: Start with a_0 = [[1, 1], [1, 1]] (uniform prior). After 10 observations of (o=0, s=0) and 10 of (o=1, s=1), compute the updated concentration parameters and the expected A matrix.

### Part 4: Message Passing in a Two-Level Hierarchy (20 minutes)

**Step 1**: Define a two-level generative model: Level 1 generates observations o from states s1; Level 2 generates s1 from states s2.

**Step 2**: Write the prediction error at each level: epsilon_1 = o - g_1(mu_1) and epsilon_2 = mu_1 - g_2(mu_2), where g is the generative mapping and mu is the posterior mean.

**Step 3**: Write the belief update equations with precision weighting: dmu_1/dt = -Pi_1 * epsilon_1 + Pi_2 * epsilon_2.

**Step 4**: Explain the role of precision Pi at each level: high Pi_1 means sensory errors dominate; high Pi_2 means prior errors dominate.

**Step 5**: Simulate (by hand or on paper) a scenario where a strong top-down prior overrides a weak sensory signal. Then reverse the precisions and show how the same sensory input now drives perception.

## Discussion Questions

1. At which step in the free energy derivation does the approximation (the gap between F and true surprise) enter? What determines the size of this gap?
2. How does the expected free energy decomposition formally capture the exploration-exploitation tradeoff? When would an agent choose a purely epistemic policy over a purely pragmatic one?
3. What happens to Dirichlet learning as the concentration parameters grow very large? What are the implications for an agent's ability to adapt to a changing environment?
