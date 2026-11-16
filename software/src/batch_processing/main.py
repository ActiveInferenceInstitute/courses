"""Main functions for batch processing."""

import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .logging_config import get_logger
from .utils import (
    ensure_output_directory,
    find_audio_files,
    find_markdown_files,
    get_relative_output_path,
    preprocess_lab_markdown,
    should_process_file,
)
import time
import tempfile

logger = get_logger()


def process_module_to_pdf(module_path: str, output_dir: str) -> List[str]:
    """Convert all Markdown files in a module to PDF.

    Args:
        module_path: Path to module directory
        output_dir: Output directory for PDF files

    Returns:
        List of output PDF file paths

    Raises:
        ValueError: If module path doesn't exist
        OSError: If PDF conversion fails
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    output_directory = Path(output_dir)
    ensure_output_directory(output_directory)

    # Find all Markdown files
    markdown_files = find_markdown_files(module_dir)

    # Filter out files in skip directories
    markdown_files = [f for f in markdown_files if should_process_file(f, config.SKIP_DIRECTORIES)]

    output_files = []

    for md_file in markdown_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(md_file, module_dir, output_directory)
            output_file = output_file.with_suffix(".pdf")

            # Ensure output directory exists
            ensure_output_directory(output_file.parent)

            # Convert to PDF
            from ..markdown_to_pdf.main import render_markdown_to_pdf

            render_markdown_to_pdf(str(md_file), str(output_file))
            output_files.append(str(output_file))
        except Exception as e:
            raise OSError(f"Error converting {md_file} to PDF: {e}") from e

    return output_files


def process_module_to_audio(module_path: str, output_dir: str) -> List[str]:
    """Convert all text/Markdown files in a module to audio.

    Args:
        module_path: Path to module directory
        output_dir: Output directory for audio files

    Returns:
        List of output audio file paths

    Raises:
        ValueError: If module path doesn't exist
        OSError: If audio generation fails
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    output_directory = Path(output_dir)
    ensure_output_directory(output_directory)

    # Find all Markdown and text files
    text_files = find_markdown_files(module_dir)
    text_files.extend(module_dir.rglob("*.txt"))

    # Filter out files in skip directories
    text_files = [f for f in text_files if should_process_file(f, config.SKIP_DIRECTORIES)]

    output_files = []

    for text_file in text_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(text_file, module_dir, output_directory)
            output_file = output_file.with_suffix(".mp3")

            # Ensure output directory exists
            ensure_output_directory(output_file.parent)

            # Read and extract text
            from ..text_to_speech.utils import (
                extract_text_from_markdown,
                read_text_file,
            )

            content = read_text_file(text_file)
            if text_file.suffix in [".md", ".markdown"]:
                content = extract_text_from_markdown(content)

            # Generate speech
            from ..text_to_speech.main import generate_speech

            generate_speech(content, str(output_file))
            output_files.append(str(output_file))
        except Exception as e:
            raise OSError(f"Error converting {text_file} to audio: {e}") from e

    return output_files


def process_module_to_text(module_path: str, output_dir: str) -> List[str]:
    """Transcribe all audio files in a module to text.

    Args:
        module_path: Path to module directory
        output_dir: Output directory for text files

    Returns:
        List of output text file paths

    Raises:
        ValueError: If module path doesn't exist
        OSError: If transcription fails
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    output_directory = Path(output_dir)
    ensure_output_directory(output_directory)

    # Find all audio files
    audio_files = find_audio_files(module_dir)

    # Filter out files in skip directories
    audio_files = [f for f in audio_files if should_process_file(f, config.SKIP_DIRECTORIES)]

    output_files = []

    for audio_file in audio_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(audio_file, module_dir, output_directory)
            output_file = output_file.with_suffix(".txt")

            # Ensure output directory exists
            ensure_output_directory(output_file.parent)

            # Transcribe audio
            from ..speech_to_text.main import transcribe_audio

            transcribe_audio(str(audio_file), str(output_file))
            output_files.append(str(output_file))
        except Exception as e:
            raise OSError(f"Error transcribing {audio_file}: {e}") from e

    return output_files


def generate_module_media(module_path: str, output_dir: str) -> Dict[str, Any]:
    """Generate all media formats for a module (PDF, audio, text transcriptions).

    Args:
        module_path: Path to module directory
        output_dir: Base output directory for all media

    Returns:
        Dictionary with results for each media type:
        - pdf_files: List of generated PDF files
        - audio_files: List of generated audio files
        - text_files: List of generated text transcriptions
        - errors: List of errors encountered

    Raises:
        ValueError: If module path doesn't exist
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    base_output = Path(output_dir)
    ensure_output_directory(base_output)

    results: Dict[str, Any] = {
        "pdf_files": [],
        "audio_files": [],
        "text_files": [],
        "errors": [],
    }

    # Generate PDFs
    try:
        pdf_output = base_output / config.OUTPUT_DIRECTORIES["pdf"]
        results["pdf_files"] = process_module_to_pdf(module_path, str(pdf_output))
    except Exception as e:
        results["errors"].append(f"PDF generation error: {e}")

    # Generate audio
    try:
        audio_output = base_output / config.OUTPUT_DIRECTORIES["audio"]
        results["audio_files"] = process_module_to_audio(module_path, str(audio_output))
    except Exception as e:
        results["errors"].append(f"Audio generation error: {e}")

    # Transcribe audio to text
    try:
        text_output = base_output / config.OUTPUT_DIRECTORIES["text"]
        # First generate audio if not already done
        if not results["audio_files"]:
            audio_output = base_output / config.OUTPUT_DIRECTORIES["audio"]
            results["audio_files"] = process_module_to_audio(module_path, str(audio_output))
        # Then transcribe the generated audio
        if results["audio_files"]:
            results["text_files"] = process_module_to_text(str(audio_output), str(text_output))
    except Exception as e:
        results["errors"].append(f"Text transcription error: {e}")

    return results


