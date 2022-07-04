from flask import Blueprint, jsonify
from utils import Funcs
from logger import logger

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def api_posts():
    data = Funcs('app/main/data/data.json')
    data = data.get_all_data()
    logger.info("Запрос api/app")
    return jsonify(data)


@api_blueprint.route('/api/<int:post_id>')
def api_posts_id(post_id):
    data_post = Funcs('app/main/data/data.json')
    post = data_post.get_post_by_pk(post_id)
    logger.info(f"Запрос api/app{post_id}")
    return jsonify(post)
