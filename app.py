from flask import Flask, jsonify
from main.views import app_blueprint
from logger import logger
from utils import Funcs


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_blueprint(app_blueprint)

    return app


app = create_app()


@app.route('/api/posts')
def api_posts():
    data = Funcs('main/data/data.json')
    data = data.get_all_data()
    logger.info("Запрос api/main")
    return jsonify(data)


@app.route('/api/posts/<int:post_id>')
def api_posts_id(post_id):
    data_post = Funcs('main/data/data.json')
    post = data_post.get_post_by_pk(post_id)
    logger.info(f"Запрос api/main{post_id}")
    return jsonify(post)


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось!", 404


@app.errorhandler(500)
def not_found(e):
    logger.info("Ошибка сервера")
    return "Сервер наелся и спит! :(", 500


if __name__ == '__main__':
    app.run()
