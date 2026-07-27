from langchain_ollama import OllamaEmbeddings

from config.settings import settings
from utils.logger import get_logger
from utils.exceptions import EmbeddingError


class EmbeddingEngine:
    """
    Enterprise Embedding Engine.

    Responsible for:
    - Initializing the embedding model
    - Validating input documents
    - Generating embeddings
    """

    def __init__(self):


        """Initialize the embedding engine."""

        self.logger = get_logger(__name__)
        self.model = self._initialize_model()

    def _initialize_model(self):
            
        """
        Initialize the embedding model.
        """

        try:
            self.logger.info("Initializing embedding model...")

            model = OllamaEmbeddings(
                model=settings.EMBEDDING_MODEL
            )

            self.logger.info(
                f"Embedding model '{settings.EMBEDDING_MODEL}' initialized successfully."
            )

            return model

        except Exception as error:
            self.logger.error(
                f"Failed to initialize embedding model: {error}"
            )

            raise EmbeddingError(
                "Failed to initialize embedding model."
            ) from error

    def validate_documents(self, documents):
        """
        Validate the input documents.
        """

        if documents is None:
            raise EmbeddingError("Documents cannot be None.")

        if not isinstance(documents, list):
            raise EmbeddingError("Documents must be provided as a list.")

        if len(documents) == 0:
            raise EmbeddingError("Document list cannot be empty.")

        self.logger.info(
            f"Validated {len(documents)} document(s) successfully."
        )

    def generate_embeddings(self, documents):
        """
        Generate embeddings for the provided documents.
        """

        try:
            # Validate input
            self.validate_documents(documents)

            self.logger.info(
                f"Generating embeddings for {len(documents)} document(s)..."
            )

            # Extract text from documents
            texts = [doc.page_content for doc in documents]

            # Generate embeddings
            embeddings = self.model.embed_documents(texts)

            self.logger.info(
                f"Successfully generated {len(embeddings)} embeddings."
            )

            return embeddings

        except Exception as error:
            self.logger.error(
                f"Embedding generation failed: {error}"
            )

            raise EmbeddingError(
                "Failed to generate document embeddings."
            ) from error