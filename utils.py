import json


class Funcs:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """loads data from json file"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all_data(self) -> list[dict]:
        """returns all data"""
        feed = self.load_data()
        return feed

    def get_post_by_pk(self, pk) -> dict:
        """returns the post by it's pk"""
        feed = self.load_data()
        for n in feed:
            if n['pk'] == pk:
                return n

    def search_for_post(self, query) -> list[dict]:
        """returns the list of app bu the keyword"""
        needed_posts = []
        feed = self.load_data()
        for n in feed:
            if query in n['content']:
                needed_posts.append(n)
        return needed_posts

    def get_posts_by_user(self, user_name) -> list[dict] | str:
        """returns app of a specific user"""
        feed = self.load_data()
        needed_posts = []
        for n in feed:
            if user_name == n['poster_name']:
                needed_posts.append(n)
        return needed_posts

    def get_comments_by_post_id(self, post_id) -> tuple:
        """returns comment for certain post"""
        needed_comments = []
        counter_comments = 'Комментариев'
        feed = self.load_data()
        for n in feed:
            if post_id == n['post_id']:
                needed_comments.append(n)
        number_of_comments = len(needed_comments)
        if str(len(needed_comments)).endswith('1') and len(needed_comments) > 20 or len(needed_comments) == 1:
            counter_comments = 'Комментарий'
        elif str(len(needed_comments)).endswith('2') or str(len(needed_comments)).endswith('3')\
                or str(len(needed_comments)).endswith('4') and \
                len(needed_comments) > 20 or len(needed_comments) in [2, 3, 4]:
            counter_comments = 'Комментария'
        return needed_comments, number_of_comments, counter_comments






