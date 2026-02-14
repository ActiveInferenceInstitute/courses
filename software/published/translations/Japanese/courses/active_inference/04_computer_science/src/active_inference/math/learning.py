"""Learning — Dirichlet parameter updates and Bayesian Model Reduction.

Notation (from resources/notation_table.md):
    pA          — Dirichlet concentration parameters for A-matrix
    pB          — Dirichlet concentration parameters for B-matrix
    pD          — Dirichlet concentration parameters for D-vector
    BMR         — Bayesian Model Reduction
    ΔF          — Log Bayes factor (change in free energy under reduced model)

Cross-course connections (see resources/cross_course_map.md):
    Philosophy M6  — Epistemic growth, niche construction
    CogSci M6      — Synaptic plasticity, dopamine, sleep consolidation
    Math M6        — Gradient descent on VFE, BMR derivation
    CS M6          — Parameter learning: updating Dirichlet concentrations

See glossary.md:
    "Concentration Parameters", "Bayesian Model Reduction",
    "Dirichlet Distribution"
"""

import numpy as np
from scipy.special import gammaln, digamma
import logging

logger = logging.getLogger(__name__)


# ======================================================================
# Dirichlet A-matrix updates
# ======================================================================

def update_dirichlet_A(
    pA: np.ndarray,
    observation: int,
    q_s: np.ndarray,
) -> np.ndarray:
    """Update Dirichlet concentration parameters for the A-matrix.

    ``pA'[o, s] = pA[o, s] + q(s_t = s) × δ(o_t = o)``

    Each observation adds a fractional count proportional to the
    posterior belief about which state caused it.

    Parameters
    ----------
    pA : np.ndarray
        Concentration parameters, shape ``(num_obs, num_states)``.
    observation : int
        Observed index ``o_t``.
    q_s : np.ndarray
        Posterior beliefs ``q(s)``, shape ``(num_states,)``.

    Returns
    -------
    np.ndarray
        Updated concentration parameters ``pA'``.

    Raises
    ------
    ValueError
        If dimensions are inconsistent.
    """
    if pA.ndim != 2:
        raise ValueError(f"pA must be 2-D, got {pA.ndim}-D")
    if not 0 <= observation < pA.shape[0]:
        raise ValueError(
            f"observation {observation} out of range [0, {pA.shape[0]})"
        )
    if q_s.shape[0] != pA.shape[1]:
        raise ValueError(
            f"q_s length {q_s.shape[0]} != pA columns {pA.shape[1]}"
        )

    pA_new = pA.copy()
    pA_new[observation, :] += q_s
    logger.debug("Updated pA: observation=%d", observation)
    return pA_new


# ======================================================================
# Dirichlet B-matrix updates
# ======================================================================

def update_dirichlet_B(
    pB: np.ndarray,
    q_s_prev: np.ndarray,
    q_s_curr: np.ndarray,
    action: int,
) -> np.ndarray:
    """Update Dirichlet concentration parameters for the B-matrix.

    ``pB'[s', s, a] = pB[s', s, a] + q(s'_t) × q(s_{t−1}) × δ(a_t = a)``

    Parameters
    ----------
    pB : np.ndarray
        Concentration parameters, shape ``(num_states, num_states, num_actions)``.
    q_s_prev : np.ndarray
        Posterior beliefs at previous timestep ``q(s_{t−1})``.
    q_s_curr : np.ndarray
        Posterior beliefs at current timestep ``q(s_t)``.
    action : int
        Action taken at previous timestep.

    Returns
    -------
    np.ndarray
        Updated ``pB'``.

    Raises
    ------
    ValueError
        If dimensions are inconsistent or action out of range.
    """
    if pB.ndim != 3:
        raise ValueError(f"pB must be 3-D, got {pB.ndim}-D")
    if not 0 <= action < pB.shape[2]:
        raise ValueError(
            f"action {action} out of range [0, {pB.shape[2]})"
        )

    pB_new = pB.copy()
    pB_new[:, :, action] += np.outer(q_s_curr, q_s_prev)
    logger.debug("Updated pB: action=%d", action)
    return pB_new


# ======================================================================
# Dirichlet D-vector updates  (notation_table.md line 56)
# ======================================================================

def update_dirichlet_D(
    pD: np.ndarray,
    q_s_initial: np.ndarray,
) -> np.ndarray:
    """Update Dirichlet concentration parameters for the D-vector.

    ``pD'[s] = pD[s] + q(s_0)``

    Called once per episode with the inferred initial-state beliefs.

    See notation_table.md: Learning Parameters, ``pD`` — Dirichlet hyperparameters
    for D-vector. Updated each episode start.

    Parameters
    ----------
    pD : np.ndarray
        Concentration parameters, shape ``(num_states,)``.
    q_s_initial : np.ndarray
        Posterior beliefs about the initial state ``q(s_0)``.

    Returns
    -------
    np.ndarray
        Updated ``pD'``.
    """
    if pD.shape != q_s_initial.shape:
        raise ValueError(
            f"Shape mismatch: pD {pD.shape} vs q_s_initial {q_s_initial.shape}"
        )
    pD_new = pD.copy()
    pD_new += q_s_initial
    logger.debug("Updated pD")
    return pD_new


