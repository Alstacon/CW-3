import pytest
from run import app


@pytest.fixture()
def right_keys():
    return ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]


def test_api_posts(right_keys):
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) == list, 'Возвращает не список'
    for post in response.json:
        for k in post.keys():
            assert k in right_keys, 'В словарях не те ключи'


def test_api_post_id(right_keys):
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) == dict, 'Возвращает не словарь'
    for k in response.json.keys():
        assert k in right_keys, 'В словаре не те ключи'
