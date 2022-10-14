import json

import pytest

import conftest
from utils import Funcs, get_tags


class TestFuncs:
    def test_load_data(self, posts_data):
        posts_feed = posts_data.get_all_data()
        assert type(posts_feed) == list, 'Возвращает не список'
        assert len(posts_feed) > 0, 'Возвращает пустой список'

    def test_get_post_by_pk(self, posts_data, post_pk):
        for pk in post_pk:
            post = posts_data.get_post_by_pk(pk)
            assert type(post) == dict, 'Возвращает не словарь'
            assert len(post) > 0, 'Возвращает пустой словарь'
            assert post['pk'] == pk, 'Возвращает не тот пост'

    def test_search_for_post(self, posts_data, key_words):
        for word in key_words:
            posts = posts_data.search_for_post(word)
            assert type(posts) == list, 'Возвращает не список'
            for post in posts:
                assert word in post['content'], 'Возвращает не тот пост'
                assert len(post) > 0, 'Возвращает пустой словарь поста'

    def test_get_posts_by_user(self, posts_data, users):
        for user in users:
            posts = posts_data.get_posts_by_user(user)
            assert type(posts) == list, 'Возвращает не список'
            for post in posts:
                assert post['poster_name'] == user, 'Возвращает ленту не того пользователя'

    def test_get_comments_by_post_id(self, comments_data, post_pk):
        for pk in post_pk:
            comments, number_of_comments, counter_comments = comments_data.get_comments_by_post_id(pk)
            assert type(comments) == list, 'Возвращает не список'
            assert number_of_comments == len(comments), 'Возвращает не то количество комментариев'
            for comment in comments:
                assert comment['post_id'] == pk, 'Возвращает комменты не к тому посту'

    def test_get_tag(self, posts_data, post_pk):
        for pk in post_pk:
            post = posts_data.get_post_by_pk(pk)
            tagged_post = get_tags(post)
            assert type(tagged_post) == dict, 'Пост возвращается не словарем'
            for word in tagged_post['content']:
                if word.startswith('#'):
                    assert word not in tagged_post['content'], 'Слова с хештегом не заменяются'
                if word.startswith('<a href='):
                    assert word in tagged_post, 'Слова заменяются неправильно'

    def test_add_bookmark(self, post_pk, bookmarks_data, posts_data):
        bookmarks = bookmarks_data.get_all_data()
        for pk in post_pk:
            posts_data.add_bookmark(pk, bookmarks)
            with open('./main/data/bookmarks.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                assert len(data) > 0, 'Файл закладок не записывается'
                assert type(data) == list, 'В файл записывается не json'

    def test_delete_bookmark(self, post_pk, bookmarks_data, posts_data):
        bookmarks = bookmarks_data.get_all_data()
        for pk in post_pk:
            posts_data.delete_bookmark(pk, bookmarks)
            with open('./main/data/bookmarks.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                for post in data:
                    assert post['pk'] != pk, 'Пост не удален/удален не тот пост'