def _render_artifacts(artifacts: List[dict]) -> Dict[str, Any]:
    """Render each admitted artifact once; retain every per-artifact failure."""
    results: Dict[str, Any] = {"files": [], "errors": [], "by_type": {},
                               "by_format": {fmt: [] for fmt in config.AVAILABLE_FORMATS},
                               "summary": {fmt: 0 for fmt in config.AVAILABLE_FORMATS}}
    for artifact in artifacts:
        source = artifact["source"]
        destination = artifact["destination"]
        fmt = artifact["format"]
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if artifact["kind"] == "website":
                process_module_website(str(source), str(destination.parent))
            elif artifact["kind"] == "lab":
                from ..lab_manual.main import render_lab_manual

                render_lab_manual(str(source), str(destination), output_format=fmt)
            else:
                # Preprocessing remains local to lab renderings and never rewrites source.
                with tempfile.TemporaryDirectory(prefix="courses-render-") as temporary:
                    render_file = source
                    if artifact.get("category") == "lab-protocols":
                        render_file = Path(temporary) / source.name
                        render_file.write_text(preprocess_lab_markdown(source.read_text(encoding="utf-8")), encoding="utf-8")
                    if fmt == "md":
                        shutil.copy2(render_file, destination)
                    elif fmt == "txt":
                        from ..text_to_speech.utils import extract_text_from_markdown

                        destination.write_text(extract_text_from_markdown(render_file.read_text(encoding="utf-8")), encoding="utf-8")
                    elif fmt == "mp3":
                        from ..text_to_speech.main import generate_speech
                        from ..text_to_speech.utils import extract_text_from_markdown

                        generate_speech(extract_text_from_markdown(render_file.read_text(encoding="utf-8")), str(destination))
                        if config.TTS_RATE_LIMIT_DELAY > 0:
                            time.sleep(config.TTS_RATE_LIMIT_DELAY)
                    elif fmt == "pdf":
                        from ..markdown_to_pdf.main import render_markdown_to_pdf

                        render_markdown_to_pdf(str(render_file), str(destination))
                    else:
                        from ..format_conversion.main import convert_file

                        convert_file(str(render_file), fmt, str(destination))
            if not destination.is_file() or destination.stat().st_size == 0:
                raise OSError(f"Renderer produced no nonempty artifact: {destination}")
            results["files"].append(str(destination))
            results["by_format"][fmt].append(str(destination))
            results["summary"][fmt] += 1
            if "category" in artifact:
                results["by_type"].setdefault(artifact["category"], []).append(str(destination))
        except Exception as error:
            message = f"{source} -> {destination}: {error}"
            logger.error(message)
            results["errors"].append(message)
    return results


def process_module_by_type(module_path: str, output_dir: str,
                           formats: Optional[List[str]] = None, *, skip_labs: bool = False) -> Dict[str, Any]:
    from .utils import module_artifacts

    module = Path(module_path)
    if not module.is_dir():
        raise ValueError(f"Module path does not exist: {module}")
    artifacts = module_artifacts(module, config.AVAILABLE_FORMATS if formats is None else formats,
                                 output_dir=Path(output_dir), skip_labs=skip_labs)
    return _render_artifacts(artifacts)


