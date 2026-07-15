"""
Application runtime settings.

This module centralizes all configurable values used by the application.
Keeping runtime configuration in one place improves maintainability,
consistency, and supports future environment-specific configurations.
"""

from pathlib import Path


class Settings:
    """Centralized runtime configuration for the application."""

    # ---------------------------------------------------------------------
    # Project Root
    # ---------------------------------------------------------------------

    BASE_DIR = Path(__file__).resolve().parent.parent

    # ---------------------------------------------------------------------
    # Directories
    # ---------------------------------------------------------------------

    DATA_DIR = BASE_DIR / "data"
    LOG_DIR = BASE_DIR / "logs"
    DOCS_DIR = BASE_DIR / "docs"

    # ---------------------------------------------------------------------
    # Ollama Configuration
    # ---------------------------------------------------------------------

    OLLAMA_HOST = "http://localhost:11434"
    OLLAMA_MODEL = "llama3.2"

    # ---------------------------------------------------------------------
    # Logging
    # ---------------------------------------------------------------------

    LOG_LEVEL = "INFO"

    # ---------------------------------------------------------------------
    # Runtime
    # ---------------------------------------------------------------------

    REQUEST_TIMEOUT = 30
    MAX_RETRY_COUNT = 3


settings = Settings()



