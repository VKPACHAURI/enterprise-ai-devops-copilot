import pytest

from unittest.mock import MagicMock
from langchain_core.documents import Document

from app.embeddings import EmbeddingEngine
from utils.exceptions import EmbeddingError

def test_embedding_engine_initialization(monkeypatch):
    """
    Test that EmbeddingEngine initializes successfully.
    """

    mock_model = MagicMock()

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: mock_model
    )

    engine = EmbeddingEngine()

    assert engine.model == mock_model