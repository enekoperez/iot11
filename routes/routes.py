from api.iot_api import iotApi


# prefijos de url
def init_routes(flask_app):
    # prefijo url para iot
    flask_app.register_blueprint(iotApi, url_prefix='/iot/')
