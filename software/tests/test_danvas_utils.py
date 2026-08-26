"""Tests for danvas.utils — data layer operations."""

import json

import pytest

from src.danvas import config
from src.danvas.store import load_store, save_store
from src.danvas.discovery import discover_courses, get_course_modules
from src.danvas.enrollment import enroll_user, unenroll_user, get_roster
from src.danvas.gradebook import record_grade, get_grades, calculate_course_grade
from src.danvas.announcements import post_announcement, get_announcements
from src.danvas.calendar_events import add_event, get_events


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────────────


@pytest.fixture
def data_dir(temp_dir):
    """Temporary data directory for Danvas state."""
    d = temp_dir / "danvas_state"
    d.mkdir()
    return d


@pytest.fixture
def repo_root(temp_dir):
    """Create a minimal repo structure with course_development/."""
    root = temp_dir / "repo"
    dev = root / "course_development"
    dev.mkdir(parents=True)

    # Create a sample course
    course = dev / "test_course"
    course.mkdir()
    for num, name in [(1, "intro"), (2, "basics"), (3, "advanced")]:
        mod = course / f"{num:02d}_{name}"
        mod.mkdir()
        (mod / "module.md").write_text(f"# Module {num}\n\nContent.\n", encoding="utf-8")
        (mod / "practice_quiz.md").write_text(f"# Quiz {num}\n", encoding="utf-8")

    # Create a second course
    course2 = dev / "another_course"
    course2.mkdir()
    (course2 / "01_topic").mkdir()
    (course2 / "01_topic" / "module.md").write_text("# Topic\n", encoding="utf-8")

    return root


# ──────────────────────────────────────────────────────────────────────────────
# Store tests
# ──────────────────────────────────────────────────────────────────────────────


class TestStore:
    """JSON store load/save."""

    def test_load_empty_returns_defaults(self, data_dir):
        store = load_store("nonexistent", data_dir)
        assert "enrollments" in store
        assert "grades" in store
        assert "announcements" in store
        assert "calendar_events" in store
        assert store["enrollments"] == []

    def test_save_and_load_roundtrip(self, data_dir):
        store = {
            "enrollments": [{"name": "Alice"}],
            "grades": {},
            "announcements": [],
            "calendar_events": [],
        }
        save_store("test_course", store, data_dir)
        loaded = load_store("test_course", data_dir)
        assert loaded["enrollments"][0]["name"] == "Alice"

    def test_save_creates_directories(self, data_dir):
        save_store(
            "nested_course",
            {"enrollments": [], "grades": {}, "announcements": [], "calendar_events": []},
            data_dir,
        )
        assert (data_dir / "nested_course" / config.STORE_FILENAME).exists()

    def test_save_rejects_path_traversal_course_id(self, data_dir):
        """A course_id containing path separators or '..' must never escape data_dir."""
        with pytest.raises(ValueError):
            save_store(
                "nested/course",
                {"enrollments": [], "grades": {}, "announcements": [], "calendar_events": []},
                data_dir,
            )
        with pytest.raises(ValueError):
            save_store(
                "..",
                {"enrollments": [], "grades": {}, "announcements": [], "calendar_events": []},
                data_dir,
            )
        with pytest.raises(ValueError):
            save_store(
                "../etc",
                {"enrollments": [], "grades": {}, "announcements": [], "calendar_events": []},
                data_dir,
            )
        # Nothing may have been written outside the data dir.
        assert not (data_dir.parent / "danvas_store.json").exists()

    def test_load_persisted_data(self, data_dir):
        # Manually write JSON
        course_dir = data_dir / "manual_course"
        course_dir.mkdir(parents=True)
        store_path = course_dir / config.STORE_FILENAME
        store_path.write_text(
            json.dumps(
                {
                    "enrollments": [{"user": "Bob"}],
                    "grades": {},
                    "announcements": [],
                    "calendar_events": [],
                }
            ),
            encoding="utf-8",
        )
        loaded = load_store("manual_course", data_dir)
        assert loaded["enrollments"][0]["user"] == "Bob"

    def test_corrupt_store_falls_back_to_empty(self, data_dir):
        """A truncated/corrupt store must fall back to empty state, not crash."""
        course_dir = data_dir / "corrupt_course"
        course_dir.mkdir(parents=True)
        (course_dir / config.STORE_FILENAME).write_text("{not valid json!!", encoding="utf-8")
        loaded = load_store("corrupt_course", data_dir)
        assert loaded["enrollments"] == []
        assert "grades" in loaded
        # A subsequent write still works and replaces the corrupt file.
        save_store(
            "corrupt_course",
            {
                "enrollments": [{"name": "A"}],
                "grades": {},
                "announcements": [],
                "calendar_events": [],
            },
            data_dir,
        )
        reloaded = load_store("corrupt_course", data_dir)
        assert reloaded["enrollments"][0]["name"] == "A"

    def test_store_transaction_persists_mutation(self, data_dir):
        """store_transaction serializes a load-modify-save cycle."""
        from src.danvas.store import store_transaction

        with store_transaction("txn_course", data_dir) as store:
            store["enrollments"].append({"name": "Carol", "id": "x"})
        loaded = load_store("txn_course", data_dir)
        assert loaded["enrollments"][0]["name"] == "Carol"


