"""Free Energy — VFE, EFE, KL divergence, entropy, surprisal, mutual information.

Notation (from resources/notation_table.md):
    F    = E_q[ln q(s) − ln p(o, s)]       — Variational Free Energy
         = D_KL[q(s) ‖ p(s)] − E_q[ln p(o|s)]   (complexity − accuracy)
         = E_q[−ln p(o,s)]   − H[q(s)]           (energy   − entropy)
    G(π) = risk + ambiguity                 — Expected Free Energy
    D_KL = Kullback-Leibler divergence      — always ≥ 0
    H    = Shannon entropy                  — H[p] = −E_p[ln p]
    S    = −ln p(o)                         — surprisal
    I    = H(X) − H(X|Y)                   — mutual information
    σ(·) = softmax function

Cross-course connections (see resources/cross_course_map.md):
    Philosophy M3  — Perception as hypothesis testing
    CogSci M3      — Predictive coding, sensory attenuation
    Math M3        — VFE derivation, recognition density
    CS M3          — State estimation via A/B matrices
"""

import numpy as np
import logging

logger = logging.getLogger(__name__)

LOG_ZERO_GUARD: float = 1e-16
"""Small constant added before log to prevent ``-inf``."""


# ======================================================================
# Core utilities
# ======================================================================

def softmax(x: np.ndarray, tau: float = 1.0) -> np.ndarray:
    """Softmax: σ(x)_i = exp(x_i / τ) / Σ_j exp(x_j / τ).

    In Active Inference this implements policy selection:
    ``P(π) = σ(−γ · G(π))``, where ``τ = 1/γ``
    (see notation_table.md, Policy Selection).

    Parameters
    ----------
    x : np.ndarray
        Input log-values.
    tau : float
        Temperature (``1/γ``).  Lower → more deterministic.

    Returns
    -------
    np.ndarray
        Normalised probability distribution.
    """
    x_scaled = x / (tau + LOG_ZERO_GUARD)
    x_shifted = x_scaled - np.max(x_scaled)
    exp_x = np.exp(x_shifted)
    return exp_x / exp_x.sum()


def entropy(p: np.ndarray) -> float:
    """Shannon entropy H(p) = −Σ_i p_i ln p_i.

    See notation_table.md: Information-Theoretic Quantities, line 65: ``H[p] = −E_p[ln p]``.
    See glossary.md: "Entropy".

    Parameters
    ----------
    p : np.ndarray
        Probability distribution (must sum to 1).

    Returns
    -------
    float
        Entropy in nats.
    """
    p_safe = np.clip(p, LOG_ZERO_GUARD, 1.0)
    return float(-np.sum(p_safe * np.log(p_safe)))


def kl_divergence(q: np.ndarray, p: np.ndarray) -> float:
    """KL divergence D_KL[q ‖ p] = Σ_i q_i ln(q_i / p_i).

    See notation_table.md: Information-Theoretic Quantities, line 64: ``D_KL[q||p]``.
    Always ≥ 0; zero iff q = p.
    See glossary.md: "D_KL (KL Divergence)".

    Parameters
    ----------
    q : np.ndarray
        Approximate posterior (recognition density).
    p : np.ndarray
        Prior or target distribution.

    Returns
    -------
    float
        KL divergence in nats (floored at 0.0).
    """
    q_safe = np.clip(q, LOG_ZERO_GUARD, 1.0)
    p_safe = np.clip(p, LOG_ZERO_GUARD, 1.0)
    return float(max(np.sum(q_safe * np.log(q_safe / p_safe)), 0.0))


# ======================================================================
# Information-theoretic quantities
# ======================================================================

def surprisal(o: int, A: np.ndarray, q_s: np.ndarray) -> float:
    """Surprisal S(o) = −ln p(o) = −ln Σ_s P(o|s) q(s).

    See notation_table.md line 67:
        ``S(o) = −ln p(o)`` — negative log model evidence (surprisal).
    See glossary.md: "Surprisal".

    Parameters
    ----------
    o : int
        Observation index.
    A : np.ndarray
        Likelihood matrix, shape ``(num_obs, num_states)``.
    q_s : np.ndarray
        Belief distribution over states, shape ``(num_states,)``.

    Returns
    -------
    float
        Surprisal in nats.
    """
    p_o = float(A[o, :] @ q_s)
    return -np.log(p_o + LOG_ZERO_GUARD)


def mutual_information(joint: np.ndarray) -> float:
    """Mutual information I(X; Y) from a joint distribution table.

    ``I(X; Y) = H(X) + H(Y) − H(X, Y)``
    Equivalent to ``H(X) − H(X|Y)`` (notation_table.md line 66).

    See glossary.md: "Mutual Information".

    Parameters
    ----------
    joint : np.ndarray
        Joint probability table P(X, Y), shape ``(|X|, |Y|)``.
        Must sum to 1.

    Returns
    -------
    float
        Mutual information in nats (floored at 0.0).
    """
    p_x = joint.sum(axis=1)
    p_y = joint.sum(axis=0)
    return float(max(entropy(p_x) + entropy(p_y) - entropy(joint.ravel()), 0.0))


# ======================================================================
# Variational Free Energy
# ======================================================================

