"""
Unit tests for the Enterprise File Utility Framework.
"""

from pathlib import Path

from utils.file_utils import FileUtility
import pytest
from utils.exceptions import FileOperationError

def test_create_directory(tmp_path):
    """
    Verify that create_directory() creates a new directory.
    """

    # Arrange
    new_directory = tmp_path / "logs"

    # Act
    FileUtility.create_directory(str(new_directory))

    # Assert
    assert new_directory.exists()
    assert new_directory.is_dir()

def test_create_existing_directory(tmp_path):
    """
    Verify that create_directory() does not raise an exception
    when the directory already exists.
    """

    # Arrange
    existing_directory = tmp_path / "logs"
    existing_directory.mkdir()

    # Act
    FileUtility.create_directory(str(existing_directory))

    # Assert
    assert existing_directory.exists()
    assert existing_directory.is_dir()


def test_create_directory_failure(monkeypatch, tmp_path):

    def mock_mkdir(*args, **kwargs):
        raise PermissionError("Permission denied")

    monkeypatch.setattr(Path, "mkdir", mock_mkdir)

    new_directory = tmp_path / "logs"

    with pytest.raises(FileOperationError):
        FileUtility.create_directory(str(new_directory))