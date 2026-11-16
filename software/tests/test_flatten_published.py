"""Flatten only known generated categories without destroying website assets."""
import subprocess
import sys
from pathlib import Path


def test_cli_dry_run_and_real_flatten_preserve_guides_and_website(tmp_path):
    published = tmp_path / "published"
    module = published / "ai-philosophy/01_systems"
    for folder in ("lecture-content", "website"):
        (module / folder).mkdir(parents=True)
    (module / "lecture-content/01_systems-module.md").write_text("# Source")
    (module / "lecture-content/README.md").write_text("authored guide")
    (module / "website/index.html").write_text("<html>site</html>")
    script = Path(__file__).resolve().parents[1] / "scripts/flatten_published.py"
    command = [sys.executable, str(script), "--path", str(published)]
    dry_run = subprocess.run([*command, "--dry-run"], capture_output=True, text=True, check=False)
    assert dry_run.returncode == 0, dry_run.stderr
    assert (module / "lecture-content/01_systems-module.md").is_file()
    actual = subprocess.run(command, capture_output=True, text=True, check=False)
    assert actual.returncode == 0, actual.stderr
    assert (module / "01_systems-module.md").read_text() == "# Source"
    assert (module / "website/index.html").read_text() == "<html>site</html>"
    assert (module / "lecture-content/README.md").read_text() == "authored guide"
