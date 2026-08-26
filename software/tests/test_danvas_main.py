"""Tests for danvas.main — HTTP server and route handlers.

All business logic (gradebook, announcements, roster, calendar) runs
against real temporary data stores — no mocked data layer.
"""

import io
import json
from pathlib import Path

import pytest

from src.danvas.main import _parse_args, create_test_handler
from src.danvas.enrollment import enroll_user
from src.danvas.announcements import post_announcement, get_announcements
from src.danvas.gradebook import record_grade, get_grades
from src.danvas.calendar_events import get_events
from src.danvas.enrollment import get_roster
from src.danvas import handlers as _handlers


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────────────


@pytest.fixture
def data_dir(temp_dir):
    d = temp_dir / "danvas_state"
    d.mkdir()
    return d


@pytest.fixture
def repo_root(temp_dir):
    """Create a minimal repo with a demo course containing 2 modules."""
    root = temp_dir / "repo"
    dev = root / "course_development"
    dev.mkdir(parents=True)

    course = dev / "demo_course"
    course.mkdir()
    for num, name in [(1, "intro"), (2, "data")]:
        mod = course / f"{num:02d}_{name}"
        mod.mkdir()
        (mod / "module.md").write_text(f"# Module {num}\n", encoding="utf-8")

    return root


@pytest.fixture
def handler(repo_root, data_dir):
    """Create a DanvasHandler wired to temp directories (no mocks)."""
    h = create_test_handler(repo_root, data_dir)
    h.path = "/"
    return h


# ──────────────────────────────────────────────────────────────────────────────
# Route dispatch tests
# ──────────────────────────────────────────────────────────────────────────────


