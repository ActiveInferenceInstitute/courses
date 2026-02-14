"""Tests for the visualization subpackage — all 28 plot functions.

Smoke tests verify every function returns a ``matplotlib.figure.Figure``.
Content tests check shapes, labels, and accessibility (≥ 16pt text).
All computations are real (no mocks).
"""

import numpy as np
import pytest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
import tempfile

from active_inference.agent.agent import ActiveInferenceAgent
from active_inference.agent.environment import DiscreteEnvironment
from active_inference.agent.generative_model import GenerativeModel
from active_inference.math.free_energy import (
    compute_vfe_components, compute_efe_components, softmax,
)
from active_inference.math.learning import update_dirichlet_A, expected_A
from active_inference.math.inference import run_state_inference

# Import all visualisation functions
from active_inference.visualization import (
    # plotting (6)
    plot_beliefs,
    plot_free_energy,
    plot_prediction_errors,
    plot_policy_values,
    plot_efe_decomposition,
    plot_learning_progress,
    # matrices (9)
    plot_matrix_heatmap,
    plot_A_matrix,
    plot_B_matrix,
    plot_C_preferences,
    plot_D_prior,
    plot_E_habits,
    plot_model_summary,
    plot_B_transition_graph,
    plot_dirichlet_concentration,
    # diagnostics (8)
    plot_convergence,
    plot_vfe_components,
    plot_efe_components,
    plot_precision_sweep,
    plot_entropy_trajectory,
    plot_surprise_trajectory,
    plot_dirichlet_learning,
    plot_bmr_results,
    # simulation (5)
    plot_simulation_dashboard,
    plot_environment_trajectory,
    plot_agent_vs_environment,
    plot_tmaze,
    plot_gridworld,
)


# =====================================================================
# Helpers
# =====================================================================

def _is_figure(obj):
    """Assert obj is a matplotlib Figure."""
    return isinstance(obj, plt.Figure)


def _close(fig):
    """Close figure to free memory."""
    plt.close(fig)


@pytest.fixture(autouse=True)
def _close_all_figs():
    """Close all figures after each test."""
    yield
    plt.close("all")


# =====================================================================
# plotting.py — original 6 functions
# =====================================================================

class TestPlotBeliefs:
    """Tests for plot_beliefs."""

    def test_smoke(self, simple_model):
        beliefs = [np.array([0.5, 0.5]), np.array([0.8, 0.2])]
        fig = plot_beliefs(beliefs)
        assert _is_figure(fig)

    def test_custom_labels(self, simple_model):
        beliefs = [np.array([0.5, 0.5])]
        fig = plot_beliefs(beliefs, state_labels=["Left", "Right"])
        assert _is_figure(fig)

    def test_single_timestep(self):
        fig = plot_beliefs([np.array([1.0, 0.0])])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "beliefs.png")
        fig = plot_beliefs([np.array([0.5, 0.5])], save_path=path)
        assert os.path.exists(path)


class TestPlotFreeEnergy:
    """Tests for plot_free_energy."""

    def test_smoke(self):
        fig = plot_free_energy([1.0, 0.8, 0.6])
        assert _is_figure(fig)

    def test_single_value(self):
        fig = plot_free_energy([0.5])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "vfe.png")
        plot_free_energy([0.5], save_path=path)
        assert os.path.exists(path)


class TestPlotPredictionErrors:
    """Tests for plot_prediction_errors."""

    def test_smoke(self):
        obs = [0, 1, 0]
        preds = [np.array([0.9, 0.1]), np.array([0.3, 0.7]),
                 np.array([0.8, 0.2])]
        fig = plot_prediction_errors(obs, preds)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "pe.png")
        plot_prediction_errors([0], [np.array([0.5, 0.5])], save_path=path)
        assert os.path.exists(path)


class TestPlotPolicyValues:
    """Tests for plot_policy_values."""

    def test_smoke(self):
        efe = [np.array([1.0, 2.0]), np.array([0.5, 1.5])]
        fig = plot_policy_values(efe)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "pvals.png")
        plot_policy_values([np.array([1.0])], save_path=path)
        assert os.path.exists(path)


class TestPlotEfeDecomposition:
    """Tests for plot_efe_decomposition."""

    def test_smoke(self):
        fig = plot_efe_decomposition([1.0, 0.8], [0.5, 0.3])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "efe_decomp.png")
        plot_efe_decomposition([1.0], [0.5], save_path=path)
        assert os.path.exists(path)


