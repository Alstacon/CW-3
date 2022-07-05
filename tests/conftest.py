import pytest
from utils import Funcs


@pytest.fixture()
def posts_data():
    data = Funcs('../main/data/data.json')
    return data


@pytest.fixture()
def comments_data():
    data = Funcs('../main/data/comments.json')
    return data


@pytest.fixture()
def post_pk():
    return [1, 2, 3, 4]


@pytest.fixture()
def key_words():
    return ['кот', 'лампочка', 'пока', 'все']


@pytest.fixture()
def users():
    return ['hank', 'leo', 'larry', 'johny']