class TestRouteDispatch:
    """Route matching and dispatch."""

    def test_dashboard_route(self, handler):
        handler.path = "/"
        _handlers.handle_dashboard(handler)
        output = handler.wfile.getvalue().decode("utf-8")
        assert "My Courses" in output
        assert "demo_course" in output.lower() or "Demo Course" in output

    def test_course_detail_route(self, handler):
        _handlers.handle_course_detail(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "Module" in output
        assert "Intro" in output

    def test_course_not_found(self, handler):
        _handlers.handle_course_detail(handler, course_id="nonexistent")
        assert handler._response_status == 404

    def test_traversal_course_id_rejected_at_dispatch(self, handler):
        """A '..' course_id must be rejected before reaching any handler (404)."""
        handler.path = "/course/../roster"
        handler._dispatch("GET")
        assert handler._response_status == 404
        assert b"danvas_store.json" not in handler.wfile.getvalue()

    def test_traversal_course_id_rejected_by_validator(self):
        """validate_course_id_safe rejects path separators and '..'."""
        from src.danvas.handlers import validate_course_id_safe

        with pytest.raises(ValueError):
            validate_course_id_safe("..")
        with pytest.raises(ValueError):
            validate_course_id_safe("nested/course")
        with pytest.raises(ValueError):
            validate_course_id_safe("../etc")
        # Safe ids are allowed through.
        assert validate_course_id_safe("demo_course") == "demo_course"

    def test_module_detail_route(self, handler):
        _handlers.handle_module_detail(handler, course_id="demo_course", module_num="1")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "module.md" in output

    def test_module_not_found(self, handler):
        _handlers.handle_module_detail(handler, course_id="demo_course", module_num="99")
        assert handler._response_status == 404


# ──────────────────────────────────────────────────────────────────────────────
# Gradebook page tests
# ──────────────────────────────────────────────────────────────────────────────


class TestGradebookPage:
    """Gradebook GET/POST handlers."""

    def test_gradebook_page_renders(self, handler, data_dir):
        record_grade("demo_course", "Alice", "hw1", 90, 100, data_dir)
        _handlers.handle_gradebook(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "Gradebook" in output
        assert "Alice" in output

    def test_gradebook_post(self, handler, data_dir):
        form_body = "user_name=Bob&assignment=hw2&score=85&max_score=100"
        handler.headers = {"Content-Length": str(len(form_body))}
        handler.rfile = io.BytesIO(form_body.encode("utf-8"))
        _handlers.handle_gradebook_post(handler, course_id="demo_course")
        assert handler._response_status == 303

        # Verify the grade was persisted
        grades = get_grades("demo_course", "Bob", data_dir)
        assert "hw2" in grades
        assert grades["hw2"]["score"] == 85.0


# ──────────────────────────────────────────────────────────────────────────────
# Announcement page tests
# ──────────────────────────────────────────────────────────────────────────────


class TestAnnouncementsPage:
    """Announcement GET/POST handlers."""

    def test_announcement_page_renders(self, handler, data_dir):
        post_announcement("demo_course", "Welcome", "Hello class!", data_dir=data_dir)
        _handlers.handle_announcements(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "Welcome" in output
        assert "Hello class!" in output

    def test_announcement_post(self, handler, data_dir):
        form_body = "title=Update&body=Big+news&author=Prof"
        handler.headers = {"Content-Length": str(len(form_body))}
        handler.rfile = io.BytesIO(form_body.encode("utf-8"))
        _handlers.handle_announcements_post(handler, course_id="demo_course")
        assert handler._response_status == 303

        anns = get_announcements("demo_course", data_dir)
        assert anns[0]["title"] == "Update"


# ──────────────────────────────────────────────────────────────────────────────
# Calendar page tests
# ──────────────────────────────────────────────────────────────────────────────


class TestCalendarPage:
    """Calendar GET/POST handlers."""

    def test_calendar_page_renders(self, handler):
        _handlers.handle_calendar(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "Calendar" in output

    def test_calendar_post(self, handler, data_dir):
        form_body = "title=Midterm&date=2026-03-15&event_type=exam&description=In+class"
        handler.headers = {"Content-Length": str(len(form_body))}
        handler.rfile = io.BytesIO(form_body.encode("utf-8"))
        _handlers.handle_calendar_post(handler, course_id="demo_course")
        assert handler._response_status == 303

        events = get_events("demo_course", data_dir)
        assert events[0]["title"] == "Midterm"


# ──────────────────────────────────────────────────────────────────────────────
# Roster page tests
# ──────────────────────────────────────────────────────────────────────────────


class TestRosterPage:
    """Roster GET/POST handlers."""

    def test_roster_page_renders(self, handler, data_dir):
        enroll_user("demo_course", "Alice", "student", data_dir)
        _handlers.handle_roster(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        assert "Alice" in output
        assert "student" in output

    def test_roster_post(self, handler, data_dir):
        form_body = "user_name=Charlie&role=ta"
        handler.headers = {"Content-Length": str(len(form_body))}
        handler.rfile = io.BytesIO(form_body.encode("utf-8"))
        _handlers.handle_roster_post(handler, course_id="demo_course")
        assert handler._response_status == 303

        roster = get_roster("demo_course", data_dir)
        assert any(r["user_name"] == "Charlie" for r in roster)


# ──────────────────────────────────────────────────────────────────────────────
# JSON API tests
# ──────────────────────────────────────────────────────────────────────────────


class TestAPIEndpoints:
    """JSON API handlers."""

    def test_api_courses(self, handler):
        _handlers.handle_api_courses(handler)
        output = handler.wfile.getvalue().decode("utf-8")
        data = json.loads(output)
        assert "courses" in data
        assert any(c["id"] == "demo_course" for c in data["courses"])

    def test_api_grades(self, handler, data_dir):
        record_grade("demo_course", "Alice", "hw1", 95, 100, data_dir)
        _handlers.handle_api_grades(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        data = json.loads(output)
        assert data["course_id"] == "demo_course"
        assert "Alice" in data["grades"]

    def test_api_announcements(self, handler, data_dir):
        post_announcement("demo_course", "News", "Big update", data_dir=data_dir)
        _handlers.handle_api_announcements(handler, course_id="demo_course")
        output = handler.wfile.getvalue().decode("utf-8")
        data = json.loads(output)
        assert len(data["announcements"]) == 1


# ──────────────────────────────────────────────────────────────────────────────
# Security hardening tests
# ──────────────────────────────────────────────────────────────────────────────


class TestSecurityHardening:
    """Path traversal, authorization, and body-limit protections."""

    def test_insufficient_role_rejected_with_403(self, handler, data_dir):
        """A student principal cannot POST a grade (instructor-only action)."""
        handler.server.role = "student"
        handler.path = "/course/demo_course/gradebook"
        form = b"user_name=Alice&assignment=Quiz+1&score=88&max_score=100"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler._dispatch("POST")
        assert handler._response_status == 403
        # Nothing was written.
        grades = get_grades("demo_course", data_dir=data_dir)
        assert grades == {}

    def test_instructor_role_allowed(self, handler, data_dir):
        """An instructor principal can POST a grade (default role)."""
        handler.server.role = "instructor"
        handler.path = "/course/demo_course/gradebook"
        form = b"user_name=Bob&assignment=Quiz+1&score=77&max_score=100"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler._dispatch("POST")
        assert handler._response_status == 303
        grades = get_grades("demo_course", data_dir=data_dir)
        assert "Bob" in grades

    def test_oversized_body_rejected(self, handler, data_dir):
        """A POST body larger than MAX_POST_BODY must be rejected with 400."""
        handler.server.role = "instructor"
        handler.path = "/course/demo_course/gradebook"
        # Announce a huge content-length; _read_form rejects before reading.
        big = (
            b"user_name=Alice&assignment=Q&score=1&max_score=100" + b"&pad=" + b"x" * (1024 * 1024)
        )
        handler.rfile = io.BytesIO(big)
        # Only claim a length beyond the cap so the body is not read in full.
        from src.danvas import config

        handler.headers = {"Content-Length": str(config.MAX_POST_BODY + 1)}
        handler._dispatch("POST")
        assert handler._response_status == 400

    def test_invalid_content_length_rejected(self, handler):
        """A non-numeric Content-Length must yield a clean 400, not a crash."""
        handler.path = "/course/demo_course/roster"
        handler.rfile = io.BytesIO(b"user_name=Bob&role=student")
        handler.headers = {"Content-Length": "not-a-number"}
        handler._dispatch("POST")
        assert handler._response_status == 400


# ──────────────────────────────────────────────────────────────────────────────
# CLI argument parsing tests
# ──────────────────────────────────────────────────────────────────────────────


class TestCLI:
    """CLI argument parsing."""

    def test_default_args(self):
        args = _parse_args([])
        assert args.port == 8420
        assert args.host == "127.0.0.1"
        assert args.data_dir is None

    def test_custom_args(self):
        args = _parse_args(["--port", "9000", "--host", "0.0.0.0", "--repo-root", "/tmp"])
        assert args.port == 9000
        assert args.host == "0.0.0.0"
        assert args.repo_root == Path("/tmp")
