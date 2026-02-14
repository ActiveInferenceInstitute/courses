"""Diagnostics — convergence, free energy decomposition, and parameter analysis.

Provides plotting utilities for inference diagnostics, precision sweeps,
entropy/surprisal trajectories, Dirichlet learning progress, and Bayesian
Model Reduction results.

Accessibility: All text ≥ 16pt.

Cross-course connections (see resources/cross_course_map.md):
    CS M3  — State inference convergence
    CS M4  — Precision weighting, attention
    CS M5  — EFE decomposition (risk + ambiguity)
    CS M6  — Dirichlet learning, BMR
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import logging
from typing import Optional, List, Dict

from .config import get_config

logger = logging.getLogger(__name__)

matplotlib.use("Agg")

# Apply centralized style
get_config().apply()



# =====================================================================
# Convergence diagnostics
# =====================================================================

def plot_convergence(
    delta_history: List[float],
    threshold: Optional[float] = 1e-8,
    title: str = "State Inference Convergence",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot belief-update convergence curve.

    Visualises the max-delta from each iteration of ``run_state_inference``,
    with a horizontal threshold line.

    Parameters
    ----------
    delta_history : list of float
        Max absolute change in q(s) per iteration (from ``run_state_inference``).
    threshold : float, optional
        Convergence threshold to draw as horizontal line.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    iters = range(1, len(delta_history) + 1)
    ax.semilogy(iters, delta_history, "b-o", linewidth=2, markersize=5,
                label="max |Δq(s)|")

    if threshold is not None:
        ax.axhline(threshold, color="red", linestyle="--", linewidth=1.5,
                   label=f"Threshold = {threshold:.0e}")

    ax.set_xlabel("Iteration")
    ax.set_ylabel("max |Δq(s)| (log scale)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved convergence plot to %s", save_path)
    return fig


# =====================================================================
# VFE components
# =====================================================================

def plot_vfe_components(
    components_history: List[Dict[str, float]],
    title: str = "VFE Decomposition over Time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot VFE component decomposition (complexity − accuracy).

    Parameters
    ----------
    components_history : list of dict
        Each dict from ``compute_vfe_components`` with keys
        ``F``, ``complexity``, ``accuracy``, ``energy``, ``entropy_q``.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = len(components_history)
    ts = range(T)

    F_vals = [c["F"] for c in components_history]
    complexity = [c["complexity"] for c in components_history]
    accuracy = [c["accuracy"] for c in components_history]

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Top: Total VFE
    axes[0].plot(ts, F_vals, "k-o", linewidth=2, markersize=4, label="F (total)")
    axes[0].set_ylabel("F (nats)")
    axes[0].set_title("Total Variational Free Energy")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Bottom: Decomposition
    axes[1].plot(ts, complexity, "r-s", linewidth=2, markersize=4,
                 label="Complexity D_KL[q||p]")
    axes[1].plot(ts, [-a for a in accuracy], "b-^", linewidth=2, markersize=4,
                 label="−Accuracy E_q[ln P(o|s)]")
    axes[1].set_xlabel("Timestep t")
    axes[1].set_ylabel("Component (nats)")
    axes[1].set_title(title)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved VFE components plot to %s", save_path)
    return fig


# =====================================================================
# EFE components (risk + ambiguity)
# =====================================================================

def plot_efe_components(
    components_history: List[Dict[str, float]],
    title: str = "EFE Components: Risk + Ambiguity",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot EFE risk/ambiguity decomposition over time.

    Parameters
    ----------
    components_history : list of dict
        Each dict from ``compute_efe_components`` with keys
        ``G``, ``risk``, ``ambiguity``.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = len(components_history)
    ts = range(T)

    G_vals = [c["G"] for c in components_history]
    risk = [c["risk"] for c in components_history]
    ambiguity = [c["ambiguity"] for c in components_history]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ts, G_vals, "k-o", linewidth=2, markersize=5, label="G (total)")
    ax.fill_between(ts, 0, risk, alpha=0.3, color="#4C72B0", label="Risk")
    ax.fill_between(ts, risk, [r + a for r, a in zip(risk, ambiguity)],
                    alpha=0.3, color="#DD8452", label="Ambiguity")
    ax.set_xlabel("Timestep t")
    ax.set_ylabel("G(π) component (nats)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved EFE components plot to %s", save_path)
    return fig


# =====================================================================
# Precision sweep
# =====================================================================

def plot_precision_sweep(
    gamma_values: List[float],
    q_pi_matrix: np.ndarray,
    policy_labels: Optional[List[str]] = None,
    title: str = "Policy Posterior q(π) across Precision γ",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Heatmap of policy posteriors across precision γ values.

    Parameters
    ----------
    gamma_values : list of float
        Values of γ tested.
    q_pi_matrix : np.ndarray
        Shape ``(len(gamma_values), num_policies)``.
        Each row is the policy posterior for that γ.
    policy_labels : list of str, optional
        Labels for policies.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    num_gamma, num_policies = q_pi_matrix.shape
    if policy_labels is None:
        policy_labels = [f"π={i}" for i in range(num_policies)]

    fig, ax = plt.subplots(figsize=(max(8, num_policies * 1.5), max(6, num_gamma * 0.5)))
    im = ax.imshow(q_pi_matrix, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1)
    ax.set_xticks(range(num_policies))
    ax.set_xticklabels(policy_labels)
    ax.set_yticks(range(num_gamma))
    ax.set_yticklabels([f"{g:.1f}" for g in gamma_values])
    ax.set_xlabel("Policy π")
    ax.set_ylabel("Precision γ")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="q(π)")

    # Annotate cells
    for i in range(num_gamma):
        for j in range(num_policies):
            v = q_pi_matrix[i, j]
            col = "white" if v > 0.5 else "black"
            ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                    color=col, fontsize=12)

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved precision sweep to %s", save_path)
    return fig


# =====================================================================
# Entropy trajectory
# =====================================================================

def plot_entropy_trajectory(
    beliefs_history: List[np.ndarray],
    title: str = "Entropy H[q(s)] over Time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot entropy of beliefs q(s) at each timestep.

    Parameters
    ----------
    beliefs_history : list of np.ndarray
        Belief vectors per timestep.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    entropies = []
    for q in beliefs_history:
        q_safe = np.clip(q, 1e-16, None)
        H = -np.sum(q_safe * np.log(q_safe))
        entropies.append(H)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(entropies, "m-o", linewidth=2, markersize=5)
    ax.set_xlabel("Timestep t")
    ax.set_ylabel("H[q(s)] (nats)")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved entropy trajectory to %s", save_path)
    return fig


# =====================================================================
# Surprisal trajectory
# =====================================================================

def plot_surprise_trajectory(
    observations: List[int],
    A: np.ndarray,
    beliefs_history: List[np.ndarray],
    title: str = "Surprisal S(o) = −ln p(o) over Time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot surprisal S(o) = −ln Σ_s P(o|s) q(s) per timestep.

    Parameters
    ----------
    observations : list of int
        Observed indices.
    A : np.ndarray
        Likelihood matrix.
    beliefs_history : list of np.ndarray
        Belief vectors per timestep.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    surprisals = []
    for o, q in zip(observations, beliefs_history):
        p_o = float(A[o, :] @ q)
        S = -np.log(p_o + 1e-16)
        surprisals.append(S)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(surprisals, "r-o", linewidth=2, markersize=5)
    ax.set_xlabel("Timestep t")
    ax.set_ylabel("S(o) (nats)")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved surprisal trajectory to %s", save_path)
    return fig


# =====================================================================
# Dirichlet learning progress
# =====================================================================

def plot_dirichlet_learning(
    pA_history: List[np.ndarray],
    true_A: Optional[np.ndarray] = None,
    title: str = "Dirichlet Learning Progress",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Multi-panel showing Dirichlet concentration convergence.

    Plots the expected A-matrix (normalised concentrations) at several
    snapshots, and optionally the distance to the true A.

    Parameters
    ----------
    pA_history : list of np.ndarray
        Snapshots of pA concentrations (one per episode/step).
    true_A : np.ndarray, optional
        Ground-truth A for distance tracking.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    n_snapshots = len(pA_history)

    if true_A is not None:
        # Distance plot + snapshots
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Left: Distance over time
        distances = []
        for pA in pA_history:
            expected = pA / pA.sum(axis=0, keepdims=True)
            dist = np.sqrt(np.mean((expected - true_A) ** 2))
            distances.append(dist)

        axes[0].plot(distances, "g-o", linewidth=2, markersize=4)
        axes[0].set_xlabel("Episode")
        axes[0].set_ylabel("RMSE(expected_A, true_A)")
        axes[0].set_title("Convergence to Ground Truth")
        axes[0].grid(True, alpha=0.3)

        # Right: Final learned vs true
        final_expected = pA_history[-1] / pA_history[-1].sum(axis=0, keepdims=True)
        diff = np.abs(final_expected - true_A)
        im = axes[1].imshow(diff, cmap="Reds", aspect="auto")
        axes[1].set_title("| E[A] − A_true | (final)")
        axes[1].set_xlabel("States")
        axes[1].set_ylabel("Observations")
        fig.colorbar(im, ax=axes[1], shrink=0.7)
        for i in range(diff.shape[0]):
            for j in range(diff.shape[1]):
                v = diff[i, j]
                col = "white" if v > diff.max() / 2 else "black"
                axes[1].text(j, i, f"{v:.3f}", ha="center", va="center",
                             color=col, fontsize=12)

        fig.suptitle(title, fontsize=18, y=1.02)
    else:
        # Just show concentration growth
        total_conc = [pA.sum() for pA in pA_history]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(total_conc, "b-o", linewidth=2, markersize=4)
        ax.set_xlabel("Episode")
        ax.set_ylabel("Total Concentration Σ pA")
        ax.set_title(title)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved Dirichlet learning plot to %s", save_path)
    return fig


# =====================================================================
# BMR results
# =====================================================================

def plot_bmr_results(
    delta_F: np.ndarray,
    should_prune: np.ndarray,
    state_labels: Optional[List[str]] = None,
    title: str = "Bayesian Model Reduction: ΔF per Column",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Bar chart of log Bayes factors with pruning threshold.

    Parameters
    ----------
    delta_F : np.ndarray
        Log Bayes factor per state column.
    should_prune : np.ndarray
        Boolean mask — True where reduced model is better.
    state_labels : list of str, optional
        Labels for state indices.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    n = len(delta_F)
    if state_labels is None:
        state_labels = [f"s={i}" for i in range(n)]

    fig, ax = plt.subplots(figsize=(max(8, n * 1.5), 5))
    x = np.arange(n)
    colours = ["#C44E52" if sp else "#55A868" for sp in should_prune]
    ax.bar(x, delta_F, color=colours, alpha=0.8)
    ax.axhline(0, color="black", linewidth=1)
    ax.set_xlabel("State column")
    ax.set_ylabel("ΔF = ln B(pA) − ln B(pA_prior)")
    ax.set_xticks(x)
    ax.set_xticklabels(state_labels)
    ax.set_title(title)
    ax.grid(True, alpha=0.3, axis="y")

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#C44E52", alpha=0.8, label="Prune (ΔF > 0)"),
        Patch(facecolor="#55A868", alpha=0.8, label="Keep (ΔF ≤ 0)"),
    ]
    ax.legend(handles=legend_elements, loc="best")

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved BMR results to %s", save_path)
    return fig
