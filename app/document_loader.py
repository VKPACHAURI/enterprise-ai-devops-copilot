"""
Enterprise Document Loader Framework

This module provides a centralized document loading framework
for the Enterprise AI DevOps Copilot.

Author: Vishesh Pachauri
Project: Enterprise AI DevOps Copilot
"""

from __future__ import annotations

# Standard Library Imports
from pathlib import Path

# Third-Party Imports
from langchain_community.document_loaders import PyPDFLoader

# Local Application Imports
from utils.logger import get_logger
from utils.exceptions import DocumentLoadError
#from utils.file_utils import FileUtility

logger = get_logger(__name__)


class DocumentLoader:
    """
    Enterprise document loader responsible for loading
    supported documents into the application.

    This class centralizes document loading, validation,
    logging, and exception handling.
    """

    def __init__(self) -> None:
        """
        Initialize the DocumentLoader.
        """
        self.supported_file_types = {".pdf"}

    def load_documents(self, directory_path: str) -> list:
        """
        Load all supported documents from a directory.

        Args:
            directory_path (str):
                Directory containing documents.

        Returns:
            list:
                Loaded LangChain documents.

        Raises:
            DocumentLoadError:
                If the directory cannot be processed.
        """

        try:
            # Step 1: Convert string to Path object
            directory = Path(directory_path)

            # Step 2: Validate directory exists
            if not directory.exists():
                raise DocumentLoadError(
                    f"Directory does not exist: {directory}"
                )

            # Step 3: Validate it is a directory
            if not directory.is_dir():
                raise DocumentLoadError(
                    f"Path is not a directory: {directory}"
                )

            # Step 4: Find supported files
            supported_files = [
                file_path
                for file_path in directory.iterdir()
                if file_path.is_file()
                and file_path.suffix.lower() in self.supported_file_types
            ]

            # Step 5: Validate supported files exist
            if not supported_files:
                raise DocumentLoadError(
                    f"No supported documents found in: {directory}"
                )

            # Step 6: Load PDF documents
            documents: list = []

            for file_path in supported_files:
                try:
                    logger.info(
                        "Loading document: %s",
                        file_path,
                    )

                    loader = PyPDFLoader(str(file_path))

                    documents.extend(loader.load())

                except Exception as error:
                    logger.error(
                        "Failed to load document: %s",
                        file_path,
                    )

                    raise DocumentLoadError(
                        f"Unable to load document: {file_path}"
                    ) from error

            logger.info(
                "Successfully loaded %d document(s).",
                len(documents),
            )

            return documents

        except DocumentLoadError:
            # Re-raise custom exceptions without wrapping them again
            raise

        except Exception as error:
            logger.error(
                "Failed to process document directory: %s",
                directory_path,
            )

            raise DocumentLoadError(
                f"Unable to access directory: {directory_path}"
            ) from error