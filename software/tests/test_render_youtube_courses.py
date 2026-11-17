"""YouTube CLI regressions using existing local transcripts only."""
import json

from scripts.render_youtube_courses import main
from src.youtube_transcript.config import TRANSCRIPTS_SUBDIR


def _manifest(root):
    courses = root / "course_development/youtube"
    courses.mkdir(parents=True)
    manifest = {"total_playlists": 1, "playlists": {
        "local-course": {"title": "Local", "id": "playlist", "url": "https://example.invalid",
                         "video_count": 1,
                         "videos": [{"id": "video_1", "title": "Intro", "playlist_index": 0}]},
    }}
    path = courses / "youtube_courses.json"
    path.write_text(json.dumps(manifest))
    return courses, path


def test_local_scaffold_and_render_success(tmp_path):
    courses, _ = _manifest(tmp_path)
    transcripts = tmp_path / "transcripts-root"
    source = transcripts / TRANSCRIPTS_SUBDIR / "video_1.txt"
    source.parent.mkdir(parents=True)
    source.write_text("A local authored transcript.")
    assert main(["--repo-root", str(tmp_path), "--transcript-dir", str(transcripts),
                 "--formats", "md", "--skip-whisper"]) == 0
    module = courses / "local-course/01_intro"
    output = module / "output/lecture-content/01_intro-module.md"
    assert "A local authored transcript." in output.read_text()
    assert (module / "output/.render-receipt.json").is_file()


def test_empty_local_transcript_is_a_failed_scaffold_without_network(tmp_path):
    _, _ = _manifest(tmp_path)
    transcripts = tmp_path / "transcripts-root"
    source = transcripts / TRANSCRIPTS_SUBDIR / "video_1.txt"
    source.parent.mkdir(parents=True)
    source.write_text("")
    assert main(["--repo-root", str(tmp_path), "--transcript-dir", str(transcripts),
                 "--formats", "md", "--skip-whisper", "--skip-render"]) == 1


def test_render_failure_and_empty_selection_are_nonzero(tmp_path):
    courses, _ = _manifest(tmp_path)
    module = courses / "local-course/01_intro"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Intro\n\nContent.")
    (module / "output").write_text("blocking file")
    args = ["--repo-root", str(tmp_path), "--skip-scaffold", "--formats", "md"]
    assert main(args) == 1
    assert main([*args, "--course", "not-present"]) == 1
    assert (module / "output").read_text() == "blocking file"


def test_dry_run_list_playlists_is_local_and_nonmutating(tmp_path):
    courses, manifest = _manifest(tmp_path)
    before = manifest.read_bytes()
    assert main(["--repo-root", str(tmp_path), "--list-playlists", "--dry-run",
                 "--formats", "md", "--course", "local-course"]) == 0
    assert manifest.read_bytes() == before
    assert list(courses.iterdir()) == [manifest]
