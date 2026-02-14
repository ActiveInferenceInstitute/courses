"""Matrix and model structure visualization.

Provides annotated heatmaps for A, B, C, D, E matrices and Dirichlet
concentration parameters, plus composite model-summary dashboards and
transition-graph renderers.

Accessibility: All text ≥ 16pt.  See STYLE below.

Cross-course connections (see resources/cross_course_map.md):
    CS M1  — Generative process vs generative model
    CS M2  — A–E matrix specification
    CS M6  — Dirichlet concentration parameters
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import logging
import warnings
from typing import Optional, List, TYPE_CHECKING

from .config import get_config

if TYPE_CHECKING:
    from ..agent.generative_model import GenerativeModel

logger = logging.getLogger(__name__)

matplotlib.use("Agg")

# Apply centralized style
get_config().apply()



# =====================================================================
# Generic heatmap
# =====================================================================

def plot_matrix_heatmap(
    matrix: np.ndarray,
    row_labels: Optional[List[str]] = None,
    col_labels: Optional[List[str]] = None,
    title: str = "Matrix",
    cmap: str = get_config().cmap_probability,
    annotate: bool = True,
    fmt: str = ".2f",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Annotated heatmap for any 2-D matrix.

    Parameters
    ----------
    matrix : np.ndarray
        2-D array to visualise.
    row_labels, col_labels : list of str, optional
        Tick labels for rows/columns.
    title : str
        Plot title.
    cmap : str
        Matplotlib colour map name.
    annotate : bool
        If True, print values inside each cell.
    fmt : str
        Format string for cell annotations.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    matrix = np.atleast_2d(matrix)
    nrows, ncols = matrix.shape

    cell_w = max(1.2, 0.9 * ncols)
    cell_h = max(1.2, 0.9 * nrows)
    fig, ax = plt.subplots(figsize=(cell_w + 2, cell_h + 2))

    im = ax.imshow(matrix, cmap=cmap, aspect="auto")
    fig.colorbar(im, ax=ax, shrink=0.8)

    if row_labels is None:
        row_labels = [str(i) for i in range(nrows)]
    if col_labels is None:
        col_labels = [str(i) for i in range(ncols)]

    ax.set_xticks(range(ncols))
    ax.set_xticklabels(col_labels)
    ax.set_yticks(range(nrows))
    ax.set_yticklabels(row_labels)
    ax.set_title(title)

    if annotate:
        for i in range(nrows):
            for j in range(ncols):
                val = matrix[i, j]
                colour = "white" if val > (matrix.max() + matrix.min()) / 2 else "black"
                ax.text(j, i, f"{val:{fmt}}", ha="center", va="center",
                        color=colour, fontsize=14)

    # plt.tight_layout() causes warnings with some aspect ratios
    # handled by flexible figure size above

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved matrix heatmap to %s", save_path)
    return fig


# =====================================================================
# A-matrix (likelihood)
# =====================================================================

def plot_A_matrix(
    model: "GenerativeModel",
    obs_labels: Optional[List[str]] = None,
    state_labels: Optional[List[str]] = None,
    title: str = "A-matrix: P(o | s)",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Visualise the likelihood matrix A as an annotated heatmap.

    Parameters
    ----------
    model : GenerativeModel
        The generative model containing matrix A.
    obs_labels : list of str, optional
        Labels for observation indices.
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
    if obs_labels is None:
        obs_labels = [f"o={i}" for i in range(model.num_obs)]
    if state_labels is None:
        state_labels = [f"s={i}" for i in range(model.num_states)]

    fig = plot_matrix_heatmap(
        model.A,
        row_labels=obs_labels, col_labels=state_labels,
        title=title, cmap=get_config().cmap_probability, save_path=save_path,
    )
    fig.axes[0].set_xlabel("Hidden states s")
    fig.axes[0].set_ylabel("Observations o")
    logger.info("Plotted A-matrix (%d×%d)", model.num_obs, model.num_states)
    return fig


# =====================================================================
# B-matrix (transitions)
# =====================================================================

def plot_B_matrix(
    model: "GenerativeModel",
    action: Optional[int] = None,
    state_labels: Optional[List[str]] = None,
    action_labels: Optional[List[str]] = None,
    title: Optional[str] = None,
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Visualise transition matrix B as heatmap(s).

    If *action* is given, plots a single B[:,:,action].
    If *action* is None, plots a grid of all actions.

    Parameters
    ----------
    model : GenerativeModel
        The generative model containing matrix B.
    action : int, optional
        Specific action to plot.  None → plot all.
    state_labels : list of str, optional
        Labels for state indices.
    action_labels : list of str, optional
        Labels for action indices.
    title : str, optional
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if state_labels is None:
        state_labels = [f"s={i}" for i in range(model.num_states)]

    if model.B.ndim == 2:
        # Single action — just a 2-D matrix
        t = title or "B-matrix: P(s' | s)"
        return plot_matrix_heatmap(
            model.B, row_labels=state_labels, col_labels=state_labels,
            title=t, cmap=get_config().cmap_probability, save_path=save_path,
        )

    if action is not None:
        t = title or f"B-matrix: P(s' | s, a={action})"
        fig = plot_matrix_heatmap(
            model.B[:, :, action],
            row_labels=state_labels, col_labels=state_labels,
            title=t, cmap=get_config().cmap_probability, save_path=save_path,
        )
        fig.axes[0].set_xlabel("Current state s")
        fig.axes[0].set_ylabel("Next state s'")
        return fig

    # Grid of all actions
    num_actions = model.num_actions
    if action_labels is None:
        action_labels = [f"a={i}" for i in range(num_actions)]

    cols = min(num_actions, 4)
    rows = (num_actions + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols + 1, 4 * rows + 1),
                             squeeze=False)

    for a_idx in range(num_actions):
        r, c = divmod(a_idx, cols)
        ax = axes[r][c]
        im = ax.imshow(model.B[:, :, a_idx], cmap=get_config().cmap_probability, aspect="auto",
                       vmin=0, vmax=1)
        ax.set_title(f"B(a={action_labels[a_idx]})", fontsize=16)
        ax.set_xticks(range(model.num_states))
        ax.set_xticklabels(state_labels, fontsize=12)
        ax.set_yticks(range(model.num_states))
        ax.set_yticklabels(state_labels, fontsize=12)
        # Annotate
        for i in range(model.num_states):
            for j in range(model.num_states):
                v = model.B[i, j, a_idx]
                col = "white" if v > 0.5 else "black"
                ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                        color=col, fontsize=12)

    # Hide unused axes
    for idx in range(num_actions, rows * cols):
        r, c = divmod(idx, cols)
        axes[r][c].set_visible(False)

    t = title or "B-matrix: P(s' | s, a) — all actions"
    fig.suptitle(t, fontsize=18, y=1.02)
    fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.6, label="P(s'|s,a)")
    # Suppress tight_layout warnings for complex grids
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        plt.tight_layout(rect=[0, 0, 1, 0.98])

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved B-matrix grid to %s", save_path)
    return fig


# =====================================================================
# C-matrix (preferences)
# =====================================================================

def plot_C_preferences(
    model: "GenerativeModel",
    obs_labels: Optional[List[str]] = None,
    title: str = "C-vector: Log-Preferences ln P(o)",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Bar chart of log-preferences C with softmax probability overlay.

    Parameters
    ----------
    model : GenerativeModel
        The generative model containing vector C.
    obs_labels : list of str, optional
        Labels for observation indices.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if obs_labels is None:
        obs_labels = [f"o={i}" for i in range(model.num_obs)]

    C = model.C
    # Softmax of C for probability overlay
    exp_C = np.exp(C - C.max())
    p_C = exp_C / exp_C.sum()

    fig, ax1 = plt.subplots(figsize=(max(6, len(C) * 1.2), 5))
    x = np.arange(len(C))

    bars = ax1.bar(x, C, color="#4C72B0", alpha=0.8, label="ln P(o)")
    ax1.set_xlabel("Observation")
    ax1.set_ylabel("ln P(o) (nats)", color="#4C72B0")
    ax1.set_xticks(x)
    ax1.set_xticklabels(obs_labels)
    ax1.axhline(0, color="grey", linewidth=0.8, linestyle="--")
    ax1.grid(True, alpha=0.3, axis="y")

    ax2 = ax1.twinx()
    ax2.plot(x, p_C, "ro-", linewidth=2, markersize=8, label="σ(C)")
    ax2.set_ylabel("P(o) = σ(C)", color="red")
    ax2.set_ylim(-0.05, 1.05)

    ax1.set_title(title)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="best")

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved C-preferences plot to %s", save_path)
    return fig


# =====================================================================
# D-vector (prior)
# =====================================================================

def plot_D_prior(
    model: "GenerativeModel",
    state_labels: Optional[List[str]] = None,
    title: str = "D-vector: Prior P(s₀)",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Bar chart of prior D with entropy annotation.

    Parameters
    ----------
    model : GenerativeModel
        The generative model containing vector D.
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
    if state_labels is None:
        state_labels = [f"s={i}" for i in range(model.num_states)]

    D = model.D
    H = -np.sum(D * np.log(D + 1e-16))

    fig, ax = plt.subplots(figsize=(max(6, len(D) * 1.2), 5))
    x = np.arange(len(D))
    ax.bar(x, D, color="#55A868", alpha=0.8)
    ax.set_xlabel("State")
    ax.set_ylabel("P(s₀)")
    ax.set_xticks(x)
    ax.set_xticklabels(state_labels)
    ax.set_ylim(0, 1.15)
    ax.set_title(title)
    ax.grid(True, alpha=0.3, axis="y")

    # Entropy annotation
    ax.text(0.98, 0.95, f"H[D] = {H:.3f} nats",
            transform=ax.transAxes, ha="right", va="top",
            fontsize=14, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    # plt.tight_layout() causes warnings with some aspect ratios
    try:
        plt.tight_layout()
    except UserWarning:  # pragma: no cover
        pass

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved D-prior plot to %s", save_path)
    return fig


# =====================================================================
# E-vector (habits)
# =====================================================================

def plot_E_habits(
    model: "GenerativeModel",
    policy_labels: Optional[List[str]] = None,
    title: str = "E-vector: Habit Prior P(π)",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Bar chart of habit vector E.

    Parameters
    ----------
    model : GenerativeModel
        The generative model (must have E set).
    policy_labels : list of str, optional
        Labels for policy indices.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure

    Raises
    ------
    ValueError
        If model.E is None.
    """
    if model.E is None:
        raise ValueError("Model has no habit prior E")

    E = model.E
    if policy_labels is None:
        policy_labels = [f"π={i}" for i in range(len(E))]

    fig, ax = plt.subplots(figsize=(max(6, len(E) * 1.2), 5))
    x = np.arange(len(E))
    ax.bar(x, E, color="#C44E52", alpha=0.8)
    ax.set_xlabel("Policy π")
    ax.set_ylabel("P(π)")
    ax.set_xticks(x)
    ax.set_xticklabels(policy_labels)
    ax.set_ylim(0, 1.15)
    ax.set_title(title)
    ax.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved E-habits plot to %s", save_path)
    return fig


