import json


def get_tags(post):
    """Превращает теги в посте в ссылки"""
    text = post['content'].split(' ')
    new_text = []
    for word in text:
        if word[0].isalpha():
            new_text.append(word)
        elif word.startswith('#'):
            index = text.index(word)
            text[index] = f"""<a href="/tag/{word.lstrip('#')}">{word}</a>"""
            new_text.append(text[index])
    post['content'] = ' '.join(new_text)
    return post


class Funcs:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружает данные из json файла"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all_data(self) -> list[dict]:
        """Возвращает полный список постов/комментов"""
        feed = self.load_data()
        return feed

    def get_post_by_pk(self, pk) -> dict:
        """Возвращает пост по номеру"""
        feed = self.load_data()
        for n in feed:
            if n['pk'] == pk:
                return n

    def search_for_post(self, query) -> list[dict]:
        """Возвращает список постов по ключевому слову"""
        feed = self.load_data()
        needed_posts = [n for n in feed if query in n['content']]
        return needed_posts

    def get_posts_by_user(self, user_name) -> list[dict] | str:
        """Возвращает посты конкретного юзера"""
        feed = self.load_data()
        needed_posts = [n for n in feed if user_name == n['poster_name']]
        return needed_posts

    def get_comments_by_post_id(self, post_id) -> tuple:
        """Возвращает комменты к выбранному посту"""
        counter_comments = 'Комментариев'
        comments = self.load_data()
        needed_comments = [n for n in comments if post_id == n['post_id']]
        number_of_comments = len(needed_comments)
        if str(len(needed_comments)).endswith('1') and len(needed_comments) > 20 or len(needed_comments) == 1:
            counter_comments = 'Комментарий'
        elif str(len(needed_comments)).endswith('2') or str(len(needed_comments)).endswith('3') \
                or str(len(needed_comments)).endswith('4') and \
                len(needed_comments) > 20 or len(needed_comments) in [2, 3, 4]:
            counter_comments = 'Комментария'
        return needed_comments, number_of_comments, counter_comments

    def add_bookmark(self, post_id, bookmarks):
        """Добавляет словарь поста в файл закладок"""
        post = self.get_post_by_pk(post_id)
        bookmarks.append(post)
        with open('./main/data/bookmarks.json', 'w', encoding='utf-8') as file:
            json.dump(bookmarks, file, indent=1, ensure_ascii=False)

    def delete_bookmark(self, post_id, bookmarks):
        """Удаляет словарь поста из файла закладок"""
        post = self.get_post_by_pk(post_id)
        index = bookmarks.index(post) if post in bookmarks else 'Такого поста нет в закладках'
        bookmarks.pop(index)
        with open('./main/data/bookmarks.json', 'w', encoding='utf-8') as file:
            json.dump(bookmarks, file, indent=1, ensure_ascii=False)
