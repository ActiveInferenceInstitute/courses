"""Tests for publish utils module — COURSE_REGISTRY-aware paths."""


from src.publish.utils import (
    flatten_module,
    flatten_published,
    copy_labs_and_dashboards,
    copy_practice_tests,
    copy_slides,
    copy_slides_to_modules,
    copy_exams,
    clean_directory,
    copy_directory_contents,
    get_course_config,
    clean_published,
)
from src.publish import config


# ── Helper ──────────────────────────────────────────────────────────────


def _rel_path(course_id: str) -> str:
    """Return the COURSE_REGISTRY rel_path for a known course ID."""
    from src.batch_processing.config import COURSE_REGISTRY
    return COURSE_REGISTRY[course_id]["rel_path"]


class TestFlattenModule:
    def test_moves_files_to_root(self, temp_dir):
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        subdir = module_dir / "assignments"
        subdir.mkdir()
        (subdir / "hw1.pdf").write_text("content", encoding="utf-8")
        (subdir / "hw2.pdf").write_text("content", encoding="utf-8")
        moved = flatten_module(module_dir)
        assert moved == 2
        assert (module_dir / "hw1.pdf").exists()
        assert not subdir.exists()

    def test_handles_name_conflicts(self, temp_dir):
        md = temp_dir / "module-01"
        md.mkdir()
        da = md / "dir_a"
        da.mkdir()
        (da / "file.pdf").write_text("a")
        db = md / "dir_b"
        db.mkdir()
        (db / "file.pdf").write_text("b")
        moved = flatten_module(md)
        assert moved == 2
        assert len(list(md.glob("*.pdf"))) == 2

    def test_dry_run_no_modification(self, temp_dir):
        md = temp_dir / "module-01"
        md.mkdir()
        sub = md / "assignments"
        sub.mkdir()
        (sub / "hw1.pdf").write_text("c")
        moved = flatten_module(md, dry_run=True)
        assert moved == 1
        assert (sub / "hw1.pdf").exists()

    def test_empty_module(self, temp_dir):
        md = temp_dir / "module-01"
        md.mkdir()
        assert flatten_module(md) == 0


class TestFlattenPublished:
    def test_flattens_all_modules(self, temp_dir):
        pub = temp_dir / "PUBLISHED"
        mod = pub / "biol-1" / "module-01" / "assignments"
        mod.mkdir(parents=True)
        (mod / "hw.pdf").write_text("c")
        assert flatten_published(pub) == 1
        assert (pub / "biol-1" / "module-01" / "hw.pdf").exists()

    def test_skips_configured_dirs(self, temp_dir):
        pub = temp_dir / "PUBLISHED"
        course = pub / "biol-1"
        for name in ["labs", "dashboards", "syllabus", "slides", "exams", "practice_tests"]:
            skip_dir = course / name / "subdir"
            skip_dir.mkdir(parents=True)
            (skip_dir / "f.pdf").write_text("c")
        assert flatten_published(pub) == 0


# ── Registry-based tests ───────────────────────────────────────────────


class TestCopyPracticeTests:
    def _make(self, root, course="ai-philosophy"):
        p = root / _rel_path(course) / "practice_tests"
        p.mkdir(parents=True)
        return p

    def test_copies_files(self, temp_dir):
        p = self._make(temp_dir)
        (p / "test.md").write_text("# T")
        (p / "test_key.md").write_text("# K")
        (p / "README.md").write_text("# R")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_practice_tests(temp_dir, courses=["ai-philosophy"]) == 2
        assert (pub / "ai-philosophy" / "practice_tests" / "test.md").exists()
        assert not (pub / "ai-philosophy" / "practice_tests" / "README.md").exists()

    def test_skips_dir(self, temp_dir):
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_practice_tests(temp_dir, courses=["ai-philosophy"]) == 0

    def test_unknown_course_warns(self, temp_dir):
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_practice_tests(temp_dir, courses=["nonexistent"]) == 0


class TestCopyLabsAndDashboards:
    def _lab_path(self, root, course="ai-philosophy"):
        p = root / _rel_path(course) / "labs"
        p.mkdir(parents=True)
        return p

    def test_copies_labs(self, temp_dir):
        lab_dir = self._lab_path(temp_dir)
        (lab_dir / "lab-01.md").write_text("# L")
        o = lab_dir / "output"
        o.mkdir()
        (o / "lab-01.pdf").write_text("pdf")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        c = copy_labs_and_dashboards(temp_dir, courses=["ai-philosophy"])
        assert c >= 2
        assert (pub / "ai-philosophy" / "labs" / "lab-01.md").exists()

    def test_copies_dashboards(self, temp_dir):
        lab_dir = self._lab_path(temp_dir)
        dashboards_dir = lab_dir / "dashboards"
        dashboards_dir.mkdir()
        (dashboards_dir / "db.html").write_text("<h>")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        c = copy_labs_and_dashboards(temp_dir, courses=["ai-philosophy"])
        assert c >= 1

    def test_missing(self, temp_dir):
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_labs_and_dashboards(temp_dir, courses=["ai-philosophy"]) == 0


