import pytest

from utils.exceptions import (
    DevOpsCopilotError,
    DocumentLoadError,
    EmbeddingError,
    VectorStoreError,
    OllamaConnectionError,
    ConfigurationError,
)

def test_base_exception_inherits_exception():
    """
    Verify that DevOpsCopilotError inherits from Python's Exception class.
    """

    assert issubclass(DevOpsCopilotError, Exception)


def test_document_load_error_inherits_base_exception():
    """
    Verify that DocumentLoadError inherits from DevOpsCopilotError.
    """

    assert issubclass(DocumentLoadError, DevOpsCopilotError)


def test_embedding_error_inherits_base_exception():
    """
    Verify that EmbeddingError inherits from DevOpsCopilotError.
    """

    assert issubclass(EmbeddingError, DevOpsCopilotError)

def test_vector_store_error_inherits_base_exception():
    """
    Verify that VectorStoreError inherits from DevOpsCopilotError.
    """

    assert issubclass(VectorStoreError, DevOpsCopilotError)

def test_ollama_connection_inherits_base_exception():
    """
    Verify that OllamaConnectionError inherits from DevOpsCopilotError.
    """

    assert issubclass(OllamaConnectionError, DevOpsCopilotError)

def test_configuration_error_inherits_base_exception():
    """
    Verify that ConfigurationError inherits from DevOpsCopilotError.
    """

    assert issubclass(ConfigurationError, DevOpsCopilotError)

def test_document_load_error_message():
    """
    Verify that DocumentLoadError stores the provided error message.
    """

    message = "Unable to load AWS.pdf"

    error = DocumentLoadError(message)

    assert str(error) == message

def test_document_load_error_is_instance_of_base_exception():
    """
    Verify that DocumentLoadError is an instance of DevOpsCopilotError.
    """

    error = DocumentLoadError("Unable to load document")

    assert isinstance(error, DevOpsCopilotError)

def test_document_load_error_is_instance_of_exception():
    """
    Verify that DocumentLoadError is also an instance
    of Python's built-in Exception class.
    """

    error = DocumentLoadError("Unable to load document")

    assert isinstance(error, Exception)
    