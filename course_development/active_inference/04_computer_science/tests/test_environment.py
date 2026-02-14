"""Tests for environment.py — generative process dynamics and validation.

All computations are real (no mocks).
"""

import numpy as np
import pytest

from active_inference.agent.environment import DiscreteEnvironment


class TestEnvironmentCreation:
    """Construction and validation tests."""

    def test_correct_dimensions(self, simple_model):
        """Environment should report correct counts."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        assert env.num_states == 2
        assert env.num_obs == 2
        assert env.num_actions == 2

    def test_initial_state(self, simple_model):
        """State should match initial_state argument."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=1)
        assert env.state == 1

    def test_invalid_initial_state(self, simple_model):
        """Out-of-range initial_state should raise ValueError."""
        with pytest.raises(ValueError, match="initial_state"):
            DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=99)

    def test_invalid_A_raises(self):
        """Non-normalised A should raise ValueError."""
        A_bad = np.array([[0.5, 0.5], [0.3, 0.3]])
        B = np.zeros((2, 2, 1)); B[:, :, 0] = np.eye(2)
        with pytest.raises(ValueError, match="true_A"):
            DiscreteEnvironment(A_bad, B)

    def test_repr(self, simple_model):
        """__repr__ should include dimensions."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        r = repr(env)
        assert "states=2" in r
        assert "obs=2" in r

    def test_invalid_A_ndim(self):
        """A must be 2-D."""
        with pytest.raises(ValueError, match="true_A must be 2-D"):
            DiscreteEnvironment(np.ones(2), np.eye(2))

    def test_invalid_B_sum(self):
        """B columns must sum to 1."""
        A = np.eye(2)
        B = np.zeros((2, 2, 1))
        # Column 0 sums to 0
        with pytest.raises(ValueError, match="true_B column"):
            DiscreteEnvironment(A, B)


class TestEnvironmentDynamics:
    """Step and reset dynamics."""

    def test_reset_returns_valid_obs(self, simple_model):
        """Reset should return a valid observation index."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        obs = env.reset(initial_state=0)
        assert 0 <= obs < env.num_obs

    def test_reset_invalid_state(self, simple_model):
        """Resetting to invalid state should raise ValueError."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        with pytest.raises(ValueError, match="initial_state"):
            env.reset(initial_state=99)

    def test_step_transitions_state(self, simple_model):
        """Deterministic swap action should change state."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        env.step(action=1)  # swap
        assert env.state == 1

    def test_step_returns_valid_obs(self, simple_model):
        """Step should return a valid observation."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        obs = env.step(0)
        assert 0 <= obs < env.num_obs

    def test_invalid_action_raises(self, simple_model):
        """Out-of-range action should raise ValueError."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        with pytest.raises(ValueError, match="Action"):
            env.step(99)

    def test_timestep_increments(self, simple_model):
        """Timestep should increment after each step."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        assert env.timestep == 0
        env.step(0)
        assert env.timestep == 1
        env.step(0)
        assert env.timestep == 2

    def test_step_2d_B_matrix(self):
        """Should handle 2D B-matrix (single action)."""
        A = np.eye(2)
        B = np.array([[0.0, 1.0], [1.0, 0.0]])  # swap
        env = DiscreteEnvironment(A, B, initial_state=0)
        
        env.step(action=0)
        assert env.state == 1
        env.step(action=0)
        assert env.state == 0


class TestEnvironmentHistory:
    """History and info tracking."""

    def test_history_tracking(self, simple_model):
        """Environment should track states, observations, actions."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        env.step(0)
        env.step(1)
        assert len(env.history["actions"]) == 2
        assert len(env.history["states"]) == 3  # initial + 2 steps
        assert len(env.history["observations"]) == 2

    def test_get_info(self, simple_model):
        """get_info should return correct metadata."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        info = env.get_info()
        assert info["state"] == 0
        assert info["timestep"] == 0
        assert info["num_states"] == 2

    def test_reset_clears_history(self, simple_model):
        """Reset should clear history."""
        env = DiscreteEnvironment(simple_model.A, simple_model.B)
        env.step(0)
        env.step(1)
        env.reset(0)
        assert len(env.history["actions"]) == 0
        assert env.timestep == 0
