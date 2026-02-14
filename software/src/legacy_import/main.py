"""Core business logic for legacy material import."""

import re
import shutil
import logging
from pathlib import Path
from typing import Dict, Any

from .config import get_chapter_to_module_mapping, EXCLUDED_MD_FILES
from .utils import (
    extract_chapter_number,
    ensure_module_exists,
    create_comprehension_questions,
)

logger = logging.getLogger(__name__)


def process_chapter_questions(
    source_dir: Path, course_root: Path, course_dir: Path, dry_run: bool
) -> Dict[str, Any]:
    """Process all Chapter Questions DOCX files.

    Converts DOCX question files to Markdown and places them in the
    appropriate module resources directory.

    Args:
        source_dir: Directory containing Chapter Questions DOCX files
        course_root: Course root directory (e.g., biol-1)
        course_dir: Course directory (e.g., biol-1/course)
        dry_run: If True, only show what would be done without doing it

    Returns:
        Dictionary with processing results containing:
            - processed: List of successfully processed files
            - skipped: List of skipped files with reasons
            - errors: List of errors encountered
            - summary: Aggregate counts
    """
    from src.format_conversion.utils import convert_docx_to_markdown

    results = {
        "processed": [],
        "skipped": [],
        "errors": [],
        "summary": {"converted": 0, "skipped": 0, "errors": 0, "modules_created": 0},
    }

    chapter_mapping = get_chapter_to_module_mapping()

    # Find all DOCX files in source directory
    docx_files = list(source_dir.glob("*.docx"))
    if not docx_files:
        logger.warning(f"No DOCX files found in {source_dir}")
        return results

    logger.info(f"Found {len(docx_files)} DOCX files to process")

    for docx_file in sorted(docx_files):
        try:
            # Extract chapter number from filename
            chapter_num = extract_chapter_number(docx_file.name)

            # Get module number from mapping (1:1 mapping)
            if chapter_num not in chapter_mapping:
                logger.warning(
                    f"Skipping {docx_file.name}: Chapter {chapter_num} not in mapping"
                )
                results["skipped"].append(
                    {
                        "file": docx_file.name,
                        "reason": f"Chapter {chapter_num} not in mapping",
                    }
                )
                results["summary"]["skipped"] += 1
                continue

            module_num = chapter_mapping[chapter_num]

            # Ensure module exists
            module_path = ensure_module_exists(course_root, module_num, dry_run)
            if not dry_run and not module_path.exists():
                # Module creation failed
                results["skipped"].append(
                    {
                        "file": docx_file.name,
                        "reason": f"Could not create module {module_num}",
                    }
                )
                results["summary"]["skipped"] += 1
                continue

            if not module_path.exists() and not dry_run:
                results["summary"]["modules_created"] += 1

            # Create comprehension questions file in resources directory
            create_comprehension_questions(module_path, module_num, dry_run)

            # Determine output path
            resources_dir = module_path / "resources"

            if not dry_run:
                resources_dir.mkdir(parents=True, exist_ok=True)

            # Output filename
            output_filename = f"module-{module_num}-keys-to-success.md"
            output_path = resources_dir / output_filename

            if dry_run:
                logger.info(
                    f"[DRY RUN] Would convert: {docx_file.name} -> {output_path}"
                )
                results["processed"].append(
                    {
                        "source": docx_file.name,
                        "destination": str(output_path),
                        "module": module_num,
                        "chapter": chapter_num,
                    }
                )
            else:
                # Convert DOCX to Markdown
                logger.info(f"Converting: {docx_file.name} -> {output_path.name}")
                markdown_content = convert_docx_to_markdown(docx_file)
                output_path.write_text(markdown_content, encoding="utf-8")
                logger.debug(f"Created: {output_path}")

                results["processed"].append(
                    {
                        "source": docx_file.name,
                        "destination": str(output_path),
                        "module": module_num,
                        "chapter": chapter_num,
                    }
                )
                results["summary"]["converted"] += 1

        except ValueError as e:
            error_msg = f"Error processing {docx_file.name}: {e}"
            logger.error(error_msg)
            results["errors"].append({"file": docx_file.name, "error": str(e)})
            results["summary"]["errors"] += 1
        except Exception as e:
            error_msg = f"Unexpected error processing {docx_file.name}: {e}"
            logger.error(error_msg, exc_info=True)
            results["errors"].append({"file": docx_file.name, "error": str(e)})
            results["summary"]["errors"] += 1

    return results