# =====================================================================
# Model summary (multi-panel)
# =====================================================================

def plot_model_summary(
    model: "GenerativeModel",
    obs_labels: Optional[List[str]] = None,
    state_labels: Optional[List[str]] = None,
    title: str = "Generative Model Summary",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Multi-panel summary: A + B[a=0] + C + D in one figure.

    Parameters
    ----------
    model : GenerativeModel
        The generative model.
    obs_labels, state_labels : list of str, optional
        Labels for observations/states.
    title : str
        Overall figure title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if obs_labels is None:
        obs_labels = [f"o={i}" for i in range(model.num_obs)]
    if state_labels is None:
        state_labels = [f"s={i}" for i in range(model.num_states)]

    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)

    # (0,0) A-matrix
    ax_a = fig.add_subplot(gs[0, 0])
    im_a = ax_a.imshow(model.A, cmap=get_config().cmap_probability, aspect="auto", vmin=0, vmax=1)
    ax_a.set_title("A: P(o | s)", fontsize=16)
    ax_a.set_xticks(range(model.num_states))
    ax_a.set_xticklabels(state_labels, fontsize=12)
    ax_a.set_yticks(range(model.num_obs))
    ax_a.set_yticklabels(obs_labels, fontsize=12)
    ax_a.set_xlabel("States")
    ax_a.set_ylabel("Observations")
    fig.colorbar(im_a, ax=ax_a, shrink=0.7)
    for i in range(model.num_obs):
        for j in range(model.num_states):
            v = model.A[i, j]
            col = "white" if v > 0.5 else "black"
            ax_a.text(j, i, f"{v:.2f}", ha="center", va="center",
                      color=col, fontsize=12)

    # (0,1) B-matrix for action 0
    ax_b = fig.add_subplot(gs[0, 1])
    B_0 = model.B[:, :, 0] if model.B.ndim == 3 else model.B
    im_b = ax_b.imshow(B_0, cmap=get_config().cmap_probability, aspect="auto", vmin=0, vmax=1)
    ax_b.set_title("B: P(s' | s, a=0)", fontsize=16)
    ax_b.set_xticks(range(model.num_states))
    ax_b.set_xticklabels(state_labels, fontsize=12)
    ax_b.set_yticks(range(model.num_states))
    ax_b.set_yticklabels(state_labels, fontsize=12)
    ax_b.set_xlabel("Current state s")
    ax_b.set_ylabel("Next state s'")
    fig.colorbar(im_b, ax=ax_b, shrink=0.7)
    for i in range(model.num_states):
        for j in range(model.num_states):
            v = B_0[i, j]
            col = "white" if v > 0.5 else "black"
            ax_b.text(j, i, f"{v:.2f}", ha="center", va="center",
                      color=col, fontsize=12)

    # (1,0) C-vector
    ax_c = fig.add_subplot(gs[1, 0])
    x_c = np.arange(model.num_obs)
    colours_c = ["#4C72B0" if c >= 0 else "#C44E52" for c in model.C]
    ax_c.bar(x_c, model.C, color=colours_c, alpha=0.8)
    ax_c.set_title("C: ln P(o)", fontsize=16)
    ax_c.set_xlabel("Observation")
    ax_c.set_ylabel("Log-preference (nats)")
    ax_c.set_xticks(x_c)
    ax_c.set_xticklabels(obs_labels, fontsize=12)
    ax_c.axhline(0, color="grey", linewidth=0.8, linestyle="--")
    ax_c.grid(True, alpha=0.3, axis="y")

    # (1,1) D-vector
    ax_d = fig.add_subplot(gs[1, 1])
    x_d = np.arange(model.num_states)
    ax_d.bar(x_d, model.D, color="#55A868", alpha=0.8)
    ax_d.set_title("D: P(s₀)", fontsize=16)
    ax_d.set_xlabel("State")
    ax_d.set_ylabel("Probability")
    ax_d.set_xticks(x_d)
    ax_d.set_xticklabels(state_labels, fontsize=12)
    ax_d.set_ylim(0, 1.15)
    ax_d.grid(True, alpha=0.3, axis="y")

    fig.suptitle(title, fontsize=20, fontweight="bold", y=1.01)
    # Multi-panel figures with suptitle often warn on tight_layout
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        plt.tight_layout(rect=[0, 0, 1, 0.96])


    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved model summary to %s", save_path)
    return fig