# ──────────────────────────────────────────────────────────────────────────────
# Course discovery tests
# ──────────────────────────────────────────────────────────────────────────────


class TestCourseDiscovery:
    """Course discovery from directory structure."""

    def test_discover_courses_finds_all(self, repo_root):
        courses = discover_courses(repo_root)
        ids = {c["id"] for c in courses}
        assert "test_course" in ids
        assert "another_course" in ids

    def test_discover_courses_counts_modules(self, repo_root):
        courses = discover_courses(repo_root)
        test_course = next(c for c in courses if c["id"] == "test_course")
        assert test_course["module_count"] == 3

    def test_discover_courses_missing_dir(self, temp_dir):
        courses = discover_courses(temp_dir / "nonexistent")
        assert courses == []

    def test_get_course_modules(self, repo_root):
        course_path = repo_root / "course_development" / "test_course"
        modules = get_course_modules(course_path)
        assert len(modules) == 3
        assert modules[0]["number"] == 1
        assert modules[0]["name"] == "Intro"
        assert "module.md" in modules[0]["files"]

    def test_get_course_modules_sorted(self, repo_root):
        course_path = repo_root / "course_development" / "test_course"
        modules = get_course_modules(course_path)
        numbers = [m["number"] for m in modules]
        assert numbers == [1, 2, 3]


# ──────────────────────────────────────────────────────────────────────────────
# Enrollment tests
# ──────────────────────────────────────────────────────────────────────────────


class TestEnrollment:
    """Enrollment CRUD operations."""

    def test_enroll_user(self, data_dir):
        record = enroll_user("test_course", "Alice", "student", data_dir)
        assert record["user_name"] == "Alice"
        assert record["role"] == "student"
        assert "id" in record
        assert "enrolled_at" in record

    def test_enroll_duplicate_returns_existing(self, data_dir):
        r1 = enroll_user("test_course", "Alice", "student", data_dir)
        r2 = enroll_user("test_course", "Alice", "student", data_dir)
        assert r1["id"] == r2["id"]

    def test_enroll_invalid_role_raises(self, data_dir):
        with pytest.raises(ValueError, match="Invalid role"):
            enroll_user("test_course", "Bob", "admin", data_dir)

    def test_unenroll_user(self, data_dir):
        enroll_user("test_course", "Alice", "student", data_dir)
        assert unenroll_user("test_course", "Alice", data_dir) is True
        roster = get_roster("test_course", data_dir)
        assert len(roster) == 0

    def test_unenroll_nonexistent(self, data_dir):
        assert unenroll_user("test_course", "Ghost", data_dir) is False

    def test_get_roster(self, data_dir):
        enroll_user("test_course", "Alice", "student", data_dir)
        enroll_user("test_course", "Bob", "ta", data_dir)
        roster = get_roster("test_course", data_dir)
        assert len(roster) == 2
        names = {r["user_name"] for r in roster}
        assert names == {"Alice", "Bob"}


# ──────────────────────────────────────────────────────────────────────────────
# Gradebook tests
# ──────────────────────────────────────────────────────────────────────────────