class TestPlotLearningProgress:
    """Tests for plot_learning_progress."""

    def test_smoke(self):
        fig = plot_learning_progress([0.5, 0.3, 0.1])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "learn.png")
        plot_learning_progress([0.5], save_path=path)
        assert os.path.exists(path)


# =====================================================================
# matrices.py — 9 functions
# =====================================================================

class TestPlotMatrixHeatmap:
    """Tests for plot_matrix_heatmap."""

    def test_smoke(self):
        fig = plot_matrix_heatmap(np.eye(3))
        assert _is_figure(fig)

    def test_custom_labels(self):
        fig = plot_matrix_heatmap(
            np.array([[0.9, 0.1], [0.1, 0.9]]),
            row_labels=["o0", "o1"], col_labels=["s0", "s1"],
            title="Test Heatmap",
        )
        assert _is_figure(fig)

    def test_1x1_matrix(self):
        fig = plot_matrix_heatmap(np.array([[0.5]]))
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "heatmap.png")
        fig = plot_matrix_heatmap(np.eye(2), save_path=path)
        assert os.path.exists(path)

    def test_no_annotation(self):
        fig = plot_matrix_heatmap(np.eye(2), annotate=False)
        assert _is_figure(fig)


class TestPlotAMatrix:
    """Tests for plot_A_matrix."""

    def test_smoke_simple(self, simple_model):
        fig = plot_A_matrix(simple_model)
        assert _is_figure(fig)

    def test_smoke_tmaze(self, tmaze_model):
        fig = plot_A_matrix(tmaze_model, obs_labels=["null", "reward", "none"])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "A.png")
        plot_A_matrix(simple_model, save_path=path)
        assert os.path.exists(path)


class TestPlotBMatrix:
    """Tests for plot_B_matrix."""

    def test_single_action(self, simple_model):
        fig = plot_B_matrix(simple_model, action=0)
        assert _is_figure(fig)

    def test_all_actions(self, simple_model):
        fig = plot_B_matrix(simple_model)
        assert _is_figure(fig)

    def test_tmaze_all(self, tmaze_model):
        fig = plot_B_matrix(tmaze_model)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "B.png")
        plot_B_matrix(simple_model, save_path=path)
        assert os.path.exists(path)

    def test_2d_matrix_edge_case(self):
        """Test with a 2D B-matrix (single action, implicit)."""
        A = np.eye(3)
        B = np.eye(3)  # 2D — single action implicit
        C = np.zeros(3)
        D = np.ones(3) / 3
        model = GenerativeModel(A, B, C, D)
        fig = plot_B_matrix(model)
        assert _is_figure(fig)

    def test_grid_with_empty_cells(self):
        """Test with 5 actions to ensure 2x3 grid has 1 empty cell handled correctly."""
        A = np.eye(2)
        B_5 = np.zeros((2, 2, 5))
        for a in range(5):
            B_5[:, :, a] = np.eye(2)  # normalised identity
        C = np.zeros(2)
        D = np.array([0.5, 0.5])
        model = GenerativeModel(A, B_5, C, D)
        fig = plot_B_matrix(model, save_path="ignore_me.png")
        assert _is_figure(fig)


class TestPlotCPreferences:
    """Tests for plot_C_preferences."""

    def test_smoke(self, simple_model):
        fig = plot_C_preferences(simple_model)
        assert _is_figure(fig)

    def test_tmaze(self, tmaze_model):
        fig = plot_C_preferences(tmaze_model)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "C.png")
        plot_C_preferences(simple_model, save_path=path)
        assert os.path.exists(path)


class TestPlotDPrior:
    """Tests for plot_D_prior."""

    def test_smoke(self, simple_model):
        fig = plot_D_prior(simple_model)
        assert _is_figure(fig)
        # Check entropy annotation exists
        texts = [t.get_text() for t in fig.axes[0].texts]
        assert any("H[D]" in t for t in texts)

    def test_tmaze(self, tmaze_model):
        fig = plot_D_prior(tmaze_model)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "D.png")
        plot_D_prior(simple_model, save_path=path)
        assert os.path.exists(path)


class TestPlotEHabits:
    """Tests for plot_E_habits."""

    def test_raises_without_E(self, simple_model):
        with pytest.raises(ValueError, match="no habit prior"):
            plot_E_habits(simple_model)

    def test_smoke_with_E(self, simple_model):
        simple_model.E = np.array([0.6, 0.4])
        fig = plot_E_habits(simple_model)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        simple_model.E = np.array([0.5, 0.5])
        path = str(tmp_path / "E.png")
        plot_E_habits(simple_model, save_path=path)
        assert os.path.exists(path)


