"""Tests for agent.py — belief updating, policy selection, prediction errors.

Verifies the perception-action loop, history tracking, and error handling.
All computations are real (no mocks).
"""

import numpy as np
import pytest

from active_inference.agent.agent import ActiveInferenceAgent
from active_inference.agent.generative_model import GenerativeModel


class TestAgentCreation:
    """Agent construction tests."""

    def test_initialises_with_prior(self, simple_model):
        """Beliefs should start at prior D."""
        agent = ActiveInferenceAgent(simple_model, gamma=1.0)
        assert np.allclose(agent.q_s, simple_model.D)

    def test_default_policies(self, simple_model):
        """Default policies should be single-step, one per action."""
        agent = ActiveInferenceAgent(simple_model)
        assert len(agent.policies) == simple_model.num_actions

    def test_custom_policies(self, simple_model):
        """Custom policies should be stored."""
        agent = ActiveInferenceAgent(simple_model, policies=[[0, 0], [1, 1]])
        assert len(agent.policies) == 2

    def test_negative_gamma_raises(self, simple_model):
        """Negative gamma should raise ValueError."""
        with pytest.raises(ValueError, match="gamma"):
            ActiveInferenceAgent(simple_model, gamma=-1.0)

    def test_repr(self, simple_model):
        """__repr__ should include gamma and policy count."""
        r = repr(ActiveInferenceAgent(simple_model, gamma=2.0))
        assert "γ=2.0" in r
        assert "policies=2" in r


class TestStateInference:
    """Tests for infer_states (perception)."""

    def test_beliefs_shift_toward_likely_state(self, simple_model):
        """After observing o=0, beliefs should favour state 0."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        assert agent.q_s[0] > 0.5

    def test_repeated_observation_increases_precision(self, simple_model):
        """Multiple consistent observations should increase precision."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        p1 = agent.q_s[0]
        agent.infer_states(0)
        p2 = agent.q_s[0]
        assert p2 >= p1 - 1e-10  # should not decrease

    def test_invalid_observation_raises(self, simple_model):
        """Out-of-range observation should raise ValueError."""
        agent = ActiveInferenceAgent(simple_model)
        with pytest.raises(ValueError, match="Observation"):
            agent.infer_states(99)


class TestActionSelection:
    """Tests for infer_policies and select_action."""

    def test_select_action_valid(self, simple_model):
        """Selected action should be in valid range."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        action = agent.select_action()
        assert 0 <= action < simple_model.num_actions

    def test_step_returns_action(self, simple_model):
        """step() should return a valid action."""
        agent = ActiveInferenceAgent(simple_model)
        action = agent.step(0)
        assert 0 <= action < simple_model.num_actions

    def test_policy_posterior_valid_dist(self, simple_model):
        """q(π) should sum to 1."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        q_pi = agent.infer_policies()
        assert np.isclose(q_pi.sum(), 1.0)

    def test_infer_policies_2d_B(self):
        """Should handle 2D B-matrix (single action implicit)."""
        A = np.eye(2)
        B = np.eye(2)
        C = np.zeros(2)
        D = np.array([0.5, 0.5])
        
        # Use real GenerativeModel instead of mock
        model = GenerativeModel(A, B, C, D)
        agent = ActiveInferenceAgent(model)
        
        q_pi = agent.infer_policies()
        assert len(q_pi) == 1


class TestPredictionErrors:
    """Tests for prediction_error and get_predicted_observation."""

    def test_predicted_obs_valid(self, simple_model):
        """Predicted observation should be a valid distribution."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        q_o = agent.get_predicted_observation()
        assert np.isclose(q_o.sum(), 1.0)

    def test_prediction_error_shape(self, simple_model):
        """Prediction error should have shape (num_obs,)."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        pe = agent.prediction_error(0)
        assert pe.shape == (simple_model.num_obs,)

    def test_prediction_error_sums_to_zero(self, simple_model):
        """Prediction error elements should sum to ≈ 0."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        pe = agent.prediction_error(0)
        assert np.isclose(pe.sum(), 0.0, atol=1e-10)


class TestHistory:
    """Tests for history tracking and reset."""

    def test_history_tracking(self, simple_model):
        """Agent should track observations, actions, beliefs."""
        agent = ActiveInferenceAgent(simple_model)
        agent.step(0)
        agent.step(1)
        assert len(agent.history["observations"]) == 2
        assert len(agent.history["actions"]) == 2
        assert len(agent.history["beliefs"]) == 2

    def test_reset(self, simple_model):
        """Reset should restore prior and clear history."""
        agent = ActiveInferenceAgent(simple_model)
        agent.step(0)
        agent.reset()
        assert np.allclose(agent.q_s, simple_model.D)
        assert len(agent.history["observations"]) == 0

    def test_vfe_history_logged(self, simple_model):
        """VFE should be logged after each state inference."""
        agent = ActiveInferenceAgent(simple_model)
        agent.infer_states(0)
        assert len(agent.history["vfe"]) == 1
        assert np.isfinite(agent.history["vfe"][0])