def process_slides(
    slides_full_dir: Path,
    slides_notes_dir: Path,
    course_root: Path,
    dry_run: bool,
) -> Dict[str, Any]:
    """Copy and organize PDF slides to module directories.

    Processes both full slides and notes slides, placing them in the
    appropriate module slides directory.

    Args:
        slides_full_dir: Directory containing full slides PDFs
        slides_notes_dir: Directory containing notes slides PDFs
        course_root: Course root directory (e.g., biol-1)
        dry_run: If True, only show what would be done without doing it

    Returns:
        Dictionary with processing results containing:
            - processed: List of successfully processed files
            - skipped: List of skipped files with reasons
            - errors: List of errors encountered
            - summary: Aggregate counts
    """
    results = {
        "processed": [],
        "skipped": [],
        "errors": [],
        "summary": {"copied": 0, "skipped": 0, "errors": 0},
    }

    chapter_mapping = get_chapter_to_module_mapping()

    # Process full slides
    if slides_full_dir.exists():
        full_slides = list(slides_full_dir.glob("*.pdf"))
        logger.info(f"Found {len(full_slides)} full slide PDFs to process")

        for pdf_file in sorted(full_slides):
            try:
                chapter_num = extract_chapter_number(pdf_file.name)

                if chapter_num not in chapter_mapping:
                    logger.warning(
                        f"Skipping {pdf_file.name}: Chapter {chapter_num} not in mapping"
                    )
                    results["skipped"].append(
                        {
                            "file": pdf_file.name,
                            "reason": f"Chapter {chapter_num} not in mapping",
                        }
                    )
                    results["summary"]["skipped"] += 1
                    continue

                module_num = chapter_mapping[chapter_num]

                # Ensure module exists
                module_path = ensure_module_exists(course_root, module_num, dry_run)
                if not module_path.exists() and not dry_run:
                    continue

                # Create slides directory in module
                slides_dir = module_path / "slides"
                if not dry_run:
                    slides_dir.mkdir(parents=True, exist_ok=True)

                output_filename = f"module-{module_num}-slides-full.pdf"
                output_path = slides_dir / output_filename

                if dry_run:
                    logger.info(
                        f"[DRY RUN] Would copy: {pdf_file.name} -> {output_path}"
                    )
                    results["processed"].append(
                        {
                            "source": pdf_file.name,
                            "destination": str(output_path),
                            "module": module_num,
                            "chapter": chapter_num,
                            "type": "full",
                        }
                    )
                else:
                    logger.info(f"Copying: {pdf_file.name} -> {output_path.name}")
                    shutil.copy2(pdf_file, output_path)
                    logger.debug(f"Copied: {output_path}")

                    results["processed"].append(
                        {
                            "source": pdf_file.name,
                            "destination": str(output_path),
                            "module": module_num,
                            "chapter": chapter_num,
                            "type": "full",
                        }
                    )
                    results["summary"]["copied"] += 1

            except ValueError as e:
                error_msg = f"Error processing {pdf_file.name}: {e}"
                logger.error(error_msg)
                results["errors"].append({"file": pdf_file.name, "error": str(e)})
                results["summary"]["errors"] += 1
            except Exception as e:
                error_msg = f"Unexpected error processing {pdf_file.name}: {e}"
                logger.error(error_msg, exc_info=True)
                results["errors"].append({"file": pdf_file.name, "error": str(e)})
                results["summary"]["errors"] += 1
    else:
        logger.warning(f"Full slides directory does not exist: {slides_full_dir}")

    # Process notes slides
    if slides_notes_dir.exists():
        notes_slides = list(slides_notes_dir.glob("*.pdf"))
        logger.info(f"Found {len(notes_slides)} notes slide PDFs to process")

        for pdf_file in sorted(notes_slides):
            try:
                chapter_num = extract_chapter_number(pdf_file.name)

                if chapter_num not in chapter_mapping:
                    logger.warning(
                        f"Skipping {pdf_file.name}: Chapter {chapter_num} not in mapping"
                    )
                    results["skipped"].append(
                        {
                            "file": pdf_file.name,
                            "reason": f"Chapter {chapter_num} not in mapping",
                        }
                    )
                    results["summary"]["skipped"] += 1
                    continue

                module_num = chapter_mapping[chapter_num]

                # Ensure module exists
                module_path = ensure_module_exists(course_root, module_num, dry_run)
                if not module_path.exists() and not dry_run:
                    continue

                # Create slides directory in module
                slides_dir = module_path / "slides"
                if not dry_run:
                    slides_dir.mkdir(parents=True, exist_ok=True)

                output_filename = f"module-{module_num}-slides-notes.pdf"
                output_path = slides_dir / output_filename

                if dry_run:
                    logger.info(
                        f"[DRY RUN] Would copy: {pdf_file.name} -> {output_path}"
                    )
                    results["processed"].append(
                        {
                            "source": pdf_file.name,
                            "destination": str(output_path),
                            "module": module_num,
                            "chapter": chapter_num,
                            "type": "notes",
                        }
                    )
                else:
                    logger.info(f"Copying: {pdf_file.name} -> {output_path.name}")
                    shutil.copy2(pdf_file, output_path)
                    logger.debug(f"Copied: {output_path}")

                    results["processed"].append(
                        {
                            "source": pdf_file.name,
                            "destination": str(output_path),
                            "module": module_num,
                            "chapter": chapter_num,
                            "type": "notes",
                        }
                    )
                    results["summary"]["copied"] += 1

            except ValueError as e:
                error_msg = f"Error processing {pdf_file.name}: {e}"
                logger.error(error_msg)
                results["errors"].append({"file": pdf_file.name, "error": str(e)})
                results["summary"]["errors"] += 1
            except Exception as e:
                error_msg = f"Unexpected error processing {pdf_file.name}: {e}"
                logger.error(error_msg, exc_info=True)
                results["errors"].append({"file": pdf_file.name, "error": str(e)})
                results["summary"]["errors"] += 1
    else:
        logger.warning(f"Notes slides directory does not exist: {slides_notes_dir}")

    return results