def process_syllabus(syllabus_path: str, output_dir: str,
                     formats: Optional[List[str]] = None) -> Dict[str, Any]:
    from .utils import document_artifacts, get_formats_to_process

    source = Path(syllabus_path)
    if not source.is_dir():
        raise ValueError(f"Syllabus directory does not exist: {source}")
    active = get_formats_to_process(",".join(config.AVAILABLE_FORMATS if formats is None else formats))
    return _render_artifacts(document_artifacts(source, Path(output_dir), active, "syllabus"))


def clear_all_outputs(repo_root: Path, *, plans: List[dict]) -> Dict[str, Any]:
    """Clear only exact admitted artifact paths. An explicit plan is mandatory.

    Never recurse-delete an output directory, guide, hidden file, unrelated
    format, course, unit or module. Validate all targets before the first unlink.
    """
    from .utils import require_contained

    paths = sorted({a["destination"] for plan in plans for a in plan["artifacts"]
                    if a["destination"].name not in ("README.md", "AGENTS.md")
                    and not any(part.startswith(".") for part in a["destination"].relative_to(repo_root).parts)})
    for path in paths:
        require_contained(path, repo_root)
        if path.exists() and not path.is_file():
            raise ValueError(f"Not a regular output file: {path}")
    result: Dict[str, Any] = {"cleared_directories": [], "total_files_removed": 0, "errors": []}
    cleared = set()
    for path in paths:
        try:
            if path.is_file():
                path.unlink()
                cleared.add(str(path.parent))
                result["total_files_removed"] += 1
        except OSError as error:
            result["errors"].append(f"{path}: {error}")
    result["cleared_directories"] = sorted(cleared)
    return result


def generate_selected_outputs(plans: List[dict]) -> Dict[str, Any]:
    """Consume the exact pre-admitted plan shared by cleanup and validation."""
    return _render_artifacts([artifact for plan in plans for artifact in plan["artifacts"]])


def process_course_modules(course_path: Path, course_name: str,
                           module_filter: Optional[int] = None, generate_website: bool = True,
                           formats: Optional[List[str]] = None, max_module: Optional[int] = None,
                           *, unit_filter: Optional[str] = None, skip_labs: bool = False) -> Dict[str, Any]:
    from .utils import module_artifacts, select_modules

    modules = select_modules(course_path, module_filter=module_filter, unit_filter=unit_filter,
                             max_module=max_module)
    result: Dict[str, Any] = {"course": course_name, "modules": [], "errors": []}
    for module in modules:
        artifacts = module_artifacts(module, config.AVAILABLE_FORMATS if formats is None else formats,
                                     skip_labs=skip_labs)
        if generate_website:
            artifacts.append({"source": module, "destination": module / "output/website/index.html",
                              "kind": "website", "format": "html"})
        started = time.monotonic()
        rendered = _render_artifacts(artifacts)
        identity = module.relative_to(course_path).as_posix()
        result["modules"].append({"name": identity, "outputs": rendered, "duration": time.monotonic() - started})
        result["errors"].extend(rendered["errors"])
    return result


def process_course_syllabus(course_path: Path, course_name: str,
                            formats: Optional[List[str]] = None,
                            course_id: Optional[str] = None) -> Dict[str, Any]:
    from .utils import syllabus_artifacts, get_formats_to_process

    active = get_formats_to_process(",".join(config.AVAILABLE_FORMATS if formats is None else formats))
    artifacts = syllabus_artifacts(course_path, active, course_id)
    result = _render_artifacts(artifacts)
    return {"processed": bool(artifacts), "results": result, "errors": result["errors"]}


def process_course_labs(course_path: Path, course_name: str, formats: Optional[List[str]] = None,
                        max_lab: Optional[int] = None, course_id: Optional[str] = None) -> Dict[str, Any]:
    from .utils import lab_artifacts, get_formats_to_process

    active = get_formats_to_process(",".join(config.AVAILABLE_FORMATS if formats is None else formats))
    artifacts = lab_artifacts(course_path, active, course_id, max_lab)
    result = _render_artifacts(artifacts)
    result["processed"] = bool(artifacts)
    return result


def process_course_practice_tests(course_path: Path, course_name: str,
                                  formats: Optional[List[str]] = None) -> Dict[str, Any]:
    from .utils import practice_artifacts, get_formats_to_process

    active = get_formats_to_process(",".join(config.AVAILABLE_FORMATS if formats is None else formats))
    artifacts = practice_artifacts(course_path, active)
    result = _render_artifacts(artifacts)
    result["processed"] = bool(artifacts)
    return result


def process_module_website(module_path: str, output_dir: Optional[str] = None) -> str:
    from ..html_website.main import generate_module_website

    return generate_module_website(module_path, output_dir)
