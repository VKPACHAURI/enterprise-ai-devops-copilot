"""
Unit tests for the Enterprise Document Loader Framework.
"""

from pathlib import Path

import pytest

from app.document_loader import DocumentLoader
from utils.exceptions import DocumentLoadError

def test_document_loader_initialization():
    """
    Verify that DocumentLoader initializes successfully.
    """

    loader = DocumentLoader()

    assert loader is not None
    assert loader.supported_file_types == {".pdf"}

def test_load_documents_directory_not_exists():
    """
    Verify that load_documents() raises DocumentLoadError
    when the specified directory does not exist.
    """

    # Arrange
    loader = DocumentLoader()

    # Act & Assert
    with pytest.raises(DocumentLoadError):
        loader.load_documents("invalid_directory")

def test_load_documents_path_is_not_directory(tmp_path):
    """
    Verify that load_documents() raises DocumentLoadError
    when the supplied path is a file instead of a directory.
    """

    # Arrange
    loader = DocumentLoader()

    test_file = tmp_path / "sample.txt"
    test_file.write_text("Enterprise AI DevOps Copilot")

    # Act & Assert
    with pytest.raises(DocumentLoadError):
        loader.load_documents(str(test_file))

def test_load_documents_no_supported_files(tmp_path):
    """
    Verify that load_documents() raises DocumentLoadError
    when the directory contains no supported PDF files.
    """

    # Arrange
    loader = DocumentLoader()

    (tmp_path / "sample.txt").write_text(
        "Enterprise AI DevOps Copilot"
    )

    # Act & Assert
    with pytest.raises(DocumentLoadError):
        loader.load_documents(str(tmp_path))

def test_load_documents_success(tmp_path, monkeypatch):
    """
    Verify that load_documents() successfully loads
    supported PDF documents.
    """

    # Arrange
    loader = DocumentLoader()

    pdf_file = tmp_path / "sample.pdf"
    pdf_file.write_text("Dummy PDF Content")

    class MockLoader:
        def __init__(self, file_path):
            self.file_path = file_path

        def load(self):
            return ["Mock Document"]

    monkeypatch.setattr(
        "app.document_loader.PyPDFLoader",
        MockLoader,
    )

    # Act
    documents = loader.load_documents(str(tmp_path))

    # Assert
    assert len(documents) == 1
    assert documents == ["Mock Document"]

def test_load_documents_pdf_loading_failure(tmp_path, monkeypatch):
    """
    Verify that load_documents() raises DocumentLoadError
    when PyPDFLoader fails to load a PDF.
    """

    # Arrange
    loader = DocumentLoader()

    pdf_file = tmp_path / "sample.pdf"
    pdf_file.write_text("Dummy PDF Content")

    class MockLoader:
        def __init__(self, file_path):
            self.file_path = file_path

        def load(self):
            raise Exception("Failed to load PDF")

    monkeypatch.setattr(
        "app.document_loader.PyPDFLoader",
        MockLoader,
    )

    # Act & Assert
    with pytest.raises(DocumentLoadError):
        loader.load_documents(str(tmp_path))