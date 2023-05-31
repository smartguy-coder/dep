import pytest
import http

from fastapi.testclient import TestClient
from main import app


@pytest.fixture()
def client():
    # for testing @app.on_event('startup') decorated
    with TestClient(app) as client:
        yield client


def test_home(client: TestClient) -> None:
    response = client.get('/')
    assert response.status_code == http.HTTPStatus.OK
    assert response.json() == {'message': 'hello'}


def test_web(client: TestClient) -> None:
    response = client.get('/pages/books')
    assert response.status_code == http.HTTPStatus.OK
