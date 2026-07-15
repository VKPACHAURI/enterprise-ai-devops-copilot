from config.settings import settings


def test_ollama_model():
    assert settings.OLLAMA_MODEL == "llama3.2"


def test_log_level():
    assert settings.LOG_LEVEL == "INFO"


def test_retry_count():
    assert settings.MAX_RETRY_COUNT == 3


def test_request_timeout():
    assert settings.REQUEST_TIMEOUT == 30


def test_data_directory():
    assert settings.DATA_DIR.name == "data"



