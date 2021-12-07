from api.iot_api import iotApi


def init_routes(flask_app):
    flask_app.register_blueprint(iotApi, url_prefix='/iot/')
