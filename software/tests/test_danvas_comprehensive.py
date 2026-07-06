"""Comprehensive tests for Danvas — templates, edge cases, validation, integration.

Extends the base test_danvas_utils.py and test_danvas_main.py suites with
deeper coverage: template rendering, HTML escaping/XSS, input validation,
empty state handling, multi-course interactions, and API endpoint verification.

All business logic (gradebook, announcements, roster, calendar) runs
against real temporary data stores — no mocked data layer.
"""

import html
import io
import json

import pytest

from src.danvas import config, templates
from src.danvas.main import create_test_handler
from src.danvas.store import load_store, save_store
from src.danvas.discovery import discover_courses
from src.danvas.enrollment import enroll_user, get_roster
from src.danvas.gradebook import record_grade, get_grades, calculate_course_grade
from src.danvas.announcements import post_announcement, get_announcements
from src.danvas.calendar_events import get_events
from src.danvas import handlers as _handlers


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────────────


@pytest.fixture
def data_dir(tmp_path):
    """Temporary data directory for Danvas state."""
    d = tmp_path / "danvas_data"
    d.mkdir()
    return d


@pytest.fixture
def repo_root(tmp_path):
    """Create a minimal repo with two courses (one with modules, one empty)."""
    rr = tmp_path / "repo"
    dev = rr / "course_development"
    # Course A: 3 modules
    for i in range(1, 4):
        mod = dev / "test_course" / f"{i:02d}_module_{i}"
        mod.mkdir(parents=True)
        (mod / "module.md").write_text(f"# Module {i}")
        (mod / "questions.md").write_text("## Questions")
    # Course B: 0 modules
    (dev / "empty_course").mkdir(parents=True)
    return rr


@pytest.fixture
def handler(repo_root, data_dir):
    """Create a DanvasHandler wired to temp directories (no mocks)."""
    h = create_test_handler(repo_root, data_dir)
    h.path = "/"
    return h


def _wfile_text(handler) -> str:
    """Read the handler's wfile output as UTF-8 string."""
    return handler.wfile.getvalue().decode("utf-8")


def _reset_handler(handler):
    """Reset handler state for a new request (no mocks)."""
    handler.wfile = io.BytesIO()
    handler._response_status = None


# ──────────────────────────────────────────────────────────────────────────────
# Template rendering tests
# ──────────────────────────────────────────────────────────────────────────────


