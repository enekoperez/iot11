from api.iot_api import iotApi


# prefixes de url
def init_routes(flask_app):
    # prefix url para iot
    flask_app.register_blueprint(iotApi, url_prefix='/iot/')
