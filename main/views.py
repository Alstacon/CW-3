from werkzeug.utils import redirect
from utils import Funcs, get_tags
from flask import Blueprint, render_template, request

app_blueprint = Blueprint('app_blueprint', __name__, template_folder='templates')


@app_blueprint.route('/')
def feed_page():
    data = Funcs('main/data/data.json')
    bookmarks = Funcs('main/data/bookmarks.json')
    bookmarks = bookmarks.get_all_data()
    count_bookmarks = len(bookmarks)
    feed = data.get_all_data()
    return render_template('index.html', feed=feed, count_bookmarks=count_bookmarks)


@app_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    data_post = Funcs('main/data/data.json')
    data_comments = Funcs('main/data/comments.json')
    post = data_post.get_post_by_pk(post_id)
    post = get_tags(post)
    try:
        comments, number_of_comments, counter_comments = data_comments.get_comments_by_post_id(post_id)
        return render_template('post.html', post=post, comments=comments,
                               number_of_comments=number_of_comments,
                               counter_comments=counter_comments)
    except ValueError:
        return 'Такого поста нет'


@app_blueprint.route('/tag/<tag_name>')
def tag_posts_page(tag_name):
    tag_name = '#' + tag_name
    data = Funcs('main/data/data.json')
    posts = data.search_for_post(tag_name)
    return render_template('tag.html', posts=posts, tag_name=tag_name)


@app_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    data = Funcs('main/data/data.json')
    posts = data.search_for_post(s)
    if len(posts) > 10:
        posts = posts[:10]
    posts_count = len(posts)
    return render_template('search.html', posts=posts, posts_count=posts_count)


@app_blueprint.route('/user/<username>')
def users_page(username):
    data = Funcs('main/data/data.json')
    posts = data.get_posts_by_user(username)
    if posts:
        return render_template('user-feed.html', posts=posts, username=username)
    return render_template('user_without_posts.html', username=username)


@app_blueprint.route('/bookmarks/add/<int:post_id>')
def bookmark_add_page(post_id):
    posts_data = Funcs('main/data/data.json')
    bookmarks_data = Funcs('main/data/bookmarks.json')
    bookmarks = bookmarks_data.load_data()
    posts_data.add_bookmark(post_id, bookmarks)
    return redirect("/", code=302)


@app_blueprint.route('/bookmarks/remove/<int:post_id>')
def bookmark_del_page(post_id):
    posts_data = Funcs('main/data/data.json')
    bookmarks_data = Funcs('main/data/bookmarks.json')
    bookmarks = bookmarks_data.load_data()
    posts_data.delete_bookmark(post_id, bookmarks)
    return redirect("/bookmarks", code=302)


@app_blueprint.route('/bookmarks')
def bookmarks_list_page():
    bookmarks_data = Funcs('main/data/bookmarks.json')
    bookmarks = bookmarks_data.load_data()
    if len(bookmarks) == 0:
        return render_template('zero_bookmarks.html')
    return render_template('bookmarks.html', bookmarks=bookmarks)
