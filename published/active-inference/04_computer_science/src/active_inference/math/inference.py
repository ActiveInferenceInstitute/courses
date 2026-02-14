"""Inference — standalone state and policy inference algorithms.

This module separates the *algorithms* (state inference, policy inference,
marginal message passing) from the *Agent* class, enabling reuse in labs,
notebooks, and tests without requiring an agent instance.

Notation (from resources/notation_table.md):
    q(s)  — Recognition density (approximate posterior)
    F     — Variational Free Energy
    G(π)  — Expected Free Energy
    γ     — Precision (inverse temperature)

Cross-course connections (see resources/cross_course_map.md):
    Philosophy M3  — Perception as hypothesis testing
    CogSci M3/M4   — Predictive coding, precision weighting
    Math M3/M4      — VFE minimisation, hierarchical inference
    CS M3/M4        — State estimation, message passing
"""

import numpy as np
import logging
from typing import Optional, List

from .free_energy import softmax, compute_vfe, compute_efe, kl_divergence, LOG_ZERO_GUARD

logger = logging.getLogger(__name__)


def run_state_inference(
    prior: np.ndarray,
    observation: int,
    A: np.ndarray,
    num_iterations: int = 16,
    convergence_threshold: float = 1e-8,
) -> dict:
    """Run variational state inference: update q(s) given observation.

    Iterates the fixed-point update ``q(s) ∝ P(o|s) · q(s)`` until
    convergence or *num_iterations* is reached.

    See glossary.md: "Recognition Density", "Predictive Coding".

    Parameters
    ----------
    prior : np.ndarray
        Prior beliefs q(s) before this observation, shape ``(num_states,)``.
    observation : int
        Observed index ``o_t``.
    A : np.ndarray
        Likelihood matrix, shape ``(num_obs, num_states)``.
    num_iterations : int
        Maximum number of belief-update iterations.
    convergence_threshold : float
        Stop early when max absolute change in q(s) drops below this.

    Returns
    -------
    dict
        Keys: ``q_s`` (posterior), ``num_iters`` (actual iterations),
        ``converged`` (bool), ``delta_history`` (list of max deltas).
    """
    q_s = prior.copy()
    log_A = np.log(A[observation, :] + LOG_ZERO_GUARD)
    delta_history: List[float] = []

    for i in range(num_iterations):
        log_q = log_A + np.log(q_s + LOG_ZERO_GUARD)
        q_s_new = softmax(log_q, tau=1.0)
        delta = float(np.max(np.abs(q_s_new - q_s)))
        delta_history.append(delta)
        q_s = q_s_new
        if delta < convergence_threshold:
            logger.debug("State inference converged at iter %d (δ=%.2e)", i, delta)
            return {
                "q_s": q_s,
                "num_iters": i + 1,
                "converged": True,
                "delta_history": delta_history,
            }

    logger.debug(
        "State inference stopped at %d iters (δ=%.2e)",
        num_iterations, delta_history[-1],
    )
    return {
        "q_s": q_s,
        "num_iters": num_iterations,
        "converged": False,
        "delta_history": delta_history,
    }


