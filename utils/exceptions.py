"""
Enterprise custom exceptions for the Enterprise AI DevOps Copilot.

This module centralizes all project-specific exceptions to ensure
consistent error handling across the application.
"""
from __future__ import annotations

#Step 3 – Create the Base Exception

class DevOpsCopilotError(Exception):
    """
    Base exception class for the Enterprise AI DevOps Copilot.

    All custom exceptions in the application should inherit
    from this class.
    """

    def __init__(self, message: str):
        super().__init__(message)

class DocumentLoadError(DevOpsCopilotError):
    """
    Raised when a document cannot be loaded.
    """

    pass

class EmbeddingError(DevOpsCopilotError):
    """
    Raised when the embedding generation process fails.
    """
    pass

class VectorStoreError(DevOpsCopilotError):
    """
    Raised when a vector database not accessed or initilized.
    """

    pass

class OllamaConnectionError(DevOpsCopilotError):
    """
    Raised when a connection to the Ollama server cannot be established.
    """

    pass

class ConfigurationError(DevOpsCopilotError):
    """
    Raised when application configuration is invalid or missing. 
    """

    pass


