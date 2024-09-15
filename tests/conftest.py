import pytest
from fastapi.testclient import TestClient

from todo_list.main import app


@pytest.fixture
def client():
    return TestClient(app)
