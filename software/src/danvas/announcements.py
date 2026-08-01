"""Announcement management for Danvas.

Provides posting and retrieval of course announcements with
length validation against ``config.MAX_ANNOUNCEMENT_LENGTH``.
"""

import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .store import load_store, store_transaction

try:
    from ..batch_processing.logging_config import get_logger
except Exception:
    import logging

    def get_logger(name: str = "danvas") -> logging.Logger:
        """Fallback logger factory."""
        _logger = logging.getLogger(name)
        if not _logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
            _logger.addHandler(handler)
            _logger.setLevel(logging.INFO)
        return _logger


logger = get_logger("danvas.announcements")


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────


def post_announcement(
    course_id: str,
    title: str,
    body: str,
    author: str = "Instructor",
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Post an announcement to a course.

    Args:
        course_id: Course identifier.
        title: Announcement title.
        body: Announcement body text.
        author: Author name.
        data_dir: Override for data directory.

    Returns:
        The announcement record dict.
    """
    if len(body) > config.MAX_ANNOUNCEMENT_LENGTH:
        raise ValueError(f"Announcement body exceeds {config.MAX_ANNOUNCEMENT_LENGTH} chars")
    if len(title) > config.MAX_FIELD_LENGTH:
        raise ValueError(f"Announcement title exceeds {config.MAX_FIELD_LENGTH} chars")
    if len(author) > config.MAX_USER_NAME_LENGTH:
        raise ValueError(f"Author name exceeds {config.MAX_USER_NAME_LENGTH} chars")

    with store_transaction(course_id, data_dir) as store:
        record: Dict[str, Any] = {
            "id": str(uuid.uuid4()),
            "title": title,
            "body": body,
            "author": author,
            "posted_at": datetime.now().strftime(config.DATETIME_FORMAT),
        }
        store["announcements"].insert(0, record)  # newest first
        logger.info("Posted announcement '%s' in %s", title, course_id)
        return record


def get_announcements(course_id: str, data_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Return announcements for a course (newest first)."""
    return load_store(course_id, data_dir).get("announcements", [])  # type: ignore[no-any-return]
