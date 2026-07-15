from  config.constants import (
        APP_NAME,
        APP_VERSION,
        AUTHOR,
        DEFAULT_ENCODING
        )


def test_app_name():
    assert APP_NAME == "Enterprise AI DevOps Copilot"

def test_app_version():
    assert APP_VERSION == "0.2.0"


def test_author():
    assert AUTHOR == "vishesh pachauri"


def test_default_encoding():
    assert DEFAULT_ENCODING == "utf-8"


