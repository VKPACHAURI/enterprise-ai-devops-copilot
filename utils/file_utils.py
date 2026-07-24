"""
Enterprise File Utility Framework

This module provides reusable utility functions for
handling files and directories across the application.

Author: Vishesh Pachauri
Project: Enterprise AI DevOps Copilot
"""

# Standard Library Imports
import json      #read and write the json file
import os        #Basic file and directory actions
import shutil    #files and dir managment
from pathlib import Path #modern and object-oriented path handling

# Third-Party Imports
from utils.logger import get_logger
from utils.exceptions import FileOperationError

logger = get_logger(__name__)


# Local Application Imports

class FileUtility:
    """
    Provides reusable utility methods for file and directory operations.

    All methods are static because the class maintains no internal state.
    """

    @staticmethod
    def create_directory(directory_path: str) -> None:
        """
        Create a directory if it does not already exist.

        Args:
            directory_path (str): Path of the directory to create.

        Raises:
            FileOperationError:
                If the directory cannot be created.
        """
        try:
            path = Path(directory_path)

            if path.exists() and path.is_dir():
                logger.info("Directory already exists: %s", path)
                return

            path.mkdir(parents=True, exist_ok=True)
            logger.info("Directory created successfully: %s", path)

        except Exception as error:
            logger.error("Failed to create directory: %s", path)

            raise FileOperationError(
                f"Unable to create directory: {path}"
            ) from error

            