import os
import subprocess

from flask import Flask, app

import config
from routes import routes
from services.main_service import MainService

my_main_service = MainService()


# FLASK APP
def get_flask_app() -> app.Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object("config.Config")
    routes.init_routes(flask_app)
    subprocess.call("./bt.sh &", shell=True)
    return flask_app


app = get_flask_app()

# Main para ejecutar flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.Config.PORT)