class TestCopySlides:
    def test_copies_pdfs(self, temp_dir):
        slides_dir = temp_dir / _rel_path("ai-philosophy") / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "slides.pdf").write_bytes(b"pdf")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_slides(temp_dir, courses=["ai-philosophy"]) == 1
        assert (pub / "ai-philosophy" / "slides" / "slides.pdf").exists()

    def test_missing(self, temp_dir):
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        assert copy_slides(temp_dir, courses=["ai-philosophy"]) == 0


class TestCopySlidesToModules:
    def test_copies_into_modules(self, temp_dir):
        slides_dir = temp_dir / _rel_path("ai-philosophy") / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "module-1-slides-full.pdf").write_bytes(b"p")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        (pub / "ai-philosophy" / "module-01-topic").mkdir(parents=True)
        assert copy_slides_to_modules(temp_dir, courses=["ai-philosophy"]) == 1
        assert (pub / "ai-philosophy" / "module-01-topic" / "module-1-slides-full.pdf").exists()

    def test_no_match(self, temp_dir):
        slides_dir = temp_dir / _rel_path("ai-philosophy") / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "module-99-slides.pdf").write_bytes(b"p")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        (pub / "ai-philosophy" / "module-01-topic").mkdir(parents=True)
        assert copy_slides_to_modules(temp_dir, courses=["ai-philosophy"]) == 0


class TestCopyExams:
    def _exams_path(self, root, course="ai-philosophy"):
        p = root / _rel_path(course) / "exams"
        p.mkdir(parents=True)
        return p

    def test_copies_exam_files(self, temp_dir):
        e = self._exams_path(temp_dir)
        (e / "exam1.md").write_text("# E")
        (e / "exam1_key.md").write_text("# K")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        copy_exams(temp_dir)
        assert (pub / "ai-philosophy" / "exams" / "exam1.md").exists()

    def test_copies_outputs(self, temp_dir):
        e = self._exams_path(temp_dir)
        o = e / "output"
        o.mkdir()
        (o / "exam1.pdf").write_bytes(b"pdf")
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()
        copy_exams(temp_dir)
        assert (pub / "ai-philosophy" / "exams" / "exam1.pdf").exists()


class TestCleanDirectory:
    def test_cleans(self, temp_dir):
        t = temp_dir / "t"
        t.mkdir()
        (t / "old").write_text("o")
        clean_directory(t)
        assert list(t.iterdir()) == []

    def test_creates(self, temp_dir):
        t = temp_dir / "new"
        clean_directory(t)
        assert t.exists()


class TestCopyDirectoryContents:
    def test_copies(self, temp_dir):
        src = temp_dir / "s"
        src.mkdir()
        (src / "a.txt").write_text("a")
        (src / "sub").mkdir()
        (src / "sub" / "b.txt").write_text("b")
        dst = temp_dir / "d"
        assert copy_directory_contents(src, dst) == 2
        assert (dst / "a.txt").exists()
        assert (dst / "sub" / "b.txt").exists()

    def test_excludes(self, temp_dir):
        src = temp_dir / "s"
        src.mkdir()
        (src / "ok.md").write_text("")
        (src / ".DS_Store").write_text("")
        dst = temp_dir / "d"
        assert copy_directory_contents(src, dst) == 1

    def test_missing_source(self, temp_dir):
        assert copy_directory_contents(temp_dir / "x", temp_dir / "d") == 0


class TestGetCourseConfig:
    def test_known(self):
        assert "module_source_dir" in get_course_config("biol-1")

    def test_unknown(self):
        assert get_course_config("x") == config.DEFAULT_CONFIG


class TestCleanPublished:
    def test_removes(self, temp_dir):
        p = temp_dir / "PUBLISHED"
        p.mkdir()
        (p / "biol-1").mkdir()
        (p / "f.txt").write_text("")
        clean_published(p)
        assert not any(f for f in p.iterdir() if not f.name.startswith("."))

    def test_preserves_dotfiles(self, temp_dir):
        p = temp_dir / "PUBLISHED"
        p.mkdir()
        (p / ".gitkeep").write_text("")
        (p / "biol-1").mkdir()
        clean_published(p)
        assert (p / ".gitkeep").exists()