"""JSON-backed persistence layer for Danvas.

Provides atomic read/write of per-course state files.  Each course
stores its data in ``<data_dir>/<course_id>/danvas_store.json``.
"""

import copy
import json
import os
import re
import tempfile
import threading
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
# Course-id validation
# ──────────────────────────────────────────────────────────────────────────────

# Only a narrow alphanumeric id (plus dash/underscore) is ever allowed to reach
# a file path.  This rejects path separators, "..", "%", and other traversal
# primitives before they are interpolated into `_store_path`.
_SAFE_COURSE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")


def validate_course_id(course_id: str) -> str:
    """Validate and return a safe *course_id*, raising ``ValueError`` otherwise.

    Args:
        course_id: Candidate course identifier.

    Returns:
        The validated id, unchanged.

    Raises:
        ValueError: If *course_id* is not a safe identifier (empty, contains
            ``/``, ``\\``, ``..``, ``%``, or path-breaking characters).
    """
    if not isinstance(course_id, str):
        raise ValueError(f"course_id must be a string, got {course_id!r}")
    if not _SAFE_COURSE_ID_RE.match(course_id):
        raise ValueError(
            f"Invalid course_id {course_id!r}: only [A-Za-z0-9_-] allowed "
            "(no path separators or '..')"
        )
    return course_id


# ──────────────────────────────────────────────────────────────────────────────
# Path helpers
# ──────────────────────────────────────────────────────────────────────────────


def _store_path(course_id: str, data_dir: Optional[Path] = None) -> Path:
    """Return the JSON store path for a given course.

    Validates *course_id* so callers cannot traverse outside *data_dir*.

    Args:
        course_id: Course identifier (validated as a safe identifier).
        data_dir: Override base directory.

    Returns:
        The resolved store path.

    Raises:
        ValueError: If *course_id* is not a safe identifier.
    """
    validate_course_id(course_id)
    base = data_dir or config.DANVAS_DATA_DIR
    path = (base / course_id / config.STORE_FILENAME).resolve()
    # Belt-and-braces: ensure the resolved path stays inside the base dir.
    if not path.is_relative_to(base.resolve()):
        raise ValueError(f"course_id {course_id!r} escapes the data directory")
    return path


# ──────────────────────────────────────────────────────────────────────────────
# Read / write
# ──────────────────────────────────────────────────────────────────────────────

# Per-course locks guard the load-modify-save cycles so concurrent writers
# cannot silently lose each other's updates (lost-update prevention).  The
# shipped single-threaded HTTPServer serializes requests today, but the lock
# makes the data layer correct under any future threaded/parallel usage.

_LOCK_REGISTRY: Dict[str, threading.Lock] = {}
_LOCK_REGISTRY_GUARD = threading.Lock()


def _course_lock(course_id: str, data_dir: Optional[Path]) -> threading.Lock:
    """Return (and cache) a per-course lock keyed by resolved path."""
    key = str(_store_path(course_id, data_dir))
    with _LOCK_REGISTRY_GUARD:
        lock = _LOCK_REGISTRY.get(key)
        if lock is None:
            lock = threading.Lock()
            _LOCK_REGISTRY[key] = lock
        return lock


def store_transaction(course_id: str, data_dir: Optional[Path] = None) -> "_StoreTransaction":
    """Return a context manager that serializes a load-modify-save cycle.

    Typical usage::

        with store_transaction(course_id, data_dir) as store:
            store["grades"]["bob"] = {...}   # mutate in place
        # store written atomically on exit

    The lock is held for the whole ``with`` block so concurrent writers on
    the same course cannot lose each other's updates.

    Args:
        course_id: Unique course identifier.
        data_dir: Override for the data directory.
    """
    return _StoreTransaction(course_id, data_dir)


class _StoreTransaction:
    """Context manager that loads a store, yields it for mutation, and saves."""

    def __init__(self, course_id: str, data_dir: Optional[Path]) -> None:
        self.course_id = course_id
        self.data_dir = data_dir
        self._lock = _course_lock(course_id, data_dir)
        self._store: Dict[str, Any] = {}

    def __enter__(self) -> Dict[str, Any]:
        self._lock.acquire()
        try:
            self._store = load_store(self.course_id, self.data_dir)
            return self._store
        except Exception:
            self._lock.release()
            raise

    def __exit__(self, exc_type, exc, tb) -> bool:
        try:
            if exc_type is None:
                save_store(self.course_id, self._store, self.data_dir)
        finally:
            self._lock.release()
        return False


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
            try:
                data: Dict[str, Any] = json.load(fh)
                return data
            except (json.JSONDecodeError, UnicodeDecodeError):
                # A truncated/tampered store must not permanently 500 every
                # request: fall back to empty state and surface a warning so
                # the corruption is visible rather than silent.
                logger.warning("Store corrupted, falling back to empty: %s", path)
                return copy.deepcopy(config.EMPTY_STORE)
    return copy.deepcopy(config.EMPTY_STORE)


def save_store(course_id: str, store: Dict[str, Any], data_dir: Optional[Path] = None) -> None:
    """Persist the store for *course_id* via atomic, durable write.

    Writes to a temp file, fsyncs it, then renames to avoid partial-write
    corruption and to guarantee durability (``os.replace`` is atomic but not
    durable on its own).

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
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, str(path))
        logger.info("Store saved: %s", path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