class TestTemplateRendering:
    """Verify that all templates produce valid HTML with expected content."""

    _COURSE = {"id": "c1", "title": "Course X", "path": "/tmp/c1",
               "module_count": 0, "description": ""}

    def test_dashboard_template_contains_css(self):
        html_out = templates.render_dashboard([])
        assert "<style>" in html_out
        assert "sidebar" in html_out

    def test_dashboard_template_shows_courses(self):
        courses = [
            {"id": "c1", "title": "Course One", "module_count": 5, "description": "Desc"},
            {"id": "c2", "title": "Course Two", "module_count": 0, "description": ""},
        ]
        html_out = templates.render_dashboard(courses)
        assert "Course One" in html_out
        assert "Course Two" in html_out
        assert "5 modules" in html_out
        assert "0 modules" in html_out
        assert "/course/c1" in html_out

    def test_dashboard_empty_state(self):
        html_out = templates.render_dashboard([])
        assert "My Courses" in html_out

    def test_course_detail_template(self):
        course = {"id": "c1", "title": "Test Course", "path": "/tmp/c1",
                  "module_count": 2, "description": "A test"}
        modules = [
            {"number": 1, "name": "Intro", "dir_name": "01_intro", "files": ["a.md"]},
            {"number": 2, "name": "Advanced", "dir_name": "02_adv", "files": ["b.md", "c.md"]},
        ]
        html_out = templates.render_course_detail(course, modules, [])
        assert "Test Course" in html_out
        assert "Intro" in html_out
        assert "Advanced" in html_out
        assert "1 files" in html_out or "1 file" in html_out

    def test_module_detail_template(self):
        course = {"id": "c1", "title": "Test", "path": "/tmp", "module_count": 1, "description": ""}
        module_info = {"number": 1, "name": "First", "dir_name": "01_first",
                       "files": ["module.md", "lab.md"], "path": "/tmp/01_first"}
        html_out = templates.render_module_detail(course, module_info)
        assert "Module 1: First" in html_out
        assert "module.md" in html_out
        assert "lab.md" in html_out

    def test_gradebook_template_empty(self):
        html_out = templates.render_gradebook(self._COURSE, {})
        assert "Gradebook" in html_out
        assert "Record Grade" in html_out

    def test_gradebook_template_with_data(self):
        grades = {
            "alice": {"hw1": {"score": 95, "max_score": 100, "percentage": 95.0, "updated_at": "2026-01-01T12:00:00"}},
        }
        html_out = templates.render_gradebook(self._COURSE, grades)
        assert "alice" in html_out
        assert "95" in html_out

    def test_announcements_template_empty(self):
        html_out = templates.render_announcements(self._COURSE, [])
        assert "Announcements" in html_out
        assert "Post Announcement" in html_out

    def test_announcements_template_with_data(self):
        announcements = [
            {"title": "Welcome!", "body": "Hello class", "author": "Prof", "posted_at": "2026-01-01T10:00:00"},
        ]
        html_out = templates.render_announcements(self._COURSE, announcements)
        assert "Welcome!" in html_out
        assert "Hello class" in html_out

    def test_calendar_template_empty(self):
        html_out = templates.render_calendar(self._COURSE, [])
        assert "Calendar" in html_out
        assert "Add Event" in html_out

    def test_calendar_template_with_events(self):
        events = [
            {"title": "Midterm", "date": "2026-03-15", "description": "Ch 1-5",
             "event_type": "exam", "created_at": "2026-01-01T12:00:00"},
        ]
        html_out = templates.render_calendar(self._COURSE, events)
        assert "Midterm" in html_out
        assert "2026-03-15" in html_out

    def test_roster_template_empty(self):
        html_out = templates.render_roster(self._COURSE, [])
        assert "Roster" in html_out
        assert "Enroll User" in html_out

    def test_roster_template_with_users(self):
        roster = [
            {"user_name": "alice", "role": "student", "enrolled_at": "2026-01-01T10:00:00"},
            {"user_name": "bob", "role": "ta", "enrolled_at": "2026-01-02T10:00:00"},
        ]
        html_out = templates.render_roster(self._COURSE, roster)
        assert "alice" in html_out
        assert "bob" in html_out
        assert "STUDENT" in html_out or "student" in html_out.lower()

    def test_404_template(self):
        html_out = templates.render_404()
        assert "Page Not Found" in html_out
        assert "Back to Dashboard" in html_out

    def test_all_templates_produce_valid_html_structure(self):
        """Every render function should produce opening and closing html/body tags."""
        _c = {"id": "x", "title": "X", "path": "/t", "module_count": 0, "description": ""}
        outputs = [
            templates.render_dashboard([]),
            templates.render_course_detail(_c, [], []),
            templates.render_gradebook(_c, {}),
            templates.render_announcements(_c, []),
            templates.render_calendar(_c, []),
            templates.render_roster(_c, []),
            templates.render_404(),
        ]
        for out in outputs:
            assert "<html" in out.lower()
            assert "</html>" in out.lower()
            assert "<body" in out.lower()


# ──────────────────────────────────────────────────────────────────────────────
# XSS / HTML escaping tests
# ──────────────────────────────────────────────────────────────────────────────


