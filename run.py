from flask import Flask
from app.main.views import app_blueprint
from app.api.views import api_blueprint
from logger import logger

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(api_blueprint)
app.register_blueprint(app_blueprint)


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось!", 404


@app.errorhandler(500)
def not_found(e):
    logger.info("Ошибка сервера")
    return "Сервер наелся и спит! :(", 500


if __name__ == '__main__':
    app.run()