def compute_vfe(
    q_s: np.ndarray,
    o: int,
    A: np.ndarray,
    D: np.ndarray,
) -> float:
    """Variational Free Energy F for a single observation.

    Decomposition 2 from notation_table.md (Free Energy Decompositions):
        ``F = D_KL[q(s) ‖ p(s)] − E_q[ln p(o|s)]`` (Complexity − Accuracy).

    Parameters
    ----------
    q_s : np.ndarray
        Recognition density q(s), shape ``(num_states,)``.
    o : int
        Observation index.
    A : np.ndarray
        Likelihood matrix A[o, s] = P(o|s).
    D : np.ndarray
        Prior over states p(s).

    Returns
    -------
    float
        Variational Free Energy F.
    """
    complexity = kl_divergence(q_s, D)
    accuracy = float(np.sum(q_s * np.log(A[o, :] + LOG_ZERO_GUARD)))
    F = complexity - accuracy
    logger.debug("VFE: complexity=%.4f, accuracy=%.4f, F=%.4f", complexity, accuracy, F)
    return F


def compute_vfe_components(
    q_s: np.ndarray,
    o: int,
    A: np.ndarray,
    D: np.ndarray,
) -> dict:
    """Return all three VFE decompositions as a dict.

    From notation_table.md Free Energy Decompositions:
        1. complexity − accuracy
        2. energy − entropy
        3. divergence + surprisal

    Parameters
    ----------
    q_s, o, A, D
        Same as :func:`compute_vfe`.

    Returns
    -------
    dict
        Keys: ``F``, ``complexity``, ``accuracy``, ``energy``,
        ``entropy_q``, ``surprisal_bound``.
    """
    complexity = kl_divergence(q_s, D)
    accuracy = float(np.sum(q_s * np.log(A[o, :] + LOG_ZERO_GUARD)))
    F = complexity - accuracy

    # Energy − Entropy decomposition
    log_joint = np.log(A[o, :] + LOG_ZERO_GUARD) + np.log(D + LOG_ZERO_GUARD)
    energy = float(-np.sum(q_s * log_joint))
    entropy_q = entropy(q_s)

    return {
        "F": F,
        "complexity": complexity,
        "accuracy": accuracy,
        "energy": energy,
        "entropy_q": entropy_q,
        "surprisal_bound": F,  # F ≥ −ln p(o)
    }


# ======================================================================
# Expected Free Energy
# ======================================================================

def compute_efe(
    q_s: np.ndarray,
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    action: int,
) -> float:
    """Expected Free Energy G for a single-step policy (action).

    Decomposition from notation_table.md (Expected Free Energy > Risk + Ambiguity):
        ``G(π) = D_KL[q(o|π) ‖ p(o)] + E_q[H[p(o|s)]]``
               = risk               + ambiguity

    See glossary.md: "Expected Free Energy", "Risk", "Ambiguity".

    Parameters
    ----------
    q_s : np.ndarray
        Current beliefs q(s), shape ``(num_states,)``.
    A : np.ndarray
        Likelihood matrix, shape ``(num_obs, num_states)``.
    B : np.ndarray
        Transition matrix, shape ``(num_states, num_states, num_actions)``
        or ``(num_states, num_states)``.
    C : np.ndarray
        Log-preferences over observations, shape ``(num_obs,)``.
    action : int
        Action index.

    Returns
    -------
    float
        Expected Free Energy G.
    """
    # Predict next state
    if B.ndim == 3:
        q_s_next = B[:, :, action] @ q_s
    else:
        q_s_next = B @ q_s

    # Predicted observations: q(o|π) = A @ q(s')
    q_o = A @ q_s_next
    q_o = np.clip(q_o, LOG_ZERO_GUARD, 1.0)
    q_o /= q_o.sum()

    # Preferred observations: p(o) = σ(C)
    p_o = softmax(C)

    # Risk: D_KL[q(o|π) ‖ p(o)]
    risk = kl_divergence(q_o, p_o)

    # Ambiguity: E_{q(s')}[H[P(o|s')]]
    ambiguity = sum(
        q_s_next[s] * entropy(A[:, s]) for s in range(len(q_s_next))
    )

    G = risk + ambiguity
    logger.debug(
        "EFE action=%d: risk=%.4f, ambiguity=%.4f, G=%.4f",
        action, risk, ambiguity, G,
    )
    return G


def compute_efe_components(
    q_s: np.ndarray,
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
    action: int,
) -> dict:
    """Return EFE with its risk/ambiguity decomposition.

    Parameters
    ----------
    q_s, A, B, C, action
        Same as :func:`compute_efe`.

    Returns
    -------
    dict
        Keys: ``G``, ``risk``, ``ambiguity``.
    """
    if B.ndim == 3:
        q_s_next = B[:, :, action] @ q_s
    else:
        q_s_next = B @ q_s

    q_o = A @ q_s_next
    q_o = np.clip(q_o, LOG_ZERO_GUARD, 1.0)
    q_o /= q_o.sum()

    p_o = softmax(C)
    risk = kl_divergence(q_o, p_o)
    ambiguity = sum(
        q_s_next[s] * entropy(A[:, s]) for s in range(len(q_s_next))
    )
    return {"G": risk + ambiguity, "risk": risk, "ambiguity": ambiguity}