class TestHTMLEscaping:
    """Verify that user-provided data is escaped in HTML output."""

    def test_course_title_escaped_in_dashboard(self):
        xss = '<script>alert("XSS")</script>'
        courses = [{"id": "x", "title": xss, "module_count": 0, "description": ""}]
        html_out = templates.render_dashboard(courses)
        assert "<script>" not in html_out or html.escape(xss) in html_out

    def test_announcement_body_escaped(self):
        _c = {"id": "c1", "title": "C", "path": "/t", "module_count": 0, "description": ""}
        xss_body = '<img onerror="alert(1)" src=x>'
        announcements = [
            {"title": "Test", "body": xss_body, "author": "A", "posted_at": "2026-01-01T00:00:00"},
        ]
        html_out = templates.render_announcements(_c, announcements)
        # The raw XSS tag should not appear unescaped
        assert 'onerror="alert(1)"' not in html_out or html.escape(xss_body) in html_out

    def test_roster_username_escaped(self):
        _c = {"id": "c1", "title": "C", "path": "/t", "module_count": 0, "description": ""}
        xss_name = '"><script>alert(1)</script>'
        roster = [{"user_name": xss_name, "role": "student", "enrolled_at": "2026-01-01T00:00:00"}]
        html_out = templates.render_roster(_c, roster)
        assert "<script>alert(1)</script>" not in html_out or html.escape(xss_name) in html_out


# ──────────────────────────────────────────────────────────────────────────────
# Edge case tests — data layer
# ──────────────────────────────────────────────────────────────────────────────


class TestEdgeCases:
    """Edge cases for data layer operations."""

    def test_special_chars_in_course_id(self, data_dir):
        """Course IDs with hyphens should work for store paths."""
        store = load_store("ai-philosophy", data_dir)
        assert "enrollments" in store
        save_store("ai-philosophy", store, data_dir)
        reloaded = load_store("ai-philosophy", data_dir)
        assert reloaded == store

    def test_empty_string_enrollment(self, data_dir):
        """Enrolling an empty-string user should still work."""
        record = enroll_user("test", "", "student", data_dir)
        assert record["user_name"] == ""

    def test_zero_max_score_grade(self, data_dir):
        """Recording a grade with max_score=0 should not crash."""
        entry = record_grade("test", "alice", "hw", 0, 0.0, data_dir)
        assert entry["percentage"] == 0.0

    def test_very_long_assignment_name(self, data_dir):
        """Long assignment names should be stored correctly."""
        long_name = "A" * 1000
        entry = record_grade("test", "alice", long_name, 50, 100.0, data_dir)
        grades = get_grades("test", "alice", data_dir)
        assert long_name in grades

    def test_unicode_in_announcement(self, data_dir):
        """Unicode characters should be handled correctly."""
        post_announcement("test", "🎓 Welcome", "Héllo wörld 日本語", "Prof", data_dir)
        anns = get_announcements("test", data_dir)
        assert anns[0]["title"] == "🎓 Welcome"
        assert "日本語" in anns[0]["body"]

    def test_concurrent_saves_dont_corrupt(self, data_dir):
        """Multiple rapid saves should not corrupt the store."""
        for i in range(10):
            enroll_user("test", f"user_{i}", "student", data_dir)
        roster = get_roster("test", data_dir)
        assert len(roster) == 10

    def test_empty_calendar_returns_empty_list(self, data_dir):
        events = get_events("nonexistent", data_dir)
        assert events == []

    def test_multiple_grades_same_assignment(self, data_dir):
        """Recording a grade for the same assignment should update, not duplicate."""
        record_grade("test", "alice", "hw1", 80, 100, data_dir)
        record_grade("test", "alice", "hw1", 95, 100, data_dir)
        grades = get_grades("test", "alice", data_dir)
        assert grades["hw1"]["score"] == 95  # Updated, not duplicated

    def test_course_grade_calculation_weighted(self, data_dir):
        """Multiple assignments with different max scores."""
        record_grade("test", "alice", "quiz", 8, 10, data_dir)
        record_grade("test", "alice", "exam", 90, 100, data_dir)
        result = calculate_course_grade("test", "alice", data_dir)
        assert result["assignments_count"] == 2
        assert result["average_percentage"] > 0

    def test_discover_courses_ignores_hidden_dirs(self, repo_root):
        """Directories starting with . should be excluded."""
        hidden = repo_root / "course_development" / ".hidden_dir"
        hidden.mkdir(parents=True)
        courses = discover_courses(repo_root)
        ids = {c["id"] for c in courses}
        assert ".hidden_dir" not in ids


