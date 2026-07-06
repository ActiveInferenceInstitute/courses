"""Tests for content_processing main module."""


from src.content_processing.main import (
    process_questions_file,
    renumber_questions_in_course,
)


class TestProcessQuestionsFile:
    """Tests for process_questions_file function."""

    def test_sectioned_to_continuous(self, temp_dir):
        """Test converting sectioned questions to continuous numbering."""
        questions_file = temp_dir / "questions.md"
        questions_file.write_text(
            "# Module 1 Questions\n\n"
            "### Part 1: Cell Biology\n\n"
            "1.  **Cell Structure**\n"
            "    *   What is the function of mitochondria in cellular respiration?\n"
            "    *   How does the cell membrane regulate transport?\n\n"
            "### Part 2: Genetics\n\n"
            "2.  **Heredity**\n"
            "    *   What are Mendel's laws of inheritance?\n"
            "    *   How do dominant and recessive alleles interact?\n",
            encoding="utf-8",
        )

        was_changed, count = process_questions_file(questions_file)

        assert was_changed is True
        assert count == 4

        # Verify file was rewritten
        content = questions_file.read_text()
        assert "1. " in content
        assert "### Part" not in content

    def test_already_continuous_no_change(self, temp_dir):
        """Test that already-continuous file is not modified."""
        questions_file = temp_dir / "questions.md"
        original = "# Questions\n\n1. First question?\n\n2. Second question?\n"
        questions_file.write_text(original, encoding="utf-8")

        was_changed, count = process_questions_file(questions_file)

        assert was_changed is False
        assert count == 2
        # Content should be unchanged
        assert questions_file.read_text() == original

    def test_empty_file(self, temp_dir):
        """Test processing empty file."""
        questions_file = temp_dir / "questions.md"
        questions_file.write_text("# Empty Questions\n", encoding="utf-8")

        was_changed, count = process_questions_file(questions_file)

        assert was_changed is False
        assert count == 0

    def test_dry_run_no_write(self, temp_dir):
        """Test that dry_run mode does not write to file."""
        questions_file = temp_dir / "questions.md"
        original = (
            "# Module 1 Questions\n\n"
            "### Part 1: Topics\n\n"
            "1.  **Topic**\n"
            "    *   What is the answer to this question?\n"
            "    *   How does this other thing work in practice?\n"
        )
        questions_file.write_text(original, encoding="utf-8")

        was_changed, count = process_questions_file(questions_file, dry_run=True)

        assert was_changed is True
        assert count == 2
        # File should NOT have been modified
        assert questions_file.read_text() == original

    def test_sectioned_with_dashes(self, temp_dir):
        """Test extraction of questions using dash bullets."""
        questions_file = temp_dir / "questions.md"
        questions_file.write_text(
            "# Questions\n\n"
            "### Part 1: Biology\n\n"
            "1.  **Cells**\n"
            "    -   What is a prokaryotic cell and how is it different?\n"
            "    -   Describe the structure of eukaryotic cell organelles.\n",
            encoding="utf-8",
        )

        was_changed, count = process_questions_file(questions_file)

        assert was_changed is True
        assert count == 2


class TestRenumberQuestionsInCourse:
    """Tests for renumber_questions_in_course function."""

    def test_processes_course_modules(self, temp_dir):
        """Test processing questions across course modules."""
        # Create course structure
        course_path = temp_dir / "course_development" / "biol-1" / "course"
        mod1 = course_path / "module-01"
        mod1.mkdir(parents=True)
        (mod1 / "questions.md").write_text(
            "# Module 1 Questions\n\n"
            "### Part 1: Intro\n\n"
            "1.  **Basics**\n"
            "    *   What is biology and why is it important?\n"
            "    *   How do scientists use the scientific method?\n",
            encoding="utf-8",
        )

        results = renumber_questions_in_course(temp_dir, courses=["biol-1"])

        assert len(results["courses_processed"]) == 1
        assert results["files_converted"] == 1
        assert results["total_questions"] == 2
        assert results["errors"] == []

    def test_nonexistent_course_path(self, temp_dir):
        """Test that missing course path records error."""
        results = renumber_questions_in_course(temp_dir, courses=["nonexistent"])

        assert len(results["errors"]) == 1
        assert "not found" in results["errors"][0]

    def test_module_filter(self, temp_dir):
        """Test filtering to specific module."""
        course_path = temp_dir / "course_development" / "biol-1" / "course"
        for i in range(1, 4):
            mod = course_path / f"module-{i:02d}"
            mod.mkdir(parents=True)
            (mod / "questions.md").write_text(
                f"# Module {i}\n\n1. Question?\n",
                encoding="utf-8",
            )

        results = renumber_questions_in_course(
            temp_dir, courses=["biol-1"], module_filter="module-02"
        )

        # Should only process module-02
        assert len(results["courses_processed"]) == 1
        modules = results["courses_processed"][0]["modules"]
        assert len(modules) == 1
        assert modules[0]["name"] == "module-02"

    def test_dry_run_preserves_files(self, temp_dir):
        """Test dry_run does not modify any files."""
        course_path = temp_dir / "course_development" / "biol-1" / "course"
        mod1 = course_path / "module-01"
        mod1.mkdir(parents=True)
        original = (
            "# Questions\n\n"
            "### Part 1: Topics\n\n"
            "1.  **Topic**\n"
            "    *   How does photosynthesis work in plant cells?\n"
        )
        (mod1 / "questions.md").write_text(original, encoding="utf-8")

        results = renumber_questions_in_course(
            temp_dir, courses=["biol-1"], dry_run=True
        )

        assert results["files_converted"] == 1
        # File should be unchanged
        assert (mod1 / "questions.md").read_text() == original

    def test_missing_questions_file_skipped(self, temp_dir):
        """Test modules without questions.md are skipped."""
        course_path = temp_dir / "course_development" / "biol-1" / "course"
        mod1 = course_path / "module-01"
        mod1.mkdir(parents=True)
        # No questions.md created

        results = renumber_questions_in_course(temp_dir, courses=["biol-1"])

        assert results["files_converted"] == 0
        assert results["total_questions"] == 0
        assert results["errors"] == []
