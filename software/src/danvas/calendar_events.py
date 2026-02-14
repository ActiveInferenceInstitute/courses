"""Calendar event management for Danvas.

Provides creation and retrieval of calendar events with
automatic date-based sorting.
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


logger = get_logger("danvas.calendar_events")


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────


def add_event(
    course_id: str,
    title: str,
    date: str,
    description: str = "",
    event_type: str = "assignment",
    data_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Add a calendar event.

    Args:
        course_id: Course identifier.
        title: Event title.
        date: Date string (YYYY-MM-DD).
        description: Optional description.
        event_type: Category (assignment, lecture, exam, holiday, other).
        data_dir: Override for data directory.

    Returns:
        The event record dict.
    """
    store = load_store(course_id, data_dir)
    record: Dict[str, Any] = {
        "id": str(uuid.uuid4()),
        "title": title,
        "date": date,
        "description": description,
        "event_type": event_type,
        "created_at": datetime.now().strftime(config.DATETIME_FORMAT),
    }
    store["calendar_events"].append(record)
    # Keep sorted by date
    store["calendar_events"].sort(key=lambda e: e["date"])
    save_store(course_id, store, data_dir)
    logger.info("Added calendar event '%s' on %s in %s", title, date, course_id)
    return record


def get_events(
    course_id: str, data_dir: Optional[Path] = None
) -> List[Dict[str, Any]]:
    """Return calendar events for a course (sorted by date)."""
    return load_store(course_id, data_dir).get("calendar_events", [])
