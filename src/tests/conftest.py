import os

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from api.utils import load_files
from api.main import start_application


@pytest.fixture(scope="session")
def app():
    """
    Инициализация приложения
    """
    _app = start_application()
    load_files(os.path.abspath('test_builds'))

    yield _app


@pytest.fixture(scope="session")
def client(app: FastAPI):
    """
    Тестовый клиент
    """
    with TestClient(app=app, base_url="http://0.0.0.0:8000/api/v1/") as client:
        yield client
