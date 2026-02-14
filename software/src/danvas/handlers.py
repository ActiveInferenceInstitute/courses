"""Page, form, and API request handlers for Danvas.

Each handler is a standalone function that receives a *context* object
(the ``DanvasHandler`` instance) plus any URL-captured keyword
arguments.  This keeps business logic separate from HTTP plumbing.
"""

from pathlib import Path
from typing import Any, Dict, Optional

from . import config, templates
from .announcements import get_announcements, post_announcement
from .calendar_events import add_event, get_events
from .discovery import discover_courses, get_course_by_id, get_course_modules
from .enrollment import enroll_user, get_roster
from .gradebook import get_grades, record_grade

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


logger = get_logger("danvas.handlers")


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────


def _get_course(ctx: Any, course_id: str) -> Optional[Dict[str, Any]]:
    """Look up a course or return ``None``."""
    return get_course_by_id(course_id, ctx.repo_root)


def _send_404(ctx: Any) -> None:
    """Send the 404 page via the context."""
    ctx._send_html(templates.render_404(), status=404)


# ──────────────────────────────────────────────────────────────────────────────
# Page handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_dashboard(ctx: Any) -> None:
    """Render the main dashboard with all discovered courses."""
    courses = discover_courses(ctx.repo_root)
    ctx._send_html(templates.render_dashboard(courses))


def handle_course_detail(ctx: Any, course_id: str) -> None:
    """Render a course's detail / modules page."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    modules = get_course_modules(Path(course["path"]))
    announcements = get_announcements(course_id, ctx.data_dir)
    ctx._send_html(templates.render_course_detail(course, modules, announcements))


def handle_module_detail(ctx: Any, course_id: str, module_num: str) -> None:
    """Render a single module's file listing."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    modules = get_course_modules(Path(course["path"]))
    target = None
    for m in modules:
        if m["number"] == int(module_num):
            target = m
            break
    if not target:
        _send_404(ctx)
        return
    ctx._send_html(templates.render_module_detail(course, target))


# ──────────────────────────────────────────────────────────────────────────────
# Gradebook handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_gradebook(ctx: Any, course_id: str) -> None:
    """Render the gradebook page for a course."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    grades = get_grades(course_id, data_dir=ctx.data_dir)
    ctx._send_html(templates.render_gradebook(course, grades))


def handle_gradebook_post(ctx: Any, course_id: str) -> None:
    """Process a gradebook form POST and redirect."""
    form = ctx._read_form()
    record_grade(
        course_id,
        user_name=form.get("user_name", ""),
        assignment=form.get("assignment", ""),
        score=float(form.get("score", 0)),
        max_score=float(form.get("max_score", 100)),
        data_dir=ctx.data_dir,
    )
    ctx._redirect(f"/course/{course_id}/gradebook")


# ──────────────────────────────────────────────────────────────────────────────
# Announcement handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_announcements(ctx: Any, course_id: str) -> None:
    """Render announcements page for a course."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    ann = get_announcements(course_id, ctx.data_dir)
    ctx._send_html(templates.render_announcements(course, ann))


def handle_announcements_post(ctx: Any, course_id: str) -> None:
    """Process an announcement form POST and redirect."""
    form = ctx._read_form()
    post_announcement(
        course_id,
        title=form.get("title", ""),
        body=form.get("body", ""),
        author=form.get("author", "Instructor"),
        data_dir=ctx.data_dir,
    )
    ctx._redirect(f"/course/{course_id}/announcements")


# ──────────────────────────────────────────────────────────────────────────────
# Calendar handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_calendar(ctx: Any, course_id: str) -> None:
    """Render the calendar page for a course."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    events = get_events(course_id, ctx.data_dir)
    ctx._send_html(templates.render_calendar(course, events))


def handle_calendar_post(ctx: Any, course_id: str) -> None:
    """Process a calendar event form POST and redirect."""
    form = ctx._read_form()
    add_event(
        course_id,
        title=form.get("title", ""),
        date=form.get("date", ""),
        description=form.get("description", ""),
        event_type=form.get("event_type", "other"),
        data_dir=ctx.data_dir,
    )
    ctx._redirect(f"/course/{course_id}/calendar")


# ──────────────────────────────────────────────────────────────────────────────
# Roster handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_roster(ctx: Any, course_id: str) -> None:
    """Render the roster page for a course."""
    course = _get_course(ctx, course_id)
    if not course:
        _send_404(ctx)
        return
    roster = get_roster(course_id, ctx.data_dir)
    ctx._send_html(templates.render_roster(course, roster))


def handle_roster_post(ctx: Any, course_id: str) -> None:
    """Process a roster enrollment form POST and redirect."""
    form = ctx._read_form()
    enroll_user(
        course_id,
        user_name=form.get("user_name", ""),
        role=form.get("role", "student"),
        data_dir=ctx.data_dir,
    )
    ctx._redirect(f"/course/{course_id}/roster")


# ──────────────────────────────────────────────────────────────────────────────
# JSON API handlers
# ──────────────────────────────────────────────────────────────────────────────


def handle_api_courses(ctx: Any) -> None:
    """Return all discovered courses as JSON."""
    courses = discover_courses(ctx.repo_root)
    ctx._send_json({"courses": courses})


def handle_api_grades(ctx: Any, course_id: str) -> None:
    """Return grades for a course as JSON."""
    grades = get_grades(course_id, data_dir=ctx.data_dir)
    ctx._send_json({"course_id": course_id, "grades": grades})


def handle_api_announcements(ctx: Any, course_id: str) -> None:
    """Return announcements for a course as JSON."""
    ann = get_announcements(course_id, ctx.data_dir)
    ctx._send_json({"course_id": course_id, "announcements": ann})