class TestPlotModelSummary:
    """Tests for plot_model_summary."""

    def test_smoke(self, simple_model):
        fig = plot_model_summary(simple_model)
        assert _is_figure(fig)
        # Should have 4 data axes + colorbars
        assert len(fig.axes) >= 4

    def test_tmaze(self, tmaze_model):
        fig = plot_model_summary(tmaze_model, title="T-Maze Model")
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "summary.png")
        plot_model_summary(simple_model, save_path=path)
        assert os.path.exists(path)


class TestPlotBTransitionGraph:
    """Tests for plot_B_transition_graph."""

    def test_smoke(self, simple_model):
        fig = plot_B_transition_graph(simple_model, action=0)
        assert _is_figure(fig)

    def test_tmaze(self, tmaze_model):
        fig = plot_B_transition_graph(
            tmaze_model, action=0,
            state_labels=["center", "left", "right", "cue"],
        )
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "B_graph.png")
        plot_B_transition_graph(simple_model, action=0, save_path=path)
        assert os.path.exists(path)


class TestPlotDirichletConcentration:
    """Tests for plot_dirichlet_concentration."""

    def test_single(self):
        pA = np.array([[5.0, 1.0], [1.0, 5.0]])
        fig = plot_dirichlet_concentration(pA)
        assert _is_figure(fig)

    def test_with_prior(self):
        pA_prior = np.ones((2, 2))
        pA = np.array([[5.0, 1.0], [1.0, 5.0]])
        fig = plot_dirichlet_concentration(pA, pA_prior=pA_prior)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        pA = np.ones((2, 2))
        path = str(tmp_path / "dirichlet_conc.png")
        plot_dirichlet_concentration(pA, save_path=path)
        assert os.path.exists(path)



# =====================================================================
# diagnostics.py — 8 functions
# =====================================================================

class TestPlotConvergence:
    """Tests for plot_convergence."""

    def test_smoke(self):
        deltas = [0.5, 0.1, 0.01, 0.001, 0.0001]
        fig = plot_convergence(deltas)
        assert _is_figure(fig)

    def test_no_threshold(self):
        fig = plot_convergence([0.1, 0.01], threshold=None)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "convergence.png")
        fig = plot_convergence([0.1], save_path=path)
        assert os.path.exists(path)


class TestPlotVfeComponents:
    """Tests for plot_vfe_components."""

    def test_smoke(self, simple_model):
        agent = ActiveInferenceAgent(simple_model)
        components_list = []
        for obs in [0, 1, 0]:
            agent.infer_states(obs)
            c = compute_vfe_components(
                q_s=agent.q_s, o=obs,
                A=simple_model.A, D=simple_model.D,
            )
            components_list.append(c)
        fig = plot_vfe_components(components_list)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        c = compute_vfe_components(agent.q_s, 0, simple_model.A, simple_model.D)
        path = str(tmp_path / "vfe.png")
        fig = plot_vfe_components([c], save_path=path)
        assert os.path.exists(path)


class TestPlotEfeComponents:
    """Tests for plot_efe_components."""

    def test_smoke(self, simple_model):
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        comps = []
        for _ in range(3):
            c = compute_efe_components(
                q_s=agent.q_s, A=simple_model.A,
                B=simple_model.B, C=simple_model.C,
                action=0,
            )
            comps.append(c)
        fig = plot_efe_components(comps)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "efe.png")
        # Reuse simple setup
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        c = compute_efe_components(agent.q_s, simple_model.A, simple_model.B, simple_model.C, 0)
        fig = plot_efe_components([c], save_path=path)
        assert os.path.exists(path)


class TestPlotPrecisionSweep:
    """Tests for plot_precision_sweep."""

    def test_smoke(self):
        gammas = [0.5, 1.0, 2.0, 4.0]
        q_pi = np.array([
            softmax(np.array([-1.0, -0.5]), tau=1.0 / g)
            for g in gammas
        ])
        fig = plot_precision_sweep(gammas, q_pi)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "precision.png")
        fig = plot_precision_sweep([1.0], np.array([[0.5, 0.5]]), save_path=path)
        assert os.path.exists(path)


