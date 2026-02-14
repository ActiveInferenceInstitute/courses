"""Visualization — plotting beliefs, free energy, prediction errors, and policies.

Provides matplotlib-based plotting utilities for Active Inference agents.
All plots use consistent styling and notation from notation_table.md.

Cross-course connections (see resources/cross_course_map.md):
    All modules — visualisation supports every CS module's lab exercises.
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import logging
from typing import Optional, List

from .config import get_config

logger = logging.getLogger(__name__)

# Use non-interactive backend for tests
matplotlib.use("Agg")

# Apply centralized style
get_config().apply()



def plot_beliefs(
    beliefs_history: List[np.ndarray],
    state_labels: Optional[List[str]] = None,
    title: str = "Beliefs q(s) over time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot evolution of beliefs q(s) across timesteps.

    Parameters
    ----------
    beliefs_history : list of np.ndarray
        Belief vectors, one per timestep.
    state_labels : list of str, optional
        Labels for each state.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    beliefs_array = np.array(beliefs_history)
    T, num_states = beliefs_array.shape

    if state_labels is None:
        state_labels = [f"s={i}" for i in range(num_states)]

    fig, ax = plt.subplots(figsize=(10, 5))
    for s in range(num_states):
        ax.plot(range(T), beliefs_array[:, s], label=state_labels[s], linewidth=2)

    # Calculate entropy H[q(s)] = -Σ q ln q
    entropy_hist = []
    for t in range(T):
        q = beliefs_array[t, :]
        h = -np.sum(q * np.log(q + 1e-16))
        entropy_hist.append(h)

    # Plot entropy on twin axis
    ax2 = ax.twinx()
    ax2.plot(range(T), entropy_hist, "k--", alpha=0.3, linewidth=1, label="Entropy H[q]")
    ax2.set_ylabel("Entropy (nats)", color="gray")
    ax2.tick_params(axis="y", labelcolor="gray")

    ax.set_xlabel("Timestep t")
    ax.set_ylabel("q(s)")
    ax.set_title(title)
    ax.legend()
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved beliefs plot to %s", save_path)

    return fig


def plot_free_energy(
    vfe_history: List[float],
    title: str = "Variational Free Energy F over time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot VFE trajectory across timesteps.

    Parameters
    ----------
    vfe_history : list of float
        VFE values per timestep.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(vfe_history, "b-o", linewidth=2, markersize=4)
    ax.set_xlabel("Timestep t")
    ax.set_ylabel("F (nats)")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved VFE plot to %s", save_path)

    return fig


def plot_prediction_errors(
    observations: List[int],
    predictions: List[np.ndarray],
    title: str = "Prediction Errors ε = o − E_q[o]",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot prediction errors (actual vs predicted observations).

    Parameters
    ----------
    observations : list of int
        Actual observations.
    predictions : list of np.ndarray
        Predicted observation distributions q(o).
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = len(observations)
    expected_o = [int(np.argmax(pred)) for pred in predictions]
    errors = [abs(observations[t] - expected_o[t]) for t in range(T)]

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    axes[0].step(range(T), observations, "r-", label="Actual o", linewidth=2)
    axes[0].step(range(T), expected_o, "b--", label="Predicted argmax q(o)", linewidth=2)
    axes[0].set_ylabel("Observation Index")
    axes[0].set_title("Observations vs Predictions")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].bar(range(T), errors, color="orange", alpha=0.7)
    axes[1].set_xlabel("Timestep t")
    axes[1].set_ylabel("|ε|")
    axes[1].set_title(title)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved prediction error plot to %s", save_path)

    return fig


def plot_policy_values(
    efe_history: List[np.ndarray],
    policy_labels: Optional[List[str]] = None,
    title: str = "Expected Free Energy G(π) over time",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot EFE values for each policy across timesteps.

    Parameters
    ----------
    efe_history : list of np.ndarray
        EFE vectors per timestep, each shape ``(num_policies,)``.
    policy_labels : list of str, optional
        Labels for each policy.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    efe_array = np.array(efe_history)
    T, num_policies = efe_array.shape

    if policy_labels is None:
        policy_labels = [f"π={i}" for i in range(num_policies)]

    fig, ax = plt.subplots(figsize=(10, 5))
    for p in range(num_policies):
        ax.plot(range(T), efe_array[:, p], label=policy_labels[p], linewidth=2)

    ax.set_xlabel("Timestep t")
    ax.set_ylabel("G(π) (nats)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved policy values plot to %s", save_path)

    return fig


def plot_efe_decomposition(
    risk_values: List[float],
    ambiguity_values: List[float],
    title: str = "EFE Decomposition: Risk + Ambiguity",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot risk vs ambiguity components of EFE.

    Risk      = D_KL[q(o|π) ‖ p(o)]  — pragmatic value
    Ambiguity = E_q[H[p(o|s)]]        — epistemic value

    See notation_table.md: EFE decomposition.
    See glossary.md: "Risk", "Ambiguity".

    Parameters
    ----------
    risk_values : list of float
        Risk at each timestep.
    ambiguity_values : list of float
        Ambiguity at each timestep.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = len(risk_values)
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(range(T), risk_values, label="Risk (pragmatic)", alpha=0.7, color="#4C72B0")
    ax.bar(
        range(T), ambiguity_values, bottom=risk_values,
        label="Ambiguity (epistemic)", alpha=0.7, color="#DD8452",
    )

    ax.set_xlabel("Timestep t")
    ax.set_ylabel("G(π) component (nats)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved EFE decomposition plot to %s", save_path)

    return fig


def plot_learning_progress(
    kl_history: List[float],
    title: str = "Learning Progress: D_KL[learned ‖ true]",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot KL divergence between learned and true parameters over episodes.

    Parameters
    ----------
    kl_history : list of float
        KL divergence per episode/step.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(kl_history, "g-o", linewidth=2, markersize=4)
    ax.set_xlabel("Episode")
    ax.set_ylabel("D_KL (nats)")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved learning progress plot to %s", save_path)

    return fig
