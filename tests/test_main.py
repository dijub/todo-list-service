from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_list.main import app


def test_get_root_must_return_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello, world!'}