class TestGradebook:
    """Gradebook operations."""

    def test_record_grade(self, data_dir):
        entry = record_grade("test_course", "Alice", "hw1", 95, 100, data_dir)
        assert entry["score"] == 95
        assert entry["max_score"] == 100
        assert entry["percentage"] == 95.0

    def test_record_grade_updates_existing(self, data_dir):
        record_grade("test_course", "Alice", "hw1", 80, 100, data_dir)
        entry = record_grade("test_course", "Alice", "hw1", 95, 100, data_dir)
        assert entry["score"] == 95

    def test_get_grades_all_students(self, data_dir):
        record_grade("test_course", "Alice", "hw1", 90, 100, data_dir)
        record_grade("test_course", "Bob", "hw1", 85, 100, data_dir)
        grades = get_grades("test_course", data_dir=data_dir)
        assert "Alice" in grades
        assert "Bob" in grades

    def test_get_grades_single_student(self, data_dir):
        record_grade("test_course", "Alice", "hw1", 90, 100, data_dir)
        record_grade("test_course", "Alice", "hw2", 85, 100, data_dir)
        grades = get_grades("test_course", "Alice", data_dir)
        assert "hw1" in grades
        assert "hw2" in grades
        assert len(grades) == 2

    def test_get_grades_nonexistent_student(self, data_dir):
        grades = get_grades("test_course", "Nobody", data_dir)
        assert grades == {}

    def test_calculate_course_grade(self, data_dir):
        record_grade("test_course", "Alice", "hw1", 95, 100, data_dir)
        record_grade("test_course", "Alice", "hw2", 85, 100, data_dir)
        result = calculate_course_grade("test_course", "Alice", data_dir)
        assert result["average_percentage"] == 90.0
        assert result["letter_grade"] == "A-"
        assert result["assignments_count"] == 2

    def test_calculate_course_grade_no_assignments(self, data_dir):
        result = calculate_course_grade("test_course", "Nobody", data_dir)
        assert result["letter_grade"] == "N/A"
        assert result["assignments_count"] == 0


# ──────────────────────────────────────────────────────────────────────────────
# Announcement tests
# ──────────────────────────────────────────────────────────────────────────────


class TestAnnouncements:
    """Announcement operations."""

    def test_post_announcement(self, data_dir):
        record = post_announcement("test_course", "Welcome", "Hello class!", data_dir=data_dir)
        assert record["title"] == "Welcome"
        assert record["body"] == "Hello class!"
        assert "id" in record

    def test_announcements_newest_first(self, data_dir):
        post_announcement("test_course", "First", "Content 1", data_dir=data_dir)
        post_announcement("test_course", "Second", "Content 2", data_dir=data_dir)
        anns = get_announcements("test_course", data_dir)
        assert anns[0]["title"] == "Second"
        assert anns[1]["title"] == "First"

    def test_announcement_body_too_long(self, data_dir):
        long_body = "x" * (config.MAX_ANNOUNCEMENT_LENGTH + 1)
        with pytest.raises(ValueError, match="exceeds"):
            post_announcement("test_course", "Long", long_body, data_dir=data_dir)

    def test_get_announcements_empty(self, data_dir):
        anns = get_announcements("test_course", data_dir)
        assert anns == []


# ──────────────────────────────────────────────────────────────────────────────
# Calendar tests
# ──────────────────────────────────────────────────────────────────────────────


class TestCalendar:
    """Calendar event operations."""

    def test_add_event(self, data_dir):
        record = add_event("test_course", "Midterm", "2026-03-15", "In class", "exam", data_dir)
        assert record["title"] == "Midterm"
        assert record["date"] == "2026-03-15"
        assert record["event_type"] == "exam"

    def test_events_sorted_by_date(self, data_dir):
        add_event("test_course", "Final", "2026-05-01", data_dir=data_dir)
        add_event("test_course", "Midterm", "2026-03-15", data_dir=data_dir)
        add_event("test_course", "Quiz 1", "2026-02-20", data_dir=data_dir)
        events = get_events("test_course", data_dir)
        dates = [e["date"] for e in events]
        assert dates == ["2026-02-20", "2026-03-15", "2026-05-01"]

    def test_get_events_empty(self, data_dir):
        events = get_events("test_course", data_dir)
        assert events == []
