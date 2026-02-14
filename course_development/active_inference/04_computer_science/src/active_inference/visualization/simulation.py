"""Simulation — end-to-end simulation dashboards and environment visualizers.

Provides multi-panel simulation dashboards, environment trajectory plots,
agent-vs-environment comparisons, and T-maze / gridworld layout renderers.

Accessibility: All text ≥ 16pt.

Cross-course connections (see resources/cross_course_map.md):
    CS M1  — Environment setup, generative process
    CS M5  — T-maze implementation
    CS M8  — Gridworld, deep temporal planning
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import logging
from typing import Optional, List, Dict, Tuple

from .config import get_config

logger = logging.getLogger(__name__)

matplotlib.use("Agg")

# Apply centralized style
get_config().apply()



# =====================================================================
# Simulation dashboard
# =====================================================================

def plot_simulation_dashboard(
    beliefs_history: List[np.ndarray],
    vfe_history: List[float],
    observations: List[int],
    actions: List[int],
    true_states: Optional[List[int]] = None,
    state_labels: Optional[List[str]] = None,
    title: str = "Active Inference Simulation Dashboard",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Multi-panel dashboard: beliefs, VFE, actions, observations, and true states.

    Parameters
    ----------
    beliefs_history : list of np.ndarray
        Agent belief vectors per timestep.
    vfe_history : list of float
        VFE values per timestep.
    observations : list of int
        Observation indices per timestep.
    actions : list of int
        Action indices per timestep.
    true_states : list of int, optional
        Ground-truth hidden states (from environment).
    state_labels : list of str, optional
        Labels for states.
    title : str
        Overall figure title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = len(observations)
    ts = range(T)
    beliefs_array = np.array(beliefs_history[:T])
    num_states = beliefs_array.shape[1] if len(beliefs_array) > 0 else 0

    if state_labels is None:
        state_labels = [f"s={i}" for i in range(num_states)]

    n_panels = 4 if true_states is None else 5
    fig, axes = plt.subplots(n_panels, 1, figsize=(14, 3 * n_panels),
                             sharex=True)

    # Panel 1: Beliefs
    for s in range(num_states):
        axes[0].plot(ts, beliefs_array[:T, s], linewidth=2,
                     label=state_labels[s])
    axes[0].set_ylabel("q(s)")
    axes[0].set_title("Beliefs q(s)")
    axes[0].legend(loc="upper right", ncol=min(num_states, 4))
    axes[0].set_ylim(-0.05, 1.05)
    axes[0].grid(True, alpha=0.3)

    # Panel 2: VFE
    vfe_plot = vfe_history[:T]
    axes[1].plot(range(len(vfe_plot)), vfe_plot, "b-o", linewidth=2,
                 markersize=4)
    axes[1].set_ylabel("F (nats)")
    axes[1].set_title("Variational Free Energy")
    axes[1].grid(True, alpha=0.3)

    # Panel 3: Observations
    axes[2].step(ts, observations[:T], "r-", linewidth=2, where="mid")
    axes[2].set_ylabel("Observation o")
    axes[2].set_title("Observations")
    axes[2].grid(True, alpha=0.3)
    axes[2].set_yticks(sorted(set(observations[:T])))

    # Panel 4: Actions
    act_plot = actions[:T]
    axes[3].step(range(len(act_plot)), act_plot, "g-", linewidth=2,
                 where="mid")
    axes[3].set_ylabel("Action a")
    axes[3].set_title("Actions")
    axes[3].grid(True, alpha=0.3)
    axes[3].set_yticks(sorted(set(act_plot)))

    # Panel 5: True states (optional)
    if true_states is not None:
        axes[4].step(ts, true_states[:T], "k-", linewidth=2, where="mid")
        axes[4].set_ylabel("True state η")
        axes[4].set_title("Environment Hidden States")
        axes[4].grid(True, alpha=0.3)
        axes[4].set_yticks(sorted(set(true_states[:T])))

    axes[-1].set_xlabel("Timestep t")
    fig.suptitle(title, fontsize=20, fontweight="bold", y=1.01)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved simulation dashboard to %s", save_path)
    return fig


# =====================================================================
# Environment trajectory
# =====================================================================

def plot_environment_trajectory(
    states: List[int],
    observations: List[int],
    actions: Optional[List[int]] = None,
    state_labels: Optional[List[str]] = None,
    title: str = "Environment Trajectory",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Plot state and observation trajectory from environment history.

    Parameters
    ----------
    states : list of int
        True state indices (includes initial state).
    observations : list of int
        Observation indices.
    actions : list of int, optional
        Action indices.
    state_labels : list of str, optional
        Labels for states.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    n_panels = 2 if actions is None else 3
    fig, axes = plt.subplots(n_panels, 1, figsize=(12, 3 * n_panels),
                             sharex=True)

    # States
    axes[0].step(range(len(states)), states, "k-", linewidth=2, where="mid")
    axes[0].set_ylabel("State η")
    axes[0].set_title("True Hidden States")
    axes[0].grid(True, alpha=0.3)
    if state_labels:
        unique_states = sorted(set(states))
        axes[0].set_yticks(unique_states)
        axes[0].set_yticklabels([state_labels[s] for s in unique_states])

    # Observations
    axes[1].step(range(len(observations)), observations, "r-", linewidth=2,
                 where="mid")
    axes[1].set_ylabel("Observation o")
    axes[1].set_title("Observations")
    axes[1].grid(True, alpha=0.3)

    # Actions (optional)
    if actions is not None:
        axes[2].step(range(len(actions)), actions, "g-", linewidth=2,
                     where="mid")
        axes[2].set_ylabel("Action a")
        axes[2].set_title("Actions")
        axes[2].grid(True, alpha=0.3)

    axes[-1].set_xlabel("Timestep t")
    fig.suptitle(title, fontsize=18, y=1.02)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved environment trajectory to %s", save_path)
    return fig


# =====================================================================
# Agent vs Environment comparison
# =====================================================================

def plot_agent_vs_environment(
    beliefs_history: List[np.ndarray],
    true_states: List[int],
    state_labels: Optional[List[str]] = None,
    title: str = "Agent Beliefs vs True States",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Side-by-side comparison of agent beliefs and true environment states.

    Parameters
    ----------
    beliefs_history : list of np.ndarray
        Agent belief vectors per timestep.
    true_states : list of int
        Ground-truth hidden states from environment.
    state_labels : list of str, optional
        Labels for states.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    T = min(len(beliefs_history), len(true_states))
    beliefs_array = np.array(beliefs_history[:T])
    num_states = beliefs_array.shape[1]

    if state_labels is None:
        state_labels = [f"s={i}" for i in range(num_states)]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Top: Agent beliefs as stacked area
    ax1.stackplot(range(T), *[beliefs_array[:, s] for s in range(num_states)],
                  labels=state_labels, alpha=0.7)
    ax1.set_ylabel("q(s)")
    ax1.set_title("Agent Beliefs q(s)")
    ax1.set_ylim(0, 1)
    ax1.legend(loc="upper right", ncol=min(num_states, 4))
    ax1.grid(True, alpha=0.3)

    # Bottom: True states
    true_onehot = np.zeros((T, num_states))
    for t, s in enumerate(true_states[:T]):
        true_onehot[t, s] = 1.0

    ax2.stackplot(range(T), *[true_onehot[:, s] for s in range(num_states)],
                  labels=state_labels, alpha=0.7)
    ax2.set_ylabel("True state (one-hot)")
    ax2.set_title("Environment True States")
    ax2.set_ylim(0, 1)
    ax2.set_xlabel("Timestep t")
    ax2.grid(True, alpha=0.3)

    fig.suptitle(title, fontsize=18, y=1.02)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved agent vs environment plot to %s", save_path)
    return fig


# =====================================================================
# T-maze layout
# =====================================================================

def plot_tmaze(
    agent_state: int = 0,
    reward_location: str = "left",
    state_labels: Optional[List[str]] = None,
    title: str = "T-Maze Environment",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Render T-maze layout with agent position highlighted.

    Default state mapping:
        0 = center, 1 = left arm, 2 = right arm, 3 = cue location

    Parameters
    ----------
    agent_state : int
        Current state index (0–3).
    reward_location : str
        "left" or "right" — where reward is.
    state_labels : list of str, optional
        Custom state labels.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    if state_labels is None:
        state_labels = ["Center", "Left Arm", "Right Arm", "Cue"]

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=18, pad=20)

    # Maze structure (rectangles)
    # Center corridor
    center = mpatches.FancyBboxPatch((-0.6, -1), 1.2, 2.5,
                                      boxstyle="round,pad=0.1",
                                      facecolor="#E8E8E8", edgecolor="black",
                                      linewidth=2)
    # Left arm
    left = mpatches.FancyBboxPatch((-2.8, 1.2), 2.5, 1.2,
                                    boxstyle="round,pad=0.1",
                                    facecolor="#E8E8E8", edgecolor="black",
                                    linewidth=2)
    # Right arm
    right = mpatches.FancyBboxPatch((0.3, 1.2), 2.5, 1.2,
                                     boxstyle="round,pad=0.1",
                                     facecolor="#E8E8E8", edgecolor="black",
                                     linewidth=2)
    # Cue location
    cue = mpatches.FancyBboxPatch((-0.6, -1.8), 1.2, 1,
                                   boxstyle="round,pad=0.1",
                                   facecolor="#FFF3CD", edgecolor="black",
                                   linewidth=2)
    for patch in [center, left, right, cue]:
        ax.add_patch(patch)

    # Positions for agent marker
    positions = {
        0: (0, 0.5),        # center
        1: (-1.55, 1.8),    # left arm
        2: (1.55, 1.8),     # right arm
        3: (0, -1.3),       # cue
    }

    # Reward marker
    reward_pos = positions[1] if reward_location == "left" else positions[2]
    ax.plot(*reward_pos, marker="*", color="gold", markersize=30, zorder=5)
    ax.text(reward_pos[0], reward_pos[1] + 0.5, "Reward",
            ha="center", fontsize=14, color="gold", fontweight="bold")

    # No-reward marker
    no_reward_pos = positions[2] if reward_location == "left" else positions[1]
    ax.plot(*no_reward_pos, marker="x", color="red", markersize=20,
            markeredgewidth=3, zorder=5)

    # Agent marker
    agent_pos = positions.get(agent_state, positions[0])
    agent_circle = plt.Circle(agent_pos, 0.3, color="#4C72B0", alpha=0.9,
                               zorder=6)
    ax.add_patch(agent_circle)
    ax.text(agent_pos[0], agent_pos[1], "A", ha="center", va="center",
            fontsize=16, color="white", fontweight="bold", zorder=7)

    # State labels
    label_positions = {
        0: (0, -0.3),
        1: (-1.55, 1.0),
        2: (1.55, 1.0),
        3: (0, -1.9),
    }
    for idx, label in enumerate(state_labels):
        lp = label_positions.get(idx)
        if lp:
            ax.text(lp[0], lp[1], label, ha="center", fontsize=14,
                    style="italic", color="#666666")

    # Cue indicator
    cue_text = f"Cue → {'Left' if reward_location == 'left' else 'Right'}"
    ax.text(0, -1.5, cue_text, ha="center", fontsize=14,
            fontweight="bold", color="#856404")

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved T-maze plot to %s", save_path)
    return fig


# =====================================================================
# Gridworld
# =====================================================================

def plot_gridworld(
    grid_shape: Tuple[int, int],
    agent_pos: Tuple[int, int],
    goal_pos: Tuple[int, int],
    obstacles: Optional[List[Tuple[int, int]]] = None,
    path: Optional[List[Tuple[int, int]]] = None,
    title: str = "Gridworld Environment",
    save_path: Optional[str] = None,
) -> plt.Figure:
    """Render gridworld with agent, goal, obstacles, and path overlay.

    Parameters
    ----------
    grid_shape : tuple of int
        (rows, cols) grid dimensions.
    agent_pos : tuple of int
        (row, col) agent position.
    goal_pos : tuple of int
        (row, col) goal position.
    obstacles : list of tuple, optional
        List of (row, col) obstacle positions.
    path : list of tuple, optional
        List of (row, col) positions showing agent's path.
    title : str
        Plot title.
    save_path : str, optional
        Path to save figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    rows, cols = grid_shape
    if obstacles is None:
        obstacles = []

    fig, ax = plt.subplots(figsize=(max(6, cols * 1.2), max(6, rows * 1.2)))

    # Draw grid
    grid = np.ones((rows, cols, 3))  # white background

    # Obstacles → dark grey
    for r, c in obstacles:
        grid[r, c] = [0.3, 0.3, 0.3]

    ax.imshow(grid, origin="upper", extent=(-0.5, cols - 0.5, rows - 0.5, -0.5))

    # Grid lines
    for i in range(rows + 1):
        ax.axhline(i - 0.5, color="grey", linewidth=0.5)
    for j in range(cols + 1):
        ax.axvline(j - 0.5, color="grey", linewidth=0.5)

    # Path overlay
    if path:
        for idx, (r, c) in enumerate(path):
            alpha = 0.3 + 0.5 * (idx / max(len(path) - 1, 1))
            ax.add_patch(plt.Rectangle((c - 0.4, r - 0.4), 0.8, 0.8,
                                        color="#4C72B0", alpha=alpha * 0.4))
        # Draw path line
        path_y = [p[0] for p in path]
        path_x = [p[1] for p in path]
        ax.plot(path_x, path_y, "b-", linewidth=2, alpha=0.5, zorder=3)

    # Goal
    ax.plot(goal_pos[1], goal_pos[0], marker="*", color="gold",
            markersize=35, zorder=5)
    ax.text(goal_pos[1], goal_pos[0] + 0.35, "Goal",
            ha="center", fontsize=12, color="gold", fontweight="bold")

    # Agent
    agent_circle = plt.Circle((agent_pos[1], agent_pos[0]), 0.3,
                               color="#4C72B0", alpha=0.9, zorder=6)
    ax.add_patch(agent_circle)
    ax.text(agent_pos[1], agent_pos[0], "A", ha="center", va="center",
            fontsize=16, color="white", fontweight="bold", zorder=7)

    # Obstacle legend
    if obstacles:
        legend_elements = [
            mpatches.Patch(facecolor="#4D4D4D", label="Obstacle"),
            mpatches.Patch(facecolor="#4C72B0", alpha=0.9, label="Agent"),
        ]
        ax.legend(handles=legend_elements, loc="upper right")

    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    ax.set_title(title, fontsize=18)

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        logger.info("Saved gridworld plot to %s", save_path)
    return fig