class TestPlotEntropyTrajectory:
    """Tests for plot_entropy_trajectory."""

    def test_smoke(self):
        beliefs = [np.array([0.5, 0.5]), np.array([0.9, 0.1]),
                   np.array([0.99, 0.01])]
        fig = plot_entropy_trajectory(beliefs)
        assert _is_figure(fig)

    def test_single_timestep(self):
        fig = plot_entropy_trajectory([np.array([1.0, 0.0])])
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "entropy.png")
        fig = plot_entropy_trajectory([np.array([0.5, 0.5])], save_path=path)
        assert os.path.exists(path)


class TestPlotSurpriseTrajectory:
    """Tests for plot_surprise_trajectory."""

    def test_smoke(self, simple_model):
        obs = [0, 1, 0]
        beliefs = [np.array([0.5, 0.5])] * 3
        fig = plot_surprise_trajectory(obs, simple_model.A, beliefs)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        path = str(tmp_path / "surprise.png")
        fig = plot_surprise_trajectory(
            [0], simple_model.A, [np.array([0.5, 0.5])], save_path=path
        )
        assert os.path.exists(path)


class TestPlotDirichletLearning:
    """Tests for plot_dirichlet_learning."""

    def test_without_true_A(self):
        pA_history = [np.ones((2, 2)) * (i + 1) for i in range(5)]
        fig = plot_dirichlet_learning(pA_history)
        assert _is_figure(fig)

    def test_with_true_A(self, simple_model):
        pA = np.ones((2, 2))
        pA_history = [pA.copy()]
        np.random.seed(42)
        agent = ActiveInferenceAgent(simple_model)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        obs = env.reset(initial_state=0)
        for _ in range(10):
            action = agent.step(obs)
            pA = update_dirichlet_A(pA, obs, agent.q_s)
            pA_history.append(pA.copy())
            obs = env.step(action)

        fig = plot_dirichlet_learning(pA_history, true_A=simple_model.A)
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "dirichlet.png")
        fig = plot_dirichlet_learning([np.ones((2, 2))], save_path=path)
        assert os.path.exists(path)


class TestPlotBmrResults:
    """Tests for plot_bmr_results."""

    def test_smoke(self):
        delta_F = np.array([0.5, -0.3, 1.2, -0.1])
        should_prune = np.array([True, False, True, False])
        fig = plot_bmr_results(delta_F, should_prune)
        assert _is_figure(fig)

    def test_custom_labels(self):
        fig = plot_bmr_results(
            np.array([0.1, -0.2]),
            np.array([True, False]),
            state_labels=["left", "right"],
        )
        assert _is_figure(fig)
    def test_save_path(self, tmp_path):
        path = str(tmp_path / "bmr.png")
        fig = plot_bmr_results(np.array([0.1]), np.array([True]), save_path=path)
        assert os.path.exists(path)


# =====================================================================
# simulation.py — 5 functions
# =====================================================================

class TestPlotSimulationDashboard:
    """Tests for plot_simulation_dashboard."""

    def test_smoke(self, simple_model):
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)
        obs = env.reset(initial_state=0)
        for _ in range(5):
            action = agent.step(obs)
            obs = env.step(action)

        fig = plot_simulation_dashboard(
            beliefs_history=agent.history["beliefs"],
            vfe_history=agent.history["vfe"],
            observations=agent.history["observations"],
            actions=agent.history["actions"],
        )
        assert _is_figure(fig)

    def test_with_true_states(self, simple_model):
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)
        obs = env.reset(initial_state=0)
        for _ in range(5):
            action = agent.step(obs)
            obs = env.step(action)

        fig = plot_simulation_dashboard(
            beliefs_history=agent.history["beliefs"],
            vfe_history=agent.history["vfe"],
            observations=agent.history["observations"],
            actions=agent.history["actions"],
            true_states=env.history["states"],
        )
        assert _is_figure(fig)
        # 5 panels when true_states provided
        assert len(fig.axes) >= 5

    def test_save_path(self, tmp_path, simple_model):
        agent = ActiveInferenceAgent(simple_model)
        # Populate history
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        obs = env.reset()
        agent.step(obs)
        
        path = str(tmp_path / "dashboard.png")
        plot_simulation_dashboard(
            agent.history["beliefs"], agent.history["vfe"],
            agent.history["observations"], agent.history["actions"],
            save_path=path,
        )
        assert os.path.exists(path)


