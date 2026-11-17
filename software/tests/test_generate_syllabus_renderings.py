"""File-style syllabi must never cause their entire course root to be rendered."""
from scripts.generate_syllabus_renderings import main


def test_file_syllabus_is_reserved_for_publication(tmp_path, capsys):
    course = tmp_path / "course_development/active_inference/01_philosophy"
    course.mkdir(parents=True)
    (course / "syllabus.md").write_text("# Syllabus\n\nAuthored overview.")
    (course / "README.md").write_text("# Guide\n\nDo not render.")
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--formats", "md"]) == 0
    assert "copied during publication" in capsys.readouterr().out
    assert not (course / "output").exists()
    assert (course / "README.md").read_text() == "# Guide\n\nDo not render."


def test_missing_syllabus_fails_without_creating_outputs(tmp_path):
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--formats", "md"]) == 1
    assert list(tmp_path.iterdir()) == []