def run_policy_inference(
    q_s: np.ndarray,
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    policies: List[List[int]],
    gamma: float = 1.0,
    E: Optional[np.ndarray] = None,
) -> dict:
    """Evaluate policies and return posterior q(π).

    For each policy π:  ``G(π) = Σ_τ G_τ(π)``
    Then:               ``q(π) = σ(−γ · G(π) + ln E(π))``

    See notation_table.md: Policy Selection, ``P(π) = σ(−γ · G(π))``.
    See glossary.md: "Expected Free Energy" (G), "Policy" (π).

    Parameters
    ----------
    q_s : np.ndarray
        Current beliefs q(s), shape ``(num_states,)``.
    A : np.ndarray
        Likelihood matrix.
    B : np.ndarray
        Transition matrix.
    C : np.ndarray
        Log-preferences.
    policies : list of list of int
        Available policies (each is a list of action indices).
    gamma : float
        Precision parameter γ.
    E : np.ndarray, optional
        Habit prior E(π).  Defaults to uniform.

    Returns
    -------
    dict
        Keys: ``q_pi`` (posterior over policies), ``G_values`` (EFE per policy),
        ``selected_policy_idx`` (argmin G), ``selected_action`` (first action).
    """
    num_policies = len(policies)
    G_values = np.zeros(num_policies)

    for i, policy in enumerate(policies):
        q_s_current = q_s.copy()
        G = 0.0
        for action in policy:
            G += compute_efe(q_s_current, A, B, C, action)
            if B.ndim == 3:
                q_s_current = B[:, :, action] @ q_s_current
            else:
                q_s_current = B @ q_s_current
        G_values[i] = G

    # Include habit prior if provided
    log_prior = np.zeros(num_policies)
    if E is not None:
        log_prior = np.log(E + LOG_ZERO_GUARD)

    q_pi = softmax(-gamma * G_values + log_prior)
    best_idx = int(np.argmin(G_values))

    return {
        "q_pi": q_pi,
        "G_values": G_values,
        "selected_policy_idx": best_idx,
        "selected_action": policies[best_idx][0],
    }


def run_mmp(
    observations: List[int],
    A: np.ndarray,
    B: np.ndarray,
    D: np.ndarray,
    policy: List[int],
    num_iterations: int = 8,
) -> dict:
    """Marginal message passing for a sequence under a fixed policy.

    Performs ascending (forward) and descending (backward) message
    passing through a temporal generative model.  This implements the
    hierarchical predictive coding message-passing scheme described in
    Math M4 (cognition) and CS M4 (hierarchical models).

    Parameters
    ----------
    observations : list of int
        Observed sequence ``[o_0, o_1, …, o_{T-1}]``.
    A : np.ndarray
        Likelihood matrix, shape ``(num_obs, num_states)``.
    B : np.ndarray
        Transition matrix, shape ``(num_states, num_states)`` or
        ``(num_states, num_states, num_actions)``.
    D : np.ndarray
        Prior over initial states, shape ``(num_states,)``.
    policy : list of int
        Actions taken: ``[a_0, a_1, …, a_{T-2}]`` (length = T − 1).
    num_iterations : int
        Number of forward-backward sweeps.

    Returns
    -------
    dict
        Keys: ``beliefs`` (list of q(s_t) per timestep), ``vfe`` (per step).
    """
    T = len(observations)
    num_states = D.shape[0]
    beliefs = [D.copy() for _ in range(T)]

    for iteration in range(num_iterations):
        # Forward (ascending) pass
        for t in range(T):
            log_likelihood = np.log(A[observations[t], :] + LOG_ZERO_GUARD)

            if t == 0:
                log_prior = np.log(D + LOG_ZERO_GUARD)
            else:
                if B.ndim == 3:
                    predicted = B[:, :, policy[t - 1]] @ beliefs[t - 1]
                else:
                    predicted = B @ beliefs[t - 1]
                log_prior = np.log(predicted + LOG_ZERO_GUARD)

            log_q = log_likelihood + log_prior
            beliefs[t] = softmax(log_q, tau=1.0)

        # Backward (descending) pass
        for t in range(T - 2, -1, -1):
            if B.ndim == 3:
                B_a = B[:, :, policy[t]]
            else:
                B_a = B
            # Backward message: what state at t would predict beliefs[t+1]?
            backward = B_a.T @ beliefs[t + 1]
            backward = backward / (backward.sum() + LOG_ZERO_GUARD)

            # Combine with forward beliefs
            log_combined = np.log(beliefs[t] + LOG_ZERO_GUARD) + np.log(backward + LOG_ZERO_GUARD)
            beliefs[t] = softmax(log_combined, tau=1.0)

    # Compute VFE at each timestep
    vfe = []
    for t in range(T):
        prior = D if t == 0 else (
            B[:, :, policy[t - 1]] @ beliefs[t - 1] if B.ndim == 3
            else B @ beliefs[t - 1]
        )
        vfe.append(compute_vfe(beliefs[t], observations[t], A, prior))

    return {"beliefs": beliefs, "vfe": vfe}
