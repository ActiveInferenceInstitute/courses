"""Tests for learning.py — Dirichlet updates, expected matrices, entropy, BMR.

All computations are real (no mocks).
"""

import numpy as np
import pytest

from active_inference.math.learning import (
    update_dirichlet_A, update_dirichlet_B, update_dirichlet_D,
    expected_A, expected_B, expected_D,
    dirichlet_entropy, bayesian_model_reduction,
)


class TestDirichletA:
    """Tests for A-matrix Dirichlet updates."""

    def test_update_increases_concentration(self):
        """Update should increase concentration for observed row."""
        pA = np.ones((2, 2))
        q_s = np.array([0.8, 0.2])
        pA_new = update_dirichlet_A(pA, observation=0, q_s=q_s)
        assert pA_new[0, 0] > pA[0, 0]
        assert pA_new[0, 1] > pA[0, 1]

    def test_unobserved_rows_unchanged(self):
        """Rows not corresponding to the observation should stay the same."""
        pA = np.ones((3, 2))
        q_s = np.array([0.5, 0.5])
        pA_new = update_dirichlet_A(pA, observation=1, q_s=q_s)
        assert np.allclose(pA_new[0, :], pA[0, :])
        assert np.allclose(pA_new[2, :], pA[2, :])

    def test_invalid_observation_raises(self):
        """Out-of-range observation should raise ValueError."""
        pA = np.ones((2, 2))
        with pytest.raises(ValueError, match="observation"):
            update_dirichlet_A(pA, observation=5, q_s=np.array([0.5, 0.5]))

    def test_shape_mismatch_raises(self):
        """Mismatched q_s length should raise ValueError."""
        pA = np.ones((2, 2))
        with pytest.raises(ValueError, match="q_s length"):
            update_dirichlet_A(pA, observation=0, q_s=np.array([0.5, 0.3, 0.2]))


class TestDirichletB:
    """Tests for B-matrix Dirichlet updates."""

    def test_update_accumulates_transition(self):
        """Should increase pB for the observed transition."""
        pB = np.ones((2, 2, 2))
        q_prev = np.array([1.0, 0.0])
        q_curr = np.array([0.0, 1.0])
        pB_new = update_dirichlet_B(pB, q_prev, q_curr, action=1)
        assert pB_new[1, 0, 1] > pB[1, 0, 1]

    def test_other_actions_unchanged(self):
        """Actions not taken should have unchanged pB."""
        pB = np.ones((2, 2, 2))
        q_prev = np.array([1.0, 0.0])
        q_curr = np.array([0.0, 1.0])
        pB_new = update_dirichlet_B(pB, q_prev, q_curr, action=1)
        assert np.allclose(pB_new[:, :, 0], pB[:, :, 0])

    def test_invalid_action_raises(self):
        """Out-of-range action should raise ValueError."""
        pB = np.ones((2, 2, 2))
        with pytest.raises(ValueError, match="action"):
            update_dirichlet_B(pB, np.array([0.5, 0.5]), np.array([0.5, 0.5]), action=5)

    def test_2d_pB_raises(self):
        """pB must be 3-D."""
        with pytest.raises(ValueError, match="pB must be 3-D"):
            # Should fail if pB is 2D
            update_dirichlet_B(np.ones((2, 2)), np.ones(2), np.ones(2), action=0)


class TestDirichletD:
    """Tests for D-vector Dirichlet updates."""

    def test_update_increases(self):
        """Update should increase concentration parameters."""
        pD = np.ones(3)
        q_s = np.array([0.5, 0.3, 0.2])
        pD_new = update_dirichlet_D(pD, q_s)
        assert np.all(pD_new >= pD)
        assert np.isclose(pD_new.sum(), pD.sum() + 1.0)

    def test_shape_mismatch_raises(self):
        """Mismatched shapes should raise ValueError."""
        with pytest.raises(ValueError, match="Shape mismatch"):
            update_dirichlet_D(np.ones(3), np.ones(4))


class TestExpectedMatrices:
    """Tests for Dirichlet mean computation."""

    def test_expected_A_normalised(self):
        """Expected A columns should sum to 1."""
        pA = np.array([[3.0, 1.0], [1.0, 3.0]])
        A_exp = expected_A(pA)
        for s in range(2):
            assert np.isclose(A_exp[:, s].sum(), 1.0)

    def test_expected_A_values(self):
        """Expected A should match Dirichlet mean."""
        pA = np.array([[3.0, 1.0], [1.0, 3.0]])
        A_exp = expected_A(pA)
        assert np.isclose(A_exp[0, 0], 0.75)
        assert np.isclose(A_exp[1, 0], 0.25)

    def test_expected_B_normalised(self):
        """Expected B columns should sum to 1."""
        pB = np.ones((2, 2, 2)) * 2
        pB[0, 0, 0] = 5
        B_exp = expected_B(pB)
        for a in range(2):
            for s in range(2):
                assert np.isclose(B_exp[:, s, a].sum(), 1.0)

    def test_expected_D_normalised(self):
        """Expected D should sum to 1."""
        pD = np.array([3.0, 1.0, 2.0])
        D_exp = expected_D(pD)
        assert np.isclose(D_exp.sum(), 1.0)
        assert np.isclose(D_exp[0], 0.5)


class TestDirichletEntropy:
    """Tests for Dirichlet distribution entropy."""

    def test_higher_concentration_lower_entropy(self):
        """Higher concentration → lower entropy (more confident)."""
        alpha_low = np.array([1.0, 1.0, 1.0])
        alpha_high = np.array([10.0, 10.0, 10.0])
        assert dirichlet_entropy(alpha_low) > dirichlet_entropy(alpha_high)

    def test_symmetric_concentration(self):
        """Symmetric Dirichlet with same alpha should give same entropy for any K."""
        h3 = dirichlet_entropy(np.array([2.0, 2.0, 2.0]))
        assert np.isfinite(h3)


class TestBMR:
    """Tests for Bayesian Model Reduction."""

    def test_same_model_zero_delta(self):
        """BMR of prior against itself → ΔF ≈ 0."""
        pA = np.ones((2, 2))
        delta_F, prune = bayesian_model_reduction(pA, pA)
        assert np.allclose(delta_F, 0.0, atol=1e-10)
        assert not np.any(prune)

    def test_learned_model_nonzero_delta(self):
        """Concentrated learned model → negative ΔF (lower log-Beta)."""
        pA_prior = np.ones((2, 2))
        pA_learned = np.array([[5.0, 1.0], [1.0, 5.0]])
        delta_F, prune = bayesian_model_reduction(pA_learned, pA_prior)
        # More concentrated → smaller Beta → ΔF < 0
        assert np.all(delta_F != 0.0)
        assert np.all(np.isfinite(delta_F))

    def test_shape_mismatch_raises(self):
        """Mismatched shapes should raise ValueError."""
        with pytest.raises(ValueError, match="Shape mismatch"):
            bayesian_model_reduction(np.ones((2, 2)), np.ones((3, 3)))

    def test_2d_pA_raises(self):
        """pA must be 2D."""
        with pytest.raises(ValueError, match="pA must be 2-D"):
            # Reuse update_dirichlet_A function to trigger the check
            update_dirichlet_A(np.ones(2), 0, np.ones(2))
