from app.text_splitter import TextSplitter
import pytest

from utils.exceptions import TextSplitterError

def test_text_splitter_initialization():
    splitter = TextSplitter()
    assert splitter is not None

def test_text_default_chunk_configuration():
    splitter = TextSplitter()
    assert splitter.chunk_size == 1000
    assert splitter.chunk_overlap == 200

def test_text_custom_chunk_configuration():
    splitter = TextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
    )
    assert splitter.chunk_size == 500
    assert splitter.chunk_overlap == 100

def test_text_empty_document_validation():
    splitter = TextSplitter()

    with pytest.raises(TextSplitterError) as exception:
        splitter.split_documents([])

    assert str(exception.value) == (
        "No documents provided for splitting."
    )

from langchain_core.documents import Document

def test_successful_document_splitting():
    """
    Verify TextSplitter successfully splits
    LangChain documents into chunks.
    """

    splitter = TextSplitter(
        chunk_size=50,
        chunk_overlap=10,
    )

    documents = [
        Document(
            page_content="This is a sample document. " * 20
        )
    ]

    chunks = splitter.split_documents(documents)

    assert chunks is not None
    assert len(chunks) > 1


def test_text_splitter_exception_handling(monkeypatch):
    """
    Verify TextSplitter raises TextSplitterError
    when an unexpected exception occurs.
    """

    splitter = TextSplitter()

    documents = [
        Document(
            page_content="This is a sample document."
        )
    ]

    def mock_split_documents(_):
        raise Exception("Unexpected error")

    monkeypatch.setattr(
        splitter.text_splitter,
        "split_documents",
        mock_split_documents,
    )

    with pytest.raises(TextSplitterError) as exception:
        splitter.split_documents(documents)

    assert str(exception.value) == (
        "Unable to split documents."
    )