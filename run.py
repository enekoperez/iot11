from flask import Flask, app

import config
from routes import routes
from services.main_service import MainService

my_main_service = MainService()


def get_flask_app() -> app.Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object("config.Config")
    routes.init_routes(flask_app)
    return flask_app


app = get_flask_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.Config.PORT)
