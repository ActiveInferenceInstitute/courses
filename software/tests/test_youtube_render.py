"""Tests for YouTube playlist course rendering."""

import json
from pathlib import Path

import pytest

from src.youtube_transcript.render import (
    format_duration,
    format_upload_date,
    load_youtube_manifest,
    render_all_youtube_courses,
    render_course_modules,
    render_module_md_template,
    save_youtube_manifest,
    scaffold_course_directory,
    slugify,
)


class TestSlugify:
    """Tests for slugify (offline)."""

    def test_basic_title(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self) -> None:
        assert slugify("Act Inf #001: Introduction!") == "act-inf-001-introduction"

    def test_long_title_truncated(self) -> None:
        long_title = "a " * 50  # 100 chars
        result = slugify(long_title, max_length=20)
        assert len(result) <= 20
        assert "-" not in result[-1:]  # no trailing hyphen

    def test_unicode_stripped(self) -> None:
        result = slugify("Café Résumé")
        assert "caf" in result
        assert "r" in result
        assert all(c.isalnum() or c == "-" for c in result)

    def test_multiple_hyphens_collapsed(self) -> None:
        assert slugify("hello---world") == "hello-world"

    def test_leading_trailing_stripped(self) -> None:
        assert slugify("--hello--") == "hello"

    def test_empty_string(self) -> None:
        assert slugify("") == ""

    def test_numbers_preserved(self) -> None:
        assert slugify("Chapter 42 Part 3") == "chapter-42-part-3"

    def test_max_length_boundary(self) -> None:
        result = slugify("short", max_length=100)
        assert result == "short"

    def test_truncation_on_word_boundary(self) -> None:
        # "active-inference-textbook" is 25 chars
        result = slugify("active inference textbook group readings", max_length=30)
        # Should truncate on a hyphen boundary
        assert len(result) <= 30
        assert not result.endswith("-")


class TestFormatDuration:
    """Tests for format_duration (offline)."""

    def test_none_returns_unknown(self) -> None:
        assert format_duration(None) == "Unknown"

    def test_seconds_only(self) -> None:
        assert format_duration(45) == "0:45"

    def test_minutes_and_seconds(self) -> None:
        assert format_duration(125) == "2:05"

    def test_hours(self) -> None:
        assert format_duration(3661) == "1:01:01"

    def test_float_seconds(self) -> None:
        assert format_duration(125.7) == "2:05"


class TestFormatUploadDate:
    """Tests for format_upload_date (offline)."""

    def test_none_returns_unknown(self) -> None:
        assert format_upload_date(None) == "Unknown"

    def test_valid_date(self) -> None:
        assert format_upload_date("20250115") == "2025-01-15"

    def test_invalid_length(self) -> None:
        assert format_upload_date("2025") == "Unknown"

    def test_empty_string(self) -> None:
        assert format_upload_date("") == "Unknown"


class TestRenderModuleMdTemplate:
    """Tests for module.md template rendering (offline)."""

    def test_contains_title(self) -> None:
        result = render_module_md_template(
            video_title="Test Video",
            video_id="abc123xyz00",
            transcript_text="Hello world transcript.",
        )
        assert "# Test Video" in result

    def test_contains_youtube_link(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
        )
        assert "https://www.youtube.com/watch?v=abc123xyz00" in result

    def test_contains_transcript_text(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="This is the actual transcript content.",
        )
        assert "This is the actual transcript content." in result

    def test_contains_playlist_title(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
            playlist_title="My Playlist",
        )
        assert "My Playlist" in result

    def test_contains_duration(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
            duration=3600,
        )
        assert "1:00:00" in result

    def test_contains_upload_date(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
            upload_date="20250301",
        )
        assert "2025-03-01" in result

    def test_contains_transcript_method(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
            transcript_method="whisper",
        )
        assert "whisper" in result

    def test_no_playlist_line_when_empty(self) -> None:
        result = render_module_md_template(
            video_title="Test",
            video_id="abc123xyz00",
            transcript_text="Content.",
            playlist_title="",
        )
        assert "**Playlist**" not in result