def create_for_upload_files(
    module_path: Path, module_num: int, dry_run: bool
) -> Dict[str, Any]:
    """Create for_upload folder with DOCX and PDF of all markdown files plus slide PDFs.

    Converts markdown resources to PDF and DOCX formats, and copies slide
    PDFs into a for_upload directory for LMS upload.

    Args:
        module_path: Path to module directory
        module_num: Module number
        dry_run: If True, only show what would be created

    Returns:
        Dictionary with processing results containing:
            - processed: List of processed files
            - errors: List of errors encountered
            - summary: Aggregate counts (pdf, docx, slides_copied, errors)
    """
    results = {
        "processed": [],
        "errors": [],
        "summary": {"pdf": 0, "docx": 0, "slides_copied": 0, "errors": 0},
    }

    for_upload_dir = module_path / "for_upload"

    if dry_run:
        logger.info(f"[DRY RUN] Would create for_upload/ directory for module-{module_num}")
    else:
        for_upload_dir.mkdir(parents=True, exist_ok=True)

    # Find all markdown files in resources directory
    resources_dir = module_path / "resources"
    markdown_files = []
    if resources_dir.exists():
        markdown_files = [
            f
            for f in resources_dir.glob("*.md")
            if f.name not in EXCLUDED_MD_FILES
        ]

    # Process each markdown file
    for md_file in markdown_files:
        base_name = md_file.stem

        if dry_run:
            logger.info(f"[DRY RUN] Would process {md_file.name} -> for_upload/")
            results["processed"].append({"file": md_file.name, "type": "markdown"})
        else:
            try:
                # Generate PDF
                pdf_file = for_upload_dir / f"{base_name}.pdf"
                from src.markdown_to_pdf.main import render_markdown_to_pdf

                logger.debug(f"Generating PDF: {pdf_file.name}")
                render_markdown_to_pdf(str(md_file), str(pdf_file))
                results["summary"]["pdf"] += 1
                results["processed"].append({"file": pdf_file.name, "type": "pdf"})

                # Generate DOCX
                docx_file = for_upload_dir / f"{base_name}.docx"
                from src.format_conversion.main import convert_file

                logger.debug(f"Generating DOCX: {docx_file.name}")
                convert_file(str(md_file), "docx", str(docx_file))
                results["summary"]["docx"] += 1
                results["processed"].append({"file": docx_file.name, "type": "docx"})

            except Exception as e:
                error_msg = f"Error processing {md_file.name}: {e}"
                logger.error(error_msg, exc_info=True)
                results["errors"].append({"file": md_file.name, "error": str(e)})
                results["summary"]["errors"] += 1

    # Copy slide PDFs to for_upload
    slides_dir = module_path / "slides"
    if slides_dir.exists():
        slide_pdfs = list(slides_dir.glob("*.pdf"))
        for slide_pdf in slide_pdfs:
            if dry_run:
                logger.info(f"[DRY RUN] Would copy {slide_pdf.name} -> for_upload/")
                results["processed"].append({"file": slide_pdf.name, "type": "slide"})
            else:
                try:
                    dest_file = for_upload_dir / slide_pdf.name
                    shutil.copy2(slide_pdf, dest_file)
                    logger.debug(f"Copied slide: {dest_file.name}")
                    results["summary"]["slides_copied"] += 1
                    results["processed"].append(
                        {"file": dest_file.name, "type": "slide"}
                    )
                except Exception as e:
                    error_msg = f"Error copying {slide_pdf.name}: {e}"
                    logger.error(error_msg, exc_info=True)
                    results["errors"].append(
                        {"file": slide_pdf.name, "error": str(e)}
                    )
                    results["summary"]["errors"] += 1

    return results


