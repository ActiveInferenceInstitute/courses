"""Configuration for Danvas course management system."""

import os
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------
DANVAS_PORT: int = 8420
DANVAS_HOST: str = "127.0.0.1"

# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------
DANVAS_DATA_DIR: Path = Path(os.environ.get("DANVAS_DATA_DIR", str(Path.home() / ".danvas")))

# Per-course state files
STORE_FILENAME: str = "danvas_store.json"

# ---------------------------------------------------------------------------
# Feature flags — toggle sections of the UI
# ---------------------------------------------------------------------------
FEATURE_FLAGS: Dict[str, bool] = {
    "gradebook": True,
    "announcements": True,
    "calendar": True,
    "roster": True,
    "discussions": False,  # future
    "analytics": False,  # future
}

# ---------------------------------------------------------------------------
# Roles & permissions
# ---------------------------------------------------------------------------
ROLES: List[str] = ["instructor", "ta", "student"]

# Default role for requests.  Local-first tool: when no authenticated
# principal is supplied, requests are treated as instructor so the tool works
# out of the box on loopback.  Configure ``DANVAS_ROLE`` (or bind a remote
# host) to scope it down; see AGENTS.md threat model.
DEFAULT_ROLE: str = os.environ.get("DANVAS_ROLE", "instructor")

ROLE_PERMISSIONS: Dict[str, List[str]] = {
    "instructor": [
        "view_course",
        "edit_course",
        "view_gradebook",
        "edit_gradebook",
        "post_announcement",
        "view_announcement",
        "manage_roster",
        "view_roster",
        "manage_calendar",
        "view_calendar",
    ],
    "ta": [
        "view_course",
        "view_gradebook",
        "edit_gradebook",
        "post_announcement",
        "view_announcement",
        "view_roster",
        "view_calendar",
    ],
    "student": [
        "view_course",
        "view_gradebook",
        "view_announcement",
        "view_roster",
        "view_calendar",
    ],
}

# ---------------------------------------------------------------------------
# Grading schema
# ---------------------------------------------------------------------------
DEFAULT_GRADING_SCHEMA: Dict[str, float] = {
    "A+": 97.0,
    "A": 93.0,
    "A-": 90.0,
    "B+": 87.0,
    "B": 83.0,
    "B-": 80.0,
    "C+": 77.0,
    "C": 73.0,
    "C-": 70.0,
    "D+": 67.0,
    "D": 63.0,
    "D-": 60.0,
    "F": 0.0,
}

# ---------------------------------------------------------------------------
# Empty store template
# ---------------------------------------------------------------------------
EMPTY_STORE: Dict[str, Any] = {
    "enrollments": [],
    "grades": {},
    "announcements": [],
    "calendar_events": [],
}

# ---------------------------------------------------------------------------
# UI constants
# ---------------------------------------------------------------------------
APP_NAME: str = "Danvas"
APP_TAGLINE: str = "Course Management, Simplified"
MAX_ANNOUNCEMENT_LENGTH: int = 5000
MAX_USER_NAME_LENGTH: int = 200
MAX_FIELD_LENGTH: int = 500
# Maximum accepted HTTP POST body (bytes).  Prevents memory-exhaustion DoS via
# an attacker-controlled Content-Length / oversized form body.
MAX_POST_BODY: int = 64 * 1024
DATE_FORMAT: str = "%Y-%m-%d"
DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