# ──────────────────────────────────────────────────────────────────────────────
# Input validation tests
# ──────────────────────────────────────────────────────────────────────────────


class TestInputValidation:
    """Verify input validation on data layer operations."""

    def test_invalid_role_raises_valueerror(self, data_dir):
        with pytest.raises(ValueError, match="Invalid role"):
            enroll_user("test", "alice", "superadmin", data_dir)

    def test_announcement_body_too_long_raises(self, data_dir):
        with pytest.raises(ValueError, match="exceeds"):
            post_announcement(
                "test", "Long", "x" * (config.MAX_ANNOUNCEMENT_LENGTH + 1), "A", data_dir
            )

    def test_valid_roles_all_accepted(self, data_dir):
        """All defined roles should be accepted without error."""
        for role in config.ROLES:
            record = enroll_user("test", f"user_{role}", role, data_dir)
            assert record["role"] == role


# ──────────────────────────────────────────────────────────────────────────────
# Multi-course isolation tests
# ──────────────────────────────────────────────────────────────────────────────


class TestMultiCourseIsolation:
    """Data in one course should not leak into another."""

    def test_enrollments_isolated(self, data_dir):
        enroll_user("course_a", "alice", "student", data_dir)
        enroll_user("course_b", "bob", "student", data_dir)
        assert len(get_roster("course_a", data_dir)) == 1
        assert len(get_roster("course_b", data_dir)) == 1
        assert get_roster("course_a", data_dir)[0]["user_name"] == "alice"

    def test_grades_isolated(self, data_dir):
        record_grade("course_a", "alice", "hw1", 90, 100, data_dir)
        record_grade("course_b", "bob", "hw1", 80, 100, data_dir)
        assert "alice" in get_grades("course_a", data_dir=data_dir)
        assert "alice" not in get_grades("course_b", data_dir=data_dir)

    def test_announcements_isolated(self, data_dir):
        post_announcement("course_a", "A1", "Body A", "Prof", data_dir)
        post_announcement("course_b", "B1", "Body B", "Prof", data_dir)
        assert len(get_announcements("course_a", data_dir)) == 1
        assert get_announcements("course_a", data_dir)[0]["title"] == "A1"


# ──────────────────────────────────────────────────────────────────────────────
# Config tests
# ──────────────────────────────────────────────────────────────────────────────


class TestConfig:
    """Verify configuration constants and defaults."""

    def test_roles_defined(self):
        assert "student" in config.ROLES
        assert "instructor" in config.ROLES
        assert "ta" in config.ROLES

    def test_grading_schema_descending(self):
        thresholds = list(config.DEFAULT_GRADING_SCHEMA.values())
        assert thresholds == sorted(thresholds, reverse=True)

    def test_empty_store_has_required_keys(self):
        store = config.EMPTY_STORE
        assert "enrollments" in store
        assert "grades" in store
        assert "announcements" in store
        assert "calendar_events" in store

    def test_feature_flags_are_booleans(self):
        for key, val in config.FEATURE_FLAGS.items():
            assert isinstance(val, bool), f"Feature flag {key} is not a boolean"

    def test_danvas_port_is_int(self):
        assert isinstance(config.DANVAS_PORT, int)
        assert config.DANVAS_PORT > 0


# ──────────────────────────────────────────────────────────────────────────────
# API endpoint integration tests
# ──────────────────────────────────────────────────────────────────────────────