def process_for_upload_all_modules(
    course_dir: Path, dry_run: bool
) -> Dict[str, Any]:
    """Process for_upload folders for all modules.

    Iterates over every module directory and creates for_upload content
    for each one.

    Args:
        course_dir: Course directory (e.g., biol-1/course)
        dry_run: If True, only show what would be created

    Returns:
        Dictionary with processing results containing:
            - modules_processed: Count of modules handled
            - modules_errors: Count of modules with errors
            - total_pdf: Total PDFs created
            - total_docx: Total DOCX files created
            - total_slides: Total slides copied
            - errors: List of error details
    """
    results = {
        "modules_processed": 0,
        "modules_errors": 0,
        "total_pdf": 0,
        "total_docx": 0,
        "total_slides": 0,
        "errors": [],
    }

    # Find all modules
    modules = sorted(
        [d for d in course_dir.iterdir() if d.is_dir() and d.name.startswith("module-")]
    )

    logger.info(f"Processing for_upload folders for {len(modules)} modules")

    for module_path in modules:
        # Extract module number
        match = re.search(r"module-(\d+)", module_path.name)
        if not match:
            continue

        module_num = int(match.group(1))

        try:
            module_results = create_for_upload_files(module_path, module_num, dry_run)
            results["modules_processed"] += 1
            results["total_pdf"] += module_results["summary"]["pdf"]
            results["total_docx"] += module_results["summary"]["docx"]
            results["total_slides"] += module_results["summary"]["slides_copied"]

            if module_results["errors"]:
                results["modules_errors"] += 1
                results["errors"].extend(module_results["errors"])
        except Exception as e:
            error_msg = f"Error processing for_upload for {module_path.name}: {e}"
            logger.error(error_msg, exc_info=True)
            results["modules_errors"] += 1
            results["errors"].append({"module": module_path.name, "error": str(e)})

    return results
