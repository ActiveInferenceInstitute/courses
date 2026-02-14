"""Main functions for schedule processing and generation."""

from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .utils import (
    ensure_output_directory,
    extract_schedule_sections,
    find_schedule_files,
    generate_schedule_markdown,
    parse_schedule_table,
    read_schedule_file,
    validate_schedule_entry,
)


def parse_schedule_markdown(schedule_path: str) -> Dict[str, Any]:
    """Parse schedule markdown file and extract structured data.

    Args:
        schedule_path: Path to schedule markdown file

    Returns:
        Dictionary with parsed schedule data:
        - entries: List of schedule entry dictionaries
        - sections: Dictionary with additional sections (title, semester, etc.)
        - metadata: Dictionary with file metadata

    Raises:
        FileNotFoundError: If schedule file doesn't exist
        ValueError: If schedule cannot be parsed
    """
    schedule_file = Path(schedule_path)
    if not schedule_file.exists():
        raise FileNotFoundError(f"Schedule file not found: {schedule_path}")

    content = read_schedule_file(schedule_file)

    # Parse table entries
    entries = parse_schedule_table(content)
    validated_entries = [e for e in entries if validate_schedule_entry(e)]

    # Extract sections
    sections = extract_schedule_sections(content)

    return {
        "entries": validated_entries,
        "sections": sections,
        "metadata": {
            "file_path": str(schedule_file),
            "file_name": schedule_file.name,
            "total_weeks": len(validated_entries),
        },
    }


def process_schedule(
    schedule_path: str, output_dir: str, formats: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Process schedule file and generate outputs in specified formats.

    Args:
        schedule_path: Path to schedule markdown file
        output_dir: Output directory for generated files
        formats: List of output formats (default: all supported formats)

    Returns:
        Dictionary with results:
        - outputs: Dictionary mapping format to list of output file paths
        - summary: Dictionary with counts of generated files by format
        - errors: List of errors encountered

    Raises:
        FileNotFoundError: If schedule file doesn't exist
        ValueError: If schedule cannot be parsed
    """
    if formats is None:
        formats = config.SUPPORTED_OUTPUT_FORMATS

    # Validate formats
    invalid_formats = [f for f in formats if f not in config.SUPPORTED_OUTPUT_FORMATS]
    if invalid_formats:
        raise ValueError(f"Unsupported output formats: {invalid_formats}")

    # Parse schedule
    schedule_data = parse_schedule_markdown(schedule_path)
    schedule_file = Path(schedule_path)
    base_name = schedule_file.stem

    # Setup output directory
    output_directory = Path(output_dir)
    ensure_output_directory(output_directory)

    results = {
        "outputs": {fmt: [] for fmt in formats},
        "summary": {fmt: 0 for fmt in formats},
        "errors": [],
    }

    # Generate outputs for each format
    for fmt in formats:
        try:
            output_files = generate_schedule_outputs(
                schedule_data, output_directory, base_name, [fmt]
            )
            results["outputs"][fmt] = output_files.get(fmt, [])
            results["summary"][fmt] = len(results["outputs"][fmt])
        except Exception as e:
            error_msg = f"Failed to generate {fmt} output: {e}"
            results["errors"].append(error_msg)

    return results


def generate_schedule_outputs(
    schedule_data: Dict[str, Any],
    output_dir: Path,
    base_name: str,
    formats: List[str],
) -> Dict[str, List[str]]:
    """Generate schedule outputs in specified formats.

    Args:
        schedule_data: Parsed schedule data dictionary
        output_dir: Output directory
        base_name: Base name for output files
        formats: List of output formats to generate

    Returns:
        Dictionary mapping format to list of output file paths

    Raises:
        ValueError: If format is not supported
        OSError: If file generation fails
    """
    outputs = {fmt: [] for fmt in formats}
    ensure_output_directory(output_dir)

    # Generate markdown first (used as source for other formats)
    markdown_content = generate_schedule_markdown(
        schedule_data["entries"], schedule_data.get("sections")
    )
    markdown_file = output_dir / f"{base_name}.md"
    markdown_file.write_text(markdown_content, encoding="utf-8")

    for fmt in formats:
        try:
            output_file = output_dir / f"{base_name}.{fmt}"

            if fmt == "pdf":
                from ..markdown_to_pdf.main import render_markdown_to_pdf

                render_markdown_to_pdf(str(markdown_file), str(output_file))
                outputs[fmt].append(str(output_file))

            elif fmt == "html":
                from ..format_conversion.main import convert_file

                convert_file(str(markdown_file), "html", str(output_file))
                outputs[fmt].append(str(output_file))

            elif fmt == "docx":
                from ..format_conversion.main import convert_file

                convert_file(str(markdown_file), "docx", str(output_file))
                outputs[fmt].append(str(output_file))

            elif fmt == "txt":
                # Extract text from markdown
                from ..text_to_speech.utils import extract_text_from_markdown

                text_content = extract_text_from_markdown(markdown_content)
                output_file.write_text(text_content, encoding="utf-8")
                outputs[fmt].append(str(output_file))

            elif fmt == "mp3":
                # Generate audio from text
                from ..text_to_speech.utils import extract_text_from_markdown
                from ..text_to_speech.main import generate_speech

                text_content = extract_text_from_markdown(markdown_content)
                generate_speech(text_content, str(output_file))
                outputs[fmt].append(str(output_file))

            else:
                raise ValueError(f"Unsupported format: {fmt}")

        except Exception as e:
            raise OSError(f"Failed to generate {fmt} output: {e}") from e

    return outputs


def batch_process_schedules(
    directory: str, output_dir: str, formats: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Batch process all schedule files in a directory.

    Args:
        directory: Directory containing schedule files
        output_dir: Output directory for generated files
        formats: List of output formats (default: all supported formats)

    Returns:
        Dictionary with results:
        - processed_files: List of processed schedule file paths
        - outputs: Dictionary mapping format to list of output file paths
        - summary: Dictionary with counts of generated files by format
        - errors: List of errors encountered
    """
    directory_path = Path(directory)
    if not directory_path.exists():
        raise ValueError(f"Directory does not exist: {directory}")

    schedule_files = find_schedule_files(directory_path)

    results = {
        "processed_files": [],
        "outputs": {},
        "summary": {},
        "errors": [],
    }

    if formats is None:
        formats = config.SUPPORTED_OUTPUT_FORMATS

    for schedule_file in schedule_files:
        try:
            file_results = process_schedule(
                str(schedule_file), output_dir, formats
            )
            results["processed_files"].append(str(schedule_file))
            for fmt in formats:
                if fmt not in results["outputs"]:
                    results["outputs"][fmt] = []
                results["outputs"][fmt].extend(file_results["outputs"][fmt])
        except Exception as e:
            error_msg = f"Failed to process {schedule_file}: {e}"
            results["errors"].append(error_msg)

    # Calculate summary
    for fmt in formats:
        results["summary"][fmt] = len(results["outputs"].get(fmt, []))

    return results
