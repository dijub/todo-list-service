from http import HTTPStatus


def test_get_root_must_return_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_get_hello_html_must_return_hello_world_in_html(client):
    response = client.get('/hello-html')

    assert response.status_code == HTTPStatus.OK

    assert '<h1>Hello World</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'diego',
            'email': 'diego@email.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'diego',
        'email': 'diego@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'diego', 'email': 'diego@email.com', 'id': 1}]
    }


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'diego',
        'email': 'diego@email.com',
        'id': 1,
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'newpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_update_user_error_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'error',
            'email': 'error@error.com',
            'password': 'errorpass',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_delete_user_error_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_get_user_error_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}
