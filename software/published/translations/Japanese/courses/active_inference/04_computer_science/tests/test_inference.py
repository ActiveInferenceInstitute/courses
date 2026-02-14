"""Tests for inference.py — standalone state/policy inference and MMP.

All computations are real (no mocks).
"""

import numpy as np
import pytest

from active_inference.math.inference import (
    run_state_inference, run_policy_inference, run_mmp,
)


class TestStateInference:
    """Tests for run_state_inference."""

    def test_converges(self, simple_model):
        """Should converge within default iterations."""
        result = run_state_inference(
            prior=simple_model.D.copy(),
            observation=0,
            A=simple_model.A,
        )
        assert result["converged"]
        assert result["num_iters"] <= 16

    def test_posterior_shifts(self, simple_model):
        """After observing o=0, beliefs should favour state 0."""
        result = run_state_inference(
            prior=np.array([0.5, 0.5]),
            observation=0,
            A=simple_model.A,
        )
        assert result["q_s"][0] > 0.5

    def test_delta_history_tracked(self, simple_model):
        """Delta history should have one entry per iteration."""
        result = run_state_inference(
            prior=simple_model.D.copy(),
            observation=0,
            A=simple_model.A,
        )
        assert len(result["delta_history"]) == result["num_iters"]

    def test_delta_decreases(self, simple_model):
        """Convergence deltas should generally decrease."""
        result = run_state_inference(
            prior=simple_model.D.copy(),
            observation=0,
            A=simple_model.A,
            num_iterations=20,
            convergence_threshold=1e-12,
        )
        deltas = result["delta_history"]
        # Last delta should be smaller than first
        if len(deltas) > 2:
            assert deltas[-1] <= deltas[0] + 1e-10


class TestPolicyInference:
    """Tests for run_policy_inference."""

    def test_returns_valid_distribution(self, simple_model):
        """q(π) should sum to 1."""
        result = run_policy_inference(
            q_s=simple_model.D.copy(),
            A=simple_model.A, B=simple_model.B,
            C=simple_model.C,
            policies=[[0], [1]],
            gamma=1.0,
        )
        assert np.isclose(result["q_pi"].sum(), 1.0)

    def test_G_values_finite(self, simple_model):
        """All EFE values should be finite."""
        result = run_policy_inference(
            q_s=simple_model.D.copy(),
            A=simple_model.A, B=simple_model.B,
            C=simple_model.C,
            policies=[[0], [1]],
        )
        assert np.all(np.isfinite(result["G_values"]))

    def test_selected_action_valid(self, simple_model):
        """Selected action should be a valid index."""
        result = run_policy_inference(
            q_s=simple_model.D.copy(),
            A=simple_model.A, B=simple_model.B,
            C=simple_model.C,
            policies=[[0], [1]],
        )
        assert 0 <= result["selected_action"] < simple_model.num_actions

    def test_habit_prior_influence(self, simple_model):
        """Habit prior E should bias policy selection."""
        # Strongly favour policy 0 via habit
        E = np.array([0.99, 0.01])
        result = run_policy_inference(
            q_s=simple_model.D.copy(),
            A=simple_model.A, B=simple_model.B,
            C=simple_model.C,
            policies=[[0], [1]],
            gamma=0.01,  # low precision → habits dominate
            E=E,
        )
        assert result["q_pi"][0] > result["q_pi"][1]


class TestMMP:
    """Tests for run_mmp (marginal message passing)."""

    def test_returns_beliefs_list(self, simple_model):
        """Should return one belief vector per observation."""
        result = run_mmp(
            observations=[0, 0, 1],
            A=simple_model.A,
            B=simple_model.B,
            D=simple_model.D,
            policy=[0, 0],
        )
        assert len(result["beliefs"]) == 3

    def test_beliefs_are_valid_dists(self, simple_model):
        """Each belief should be a valid probability distribution."""
        result = run_mmp(
            observations=[0, 0],
            A=simple_model.A,
            B=simple_model.B,
            D=simple_model.D,
            policy=[0],
        )
        for q in result["beliefs"]:
            assert np.isclose(q.sum(), 1.0, atol=1e-6)
            assert np.all(q >= -1e-10)

    def test_vfe_returned(self, simple_model):
        """VFE should be returned for each timestep."""
        result = run_mmp(
            observations=[0, 1, 0],
            A=simple_model.A,
            B=simple_model.B,
            D=simple_model.D,
            policy=[0, 0],
        )
        assert len(result["vfe"]) == 3
        assert all(np.isfinite(v) for v in result["vfe"])

    def test_3d_B_matrix(self, simple_model):
        """MMP should work with 3-D B matrices."""
        result = run_mmp(
            observations=[0, 1],
            A=simple_model.A,
            B=simple_model.B,
            D=simple_model.D,
            policy=[1],  # swap action
        )
        assert len(result["beliefs"]) == 2


class TestInference2D:
    """Tests for inference with 2D B-matrices (simple transitions)."""

    def test_policy_inference_2d(self):
        """Should handle 2D B-matrix in policy inference."""
        A = np.eye(2)
        B = np.eye(2)
        C = np.zeros(2)
        D = np.array([0.5, 0.5])
        
        result = run_policy_inference(
            q_s=D, A=A, B=B, C=C,
            policies=[[0]],
        )
        assert result["selected_action"] == 0

    def test_mmp_2d(self):
        """Should handle 2D B-matrix in marginal message passing."""
        A = np.eye(2)
        B = np.eye(2)
        D = np.array([0.5, 0.5])
        
        result = run_mmp(
            observations=[0, 0],
            A=A, B=B, D=D,
            policy=[0],
        )
        assert len(result["beliefs"]) == 2
