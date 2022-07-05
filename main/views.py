from utils import Funcs
from flask import Blueprint, render_template, request

app_blueprint = Blueprint('app_blueprint', __name__, template_folder='templates')


@app_blueprint.route('/')
def feed_page():
    data = Funcs('main/data/data.json')
    feed = data.get_all_data()
    return render_template('index.html', feed=feed)


@app_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    data_post = Funcs('main/data/data.json')
    data_comments = Funcs('main/data/comments.json')
    post = data_post.get_post_by_pk(post_id)
    try:
        comments, number_of_comments, counter_comments = data_comments.get_comments_by_post_id(post_id)
        return render_template('post.html', post=post, comments=comments,
                               number_of_comments=number_of_comments,
                               counter_comments=counter_comments)
    except ValueError:
        return 'Такого поста нет'


@app_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    data = Funcs('main/data/data.json')
    posts = data.search_for_post(s)
    posts_count = len(posts)
    return render_template('search.html', posts=posts, posts_count=posts_count)


@app_blueprint.route('/user/<username>')
def users_page(username):
    data = Funcs('main/data/data.json')
    posts = data.get_posts_by_user(username)

    return render_template('user-feed.html', posts=posts, username=username)