class TestAPIIntegration:
    """Full-cycle integration: POST data via handler, retrieve via API."""

    def test_gradebook_roundtrip(self, handler, data_dir):
        """POST a grade then verify it shows in the gradebook page."""
        # Post a grade
        form = b"user_name=Alice&assignment=Quiz+1&score=88&max_score=100"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler.path = "/course/test_course/gradebook"
        _handlers.handle_gradebook_post(handler, course_id="test_course")
        assert handler._response_status == 303

        # Render the gradebook page
        _reset_handler(handler)
        _handlers.handle_gradebook(handler, course_id="test_course")
        out = _wfile_text(handler)
        assert "Alice" in out
        assert "Quiz 1" in out
        assert "88" in out

    def test_announcement_roundtrip(self, handler, data_dir):
        """POST an announcement then verify it appears."""
        form = b"title=Important&author=Dean&body=Read+this"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler.path = "/course/test_course/announcements"
        _handlers.handle_announcements_post(handler, course_id="test_course")
        assert handler._response_status == 303

        _reset_handler(handler)
        _handlers.handle_announcements(handler, course_id="test_course")
        out = _wfile_text(handler)
        assert "Important" in out
        assert "Read this" in out

    def test_calendar_roundtrip(self, handler, data_dir):
        """POST a calendar event then verify it appears."""
        form = b"title=Lab+Due&date=2026-06-01&event_type=assignment&description=Submit+lab"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler.path = "/course/test_course/calendar"
        _handlers.handle_calendar_post(handler, course_id="test_course")
        assert handler._response_status == 303

        _reset_handler(handler)
        _handlers.handle_calendar(handler, course_id="test_course")
        out = _wfile_text(handler)
        assert "Lab Due" in out
        assert "2026-06-01" in out

    def test_roster_roundtrip(self, handler, data_dir):
        """POST an enrollment then verify it appears."""
        form = b"user_name=Charlie&role=student"
        handler.rfile = io.BytesIO(form)
        handler.headers = {"Content-Length": str(len(form))}
        handler.path = "/course/test_course/roster"
        _handlers.handle_roster_post(handler, course_id="test_course")

        _reset_handler(handler)
        _handlers.handle_roster(handler, course_id="test_course")
        out = _wfile_text(handler)
        assert "Charlie" in out

    def test_api_courses_json_structure(self, handler):
        """API /api/courses should return valid JSON with expected keys."""
        _handlers.handle_api_courses(handler)
        out = _wfile_text(handler)
        data = json.loads(out)
        assert "courses" in data
        assert isinstance(data["courses"], list)
        for course in data["courses"]:
            assert "id" in course
            assert "title" in course
            assert "module_count" in course

    def test_api_grades_json_structure(self, handler, data_dir):
        """API /api/grades should return valid JSON after recording grades."""
        record_grade("test_course", "alice", "hw1", 90, 100, data_dir)
        _handlers.handle_api_grades(handler, course_id="test_course")
        out = _wfile_text(handler)
        data = json.loads(out)
        assert "grades" in data
        assert "alice" in data["grades"]

    def test_api_announcements_json_structure(self, handler, data_dir):
        """API /api/announcements should return valid JSON."""
        post_announcement("test_course", "Hello", "World", "Prof", data_dir)
        _handlers.handle_api_announcements(handler, course_id="test_course")
        out = _wfile_text(handler)
        data = json.loads(out)
        assert "announcements" in data
        assert isinstance(data["announcements"], list)
        assert data["announcements"][0]["title"] == "Hello"


# ──────────────────────────────────────────────────────────────────────────────
# Route dispatch edge cases
# ──────────────────────────────────────────────────────────────────────────────


class TestRouteEdgeCases:
    """Edge cases for route matching and dispatch."""

    def test_trailing_slash_dashboard(self, handler):
        handler.path = "/"
        handler._dispatch("GET")
        out = _wfile_text(handler)
        assert "My Courses" in out

    def test_empty_course_has_no_modules(self, handler):
        _handlers.handle_course_detail(handler, course_id="empty_course")
        out = _wfile_text(handler)
        assert "No modules found" in out

    def test_nonexistent_course_returns_404(self, handler):
        _handlers.handle_course_detail(handler, course_id="nonexistent_xyz")
        out = _wfile_text(handler)
        assert "Page Not Found" in out

    def test_nonexistent_module_returns_404(self, handler):
        _handlers.handle_module_detail(handler,
            course_id="test_course", module_num="99"
        )
        out = _wfile_text(handler)
        assert "Page Not Found" in out
