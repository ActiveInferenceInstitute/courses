"""Agent subpackage — generative model, agent, and environment.

Re-exports all public classes for convenient access:
    from active_inference.agent import GenerativeModel, ActiveInferenceAgent, DiscreteEnvironment
"""

from .generative_model import GenerativeModel
from .agent import ActiveInferenceAgent
from .environment import DiscreteEnvironment

__all__ = [
    "GenerativeModel",
    "ActiveInferenceAgent",
    "DiscreteEnvironment",
]
