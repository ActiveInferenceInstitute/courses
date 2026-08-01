"""Tests for the course_config module.

All tests use real file operations (no mocks), per project convention.
"""

import tomllib
from pathlib import Path

import pytest

from src.course_config.config import CONFIG_FILENAME, DEFAULT_CONFIG
from src.course_config.utils import (
    deep_merge,
    find_config_chain,
    load_toml_file,
    resolve_config_chain,
    validate_config,
)
from src.course_config.main import (
    get_enabled_formats,
    get_localization,
    get_metadata,
    get_pdf_css,
    get_rendering_config,
    get_tts_settings,
    is_format_enabled,
    load_course_config,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def fake_repo(tmp_path: Path) -> Path:
    """Create a minimal repo structure with course_development/."""
    (tmp_path / "course_development").mkdir()
    return tmp_path


@pytest.fixture
def fake_curriculum(fake_repo: Path) -> Path:
    """Create a fake active_inference curriculum with TOML files."""
    curriculum = fake_repo / "course_development" / "active_inference"
    curriculum.mkdir()

    course = curriculum / "01_philosophy"
    course.mkdir()

    module = course / "01_systems"
    module.mkdir()

    # Curriculum-level config
    (curriculum / CONFIG_FILENAME).write_text(
        '[metadata]\ntitle = "Active Inference"\ninstitution = "AII"\n'
        "[audience]\ndifficulty = \"intermediate\"\nestimated_hours = 160\n"
        "[localization]\nlanguage = \"en\"\n"
        "[rendering.audio]\nlang = \"en\"\n",
        encoding="utf-8",
    )

    # Course-level config (overrides title)
    (course / CONFIG_FILENAME).write_text(
        '[metadata]\ntitle = "Active Inference: Philosophy"\n'
        "[audience]\nestimated_hours = 40\n",
        encoding="utf-8",
    )

    return curriculum


# ---------------------------------------------------------------------------
# deep_merge
# ---------------------------------------------------------------------------


class TestDeepMerge:
    def test_flat_merge(self) -> None:
        base = {"a": 1, "b": 2}
        override = {"b": 3, "c": 4}
        result = deep_merge(base, override)
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_nested_merge(self) -> None:
        base = {"x": {"a": 1, "b": 2}, "y": 10}
        override = {"x": {"b": 99, "c": 3}}
        result = deep_merge(base, override)
        assert result == {"x": {"a": 1, "b": 99, "c": 3}, "y": 10}

    def test_override_replaces_non_dict(self) -> None:
        base = {"a": [1, 2]}
        override = {"a": [3, 4, 5]}
        result = deep_merge(base, override)
        assert result == {"a": [3, 4, 5]}

    def test_does_not_mutate_inputs(self) -> None:
        base = {"x": {"a": 1}}
        override = {"x": {"b": 2}}
        result = deep_merge(base, override)
        # Mutating result must not affect originals
        result["x"]["a"] = 999
        assert base["x"]["a"] == 1

    def test_empty_override(self) -> None:
        base = {"a": 1}
        result = deep_merge(base, {})
        assert result == {"a": 1}

    def test_empty_base(self) -> None:
        override = {"a": 1}
        result = deep_merge({}, override)
        assert result == {"a": 1}

    def test_deeply_nested(self) -> None:
        base = {"l1": {"l2": {"l3": {"val": "old"}}}}
        override = {"l1": {"l2": {"l3": {"val": "new", "extra": True}}}}
        result = deep_merge(base, override)
        assert result["l1"]["l2"]["l3"] == {"val": "new", "extra": True}


# ---------------------------------------------------------------------------
# load_toml_file
# ---------------------------------------------------------------------------


class TestLoadTomlFile:
    def test_loads_valid_toml(self, tmp_path: Path) -> None:
        toml_file = tmp_path / "test.toml"
        toml_file.write_text('[metadata]\ntitle = "Test"\n', encoding="utf-8")
        data = load_toml_file(toml_file)
        assert data["metadata"]["title"] == "Test"

    def test_raises_on_missing_file(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            load_toml_file(tmp_path / "nonexistent.toml")

    def test_raises_on_invalid_toml(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "bad.toml"
        bad_file.write_text("not valid [[ toml", encoding="utf-8")
        with pytest.raises(Exception):
            load_toml_file(bad_file)


# ---------------------------------------------------------------------------
# find_config_chain
# ---------------------------------------------------------------------------


class TestFindConfigChain:
    def test_finds_curriculum_and_course_configs(self, fake_curriculum: Path) -> None:
        repo_root = fake_curriculum.parent.parent
        course_path = fake_curriculum / "01_philosophy"
        chain = find_config_chain(course_path, repo_root)
        assert len(chain) == 2
        assert chain[0].parent.name == "active_inference"
        assert chain[1].parent.name == "01_philosophy"

    def test_finds_only_curriculum_config_from_module(
        self, fake_curriculum: Path
    ) -> None:
        repo_root = fake_curriculum.parent.parent
        module_path = fake_curriculum / "01_philosophy" / "01_systems"
        chain = find_config_chain(module_path, repo_root)
        # Should find curriculum and course configs (module has no config)
        assert len(chain) == 2

    def test_returns_empty_for_no_configs(self, fake_repo: Path) -> None:
        bare_course = fake_repo / "course_development" / "bare_course"
        bare_course.mkdir()
        chain = find_config_chain(bare_course, fake_repo)
        assert chain == []

    def test_returns_empty_when_no_course_development(self, tmp_path: Path) -> None:
        chain = find_config_chain(tmp_path / "some" / "path", tmp_path)
        assert chain == []


# ---------------------------------------------------------------------------
# resolve_config_chain
# ---------------------------------------------------------------------------


class TestResolveConfigChain:
    def test_returns_defaults_for_empty_chain(self) -> None:
        result = resolve_config_chain([])
        assert result["localization"]["language"] == "en"
        assert result["rendering"]["pdf"]["enabled"] is True

    def test_merges_single_file(self, tmp_path: Path) -> None:
        toml_file = tmp_path / "course.toml"
        toml_file.write_text(
            '[metadata]\ntitle = "Test Course"\n', encoding="utf-8"
        )
        result = resolve_config_chain([toml_file])
        assert result["metadata"]["title"] == "Test Course"
        # Other defaults preserved
        assert result["metadata"]["institution"] == ""
        assert result["localization"]["language"] == "en"

    def test_later_files_override_earlier(self, tmp_path: Path) -> None:
        parent_toml = tmp_path / "parent.toml"
        child_toml = tmp_path / "child.toml"
        parent_toml.write_text(
            '[metadata]\ntitle = "Parent"\ndescription = "From parent"\n',
            encoding="utf-8",
        )
        child_toml.write_text(
            '[metadata]\ntitle = "Child"\n', encoding="utf-8"
        )
        result = resolve_config_chain([parent_toml, child_toml])
        assert result["metadata"]["title"] == "Child"
        assert result["metadata"]["description"] == "From parent"

    def test_malformed_file_raises(self, tmp_path: Path) -> None:
        """A malformed config file must raise, not silently drop the settings."""
        good = tmp_path / "good.toml"
        bad = tmp_path / "bad.toml"
        good.write_text('[metadata]\ntitle = "Good"\n', encoding="utf-8")
        bad.write_text("this is not valid toml [[", encoding="utf-8")
        # A chain containing a malformed file raises so the author's settings
        # are never silently discarded.
        with pytest.raises(tomllib.TOMLDecodeError):
            resolve_config_chain([bad, good])
        with pytest.raises(tomllib.TOMLDecodeError):
            resolve_config_chain([good, bad])


# ---------------------------------------------------------------------------
# validate_config
# ---------------------------------------------------------------------------


class TestValidateConfig:
    def test_valid_default_config(self) -> None:
        warnings = validate_config(DEFAULT_CONFIG)
        assert warnings == []

    def test_unknown_section(self) -> None:
        cfg = {**DEFAULT_CONFIG, "unknown_section": {}}
        warnings = validate_config(cfg)
        assert any("Unknown config section" in w for w in warnings)

    def test_authors_not_list(self) -> None:
        cfg = deep_merge(DEFAULT_CONFIG, {"metadata": {"authors": "single_author"}})
        warnings = validate_config(cfg)
        assert any("authors" in w for w in warnings)

    def test_estimated_hours_not_number(self) -> None:
        cfg = deep_merge(DEFAULT_CONFIG, {"audience": {"estimated_hours": "forty"}})
        warnings = validate_config(cfg)
        assert any("estimated_hours" in w for w in warnings)

    def test_rtl_not_boolean(self) -> None:
        cfg = deep_merge(DEFAULT_CONFIG, {"localization": {"rtl": "yes"}})
        warnings = validate_config(cfg)
        assert any("rtl" in w for w in warnings)

    def test_audio_slow_not_boolean(self) -> None:
        cfg = deep_merge(
            DEFAULT_CONFIG, {"rendering": {"audio": {"slow": "yes"}}}
        )
        warnings = validate_config(cfg)
        assert any("slow" in w for w in warnings)


# ---------------------------------------------------------------------------
# load_course_config (integration)
# ---------------------------------------------------------------------------


class TestLoadCourseConfig:
    def test_loads_with_no_toml_files(self, fake_repo: Path) -> None:
        bare_course = fake_repo / "course_development" / "bare"
        bare_course.mkdir()
        config = load_course_config(bare_course, fake_repo)
        assert config["localization"]["language"] == "en"
        assert config["rendering"]["pdf"]["enabled"] is True

    def test_loads_curriculum_level(self, fake_curriculum: Path) -> None:
        repo_root = fake_curriculum.parent.parent
        config = load_course_config(fake_curriculum, repo_root)
        assert config["metadata"]["title"] == "Active Inference"
        assert config["metadata"]["institution"] == "AII"
        assert config["audience"]["estimated_hours"] == 160

    def test_course_level_overrides_curriculum(
        self, fake_curriculum: Path
    ) -> None:
        repo_root = fake_curriculum.parent.parent
        course_path = fake_curriculum / "01_philosophy"
        config = load_course_config(course_path, repo_root)
        # Title overridden at course level
        assert config["metadata"]["title"] == "Active Inference: Philosophy"
        # Institution inherited from curriculum level
        assert config["metadata"]["institution"] == "AII"
        # estimated_hours overridden at course level
        assert config["audience"]["estimated_hours"] == 40
        # difficulty inherited from curriculum level
        assert config["audience"]["difficulty"] == "intermediate"

    def test_module_level_inherits_all(self, fake_curriculum: Path) -> None:
        repo_root = fake_curriculum.parent.parent
        module_path = fake_curriculum / "01_philosophy" / "01_systems"
        config = load_course_config(module_path, repo_root)
        # Title from course level
        assert config["metadata"]["title"] == "Active Inference: Philosophy"
        # Institution from curriculum level
        assert config["metadata"]["institution"] == "AII"

    def test_module_level_override(self, fake_curriculum: Path) -> None:
        repo_root = fake_curriculum.parent.parent
        module_path = fake_curriculum / "01_philosophy" / "01_systems"
        # Add a module-level config
        (module_path / CONFIG_FILENAME).write_text(
            "[rendering.audio]\nlang = \"es\"\nslow = true\n",
            encoding="utf-8",
        )
        config = load_course_config(module_path, repo_root)
        assert config["rendering"]["audio"]["lang"] == "es"
        assert config["rendering"]["audio"]["slow"] is True
        # Title still inherited
        assert config["metadata"]["title"] == "Active Inference: Philosophy"


# ---------------------------------------------------------------------------
# Helper functions (main.py)
# ---------------------------------------------------------------------------


class TestGetRenderingConfig:
    def test_returns_rendering_section(self) -> None:
        config = {"rendering": {"pdf": {"enabled": False}}}
        result = get_rendering_config(config)
        assert result["pdf"]["enabled"] is False

    def test_returns_defaults_when_missing(self) -> None:
        result = get_rendering_config({})
        assert result["pdf"]["enabled"] is True


class TestIsFormatEnabled:
    def test_enabled_by_default(self) -> None:
        assert is_format_enabled(DEFAULT_CONFIG, "pdf") is True
        assert is_format_enabled(DEFAULT_CONFIG, "html") is True
        assert is_format_enabled(DEFAULT_CONFIG, "mp3") is True

    def test_disabled_format(self) -> None:
        config = deep_merge(DEFAULT_CONFIG, {"rendering": {"pdf": {"enabled": False}}})
        assert is_format_enabled(config, "pdf") is False
        assert is_format_enabled(config, "html") is True

    def test_mp3_alias(self) -> None:
        config = deep_merge(
            DEFAULT_CONFIG, {"rendering": {"audio": {"enabled": False}}}
        )
        assert is_format_enabled(config, "mp3") is False

    def test_unknown_format_returns_true(self) -> None:
        assert is_format_enabled(DEFAULT_CONFIG, "unknown_format") is True


class TestGetMetadata:
    def test_extracts_metadata(self) -> None:
        config = deep_merge(DEFAULT_CONFIG, {"metadata": {"title": "Test"}})
        meta = get_metadata(config)
        assert meta["title"] == "Test"
        assert meta["institution"] == ""

    def test_returns_defaults_when_missing(self) -> None:
        meta = get_metadata({})
        assert meta["title"] == ""


class TestGetLocalization:
    def test_extracts_localization(self) -> None:
        config = deep_merge(
            DEFAULT_CONFIG, {"localization": {"language": "es"}}
        )
        loc = get_localization(config)
        assert loc["language"] == "es"
        assert loc["locale"] == "en-US"  # default

    def test_returns_defaults_when_missing(self) -> None:
        loc = get_localization({})
        assert loc["language"] == "en"


class TestGetTtsSettings:
    def test_extracts_tts_settings(self) -> None:
        config = deep_merge(
            DEFAULT_CONFIG,
            {"rendering": {"audio": {"lang": "es", "slow": True, "speed": 0.8}}},
        )
        tts = get_tts_settings(config)
        assert tts["lang"] == "es"
        assert tts["slow"] is True
        assert tts["speed"] == 0.8

    def test_returns_defaults(self) -> None:
        tts = get_tts_settings({})
        assert tts["lang"] == "en"
        assert tts["slow"] is False
        assert tts["speed"] == 1.0


class TestGetPdfCss:
    def test_returns_none_when_unset(self) -> None:
        assert get_pdf_css(DEFAULT_CONFIG) is None

    def test_returns_path_when_set(self) -> None:
        config = deep_merge(
            DEFAULT_CONFIG,
            {"rendering": {"pdf": {"css_file": "custom.css"}}},
        )
        assert get_pdf_css(config) == "custom.css"


class TestGetEnabledFormats:
    def test_all_enabled_by_default(self) -> None:
        formats = get_enabled_formats(DEFAULT_CONFIG)
        assert set(formats) == {"pdf", "mp3", "docx", "html", "txt", "md"}

    def test_disabled_format_excluded(self) -> None:
        config = deep_merge(
            DEFAULT_CONFIG,
            {"rendering": {"pdf": {"enabled": False}, "audio": {"enabled": False}}},
        )
        formats = get_enabled_formats(config)
        assert "pdf" not in formats
        assert "mp3" not in formats
        assert "html" in formats


# ---------------------------------------------------------------------------
# Integration: real course_development TOML files
# ---------------------------------------------------------------------------


class TestRealCourseToml:
    """Tests against the actual TOML files checked into the repository."""

    @staticmethod
    def _repo_root() -> Path:
        """Return the repository root (parent of software/)."""
        return Path(__file__).resolve().parent.parent.parent

    def test_curriculum_level_config(self) -> None:
        repo = self._repo_root()
        curriculum = repo / "course_development" / "active_inference"
        if not (curriculum / CONFIG_FILENAME).exists():
            pytest.skip("No curriculum-level course.toml found")
        config = load_course_config(curriculum, repo)
        assert config["metadata"]["title"] == "Active Inference"
        assert "Active Inference Institute" in config["metadata"]["authors"]

    def test_philosophy_course_config(self) -> None:
        repo = self._repo_root()
        course = repo / "course_development" / "active_inference" / "01_philosophy"
        if not (course / CONFIG_FILENAME).exists():
            pytest.skip("No course-level course.toml found")
        config = load_course_config(course, repo)
        assert config["metadata"]["title"] == "Active Inference: Philosophy"
        # Inherited from curriculum
        assert config["metadata"]["institution"] == "Active Inference Institute"
        assert config["audience"]["estimated_hours"] == 40
        assert config["audience"]["difficulty"] == "intermediate"

    def test_math_course_config(self) -> None:
        repo = self._repo_root()
        course = repo / "course_development" / "active_inference" / "03_math"
        if not (course / CONFIG_FILENAME).exists():
            pytest.skip("No course-level course.toml found")
        config = load_course_config(course, repo)
        assert config["metadata"]["title"] == "Active Inference: Mathematics"
        assert config["audience"]["estimated_hours"] == 40

    def test_no_config_returns_defaults(self) -> None:
        repo = self._repo_root()
        # A path with no TOML files should still work
        bare = repo / "course_development"
        if not bare.exists():
            pytest.skip("course_development/ not found")
        config = load_course_config(bare, repo)
        assert config["localization"]["language"] == "en"
        assert config["rendering"]["pdf"]["enabled"] is True
