"""URL routing for the Danvas HTTP server.

Compiles URL patterns at import time and provides a ``dispatch``
function that matches (method, path) to handler names with captured
keyword arguments.
"""

import re
from typing import Any, Dict, List, Optional, Tuple

# ──────────────────────────────────────────────────────────────────────────────
# Route table  (compiled once at import time)
# ──────────────────────────────────────────────────────────────────────────────

ROUTES: List[Tuple[str, "re.Pattern[str]", str]] = [
    # (method, pattern, handler_name)
    # ── Dashboard ─────────────────────────────────────────────────────────
    ("GET", re.compile(r"^/$"), "handle_dashboard"),
    # ── Course pages ──────────────────────────────────────────────────────
    ("GET", re.compile(r"^/course/(?P<course_id>[^/]+)$"), "handle_course_detail"),
    (
        "GET",
        re.compile(r"^/course/(?P<course_id>[^/]+)/module/(?P<module_num>\d+)$"),
        "handle_module_detail",
    ),
    # ── Gradebook ─────────────────────────────────────────────────────────
    ("GET", re.compile(r"^/course/(?P<course_id>[^/]+)/gradebook$"), "handle_gradebook"),
    ("POST", re.compile(r"^/course/(?P<course_id>[^/]+)/gradebook$"), "handle_gradebook_post"),
    # ── Announcements ─────────────────────────────────────────────────────
    ("GET", re.compile(r"^/course/(?P<course_id>[^/]+)/announcements$"), "handle_announcements"),
    (
        "POST",
        re.compile(r"^/course/(?P<course_id>[^/]+)/announcements$"),
        "handle_announcements_post",
    ),
    # ── Calendar ──────────────────────────────────────────────────────────
    ("GET", re.compile(r"^/course/(?P<course_id>[^/]+)/calendar$"), "handle_calendar"),
    ("POST", re.compile(r"^/course/(?P<course_id>[^/]+)/calendar$"), "handle_calendar_post"),
    # ── Roster ────────────────────────────────────────────────────────────
    ("GET", re.compile(r"^/course/(?P<course_id>[^/]+)/roster$"), "handle_roster"),
    ("POST", re.compile(r"^/course/(?P<course_id>[^/]+)/roster$"), "handle_roster_post"),
    # ── JSON API ──────────────────────────────────────────────────────────
    ("GET", re.compile(r"^/api/courses$"), "handle_api_courses"),
    ("GET", re.compile(r"^/api/course/(?P<course_id>[^/]+)/grades$"), "handle_api_grades"),
    (
        "GET",
        re.compile(r"^/api/course/(?P<course_id>[^/]+)/announcements$"),
        "handle_api_announcements",
    ),
]


def dispatch(method: str, path: str) -> Optional[Tuple[str, Dict[str, Any]]]:
    """Match *method* + *path* against the route table.

    Args:
        method: HTTP method (GET, POST, …).
        path: URL path (already stripped of trailing slash).

    Returns:
        ``(handler_name, kwargs)`` on match, or ``None`` if no route
        matches.
    """
    for route_method, pattern, handler_name in ROUTES:
        if route_method != method:
            continue
        match = pattern.match(path)
        if match:
            return handler_name, match.groupdict()
    return None
