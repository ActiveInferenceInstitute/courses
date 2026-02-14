"""Tests for generative_model.py — A, B, C, D, E matrix management.

Verifies shapes, normalisation, predictions, surprisal, log-joint,
validation errors, and repr.  All computations are real (no mocks).
"""

import numpy as np
import pytest

from active_inference.agent.generative_model import GenerativeModel


class TestGenerativeModelCreation:
    """Construction and validation tests."""

    def test_correct_dimensions(self, simple_model):
        """Model should report correct obs/state/action counts."""
        assert simple_model.num_obs == 2
        assert simple_model.num_states == 2
        assert simple_model.num_actions == 2

    def test_tmaze_dimensions(self, tmaze_model):
        """T-maze should have 4 states, 3 obs, 3 actions."""
        assert tmaze_model.num_obs == 3
        assert tmaze_model.num_states == 4
        assert tmaze_model.num_actions == 3

    def test_A_column_normalisation(self, simple_model):
        """Every column of A must sum to 1."""
        for s in range(simple_model.num_states):
            assert np.isclose(simple_model.A[:, s].sum(), 1.0)

    def test_B_column_normalisation(self, simple_model):
        """Every column of B[:, :, a] must sum to 1."""
        for a in range(simple_model.num_actions):
            for s in range(simple_model.num_states):
                assert np.isclose(simple_model.B[:, s, a].sum(), 1.0)

    def test_D_normalisation(self, simple_model):
        """D must sum to 1."""
        assert np.isclose(simple_model.D.sum(), 1.0)

    def test_E_optional(self, simple_model):
        """E defaults to None when not provided."""
        assert simple_model.E is None

    def test_E_provided(self):
        """E should be stored when provided."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        B = np.zeros((2, 2, 2)); B[:, :, 0] = np.eye(2); B[:, :, 1] = np.eye(2)
        m = GenerativeModel(A=A, B=B, C=np.zeros(2), D=np.array([0.5, 0.5]),
                            E=np.array([0.6, 0.4]))
        assert m.E is not None
        assert np.isclose(m.E.sum(), 1.0)


class TestGenerativeModelValidation:
    """Validation should raise ValueError for invalid inputs."""

    def test_invalid_A_non_normalised(self):
        """Non-normalised A columns should raise ValueError."""
        A_bad = np.array([[0.5, 0.5], [0.3, 0.3]])
        B = np.zeros((2, 2, 1)); B[:, :, 0] = np.eye(2)
        with pytest.raises(ValueError, match="A column"):
            GenerativeModel(A=A_bad, B=B, C=np.zeros(2), D=np.array([0.5, 0.5]))

    def test_invalid_A_wrong_ndim(self):
        """1-D A should raise ValueError."""
        with pytest.raises(ValueError, match="A must be 2-D"):
            GenerativeModel(
                A=np.array([0.5, 0.5]),
                B=np.zeros((2, 2, 1)),
                C=np.zeros(2),
                D=np.array([0.5, 0.5]),
            )

    def test_invalid_B_shape(self):
        """B shape must match num_states."""
        with pytest.raises(ValueError, match="B shape"):
            GenerativeModel(
                A=np.eye(2),
                B=np.zeros((3, 3, 1)), # mismatch with 2 states from A
                C=np.zeros(2),
                D=np.array([0.5, 0.5]),
            )

    def test_invalid_B_ndim(self):
        """B must be 2D or 3D."""
        with pytest.raises(ValueError, match="B must be 2-D or 3-D"):
            GenerativeModel(
                A=np.eye(2),
                B=np.zeros(4),
                C=np.zeros(2),
                D=np.array([0.5, 0.5]),
            )

    def test_invalid_B_sum(self):
        """B columns must sum to 1."""
        B = np.zeros((2, 2, 1))
        with pytest.raises(ValueError, match="B column"):
            GenerativeModel(
                A=np.eye(2),
                B=B,
                C=np.zeros(2),
                D=np.array([0.5, 0.5]),
            )

    def test_invalid_D_shape(self):
        """D shape must match num_states."""
        with pytest.raises(ValueError, match="D shape"):
            GenerativeModel(
                A=np.eye(2),
                B=np.eye(2),
                C=np.zeros(2),
                D=np.array([0.5, 0.5, 0.0]),
            )

    def test_invalid_D_non_normalised(self):
        """Non-normalised D should raise ValueError."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        B = np.zeros((2, 2, 1)); B[:, :, 0] = np.eye(2)
        with pytest.raises(ValueError, match="D sums"):
            GenerativeModel(A=A, B=B, C=np.zeros(2), D=np.array([0.5, 0.3]))

    def test_invalid_C_shape(self):
        """C with wrong shape should raise ValueError."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        B = np.zeros((2, 2, 1)); B[:, :, 0] = np.eye(2)
        with pytest.raises(ValueError, match="C shape"):
            GenerativeModel(A=A, B=B, C=np.zeros(3), D=np.array([0.5, 0.5]))

    def test_invalid_E_non_normalised(self):
        """Non-normalised E should raise ValueError."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        B = np.zeros((2, 2, 1)); B[:, :, 0] = np.eye(2)
        with pytest.raises(ValueError, match="E sums"):
            GenerativeModel(A=A, B=B, C=np.zeros(2), D=np.array([0.5, 0.5]),
                            E=np.array([0.5, 0.3]))