class TestYoutubeManifestIO:
    """Tests for youtube_courses.json manifest I/O (offline)."""

    def test_load_nonexistent_returns_empty(self, tmp_path: Path) -> None:
        manifest = load_youtube_manifest(tmp_path / "missing.json")
        assert manifest["playlists"] == {}
        assert manifest["total_playlists"] == 0

    def test_roundtrip(self, tmp_path: Path) -> None:
        manifest = {
            "channel_url": "https://www.youtube.com/@ActiveInference",
            "last_updated": "2025-06-01T00:00:00Z",
            "total_playlists": 1,
            "playlists": {
                "test-playlist": {
                    "id": "PLtest123",
                    "title": "Test Playlist",
                    "url": "https://www.youtube.com/playlist?list=PLtest123",
                    "slug": "test-playlist",
                    "video_count": 2,
                    "videos": [
                        {"id": "vid1", "title": "Video 1", "playlist_index": 0},
                        {"id": "vid2", "title": "Video 2", "playlist_index": 1},
                    ],
                }
            },
        }
        path = tmp_path / "youtube_courses.json"
        save_youtube_manifest(manifest, path)

        loaded = load_youtube_manifest(path)
        assert loaded["channel_url"] == "https://www.youtube.com/@ActiveInference"
        assert loaded["total_playlists"] == 1
        assert "test-playlist" in loaded["playlists"]
        assert loaded["playlists"]["test-playlist"]["video_count"] == 2

    def test_atomic_write_valid_json(self, tmp_path: Path) -> None:
        path = tmp_path / "youtube_courses.json"
        manifest = {
            "channel_url": "",
            "last_updated": "",
            "total_playlists": 0,
            "playlists": {},
        }
        save_youtube_manifest(manifest, path)
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
        assert parsed == manifest

    def test_save_overwrites_existing(self, tmp_path: Path) -> None:
        path = tmp_path / "youtube_courses.json"
        save_youtube_manifest(
            {"channel_url": "first", "last_updated": "", "total_playlists": 0, "playlists": {}},
            path,
        )
        save_youtube_manifest(
            {"channel_url": "second", "last_updated": "", "total_playlists": 0, "playlists": {}},
            path,
        )
        loaded = load_youtube_manifest(path)
        assert loaded["channel_url"] == "second"


