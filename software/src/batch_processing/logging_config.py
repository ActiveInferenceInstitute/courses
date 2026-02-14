"""Logging configuration for batch processing operations."""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def setup_logging(
    log_dir: Optional[Path] = None,
    log_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> logging.Logger:
    """Set up logging configuration for batch processing.

    Configures both console and file handlers with appropriate formatting.
    Console handler shows INFO level and above with simplified format.
    File handler shows DEBUG level and above with detailed format.

    Args:
        log_dir: Directory for log files (defaults to software/logs/)
        log_level: Logging level for console handler (default: INFO)
        file_level: Logging level for file handler (default: DEBUG)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("batch_processing")
    logger.setLevel(logging.DEBUG)  # Capture all levels, handlers filter

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    # Console handler with simplified format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_format = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # File handler with detailed format
    if log_dir is None:
        # Default to software/logs/ relative to this file
        base_dir = Path(__file__).parent.parent.parent
        log_dir = base_dir / "logs"

    log_dir.mkdir(parents=True, exist_ok=True)

    # Create timestamped log file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"generation_{timestamp}.log"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(file_level)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S,%f",
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    logger.info(f"Logging initialized - Console: {logging.getLevelName(log_level)}, File: {logging.getLevelName(file_level)}")
    logger.debug(f"Log file: {log_file}")

    return logger


def get_logger(name: str = "batch_processing") -> logging.Logger:
    """Get a logger instance.

    Args:
        name: Logger name (default: "batch_processing")

    Returns:
        Logger instance
    """
    return logging.getLogger(name)
