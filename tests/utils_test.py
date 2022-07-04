import pytest
from utils import Funcs


@pytest.fixture()
def data():
    data_posts = Funcs('app/main/data/data.json')
    return data_posts


@pytest.fixture()
def pk():
    return [1, 2, 3, 4, 5, 6, 7, 8]


class TestFunc:
    def test_get_all(self, data):
        full_posts_data = data.get_all_data()
        assert type(full_posts_data) == list, 'Возвращает не список'
        assert len(full_posts_data) > 0, 'Возвращает пустой список'
        for n in full_posts_data:
            assert type(n) == dict, 'Внутри списка не словари'


    def test_get_post_by_pk(self, data, pk):
        needed_post = data.get_post_by_pk(pk[0])
        assert needed_post['pk'] == 1, 'Возвращает не тот пост'
        needed_post = data.get_post_by_pk(pk[1])
        assert needed_post['pk'] == 2, 'Возвращает не тот пост'
