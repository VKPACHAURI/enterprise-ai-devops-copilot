"""
Enterprise Logging Utility

Provides a centralized logging configuration for the entire application.
"""

import logging

from config.settings import settings


# Log directory
LOG_DIR = settings.LOG_DIR

# Log file
LOG_FILE = LOG_DIR / "application.log"

# Log message format
LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

# Date format
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Name of the module requesting the logger.

    Returns:
        Configured logger instance.
    """

    # Create logs directory if it doesn't exist
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Get logger instance
    logger = logging.getLogger(name)

    # Set minimum log level
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        # Create formatter
        formatter = logging.Formatter(
            fmt=LOG_FORMAT,
            datefmt=DATE_FORMAT
        )

        # Configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Configure file handler
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
