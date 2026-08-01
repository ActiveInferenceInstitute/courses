"""Gradebook operations for Danvas.

Provides grade recording, retrieval, course-grade calculation, and
letter-grade conversion using ``config.DEFAULT_GRADING_SCHEMA``.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
import math

from . import config
from .store import load_store, store_transaction

try:
    from ..batch_processing.logging_config import get_logger
except Exception:
    import logging

    def get_logger(name: str) -> logging.Logger:
        """Fallback logger factory."""
        _logger = logging.getLogger(name)
        if not _logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
            _logger.addHandler(handler)
            _logger.setLevel(logging.INFO)
        return _logger


logger = get_logger("danvas.gradebook")


# ──────────────────────────────────────────────────────────────────────────────
# Grade recording
# ──────────────────────────────────────────────────────────────────────────────


def record_grade(
    course_id: str,
    user_name: str,
    assignment: str,
    score: float,
    max_score: float = 100.0,
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Record or update a grade for a student.

    Args:
        course_id: Course identifier.
        user_name: Student username.
        assignment: Assignment identifier / name.
        score: Points earned.
        max_score: Maximum possible points.
        data_dir: Override for data directory.

    Returns:
        The grade entry dict.

    Raises:
        ValueError: If *score* or *max_score* is not finite, or if
            *max_score* is negative.
    """
    if not math.isfinite(score):
        raise ValueError(f"score must be finite, got {score!r}")
    if not math.isfinite(max_score):
        raise ValueError(f"max_score must be finite, got {max_score!r}")
    if max_score < 0:
        raise ValueError(f"max_score must be non-negative, got {max_score!r}")

    with store_transaction(course_id, data_dir) as store:
        grades = store.setdefault("grades", {})
        user_grades = grades.setdefault(user_name, {})

        entry: Dict[str, Any] = {
            "score": score,
            "max_score": max_score,
            "percentage": round((score / max_score) * 100, 2) if max_score else 0.0,
            "updated_at": datetime.now().strftime(config.DATETIME_FORMAT),
        }
        user_grades[assignment] = entry
        logger.info(
            "Recorded grade %s/%s for '%s' on '%s' in %s",
            score,
            max_score,
            user_name,
            assignment,
            course_id,
        )
        return entry


# ──────────────────────────────────────────────────────────────────────────────
# Grade retrieval
# ──────────────────────────────────────────────────────────────────────────────


def get_grades(
    course_id: str,
    user_name: Optional[str] = None,
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Retrieve grades.

    If *user_name* is provided, returns that student's grades dict.
    Otherwise returns the full gradebook mapping.
    """
    grades = load_store(course_id, data_dir).get("grades", {})
    if user_name:
        return grades.get(user_name, {})
    return grades


# ──────────────────────────────────────────────────────────────────────────────
# Aggregate calculation
# ──────────────────────────────────────────────────────────────────────────────


def calculate_course_grade(
    course_id: str,
    user_name: str,
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Calculate overall course grade for a student.

    Returns:
        Dict with ``average_percentage``, ``letter_grade``, ``assignments_count``.
    """
    user_grades = get_grades(course_id, user_name, data_dir)
    if not user_grades:
        return {"average_percentage": 0.0, "letter_grade": "N/A", "assignments_count": 0}

    total_pct = sum(g["percentage"] for g in user_grades.values())
    avg = round(total_pct / len(user_grades), 2)
    letter = _percentage_to_letter(avg)

    return {
        "average_percentage": avg,
        "letter_grade": letter,
        "assignments_count": len(user_grades),
    }


def _percentage_to_letter(pct: float) -> str:
    """Convert percentage to letter grade using the default schema."""
    for letter, threshold in config.DEFAULT_GRADING_SCHEMA.items():
        if pct >= threshold:
            return letter
    return "F"
