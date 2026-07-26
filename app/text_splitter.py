"""
Enterprise Text Splitter Framework

This module provides a centralized text splitting framework
for the Enterprise AI DevOps Copilot.

Author: Vishesh Pachauri
Project: Enterprise AI DevOps Copilot
"""

from __future__ import annotations

# Third-Party Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Local Application Imports
from utils.logger import get_logger
from utils.exceptions import TextSplitterError

logger = get_logger(__name__)


class TextSplitter:
    """
    Enterprise text splitter responsible for splitting
    LangChain documents into optimized chunks.

    This class centralizes text splitting, validation,
    logging, and exception handling.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> None:
        """
        Initialize the TextSplitter.

        Args:
            chunk_size (int):
                Maximum size of each chunk.

            chunk_overlap (int):
                Number of overlapping characters
                between consecutive chunks.
        """

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split LangChain documents into smaller chunks.

        Args:
            documents (list[Document]):
                List of LangChain Document objects.

        Returns:
            list[Document]:
                Chunked LangChain documents.

        Raises:
            TextSplitterError:
                If document splitting fails.
        """

        try:
            # Step 1: Validate input documents
            if not documents:
                raise TextSplitterError(
                    "No documents provided for splitting."
                )

            # Step 2: Log splitting operation
            logger.info(
                "Splitting %d document(s).",
                len(documents),
            )

            # Step 3: Split documents into chunks
            chunks = self.text_splitter.split_documents(
                documents
            )

            # Step 4: Log successful chunk creation
            logger.info(
                "Successfully created %d chunk(s).",
                len(chunks),
            )

            # Step 5: Return chunked documents
            return chunks

        except TextSplitterError:
            raise

        except Exception as error:
            logger.error(
                "Failed to split documents."
            )

            raise TextSplitterError(
                "Unable to split documents."
            ) from error