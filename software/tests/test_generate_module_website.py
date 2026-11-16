"""Real website selection and numeric ambiguity regressions."""
from scripts.generate_module_website import main


def test_website_uses_selected_unit_only(tmp_path):
    course = tmp_path / "course_development/active_inference"
    for unit in ("01_philosophy", "02_cognitive_science"):
        module = course / unit / "01_systems"
        module.mkdir(parents=True)
        (module / "module.md").write_text("# Systems\n\nA real module.")
    args = ["--repo-root", str(tmp_path), "--course", "active-inference", "--module", "1"]
    assert main(args) == 1
    assert not list(course.rglob("index.html"))
    assert main([*args, "--unit", "01_philosophy"]) == 0
    page = course / "01_philosophy/01_systems/output/website/index.html"
    assert "<html" in page.read_text().lower()
    assert not (course / "02_cognitive_science/01_systems/output").exists()
