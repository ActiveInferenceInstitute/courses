"""JSON-backed persistence layer for Danvas.

Provides atomic read/write of per-course state files.  Each course
stores its data in ``<data_dir>/<course_id>/danvas_store.json``.
"""

import copy
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from . import config

try:
    from ..batch_processing.logging_config import get_logger
except Exception:  # standalone usage
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


logger = get_logger("danvas.store")


# ──────────────────────────────────────────────────────────────────────────────
# Path helpers
# ──────────────────────────────────────────────────────────────────────────────


def _store_path(course_id: str, data_dir: Optional[Path] = None) -> Path:
    """Return the JSON store path for a given course."""
    base = data_dir or config.DANVAS_DATA_DIR
    return base / course_id / config.STORE_FILENAME


# ──────────────────────────────────────────────────────────────────────────────
# Read / write
# ──────────────────────────────────────────────────────────────────────────────


def load_store(course_id: str, data_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Load the JSON store for *course_id*, creating defaults if missing.

    Args:
        course_id: Unique course identifier.
        data_dir: Override for the data directory.

    Returns:
        Mutable dictionary with course state.
    """
    path = _store_path(course_id, data_dir)
    if path.exists():
        with open(path, encoding="utf-8") as fh:
            data: Dict[str, Any] = json.load(fh)
            return data
    return copy.deepcopy(config.EMPTY_STORE)


def save_store(
    course_id: str, store: Dict[str, Any], data_dir: Optional[Path] = None
) -> None:
    """Persist the store for *course_id* via atomic write.

    Writes to a temp file then renames to avoid partial-write corruption.

    Args:
        course_id: Unique course identifier.
        store: The complete store dict to persist.
        data_dir: Override for the data directory.
    """
    path = _store_path(course_id, data_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(store, fh, indent=2, default=str)
        os.replace(tmp, str(path))
        logger.info("Store saved: %s", path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
