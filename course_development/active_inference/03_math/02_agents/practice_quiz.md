# Practice Quiz: Agents

## Part A: Multiple Choice

1. A generative model p(o, s, θ) specifies:
A) Only the probability of observations
B) The joint distribution over observations, hidden states, and parameters — encoding how observations are generated from hidden causes
C) The mapping from inputs to outputs (discriminative)
D) Only the prior over parameters

2. The recognition density q(s, θ) is:
A) The exact posterior p(s, θ | o)
B) An approximate posterior that is optimized to be close to the true posterior by minimizing free energy
C) A fixed distribution that never changes
D) The likelihood function

3. Sufficient statistics of an exponential family distribution:
A) Are always the mean and variance
B) Are the minimal statistics that fully determine the distribution (e.g., mean and covariance for Gaussian, concentration parameters for Dirichlet)
C) Are irrelevant to Active Inference
D) Must be computed exactly

4. The Free Energy Principle states that:
A) All systems minimize thermodynamic free energy
B) The internal states of a Markov-blanketed system can be described as parameterizing a recognition density that minimizes variational free energy
C) Free energy is always zero for biological systems
D) Only brains perform free energy minimization

5. A Partially Observed Markov Decision Process (POMDP) extends an HMM by adding:
A) More hidden states
B) Actions that influence state transitions, making the agent an active participant
C) Continuous observations only
D) Deterministic dynamics

6. The mean-field approximation q(s, θ) = q(s) · q(θ):
A) Is always exact
B) Assumes independence between hidden states and parameters, which may introduce approximation error
C) Requires Monte Carlo sampling
D) Only works for discrete distributions

7. The natural gradient ∂F/∂μ in the space of sufficient statistics:
A) Is identical to the ordinary gradient
B) Accounts for the geometry of the probability distribution (Fisher information metric), enabling more efficient updates
C) Is always zero
D) Only applies to Gaussian distributions

## Part B: Short Answer

1. For a Gaussian generative model p(s) = N(0, σ_p²) and p(o|s) = N(s, σ_o²), with recognition density q(s) = N(μ_q, σ_q²), derive the optimal μ_q*and σ_q²* that minimize free energy. Show that the result is precision-weighted combination of prior and likelihood.
2. Explain why model evidence ln p(o) is important for model comparison. If two generative models M₁ and M₂ are compared, how does the free energy F serve as a proxy for model evidence?
3. Write the generative model for a two-level hierarchical model where observations depend on level-1 states, which depend on level-2 states. Explain how this hierarchy enables the representation of increasingly abstract causes.
