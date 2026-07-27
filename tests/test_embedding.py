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


def test_validate_documents_none(monkeypatch):
    """
    Test that validate_documents raises EmbeddingError
    when documents is None.
    """

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: MagicMock()
    )

    engine = EmbeddingEngine()

    with pytest.raises(
        EmbeddingError,
        match="Documents cannot be None."
    ):
        engine.validate_documents(None)


def test_validate_documents_empty_list(monkeypatch):
    """
    Test that validate_documents raises EmbeddingError
    when an empty list is provided.
    """

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: MagicMock()
    )

    engine = EmbeddingEngine()

    with pytest.raises(
        EmbeddingError,
        match="Document list cannot be empty."
    ):
        engine.validate_documents([])


def test_validate_documents_invalid_type(monkeypatch):
    """
    Test that validate_documents raises EmbeddingError
    when input is not a list.
    """

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: MagicMock()
    )

    engine = EmbeddingEngine()

    with pytest.raises(
        EmbeddingError,
        match="Documents must be provided as a list."
    ):
        engine.validate_documents("AWS")


def test_generate_embeddings_success(monkeypatch):
    """
    Test successful embedding generation.
    """

    mock_model = MagicMock()

    expected_embeddings = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6]
    ]

    mock_model.embed_documents.return_value = expected_embeddings

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: mock_model
    )

    engine = EmbeddingEngine()

    documents = [
        Document(page_content="Amazon EC2"),
        Document(page_content="Amazon S3")
    ]

    embeddings = engine.generate_embeddings(documents)

    assert embeddings == expected_embeddings

    mock_model.embed_documents.assert_called_once_with(
        [
            "Amazon EC2",
            "Amazon S3"
        ]
    )


def test_generate_embeddings_failure(monkeypatch):
    """
    Test that generate_embeddings raises EmbeddingError
    when the embedding model fails.
    """

    mock_model = MagicMock()

    mock_model.embed_documents.side_effect = Exception(
        "Ollama connection failed."
    )

    monkeypatch.setattr(
        EmbeddingEngine,
        "_initialize_model",
        lambda self: mock_model
    )

    engine = EmbeddingEngine()

    documents = [
        Document(page_content="Amazon EC2")
    ]

    with pytest.raises(
        EmbeddingError,
        match="Failed to generate document embeddings."
    ):
        engine.generate_embeddings(documents)


