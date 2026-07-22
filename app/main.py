"""
Application Entry Point
"""

from utils.logger import get_logger


logger = get_logger(__name__)


def main():
    logger.debug("Debug message")
    logger.info("Application started successfully.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")


if __name__ == "__main__":
    main()

