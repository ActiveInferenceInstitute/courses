"""Validation module for course output verification.

This module provides functions to validate that course outputs have been
generated correctly and published to the expected locations.
"""

from .main import (
    validate_outputs,
    validate_published,
    generate_validation_report,
    get_output_summary,
)

__all__ = [
    "validate_outputs",
    "validate_published",
    "generate_validation_report",
    "get_output_summary",
]
