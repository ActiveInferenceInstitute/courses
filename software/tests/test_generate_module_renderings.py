"""Exercise the real single-module producer without path or renderer substitutions."""
from scripts.generate_module_renderings import main


def test_one_selection_renders_each_authored_content_type(tmp_path):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    for name in ("module", "questions", "lab"):
        (module / f"{name}.md").write_text(f"# {name}\n\nAuthored {name} body.\n")
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--module", "1", "--formats", "md,txt"]) == 0
    expected = {
        f"{category}/01_systems-{name}.{fmt}"
        for category, name in [("lecture-content", "module"), ("study-guides", "questions"),
                               ("lab-protocols", "lab")]
        for fmt in ("md", "txt")
    }
    assert {str(path.relative_to(module / "output")) for path in (module / "output").rglob("*")
            if path.is_file()} == expected
    assert "Authored questions body" in (module / "output/study-guides/01_systems-questions.txt").read_text()


def test_missing_module_is_nonzero_without_outputs(tmp_path):
    course = tmp_path / "course_development/active_inference/01_philosophy"
    course.mkdir(parents=True)
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--module", "99", "--formats", "md"]) == 1
    assert not list(course.rglob("output"))