class TestScaffoldCourseDirectory:
    """Tests for course scaffolding with pre-created transcripts (offline)."""

    def test_creates_module_dirs_and_files(self, tmp_path: Path) -> None:
        # Set up transcript directory with pre-existing transcripts
        transcript_dir = tmp_path / "transcription"
        transcripts_path = transcript_dir / "transcripts"
        transcripts_path.mkdir(parents=True)
        (transcripts_path / "vid001.txt").write_text("Hello world transcript.", encoding="utf-8")
        (transcripts_path / "vid002.txt").write_text("Second video transcript.", encoding="utf-8")

        youtube_dir = tmp_path / "youtube"

        videos = [
            {
                "id": "vid001",
                "title": "Introduction to Active Inference",
                "duration": 3600,
                "upload_date": "20250101",
                "playlist_index": 0,
            },
            {
                "id": "vid002",
                "title": "Chapter 2: Notation",
                "duration": 1800,
                "upload_date": "20250115",
                "playlist_index": 1,
            },
        ]

        course_meta = {
            "id": "PLtest",
            "title": "Test Textbook Group",
            "url": "https://www.youtube.com/playlist?list=PLtest",
        }

        result = scaffold_course_directory(
            course_slug="test-textbook",
            videos=videos,
            transcript_dir=transcript_dir,
            youtube_courses_dir=youtube_dir,
            course_metadata=course_meta,
        )

        assert result["created"] == 2
        assert result["failed"] == 0

        # Verify directory structure
        course_dir = youtube_dir / "test-textbook"
        assert course_dir.is_dir()
        assert (course_dir / "course.json").exists()

        # Verify module directories
        mod1 = course_dir / "01_introduction-to-active-inference"
        mod2 = course_dir / "02_chapter-2-notation"
        assert mod1.is_dir()
        assert mod2.is_dir()

        # Verify module.md content
        md1 = (mod1 / "module.md").read_text(encoding="utf-8")
        assert "# Introduction to Active Inference" in md1
        assert "Hello world transcript." in md1
        assert "youtube.com/watch?v=vid001" in md1
        assert "Test Textbook Group" in md1
        assert "1:00:00" in md1
        assert "2025-01-01" in md1

        md2 = (mod2 / "module.md").read_text(encoding="utf-8")
        assert "# Chapter 2: Notation" in md2
        assert "Second video transcript." in md2

    def test_skips_existing_modules(self, tmp_path: Path) -> None:
        transcript_dir = tmp_path / "transcription"
        transcripts_path = transcript_dir / "transcripts"
        transcripts_path.mkdir(parents=True)
        (transcripts_path / "vid001.txt").write_text("Transcript.", encoding="utf-8")

        youtube_dir = tmp_path / "youtube"

        videos = [{"id": "vid001", "title": "Already Done", "playlist_index": 0}]
        course_meta = {"id": "PL", "title": "Test", "url": ""}

        # First scaffold
        scaffold_course_directory("test-course", videos, transcript_dir, youtube_dir, course_meta)

        # Second scaffold should skip
        result = scaffold_course_directory(
            "test-course", videos, transcript_dir, youtube_dir, course_meta
        )
        assert result["skipped"] == 1
        assert result["created"] == 0

    def test_missing_transcript_fails(self, tmp_path: Path) -> None:
        transcript_dir = tmp_path / "transcription"
        (transcript_dir / "transcripts").mkdir(parents=True)

        youtube_dir = tmp_path / "youtube"

        videos = [{"id": "no_transcript", "title": "No Transcript Video", "playlist_index": 0}]
        course_meta = {"id": "PL", "title": "Test", "url": ""}

        result = scaffold_course_directory(
            "test-course",
            videos,
            transcript_dir,
            youtube_dir,
            course_meta,
            skip_whisper=True,
        )
        assert result["failed"] == 1
        assert result["created"] == 0

    def test_force_overwrites_existing(self, tmp_path: Path) -> None:
        """Verify force=True replaces template-only module.md with real transcript."""
        transcript_dir = tmp_path / "transcription"
        transcripts_path = transcript_dir / "transcripts"
        transcripts_path.mkdir(parents=True)
        (transcripts_path / "vid001.txt").write_text(
            "Real transcript content from the video.", encoding="utf-8"
        )

        youtube_dir = tmp_path / "youtube"

        videos = [{"id": "vid001", "title": "Test Video Title", "playlist_index": 0}]
        course_meta = {"id": "PL", "title": "Test Playlist", "url": ""}

        # First scaffold creates module.md
        scaffold_course_directory("test-course", videos, transcript_dir, youtube_dir, course_meta)
        course_dir = youtube_dir / "test-course"
        mod_dir = course_dir / "01_test-video-title"
        module_md = mod_dir / "module.md"
        assert module_md.exists()

        # Overwrite with template placeholder (simulating the pre-existing state)
        module_md.write_text("# Module 01: Systems in Youtube\n\nPlaceholder.\n", encoding="utf-8")

        # Without force: should skip
        result = scaffold_course_directory(
            "test-course", videos, transcript_dir, youtube_dir, course_meta
        )
        assert result["skipped"] == 1
        assert "Placeholder" in module_md.read_text(encoding="utf-8")

        # With force: should overwrite
        result = scaffold_course_directory(
            "test-course", videos, transcript_dir, youtube_dir, course_meta, force=True
        )
        assert result["created"] == 1
        assert result["skipped"] == 0
        content = module_md.read_text(encoding="utf-8")
        assert "Real transcript content from the video." in content
        assert "# Test Video Title" in content
        assert "Placeholder" not in content

    def test_course_json_written(self, tmp_path: Path) -> None:
        transcript_dir = tmp_path / "transcription"
        (transcript_dir / "transcripts").mkdir(parents=True)

        youtube_dir = tmp_path / "youtube"
        course_meta = {
            "id": "PLtest",
            "title": "My Course",
            "url": "https://youtube.com/playlist?list=PLtest",
        }

        scaffold_course_directory("my-course", [], transcript_dir, youtube_dir, course_meta)

        course_json = youtube_dir / "my-course" / "course.json"
        assert course_json.exists()
        data = json.loads(course_json.read_text(encoding="utf-8"))
        assert data["title"] == "My Course"
        assert data["playlist_id"] == "PLtest"