# =====================================================================
# B-matrix transition graph
# =====================================================================

def plot_B_transition_graph(
    model: "GenerativeModel",
    action: int = 0,
    state_labels: Optional[List[str]] = None,
    threshold: float = 0.05,
    title: Optional[str] = None,
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Directed graph of state transitions for a given action.

    Nodes are states, edges are weighted by P(s'|s,a) above *threshold*.
    Uses circular layout with arrows whose width encodes probability.

    Parameters
    ----------
    model : GenerativeModel
        The generative model.
    action : int
        Action index.
    state_labels : list of str, optional
        Labels for state indices.
    threshold : float
        Minimum transition probability to draw an edge.
    title : str, optional
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if state_labels is None:
        state_labels = [f"s{i}" for i in range(model.num_states)]

    B_a = model.B[:, :, action] if model.B.ndim == 3 else model.B
    n = model.num_states
    t = title or f"Transition Graph (a={action})"

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.set_title(t, fontsize=18)
    ax.axis("off")

    # Circular node positions
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False) - np.pi / 2
    positions = np.column_stack([np.cos(angles), np.sin(angles)])

    # Draw nodes
    for i in range(n):
        circle = plt.Circle(positions[i], 0.15, color="#4C72B0", alpha=0.8,
                             zorder=3)
        ax.add_patch(circle)
        ax.text(positions[i][0], positions[i][1], state_labels[i],
                ha="center", va="center", fontsize=14, color="white",
                fontweight="bold", zorder=4)

    # Draw edges
    for s_from in range(n):
        for s_to in range(n):
            prob = B_a[s_to, s_from]  # B[s', s, a]
            if prob < threshold:
                continue
            if s_from == s_to:
                # Self-loop — draw a small arc above the node
                loop_x = positions[s_from][0]
                loop_y = positions[s_from][1] + 0.25
                ax.annotate("", xy=(loop_x + 0.08, positions[s_from][1] + 0.15),
                            xytext=(loop_x - 0.08, positions[s_from][1] + 0.15),
                            arrowprops=dict(arrowstyle="->", lw=1.5 + 3 * prob,
                                            color="#DD8452", connectionstyle="arc3,rad=1.5"))
                ax.text(loop_x, loop_y + 0.12, f"{prob:.2f}",
                        ha="center", fontsize=12, color="#DD8452")
            else:
                dx = positions[s_to] - positions[s_from]
                unit = dx / np.linalg.norm(dx)
                start = positions[s_from] + unit * 0.17
                end = positions[s_to] - unit * 0.17
                ax.annotate("", xy=end, xytext=start,
                            arrowprops=dict(arrowstyle="-|>",
                                            lw=1 + 3 * prob,
                                            color="#DD8452", alpha=0.8))
                mid = (start + end) / 2 + np.array([-unit[1], unit[0]]) * 0.1
                ax.text(mid[0], mid[1], f"{prob:.2f}",
                        ha="center", fontsize=12, color="#DD8452")

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved transition graph to %s", save_path)
    return fig


# =====================================================================
# Dirichlet concentration heatmap
# =====================================================================

def plot_dirichlet_concentration(
    pA: np.ndarray,
    pA_prior: Optional[np.ndarray] = None,
    row_labels: Optional[List[str]] = None,
    col_labels: Optional[List[str]] = None,
    title: str = "Dirichlet Concentrations pA",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Heatmap of Dirichlet concentration parameters.

    If *pA_prior* is given, plots side-by-side (prior vs learned).

    Parameters
    ----------
    pA : np.ndarray
        Current (learned) concentration parameters, shape (num_obs, num_states).
    pA_prior : np.ndarray, optional
        Prior concentration parameters for comparison.
    row_labels, col_labels : list of str, optional
        Row/column labels.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    pA = np.atleast_2d(pA)

    if pA_prior is not None:
        pA_prior = np.atleast_2d(pA_prior)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        vmax = max(pA.max(), pA_prior.max())
        vmin = min(pA.min(), pA_prior.min())

        im1 = ax1.imshow(pA_prior, cmap=get_config().cmap_concentration, aspect="auto",
                         vmin=vmin, vmax=vmax)
        ax1.set_title("Prior pA", fontsize=16)

        im2 = ax2.imshow(pA, cmap=get_config().cmap_concentration, aspect="auto",
                         vmin=vmin, vmax=vmax)
        ax2.set_title("Learned pA", fontsize=16)

        if row_labels is None:
            row_labels = [f"o={i}" for i in range(pA.shape[0])]
        if col_labels is None:
            col_labels = [f"s={i}" for i in range(pA.shape[1])]

        for ax in (ax1, ax2):
            ax.set_xticks(range(pA.shape[1]))
            ax.set_xticklabels(col_labels)
            ax.set_yticks(range(pA.shape[0]))
            ax.set_yticklabels(row_labels)
            # Annotate cells
            data = pA_prior if ax is ax1 else pA
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    v = data[i, j]
                    col = "white" if v > (vmax + vmin) / 2 else "black"
                    ax.text(j, i, f"{v:.1f}", ha="center", va="center",
                            color=col, fontsize=12)

        fig.colorbar(im2, ax=[ax1, ax2], shrink=0.7, label="Concentration")
        fig.suptitle(title, fontsize=18, y=1.02)
    else:
        fig = plot_matrix_heatmap(
            pA, row_labels=row_labels, col_labels=col_labels,
            title=title, cmap=get_config().cmap_concentration, fmt=".1f",
        )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        plt.tight_layout(rect=[0, 0, 1, 0.96])

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved Dirichlet concentration plot to %s", save_path)
    return fig
