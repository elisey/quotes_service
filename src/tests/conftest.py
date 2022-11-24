from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def fixture_dir() -> Path:
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def test_quotes_dir(fixture_dir) -> Path:
    return fixture_dir / "test_quotes.json.gz"


@pytest.fixture
def test_client(test_quotes_dir):
    from core.config import settings

    settings.quotes_json_file_path = test_quotes_dir

    from main import app

    client = TestClient(app)
    yield client