class TestGenerativeModelQueries:
    """Prediction and information-theoretic queries."""

    def test_predict_observation_valid_dist(self, simple_model):
        """predict_observation should return a valid distribution."""
        q_s = np.array([1.0, 0.0])
        q_o = simple_model.predict_observation(q_s)
        assert np.isclose(q_o.sum(), 1.0)
        assert np.isclose(q_o[0], 0.9)

    def test_predict_state_swap(self, simple_model):
        """Swap action on state 0 should yield state 1."""
        q_s = np.array([1.0, 0.0])
        q_next = simple_model.predict_state(q_s, action=1)
        assert np.isclose(q_next[1], 1.0)

    def test_predict_state_2d(self):
        """Should handle 2D B-matrix."""
        gm = GenerativeModel(
            A=np.eye(2),
            B=np.eye(2),
            C=np.zeros(2),
            D=np.array([0.5, 0.5]),
        )
        q_s = np.array([1.0, 0.0])
        q_next = gm.predict_state(q_s, action=0)
        assert np.allclose(q_next, q_s)

    def test_predict_state_invalid_action(self, simple_model):
        """Out-of-range action should raise ValueError."""
        with pytest.raises(ValueError, match="Action"):
            simple_model.predict_state(np.array([0.5, 0.5]), action=99)

    def test_log_likelihood_shape(self, simple_model):
        """log_likelihood should return (num_states,) vector."""
        ll = simple_model.log_likelihood(0)
        assert ll.shape == (simple_model.num_states,)

    def test_log_likelihood_invalid_obs(self, simple_model):
        """Out-of-range observation should raise ValueError."""
        with pytest.raises(ValueError, match="Observation"):
            simple_model.log_likelihood(99)

    def test_surprisal_positive(self, simple_model):
        """Surprisal should be non-negative for any valid observation."""
        q_s = np.array([0.5, 0.5])
        s = simple_model.surprisal(0, q_s)
        assert s >= 0.0

    def test_surprisal_low_for_expected(self, simple_model):
        """Surprisal should be lower for expected observations."""
        q_s = np.array([0.99, 0.01])  # confident state 0
        s0 = simple_model.surprisal(0, q_s)  # obs 0 is likely
        s1 = simple_model.surprisal(1, q_s)  # obs 1 is unlikely
        assert s0 < s1

    def test_surprisal_invalid_obs(self, simple_model):
        """Out-of-range observation should raise ValueError."""
        with pytest.raises(ValueError, match="Observation"):
            simple_model.surprisal(99, np.array([0.5, 0.5]))

    def test_log_joint(self, simple_model):
        """log_joint should equal ln A[o,s] + ln D[s]."""
        lj = simple_model.log_joint(0, 0)
        expected = np.log(0.9) + np.log(0.5)
        assert np.isclose(lj, expected, atol=1e-10)

    def test_log_joint_invalid_state(self, simple_model):
        """Out-of-range state should raise ValueError."""
        with pytest.raises(ValueError, match="State"):
            simple_model.log_joint(0, 99)

    def test_log_joint_invalid_obs(self, simple_model):
        """Out-of-range observation should raise ValueError."""
        with pytest.raises(ValueError, match="Observation"):
            simple_model.log_joint(99, 0)

    def test_repr(self, simple_model):
        """__repr__ should include dimensions."""
        r = repr(simple_model)
        assert "obs=2" in r
        assert "states=2" in r
        assert "actions=2" in r
