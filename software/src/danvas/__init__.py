"""Danvas — lightweight course management system.

A self-hosted Canvas clone that reads the existing course directory
structure and provides a web UI for classroom orchestration.

Sub-modules
-----------
- :mod:`config` — server, storage, roles, grading, UI constants
- :mod:`store` — JSON-backed persistence layer
- :mod:`discovery` — course & module scanning
- :mod:`enrollment` — roster management
- :mod:`gradebook` — grade recording & calculation
- :mod:`announcements` — announcement posting & retrieval
- :mod:`calendar_events` — calendar event management
- :mod:`templates` — inline HTML templates
- :mod:`router` — URL pattern dispatch
- :mod:`handlers` — page / form / API handlers
- :mod:`middleware` — feature flags, permissions, logging
- :mod:`main` — HTTP server & CLI entry point
"""

from .main import DanvasHandler, start_server

# Data-layer functions
from .store import load_store, save_store
from .discovery import discover_courses, get_course_by_id, get_course_modules
from .enrollment import enroll_user, unenroll_user, get_roster
from .gradebook import record_grade, get_grades, calculate_course_grade
from .announcements import post_announcement, get_announcements
from .calendar_events import add_event, get_events

__all__ = [
    # server
    "DanvasHandler",
    "start_server",
    # store
    "load_store",
    "save_store",
    # discovery
    "discover_courses",
    "get_course_by_id",
    "get_course_modules",
    # enrollment
    "enroll_user",
    "unenroll_user",
    "get_roster",
    # gradebook
    "record_grade",
    "get_grades",
    "calculate_course_grade",
    # announcements
    "post_announcement",
    "get_announcements",
    # calendar
    "add_event",
    "get_events",
]
