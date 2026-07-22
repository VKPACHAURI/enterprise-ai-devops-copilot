"""
Unit tests for the enterprise logging utility.
"""

import logging

from utils.logger import get_logger


def test_get_logger_returns_logger_instance():
    """
    Verify that get_logger() returns a logging.Logger instance.
    """

    logger = get_logger(__name__)

    assert isinstance(logger, logging.Logger)


def test_logger_name():
    """
    Verify that the logger has the correct name.
    """
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"

def test_logger_level():
    """
    Verify that the logger uses the configured log level
    """

    logger = get_logger("test_level")
    assert logger.level == logging.INFO

def test_logger_does_not_duplicate_handlers():
    """
    Verify that duplicate handlers are not added
    when get_logger() is called multiple times.
    """

    logger1 = get_logger("duplicate_test")
    handlers_before = len(logger1.handlers)

    logger2 = get_logger("duplicate_test")
    handlers_after = len(logger2.handlers)

    assert handlers_before == handlers_after


from utils.logger import LOG_DIR


def test_log_directory_exists():
    """
    Verify that the log directory exists.
    """

    get_logger("directory_test")

    assert LOG_DIR.exists()
    assert LOG_DIR.is_dir()

from utils.logger import LOG_FILE


def test_log_file_exists():
    """
    Verify that the log file is created.
    """

    logger = get_logger("file_test")

    logger.info("Testing log file creation")

    assert LOG_FILE.exists()
    assert LOG_FILE.is_file()

