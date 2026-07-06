"""Tests for CLI functionality of generation scripts."""

import subprocess
import sys
from pathlib import Path



# Path to the scripts directory
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
SOFTWARE_DIR = Path(__file__).parent.parent


class TestGenerateAllOutputsCLI:
    """Test CLI for generate_all_outputs.py."""

    def test_help_output(self):
        """Test that --help displays usage information."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_all_outputs.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "--course" in result.stdout
        assert "--module" in result.stdout
        assert "--formats" in result.stdout
        assert "--dry-run" in result.stdout
        assert "--skip-clear" in result.stdout
        assert "--no-website" in result.stdout

    def test_course_choices(self):
        """Test that --course only accepts valid choices."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_all_outputs.py"), "--course", "invalid"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()

    def test_dry_run_mode(self):
        """Test that dry-run mode doesn't generate files."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "generate_all_outputs.py"),
                "--dry-run",
                "--course",
                "ai-philosophy",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "DRY RUN" in result.stdout or "DRY RUN" in result.stderr
        assert "No files were generated" in result.stdout or "No files were generated" in result.stderr

    def test_module_filter_display(self):
        """Test that module filter is displayed correctly."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "generate_all_outputs.py"),
                "--dry-run",
                "--course",
                "ai-philosophy",
                "--module",
                "1",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        # Check that module filter is mentioned
        output = result.stdout + result.stderr
        assert "module-1" in output.lower() or "module filter" in output.lower()


class TestGenerateModuleRenderingsCLI:
    """Test CLI for generate_module_renderings.py."""

    def test_help_output(self):
        """Test that --help displays usage information."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_module_renderings.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "--course" in result.stdout
        assert "--module" in result.stdout

    def test_course_choices(self):
        """Test that --course only accepts valid choices."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_module_renderings.py"), "--course", "invalid"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()

    def test_invalid_module_shows_available(self):
        """Test that invalid module number shows available modules."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "generate_module_renderings.py"),
                "--course",
                "ai-philosophy",
                "--module",
                "999",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 1
        # Should show available modules
        assert "available" in result.stdout.lower() or "module-" in result.stdout.lower()


class TestGenerateSyllabusRenderingsCLI:
    """Test CLI for generate_syllabus_renderings.py."""

    def test_help_output(self):
        """Test that --help displays usage information."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_syllabus_renderings.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "--course" in result.stdout

    def test_course_choices(self):
        """Test that --course only accepts valid choices."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_syllabus_renderings.py"), "--course", "invalid"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()


class TestGenerateModuleWebsiteCLI:
    """Test CLI for generate_module_website.py."""

    def test_help_output(self):
        """Test that --help displays usage information."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_module_website.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "--course" in result.stdout
        assert "--module" in result.stdout

    def test_course_choices(self):
        """Test that --course only accepts valid choices."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "generate_module_website.py"), "--course", "invalid"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()

    def test_invalid_module_shows_available(self):
        """Test that invalid module number shows available modules."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "generate_module_website.py"),
                "--course",
                "ai-math",
                "--module",
                "999",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 1
        # Should show available modules
        assert "available" in result.stdout.lower() or "module-" in result.stdout.lower()


class TestImportLegacyMaterialsCLI:
    """Test CLI for import_legacy_materials.py."""

    def test_help_output(self):
        """Test that --help displays usage information."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "import_legacy_materials.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "--course" in result.stdout

    def test_valid_course(self):
        """Test that a valid course from registry is accepted (dry-run)."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "import_legacy_materials.py"),
                "--course",
                "ai-philosophy",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 2
        if result.returncode != 0:
            # Check for generic directory error
            output = (result.stdout + result.stderr).lower()
            assert "directory does not exist" in output or "directory not found" in output

    def test_invalid_course(self):
        """Test that an invalid course is rejected."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "import_legacy_materials.py"),
                "--course",
                "invalid-course-name",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()


class TestPublishAllCLI:
    """Test CLI for publish_all.py."""

    def test_help_output(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "publish_all.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()

    def test_dry_run_equivalent(self):
        """Test execution with skip flags (mock dry-run)."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "publish_all.py"),
                "--skip-generation",
                "--skip-publish",
                "--skip-copy-extras",
                "--skip-flatten",
                "--skip-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        # It might still fail if it tries to list courses and finds emptiness, but it proves args are valid
        assert result.returncode != 2


class TestPublishCourseCLI:
    """Test CLI for publish_course.py."""

    def test_help_output(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "publish_course.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0
        assert "--course" in result.stdout

    def test_valid_course(self):
        """Test valid course argument."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "publish_course.py"),
                "--course",
                "ai-philosophy",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 2

    def test_invalid_course(self):
        """Test invalid course argument."""
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "publish_course.py"),
                "--course",
                "invalid-course",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()


class TestRenumberQuestionsCLI:
    """Test CLI for renumber_questions.py."""

    def test_help_output(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "renumber_questions.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0

    def test_valid_course_dry_run(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "renumber_questions.py"),
                "--course",
                "ai-philosophy",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0

    def test_invalid_course(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "renumber_questions.py"),
                "--course",
                "invalid-course",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()


class TestValidateOutputsCLI:
    """Test CLI for validate_outputs.py."""

    def test_help_output(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "validate_outputs.py"), "--help"],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode == 0

    def test_valid_course(self):
        # validation might return 1 if files missing, but not 2 (arg error)
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "validate_outputs.py"),
                "--course",
                "ai-philosophy",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 2

    def test_invalid_course(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "validate_outputs.py"),
                "--course",
                "invalid-course",
            ],
            capture_output=True,
            text=True,
            cwd=str(SOFTWARE_DIR),
        )
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()
