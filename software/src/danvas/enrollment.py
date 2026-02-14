"""Enrollment and roster management for Danvas.

Provides user enrollment, unenrollment, and roster retrieval
with role validation against ``config.ROLES``.
"""

import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .store import load_store, save_store

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


logger = get_logger("danvas.enrollment")


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────


def enroll_user(
    course_id: str,
    user_name: str,
    role: str = "student",
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Enroll a user in a course.

    Args:
        course_id: Course identifier.
        user_name: Display name / username.
        role: One of ``config.ROLES``.
        data_dir: Override for data directory.

    Returns:
        The enrollment record dict.
    """
    if role not in config.ROLES:
        raise ValueError(f"Invalid role '{role}'. Must be one of {config.ROLES}")

    store = load_store(course_id, data_dir)
    # Check for duplicate
    for e in store["enrollments"]:
        if e["user_name"] == user_name:
            logger.info("User '%s' already enrolled in %s", user_name, course_id)
            return e

    record: Dict[str, Any] = {
        "id": str(uuid.uuid4()),
        "user_name": user_name,
        "role": role,
        "enrolled_at": datetime.now().strftime(config.DATETIME_FORMAT),
    }
    store["enrollments"].append(record)
    save_store(course_id, store, data_dir)
    logger.info("Enrolled '%s' as %s in %s", user_name, role, course_id)
    return record


def unenroll_user(
    course_id: str, user_name: str, data_dir: Optional[Path] = None
) -> bool:
    """Remove a user from a course.

    Returns:
        ``True`` if the user was found and removed.
    """
    store = load_store(course_id, data_dir)
    before = len(store["enrollments"])
    store["enrollments"] = [
        e for e in store["enrollments"] if e["user_name"] != user_name
    ]
    if len(store["enrollments"]) < before:
        save_store(course_id, store, data_dir)
        logger.info("Unenrolled '%s' from %s", user_name, course_id)
        return True
    return False


def get_roster(
    course_id: str, data_dir: Optional[Path] = None
) -> List[Dict[str, Any]]:
    """Return the enrollment list for a course."""
    return load_store(course_id, data_dir)["enrollments"]