class TestRenderCourseModules:
    """Tests for rendering scaffolded modules (offline, uses real process_module_by_type)."""

    def test_renders_module_md_to_txt_and_md(self, tmp_path: Path) -> None:
        # Create a minimal course structure
        course_dir = tmp_path / "test-course"
        mod_dir = course_dir / "01_intro"
        mod_dir.mkdir(parents=True)

        module_md = mod_dir / "module.md"
        module_md.write_text(
            "# Test Video\n\nThis is a test transcript for rendering.\n",
            encoding="utf-8",
        )

        # Render with txt and md formats only (fastest)
        result = render_course_modules(course_dir, formats=["txt", "md"], resume=False)

        assert result["rendered"] == 1
        assert result["skipped"] == 0

        # Check output was created
        output_dir = mod_dir / "output" / "lecture-content"
        assert output_dir.exists()

        # Verify files exist (module.md -> lecture-content type)
        output_files = list(output_dir.iterdir())
        assert len(output_files) >= 1

        # Should have .txt and .md files
        extensions = {f.suffix for f in output_files}
        assert ".txt" in extensions
        assert ".md" in extensions

    def test_resume_skips_rendered(self, tmp_path: Path) -> None:
        # Create course with already-rendered module
        course_dir = tmp_path / "test-course"
        mod_dir = course_dir / "01_intro"
        mod_dir.mkdir(parents=True)
        (mod_dir / "module.md").write_text("# Test\n\nContent.\n", encoding="utf-8")

        # Create fake output to simulate already rendered
        lecture_dir = mod_dir / "output" / "lecture-content"
        lecture_dir.mkdir(parents=True)
        (lecture_dir / "01_intro-module.txt").write_text("rendered", encoding="utf-8")

        result = render_course_modules(course_dir, formats=["txt", "md"], resume=True)
        assert result["skipped"] == 1
        assert result["rendered"] == 0

    def test_no_modules_returns_empty(self, tmp_path: Path) -> None:
        course_dir = tmp_path / "empty-course"
        course_dir.mkdir()

        result = render_course_modules(course_dir, formats=["txt"])
        assert result["rendered"] == 0
        assert result["skipped"] == 0


class TestRenderAllYoutubeCourses:
    """Tests for rendering multiple courses (offline)."""

    def test_renders_multiple_courses(self, tmp_path: Path) -> None:
        youtube_dir = tmp_path / "youtube"

        # Create two courses with module.md files
        for course_name in ["course-a", "course-b"]:
            mod_dir = youtube_dir / course_name / "01_video"
            mod_dir.mkdir(parents=True)
            (mod_dir / "module.md").write_text(
                f"# {course_name} Video\n\nTranscript text.\n",
                encoding="utf-8",
            )

        result = render_all_youtube_courses(youtube_dir, formats=["txt", "md"], resume=False)
        assert result["total_rendered"] == 2
        assert "course-a" in result["courses"]
        assert "course-b" in result["courses"]

    def test_course_filter(self, tmp_path: Path) -> None:
        youtube_dir = tmp_path / "youtube"

        for course_name in ["course-a", "course-b"]:
            mod_dir = youtube_dir / course_name / "01_video"
            mod_dir.mkdir(parents=True)
            (mod_dir / "module.md").write_text("# Test\n\nContent.\n", encoding="utf-8")

        result = render_all_youtube_courses(
            youtube_dir, formats=["txt"], course_filter="course-a", resume=False
        )
        assert "course-a" in result["courses"]
        assert "course-b" not in result["courses"]

    def test_nonexistent_dir_returns_empty(self, tmp_path: Path) -> None:
        result = render_all_youtube_courses(tmp_path / "nonexistent")
        assert result["total_rendered"] == 0


@pytest.mark.requires_internet
class TestEnumerateChannelPlaylists:
    """Tests for playlist enumeration (requires internet)."""

    def test_enumerate_active_inference_playlists(self) -> None:
        from src.youtube_transcript.utils import enumerate_channel_playlists

        playlists = enumerate_channel_playlists("https://www.youtube.com/@ActiveInference")
        assert len(playlists) > 0
        first = playlists[0]
        assert "id" in first
        assert "title" in first
        assert "url" in first
        assert "playlist_count" in first


@pytest.mark.requires_internet
class TestEnumeratePlaylistVideos:
    """Tests for playlist video enumeration (requires internet)."""

    def test_enumerate_known_playlist(self) -> None:
        """Enumerate videos from a real known playlist (requires internet)."""
        from src.youtube_transcript.utils import enumerate_playlist_videos

        videos = enumerate_playlist_videos(
            "https://www.youtube.com/playlist?list=PLNm0u2n1Iwdr_sdTWe3T9WQGFBC3KVHJ"
        )

        assert len(videos) > 0
        first = videos[0]
        assert "id" in first
        assert "title" in first
        assert "playlist_index" in first
        assert first["playlist_index"] == 0
        # Verify ordering: indices should be sequential
        indices = [v["playlist_index"] for v in videos]
        assert indices == list(range(len(videos)))
