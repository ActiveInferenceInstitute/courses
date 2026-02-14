# Practice Quiz: The Mathematics of Active Inference

## Part A: Multiple Choice

1. The variational free energy F is best described as:
A) The exact posterior probability
B) An upper bound on surprise (negative log-evidence)
C) The entropy of the generative model
D) The mutual information between agent and environment

2. If the recognition density q(s) exactly equals the true posterior p(s|o), then the variational free energy equals:
A) Infinity
B) Zero
C) The negative log-evidence -ln p(o)
D) The KL divergence

3. In the expected free energy decomposition G = risk + ambiguity, the "risk" term measures:
A) The probability of the agent being destroyed
B) The divergence between predicted outcomes and preferred outcomes
C) The entropy of the prior distribution
D) The variance of the sensory noise

4. The Fokker-Planck equation describes:
A) The trajectory of a single particle
B) The evolution of a probability density over time
C) The equilibrium temperature of a thermodynamic system
D) The activation function of a neural network

5. In Bayesian Model Reduction, the Occam factor penalizes models for:
A) Having too few parameters
B) Making accurate predictions
C) Unnecessary complexity beyond what the data require
D) Using Dirichlet priors

6. The softmax function sigma(G) = exp(-gamma * G) / sum(exp(-gamma * G)) does what?
A) Converts free energy values into a deterministic policy selection
B) Converts expected free energy values into a probability distribution over policies, with gamma controlling exploration-exploitation
C) Normalizes the likelihood matrix A
D) Computes the KL divergence

7. Dirichlet concentration parameters pA are updated after an observation by:
A) Subtracting the observed transition from the prior
B) Adding a count vector based on the observed state-observation pair
C) Dividing by the number of observations
D) Setting them equal to the maximum likelihood estimate

## Part B: Short Answer

1. Starting from the joint distribution p(o, s) = p(o|s)p(s), derive the variational free energy F = E_q[ln q(s) - ln p(o, s)] and show that F >= -ln p(o). Identify the term that makes this an inequality rather than an equality.

2. Compute the expected free energy G for a two-state, two-action agent where action 1 leads to an informative observation and action 2 leads to a preferred but uninformative outcome. Show how the risk and ambiguity terms trade off.

3. Explain why minimizing variational free energy with respect to the recognition density q (perception) and minimizing it with respect to action a (behavior) are formally the same operation applied to different variables. What does this mathematical unity imply about the relationship between perception and action?