# ======================================================================
# Expected (mean) matrices from Dirichlet parameters
# ======================================================================

def expected_A(pA: np.ndarray) -> np.ndarray:
    """Expected A-matrix (Dirichlet mean).

    ``E[A[o, s]] = pA[o, s] / Σ_{o'} pA[o', s]``

    Parameters
    ----------
    pA : np.ndarray
        Concentration parameters, shape ``(num_obs, num_states)``.

    Returns
    -------
    np.ndarray
        Column-normalised expected likelihood.
    """
    return pA / pA.sum(axis=0, keepdims=True)


def expected_B(pB: np.ndarray) -> np.ndarray:
    """Expected B-matrix (Dirichlet mean).

    ``E[B[s', s, a]] = pB[s', s, a] / Σ_{s''} pB[s'', s, a]``

    Parameters
    ----------
    pB : np.ndarray
        Concentration parameters, shape ``(num_states, num_states, num_actions)``.

    Returns
    -------
    np.ndarray
        Column-normalised expected transition matrix.
    """
    return pB / pB.sum(axis=0, keepdims=True)


def expected_D(pD: np.ndarray) -> np.ndarray:
    """Expected D-vector (Dirichlet mean).

    ``E[D[s]] = pD[s] / Σ_{s'} pD[s']``

    Parameters
    ----------
    pD : np.ndarray
        Concentration parameters, shape ``(num_states,)``.

    Returns
    -------
    np.ndarray
        Normalised expected prior.
    """
    return pD / pD.sum()


# ======================================================================
# Dirichlet entropy
# ======================================================================

def dirichlet_entropy(alpha: np.ndarray) -> float:
    """Entropy of a Dirichlet distribution with parameters *alpha*.

    ``H[Dir(α)] = ln B(α) + (α₀ − K) ψ(α₀) − Σ_k (α_k − 1) ψ(α_k)``

    where ``α₀ = Σ_k α_k``, ``K = len(α)``, ``ψ`` is the digamma fn.

    Parameters
    ----------
    alpha : np.ndarray
        Concentration parameters (1-D).

    Returns
    -------
    float
        Entropy in nats.
    """
    alpha = np.asarray(alpha, dtype=np.float64)
    a0 = alpha.sum()
    K = len(alpha)
    log_beta = gammaln(alpha).sum() - gammaln(a0)
    return float(
        log_beta + (a0 - K) * digamma(a0) - np.sum((alpha - 1) * digamma(alpha))
    )


# ======================================================================
# Bayesian Model Reduction
# ======================================================================

def bayesian_model_reduction(
    pA: np.ndarray,
    pA_prior: np.ndarray,
) -> tuple:
    """Bayesian Model Reduction — compare full model to reduced (prior) model.

    Computes the log Bayes factor ΔF for each column of A:
        ``ΔF = ln B(pA) − ln B(pA_prior)``
    where ``B(·)`` is the multivariate Beta function.

    If ``ΔF < 0`` for a column, the reduced model is better → prune.

    See glossary.md: "Bayesian Model Reduction".
    See Math M6 lab: BMR derivation exercise.

    Parameters
    ----------
    pA : np.ndarray
        Learned concentrations, shape ``(num_obs, num_states)``.
    pA_prior : np.ndarray
        Prior concentrations, shape ``(num_obs, num_states)``.

    Returns
    -------
    delta_F : np.ndarray
        Log Bayes factor per column, shape ``(num_states,)``.
    should_prune : np.ndarray
        Boolean mask: True where the reduced model is better.
    """
    if pA.shape != pA_prior.shape:
        raise ValueError(
            f"Shape mismatch: pA {pA.shape} vs pA_prior {pA_prior.shape}"
        )

    num_states = pA.shape[1]
    delta_F = np.zeros(num_states)

    for s in range(num_states):
        log_beta_learned = gammaln(pA[:, s]).sum() - gammaln(pA[:, s].sum())
        log_beta_prior = gammaln(pA_prior[:, s]).sum() - gammaln(pA_prior[:, s].sum())
        delta_F[s] = log_beta_learned - log_beta_prior

    should_prune = delta_F < 0
    logger.info("BMR: ΔF=%s, prune=%s", delta_F, should_prune)
    return delta_F, should_prune