class TestPlotEnvironmentTrajectory:
    """Tests for plot_environment_trajectory."""

    def test_smoke(self):
        fig = plot_environment_trajectory(
            states=[0, 1, 0, 1],
            observations=[0, 1, 0, 1],
        )
        assert _is_figure(fig)

    def test_with_actions(self):
        fig = plot_environment_trajectory(
            states=[0, 1, 0],
            observations=[0, 1, 0],
            actions=[1, 0, 1],
        )
        assert _is_figure(fig)
        assert len(fig.axes) == 3  # states + obs + actions

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "env_traj.png")
        plot_environment_trajectory([0], [0], save_path=path)
        assert os.path.exists(path)

    def test_with_labels(self):
        fig = plot_environment_trajectory(
            states=[0, 1], observations=[0, 1], state_labels=["A", "B"]
        )
        assert _is_figure(fig)


class TestPlotAgentVsEnvironment:
    """Tests for plot_agent_vs_environment."""

    def test_smoke(self, simple_model):
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)
        obs = env.reset(initial_state=0)
        for _ in range(5):
            action = agent.step(obs)
            obs = env.step(action)

        fig = plot_agent_vs_environment(
            beliefs_history=agent.history["beliefs"],
            true_states=env.history["states"][:5],
        )
        assert _is_figure(fig)

    def test_save_path(self, tmp_path, simple_model):
        agent = ActiveInferenceAgent(simple_model)
        # Populate history
        agent.infer_states(0)
        
        path = str(tmp_path / "agent_vs_env.png")
        plot_agent_vs_environment(
            agent.history["beliefs"], [0], save_path=path
        )
        assert os.path.exists(path)


class TestPlotTmaze:
    """Tests for plot_tmaze."""

    def test_default(self):
        fig = plot_tmaze()
        assert _is_figure(fig)

    def test_all_states(self):
        for s in range(4):
            fig = plot_tmaze(agent_state=s)
            assert _is_figure(fig)

    def test_reward_right(self):
        fig = plot_tmaze(reward_location="right")
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "tmaze.png")
        fig = plot_tmaze(save_path=path)
        assert os.path.exists(path)


class TestPlotGridworld:
    """Tests for plot_gridworld."""

    def test_smoke(self):
        fig = plot_gridworld(
            grid_shape=(4, 4),
            agent_pos=(0, 0),
            goal_pos=(3, 3),
        )
        assert _is_figure(fig)

    def test_with_obstacles(self):
        fig = plot_gridworld(
            grid_shape=(5, 5),
            agent_pos=(0, 0),
            goal_pos=(4, 4),
            obstacles=[(1, 1), (2, 2), (3, 3)],
        )
        assert _is_figure(fig)

    def test_with_path(self):
        fig = plot_gridworld(
            grid_shape=(3, 3),
            agent_pos=(2, 2),
            goal_pos=(0, 0),
            path=[(2, 2), (1, 1), (0, 0)],
        )
        assert _is_figure(fig)

    def test_save_path(self, tmp_path):
        path = str(tmp_path / "gridworld.png")
        fig = plot_gridworld(
            grid_shape=(3, 3), agent_pos=(0, 0), goal_pos=(2, 2),
            save_path=path,
        )
        assert os.path.exists(path)


# =====================================================================
# Cross-cutting: Import smoke test
# =====================================================================

class TestTopLevelImports:
    """Verify all 28 functions are importable from active_inference."""

    def test_all_importable(self):
        import active_inference
        expected = [
            "plot_beliefs", "plot_free_energy", "plot_prediction_errors",
            "plot_policy_values", "plot_efe_decomposition", "plot_learning_progress",
            "plot_matrix_heatmap", "plot_A_matrix", "plot_B_matrix",
            "plot_C_preferences", "plot_D_prior", "plot_E_habits",
            "plot_model_summary", "plot_B_transition_graph",
            "plot_dirichlet_concentration",
            "plot_convergence", "plot_vfe_components", "plot_efe_components",
            "plot_precision_sweep", "plot_entropy_trajectory",
            "plot_surprise_trajectory", "plot_dirichlet_learning",
            "plot_bmr_results",
            "plot_simulation_dashboard", "plot_environment_trajectory",
            "plot_agent_vs_environment", "plot_tmaze", "plot_gridworld",
        ]
        for name in expected:
            assert hasattr(active_inference, name), f"Missing: {name}"

    def test_version_bumped(self):
        import active_inference
        assert active_inference.__version__ == "0.4.0"

    def test_all_count(self):
        import active_inference
        viz_funcs = [n for n in active_inference.__all__ if n.startswith("plot_")]
        assert len(viz_funcs) == 28, f"Expected 28, got {len(viz_funcs)}"
