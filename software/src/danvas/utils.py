"""Data layer utilities for Danvas course management system.

Backward-compatibility re-export shim.  The canonical implementations live in
focused sub-modules (:mod:`danvas.store`, :mod:`danvas.discovery`,
:mod:`danvas.enrollment`, :mod:`danvas.gradebook`,
:mod:`danvas.announcements`, :mod:`danvas.calendar_events`); this module
re-exports the public data-layer functions so older imports keep working.

Prefer importing directly from the focused sub-modules:
- :mod:`danvas.store` — JSON persistence
- :mod:`danvas.discovery` — course & module scanning
- :mod:`danvas.enrollment` — roster management
- :mod:`danvas.gradebook` — grade recording & calculation
- :mod:`danvas.announcements` — announcement posting
- :mod:`danvas.calendar_events` — calendar event management
"""

from .store import load_store, save_store, store_transaction, validate_course_id
from .discovery import discover_courses, get_course_by_id, get_course_modules
from .enrollment import enroll_user, unenroll_user, get_roster
from .gradebook import record_grade, get_grades, calculate_course_grade
from .announcements import post_announcement, get_announcements
from .calendar_events import add_event, get_events

__all__ = [
    # store
    "load_store",
    "save_store",
    "store_transaction",
    "validate_course_id",
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
