"""Main functions for batch processing."""

import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .logging_config import get_logger
from .log_style import format_summary, FORMAT_EMOJI, STATUS_EMOJI, CONTENT_EMOJI
from .utils import (
    ensure_output_directory,
    find_audio_files,
    find_markdown_files,
    find_modules_for_course,
    get_course_id_from_path,
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
    markdown_files = [
        f for f in markdown_files if should_process_file(f, config.SKIP_DIRECTORIES)
    ]

    output_files = []

    for md_file in markdown_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(
                md_file, module_dir, output_directory
            )
            output_file = output_file.with_suffix(".pdf")

            # Ensure output directory exists
            ensure_output_directory(output_file.parent)

            # Convert to PDF
            from ..markdown_to_pdf.main import render_markdown_to_pdf

            render_markdown_to_pdf(str(md_file), str(output_file))
            output_files.append(str(output_file))
        except Exception as e:
            print(f"Error converting {md_file} to PDF: {e}")
            continue

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
    text_files = [
        f for f in text_files if should_process_file(f, config.SKIP_DIRECTORIES)
    ]

    output_files = []

    for text_file in text_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(
                text_file, module_dir, output_directory
            )
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
            print(f"Error converting {text_file} to audio: {e}")
            continue

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
    audio_files = [
        f for f in audio_files if should_process_file(f, config.SKIP_DIRECTORIES)
    ]

    output_files = []

    for audio_file in audio_files:
        try:
            # Get output path maintaining structure
            output_file = get_relative_output_path(
                audio_file, module_dir, output_directory
            )
            output_file = output_file.with_suffix(".txt")

            # Ensure output directory exists
            ensure_output_directory(output_file.parent)

            # Transcribe audio
            from ..speech_to_text.main import transcribe_audio

            transcribe_audio(str(audio_file), str(output_file))
            output_files.append(str(output_file))
        except Exception as e:
            print(f"Error transcribing {audio_file}: {e}")
            continue

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

    results = {
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
            results["audio_files"] = process_module_to_audio(
                module_path, str(audio_output)
            )
        # Then transcribe the generated audio
        if results["audio_files"]:
            results["text_files"] = process_module_to_text(
                str(audio_output), str(text_output)
            )
    except Exception as e:
        results["errors"].append(f"Text transcription error: {e}")

    return results


def process_module_by_type(
    module_path: str,
    output_dir: str,
    formats: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Process module files by curriculum element type and generate all format renderings.

    Organizes outputs by curriculum element type (assignments, lab-protocols,
    lecture-content, study-guides) with all formats (PDF, MP3, DOCX, HTML, TXT).

    Args:
        module_path: Path to module directory
        output_dir: Base output directory for all renderings
        formats: Optional list of formats to generate (e.g. ["pdf", "html"]).
                 When None, all formats are generated.

    Returns:
        Dictionary with results:
        - by_type: Dict mapping curriculum type to list of generated files
        - summary: Dict with counts of generated files by format
        - errors: List of errors encountered

    Raises:
        ValueError: If module path doesn't exist
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    logger.info(f"Processing module: {module_dir.name}")
    base_output = Path(output_dir)
    ensure_output_directory(base_output)

    # Determine which formats to generate
    all_formats = {"pdf", "mp3", "docx", "html", "txt", "md"}
    active_formats = set(formats) if formats is not None else all_formats

    # Curriculum element type mapping
    type_mapping = {
        "assignment": "assignments",
        "lab-protocol": "lab-protocols",
        "lecture-content": "lecture-content",
        "study-guide": "study-guides",
    }

    # Find all sample markdown files
    markdown_files = find_markdown_files(module_dir)
    files_to_process = [f for f in markdown_files if f.name.startswith(config.SAMPLE_FILE_PREFIX)]
    
    # Process root-level source files (keys-to-success.md, questions.md)
    root_md_files = [f for f in module_dir.glob("*.md") 
                     if not f.name.startswith("README") and not f.name.startswith("AGENTS")]
    files_to_process.extend(root_md_files)
    
    # Process assignment files
    assignments_dir = module_dir / "assignments"
    if assignments_dir.exists():
        assignment_files = list(assignments_dir.glob("*.md"))
        files_to_process.extend(assignment_files)

    # Process resource files
    resources_dir = module_dir / "resources"
    if resources_dir.exists():
        resource_files = list(resources_dir.glob("*.md"))
        files_to_process.extend(resource_files)

    logger.debug(f"Found {len(files_to_process)} markdown files to process")

    results = {
        "by_type": {t: [] for t in type_mapping.values()},
        "summary": {"pdf": 0, "mp3": 0, "docx": 0, "html": 0, "txt": 0, "md": 0},
        "errors": [],
    }

    for md_file in files_to_process:
        try:
            # Detect curriculum element type from filename
            file_type = None
            output_subdir = None

            if "assignment" in md_file.name:
                file_type = "assignment"
                output_subdir = "assignments"
            elif "lab-protocol" in md_file.name:
                file_type = "lab-protocol"
                output_subdir = "lab-protocols"
            elif "lecture-content" in md_file.name:
                file_type = "lecture-content"
                output_subdir = "lecture-content"
            elif "study-guide" in md_file.name:
                file_type = "study-guide"
                output_subdir = "study-guides"
            elif any(pattern in md_file.name for pattern in config.CONTENT_TYPE_PATTERNS):
                file_type = "study-guide"
                output_subdir = "study-guides"
            elif md_file.name == config.QUESTIONS_FILENAME:
                file_type = "study-guide"
                output_subdir = "study-guides"
            elif md_file.parent.name == "assignments":
                file_type = "assignment"
                output_subdir = "assignments"
            # --- Active Inference content types ---
            elif md_file.name == "module.md":
                file_type = "lecture-content"
                output_subdir = "lecture-content"
            elif md_file.name == "practice_quiz.md":
                file_type = "study-guide"
                output_subdir = "study-guides"
            elif md_file.name == "lab.md":
                file_type = "lab-protocol"
                output_subdir = "lab-protocols"

            if not output_subdir:
                logger.debug(f"Skipping file (no type match): {md_file.name}")
                continue  # Skip files that don't match known types

            # Create output subdirectory for this type
            type_output_dir = base_output / output_subdir
            ensure_output_directory(type_output_dir)
            logger.debug(f"Processing {file_type}: {md_file.name} -> {output_subdir}/")

            # Base filename without extension - prefix with module name for unique identification
            base_name = md_file.stem
            # Extract module name (e.g., "module-01-topic" or "module-01")
            module_name = module_dir.name
            # Only add prefix if file is not already prefixed with module name
            if not base_name.startswith(module_name) and not base_name.startswith("module-"):
                base_name = f"{module_name}-{base_name}"

            # Preprocess lab protocol files to expand {fill:textarea} directives
            render_file = md_file
            _temp_file = None
            if file_type == "lab-protocol":
                try:
                    raw_content = md_file.read_text(encoding="utf-8")
                    processed_content = preprocess_lab_markdown(raw_content)
                    if processed_content != raw_content:
                        _temp_file = tempfile.NamedTemporaryFile(
                            mode="w", suffix=".md", delete=False, encoding="utf-8"
                        )
                        _temp_file.write(processed_content)
                        _temp_file.close()
                        render_file = Path(_temp_file.name)
                        logger.debug(f"Preprocessed lab directives for {md_file.name}")
                except Exception as e:
                    logger.warning(f"Lab preprocessing failed for {md_file.name}: {e}")

            # Generate PDF
            if "pdf" in active_formats:
                try:
                    pdf_file = type_output_dir / f"{base_name}.pdf"
                    from ..markdown_to_pdf.main import render_markdown_to_pdf

                    logger.debug(f"Generating PDF: {pdf_file.name}")
                    render_markdown_to_pdf(str(render_file), str(pdf_file))
                    results["by_type"][output_subdir].append(str(pdf_file))
                    results["summary"]["pdf"] += 1
                except Exception as e:
                    error_msg = f"PDF generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate Audio (MP3)
            if "mp3" in active_formats:
                try:
                    audio_file = type_output_dir / f"{base_name}.mp3"
                    from ..text_to_speech.utils import (
                        extract_text_from_markdown,
                        read_text_file,
                    )
                    from ..text_to_speech.main import generate_speech

                    logger.debug(f"Generating MP3: {audio_file.name}")
                    content = read_text_file(md_file)
                    text_content = extract_text_from_markdown(content)
                    generate_speech(text_content, str(audio_file))
                    time.sleep(2)  # Add delay to avoid 429 errors
                    results["by_type"][output_subdir].append(str(audio_file))
                    results["summary"]["mp3"] += 1
                except Exception as e:
                    error_msg = f"Audio generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate DOCX
            if "docx" in active_formats:
                try:
                    docx_file = type_output_dir / f"{base_name}.docx"
                    from ..format_conversion.main import convert_file

                    logger.debug(f"Generating DOCX: {docx_file.name}")
                    convert_file(str(render_file), "docx", str(docx_file))
                    results["by_type"][output_subdir].append(str(docx_file))
                    results["summary"]["docx"] += 1
                except Exception as e:
                    error_msg = f"DOCX generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate HTML
            if "html" in active_formats:
                try:
                    html_file = type_output_dir / f"{base_name}.html"
                    from ..format_conversion.main import convert_file as convert_file_func
                    logger.debug(f"Generating HTML: {html_file.name}")
                    convert_file_func(str(render_file), "html", str(html_file))
                    results["by_type"][output_subdir].append(str(html_file))
                    results["summary"]["html"] += 1
                except Exception as e:
                    error_msg = f"HTML generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate TXT (extracted text)
            if "txt" in active_formats:
                try:
                    txt_file = type_output_dir / f"{base_name}.txt"
                    from ..text_to_speech.utils import (
                        extract_text_from_markdown,
                        read_text_file,
                    )

                    logger.debug(f"Generating TXT: {txt_file.name}")
                    content = read_text_file(render_file)
                    text_content = extract_text_from_markdown(content)
                    txt_file.write_text(text_content, encoding="utf-8")
                    results["by_type"][output_subdir].append(str(txt_file))
                    results["summary"]["txt"] += 1
                except Exception as e:
                    error_msg = f"TXT generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate MD (copy source markdown with standardized name)
            if "md" in active_formats:
                try:
                    md_output_file = type_output_dir / f"{base_name}.md"
                    logger.debug(f"Generating MD: {md_output_file.name}")
                    import shutil
                    shutil.copy2(str(render_file), str(md_output_file))
                    results["by_type"][output_subdir].append(str(md_output_file))
                    results["summary"]["md"] += 1
                except Exception as e:
                    error_msg = f"MD copy failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Clean up temp file for preprocessed labs
            if _temp_file is not None:
                try:
                    import os
                    os.unlink(_temp_file.name)
                except OSError:
                    pass

        except Exception as e:
            logger.error(f"Processing failed for {md_file.name}: {e}", exc_info=True)
            results["errors"].append(f"Processing failed for {md_file.name}: {e}")

    total_outputs = sum(results["summary"].values())
    logger.info(f"Processed module {module_dir.name}: {len(files_to_process)} files, {total_outputs} outputs generated")
    if results["errors"]:
        logger.warning(f"Module processing completed with {len(results['errors'])} errors")

    return results


def process_syllabus(
    syllabus_path: str,
    output_dir: str,
    formats: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Process syllabus files and generate all format renderings.

    Organizes outputs flat in the output directory (same structure as module assignments),
    with all formats (PDF, MP3, DOCX, HTML, TXT) in the same directory.

    Args:
        syllabus_path: Path to syllabus directory
        output_dir: Base output directory for all renderings
        formats: Optional list of formats to generate (e.g. ["pdf", "html"]).
                 When None, all formats are generated.

    Returns:
        Dictionary with results:
        - by_format: Dict mapping format type to list of generated files
        - summary: Dict with counts of generated files by format
        - errors: List of errors encountered

    Raises:
        ValueError: If syllabus path doesn't exist
    """
    syllabus_dir = Path(syllabus_path)
    if not syllabus_dir.exists():
        raise ValueError(f"Syllabus path does not exist: {syllabus_path}")

    logger.info(f"Processing syllabus: {syllabus_dir.name}")
    base_output = Path(output_dir)
    ensure_output_directory(base_output)

    # Determine which formats to generate
    all_formats = {"pdf", "mp3", "docx", "html", "txt", "md"}
    active_formats = set(formats) if formats is not None else all_formats

    # Find all markdown files in syllabus directory (excluding README and AGENTS)
    markdown_files = find_markdown_files(syllabus_dir)
    syllabus_files = [
        f for f in markdown_files
        if not f.name.startswith("README") and not f.name.startswith("AGENTS")
    ]

    results = {
        "by_format": {"pdf": [], "mp3": [], "docx": [], "html": [], "txt": [], "md": []},
        "summary": {"pdf": 0, "mp3": 0, "docx": 0, "html": 0, "txt": 0, "md": 0},
        "errors": [],
    }

    for md_file in syllabus_files:
        try:
            # Base filename without extension
            base_name = md_file.stem

            # Generate PDF
            if "pdf" in active_formats:
                try:
                    pdf_file = base_output / f"{base_name}.pdf"
                    from ..markdown_to_pdf.main import render_markdown_to_pdf

                    logger.debug(f"Generating PDF: {pdf_file.name}")
                    render_markdown_to_pdf(str(md_file), str(pdf_file))
                    results["by_format"]["pdf"].append(str(pdf_file))
                    results["summary"]["pdf"] += 1
                except Exception as e:
                    error_msg = f"PDF generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate Audio (MP3)
            if "mp3" in active_formats:
                try:
                    audio_file = base_output / f"{base_name}.mp3"
                    from ..text_to_speech.utils import (
                        extract_text_from_markdown,
                        read_text_file,
                    )
                    from ..text_to_speech.main import generate_speech

                    logger.debug(f"Generating MP3: {audio_file.name}")
                    content = read_text_file(md_file)
                    text_content = extract_text_from_markdown(content)
                    generate_speech(text_content, str(audio_file))
                    time.sleep(2)  # Add delay to avoid 429 errors
                    results["by_format"]["mp3"].append(str(audio_file))
                    results["summary"]["mp3"] += 1
                except Exception as e:
                    error_msg = f"Audio generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate DOCX
            if "docx" in active_formats:
                try:
                    docx_file = base_output / f"{base_name}.docx"
                    from ..format_conversion.main import convert_file

                    logger.debug(f"Generating DOCX: {docx_file.name}")
                    convert_file(str(md_file), "docx", str(docx_file))
                    results["by_format"]["docx"].append(str(docx_file))
                    results["summary"]["docx"] += 1
                except Exception as e:
                    error_msg = f"DOCX generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate HTML
            if "html" in active_formats:
                try:
                    html_file = base_output / f"{base_name}.html"
                    from ..format_conversion.main import convert_file as convert_file_func
                    logger.debug(f"Generating HTML: {html_file.name}")
                    convert_file_func(str(md_file), "html", str(html_file))
                    results["by_format"]["html"].append(str(html_file))
                    results["summary"]["html"] += 1
                except Exception as e:
                    error_msg = f"HTML generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate TXT (extracted text)
            if "txt" in active_formats:
                try:
                    txt_file = base_output / f"{base_name}.txt"
                    from ..text_to_speech.utils import (
                        extract_text_from_markdown,
                        read_text_file,
                    )

                    logger.debug(f"Generating TXT: {txt_file.name}")
                    content = read_text_file(md_file)
                    text_content = extract_text_from_markdown(content)
                    txt_file.write_text(text_content, encoding="utf-8")
                    results["by_format"]["txt"].append(str(txt_file))
                    results["summary"]["txt"] += 1
                except Exception as e:
                    error_msg = f"TXT generation failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

            # Generate MD (copy source markdown with standardized name)
            if "md" in active_formats:
                try:
                    md_output_file = base_output / f"{base_name}.md"
                    logger.debug(f"Generating MD: {md_output_file.name}")
                    import shutil
                    shutil.copy2(str(md_file), str(md_output_file))
                    results["by_format"]["md"].append(str(md_output_file))
                    results["summary"]["md"] += 1
                except Exception as e:
                    error_msg = f"MD copy failed for {md_file.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(error_msg)

        except Exception as e:
            logger.error(f"Processing failed for {md_file.name}: {e}", exc_info=True)
            results["errors"].append(f"Processing failed for {md_file.name}: {e}")

    logger.info(f"Processed syllabus: {len(syllabus_files)} files, {sum(results['summary'].values())} outputs generated")
    if results["errors"]:
        logger.warning(f"Syllabus processing completed with {len(results['errors'])} errors")

    return results


def clear_all_outputs(repo_root: Path) -> Dict[str, Any]:
    """Clear all output directories before regeneration.

    Removes all files and subdirectories within output directories while
    preserving the output directory structure itself.

    Uses COURSE_REGISTRY for dynamic course discovery.

    Args:
        repo_root: Root path of the repository

    Returns:
        Dictionary with summary:
        - cleared_directories: List of cleared directory paths
        - total_files_removed: Total count of files removed
        - errors: List of errors encountered
    """
    logger.info("Starting output clearing process")
    results = {
        "cleared_directories": [],
        "total_files_removed": 0,
        "errors": [],
    }

    # Find all output directories using registry
    output_dirs = []
    for course_id, reg in config.COURSE_REGISTRY.items():
        course_path = repo_root / reg["rel_path"]
        if not course_path.exists():
            logger.debug(f"Course directory not found: {course_path}")
            continue

        # Module output directories (uses registry-aware discovery)
        modules = find_modules_for_course(course_path, course_id)
        for module_dir in modules:
            output_dir = module_dir / "output"
            if output_dir.exists():
                output_dirs.append(output_dir)

        # Syllabus output directory
        syllabus_location = reg.get("syllabus_location", "syllabus")
        if not syllabus_location.endswith(".md"):
            # It's a directory
            syllabus_path = course_path / syllabus_location / "output"
            if syllabus_path.exists():
                output_dirs.append(syllabus_path)

        # Labs output directory
        if reg.get("has_course_subdir", True):
            labs_output_path = course_path / "course" / "labs" / "output"
        else:
            labs_output_path = course_path / "labs" / "output"
        if labs_output_path.exists():
            output_dirs.append(labs_output_path)

    logger.info(f"Found {len(output_dirs)} output directories to clear")

    for output_dir in output_dirs:
        try:
            # Count files before clearing
            file_count = sum(1 for _ in output_dir.rglob("*") if _.is_file())
            dir_count = sum(1 for _ in output_dir.rglob("*") if _.is_dir())

            if file_count == 0 and dir_count == 0:
                logger.debug(f"Output directory already empty: {output_dir}")
                continue

            # Remove all contents but keep the directory
            for item in output_dir.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)

            results["cleared_directories"].append(str(output_dir))
            results["total_files_removed"] += file_count

            # Use DEBUG for per-directory details to reduce console verbosity
            logger.debug(f"Cleared {file_count} files and {dir_count} directories from {output_dir.relative_to(repo_root)}")

        except Exception as e:
            error_msg = f"Failed to clear {output_dir}: {e}"
            logger.error(error_msg, exc_info=True)
            results["errors"].append(error_msg)

    # Compact per-course summary
    for course_id, reg in config.COURSE_REGISTRY.items():
        count = sum(1 for d in results["cleared_directories"] if reg["rel_path"] in d)
        if count > 0:
            logger.info(f"  {reg['display_name']}: {count} directories")
    logger.info(f"Output clearing completed: {len(results['cleared_directories'])} directories, {results['total_files_removed']} files removed")
    if results["errors"]:
        logger.warning(f"Output clearing completed with {len(results['errors'])} errors")

    return results


def process_course_modules(
    course_path: Path,
    course_name: str,
    module_filter: Optional[int] = None,
    generate_website: bool = True,
    formats: Optional[List[str]] = None,
    max_module: Optional[int] = None,
) -> Dict[str, Any]:
    """Process all modules for a course.

    Args:
        course_path: Path to course directory
        course_name: Name of the course
        module_filter: If specified, only process this module number
        generate_website: Whether to generate HTML websites for modules
        formats: Optional list of formats to generate (e.g. ["pdf", "html"])
        max_module: If specified, only process modules 1 through max_module

    Returns:
        Dictionary with processing results
    """
    from ..module_organization.utils import matches_module_number

    # Use registry-aware module discovery
    course_id = get_course_id_from_path(str(course_path.relative_to(course_path.parents[len(course_path.parts) - 3])))
    if not course_id:
        # Try to infer from path
        for cid, reg in config.COURSE_REGISTRY.items():
            if str(course_path).endswith(reg["rel_path"]):
                course_id = cid
                break

    modules = find_modules_for_course(course_path, course_id)
    if not modules:
        logger.warning(f"No modules found for {course_name} at {course_path}")
        return {"modules": [], "errors": []}

    results: Dict[str, Any] = {
        "course": course_name,
        "modules": [],
        "errors": [],
    }

    # Filter by module number if specified
    if module_filter is not None:
        modules = [m for m in modules if matches_module_number(m.name, module_filter)]
        if not modules:
            logger.warning(f"Module {module_filter} not found in {course_name}")
            return results

    # Filter by max_module: include modules 1 through max_module
    if max_module is not None:
        def get_module_number(name: str) -> int:
            """Extract module number from name like 'module-01-topic' or 'module-1'."""
            import re
            match = re.search(r'module-(\d+)', name)
            return int(match.group(1)) if match else 999
        
        modules = [m for m in modules if get_module_number(m.name) <= max_module]
        logger.info(f"Filtering to modules 1-{max_module}: {len(modules)} modules")

    for module_dir in modules:
        module_name = module_dir.name
        logger.info(f"{CONTENT_EMOJI['module']} Processing {course_name} › {module_name}")

        # Process module outputs
        output_dir = module_dir / "output"
        module_start = time.time()
        try:
            module_results = process_module_by_type(
                str(module_dir), str(output_dir), formats=formats
            )
            module_duration = time.time() - module_start
            results["modules"].append({
                "name": module_name,
                "outputs": module_results,
                "duration": module_duration,
            })

            # Compact single-line format summary
            summary_str = format_summary(module_results['summary'])
            logger.info(f"  {STATUS_EMOJI['success']} {module_name} ({module_duration:.2f}s) → {summary_str}")

            if module_results["errors"]:
                logger.warning(
                    f"Errors in {module_name}: {len(module_results['errors'])} errors"
                )
                for error in module_results["errors"]:
                    logger.error(f"  {module_name}: {error}")
                    results["errors"].append(f"{module_name}: {error}")

        except Exception as e:
            error_msg = f"Failed to process {module_name}: {e}"
            logger.error(error_msg, exc_info=True)
            results["errors"].append(error_msg)
            continue

        # Generate website (if enabled)
        if generate_website:
            website_start = time.time()
            try:
                website_file = process_module_website(str(module_dir))
                website_duration = time.time() - website_start
                logger.info(
                    f"Website generated in {website_duration:.2f}s: {website_file}"
                )
            except Exception as e:
                error_msg = f"Failed to generate website for {module_name}: {e}"
                logger.error(error_msg, exc_info=True)
                results["errors"].append(error_msg)

    return results


def process_course_syllabus(
    course_path: Path,
    course_name: str,
    formats: Optional[List[str]] = None,
    course_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Process syllabus for a course.

    Args:
        course_path: Path to course directory
        course_name: Name of the course
        formats: Optional list of formats to generate (e.g. ["pdf", "html"])
        course_id: Optional course ID for registry-aware path resolution

    Returns:
        Dictionary with processing results
    """
    # Determine syllabus location from registry if available
    syllabus_location = "syllabus"
    if course_id and course_id in config.COURSE_REGISTRY:
        syllabus_location = config.COURSE_REGISTRY[course_id].get(
            "syllabus_location", "syllabus"
        )

    # If syllabus_location is a file (e.g. "syllabus.md"), it's per-module,
    # not a top-level directory — skip silently
    if syllabus_location.endswith(".md"):
        logger.debug(
            f"Syllabus is per-module ({syllabus_location}) for {course_name}, skipping directory processing"
        )
        return {"processed": False, "errors": []}

    syllabus_dir = course_path / syllabus_location
    if not syllabus_dir.exists():
        logger.debug(f"Syllabus directory not found: {syllabus_dir}")
        return {"processed": False, "errors": []}

    logger.info(f"{CONTENT_EMOJI['syllabus']} Processing {course_name} Syllabus")

    output_dir = syllabus_dir / "output"
    syllabus_start = time.time()

    try:
        results = process_syllabus(str(syllabus_dir), str(output_dir), formats=formats)
        syllabus_duration = time.time() - syllabus_start
        # Compact single-line format summary
        summary_str = format_summary(results['summary'])
        logger.info(f"  {STATUS_EMOJI['success']} Syllabus ({syllabus_duration:.2f}s) → {summary_str}")

        if results["errors"]:
            logger.warning(
                f"Errors in syllabus processing: {len(results['errors'])} errors"
            )
            for error in results["errors"]:
                logger.error(f"  {error}")

        return {
            "processed": True,
            "results": results,
            "errors": results["errors"],
            "duration": syllabus_duration,
        }

    except Exception as e:
        error_msg = f"Failed to process syllabus: {e}"
        logger.error(error_msg, exc_info=True)
        return {"processed": False, "errors": [error_msg]}


def process_course_labs(
    course_path: Path,
    course_name: str,
    formats: Optional[List[str]] = None,
    max_lab: Optional[int] = None,
    course_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Process lab manuals for a course.

    Args:
        course_path: Path to course directory
        course_name: Name of the course
        formats: Optional list of formats to generate (supports "pdf", "html")
        max_lab: If specified, only process labs 1 through max_lab
        course_id: Optional course ID for registry-aware path resolution

    Returns:
        Dictionary with processing results
    """
    # Determine labs path from registry if available
    has_course_subdir = True
    if course_id and course_id in config.COURSE_REGISTRY:
        has_course_subdir = config.COURSE_REGISTRY[course_id].get(
            "has_course_subdir", True
        )

    if has_course_subdir:
        labs_dir = course_path / "course" / "labs"
    else:
        labs_dir = course_path / "labs"

    if not labs_dir.exists():
        logger.debug(f"Labs directory not found: {labs_dir}")
        return {"processed": False, "errors": []}

    logger.info(f"{CONTENT_EMOJI['lab']} Processing {course_name} Labs")

    output_dir = labs_dir / "output"
    lab_start = time.time()

    results: Dict[str, Any] = {
        "processed": True,
        "files": [],
        "errors": [],
        "duration": 0.0,
    }

    # Lab rendering supports pdf and html formats
    lab_formats = ["pdf", "html"]
    if formats:
        lab_formats = [f for f in formats if f in ("pdf", "html")]

    if not lab_formats:
        logger.info("No lab-compatible formats requested, skipping labs")
        results["processed"] = False
        return results

    # Lazy import to avoid WeasyPrint load at module level
    from ..lab_manual.main import batch_render_lab_manuals

    for fmt in lab_formats:
        try:
            fmt_output = output_dir / fmt
            rendered = batch_render_lab_manuals(
                str(labs_dir),
                str(fmt_output),
                output_format=fmt,
                course_name=course_name,
                max_lab=max_lab,
            )
            results["files"].extend(rendered)
            logger.info(f"  {fmt.upper()}: {len(rendered)} lab files rendered")
        except Exception as e:
            error_msg = f"Lab {fmt} rendering failed: {e}"
            logger.error(error_msg, exc_info=True)
            results["errors"].append(error_msg)

    results["duration"] = time.time() - lab_start
    logger.info(
        f"  {STATUS_EMOJI['success']} Labs ({results['duration']:.2f}s) → "
        f"{FORMAT_EMOJI['pdf']} {len(results['files'])} files"
    )

    return results


def process_course_practice_tests(
    course_path: Path,
    course_name: str,
    formats: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Process practice tests for a course.

    Renders practice test markdown files (including answer keys) to PDF
    for student use.

    Args:
        course_path: Path to course directory
        course_name: Name of the course
        formats: Optional list of formats to generate (supports "pdf")

    Returns:
        Dictionary with processing results
    """
    practice_tests_dir = course_path / "course" / "practice_tests"
    if not practice_tests_dir.exists():
        logger.debug(f"Practice tests directory not found: {practice_tests_dir}")
        return {"processed": False, "errors": [], "files": []}

    logger.info(f"{CONTENT_EMOJI['practice_test']} Processing {course_name} Practice Tests")

    output_dir = practice_tests_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    start_time = time.time()

    results: Dict[str, Any] = {
        "processed": True,
        "files": [],
        "errors": [],
        "duration": 0.0,
    }

    # Practice test rendering supports pdf format
    if formats and "pdf" not in formats:
        logger.info("PDF format not requested, skipping practice tests")
        results["processed"] = False
        return results

    # Find all practice test markdown files (excluding README)
    md_files = [
        f for f in practice_tests_dir.glob("*.md")
        if not f.name.startswith("README") and not f.name.startswith("AGENTS")
    ]

    if not md_files:
        logger.info(f"No practice test files found in {practice_tests_dir}")
        results["processed"] = False
        return results

    # Lazy import to avoid load at module level
    from ..markdown_to_pdf.main import render_markdown_to_pdf

    for md_file in md_files:
        try:
            pdf_file = output_dir / f"{md_file.stem}.pdf"
            logger.debug(f"Generating PDF: {pdf_file.name}")
            render_markdown_to_pdf(str(md_file), str(pdf_file))
            results["files"].append(str(pdf_file))
        except Exception as e:
            error_msg = f"PDF generation failed for {md_file.name}: {e}"
            logger.error(error_msg, exc_info=True)
            results["errors"].append(error_msg)

    results["duration"] = time.time() - start_time
    logger.info(
        f"  PDF: {len(results['files'])} practice test files rendered"
    )
    logger.info(
        f"Practice test rendering completed in {results['duration']:.2f}s: "
        f"{len(results['files'])} files"
    )

    return results


def process_module_website(module_path: str, output_dir: Optional[str] = None) -> str:

    """Generate HTML website for a module.

    Args:
        module_path: Path to module directory
        output_dir: Optional output directory (defaults to module_path/output/website)

    Returns:
        Path to generated HTML file

    Raises:
        ValueError: If module path doesn't exist
        OSError: If website generation fails
    """
    from ..html_website.main import generate_module_website

    logger.info(f"Generating website for module: {Path(module_path).name}")
    website_file = generate_module_website(module_path, output_dir)
    logger.info(f"Website generated: {website_file}")
    return website_file
