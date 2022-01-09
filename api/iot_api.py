from flask import Blueprint, request, jsonify

from services.bluetooth import send_b
from services.main_service import MainService
from services.sensores import Sensores

iotApi = Blueprint('iotApi', __name__)

my_main_service = MainService()
my_sensores = Sensores()


# call para ejecutar
@iotApi.route('execute', methods=['GET'])
def execute():
    if request.is_json:
        my_main_service.main(request.json)
        return jsonify(message='Running...'), 200


# call para detener 'execute'
@iotApi.route('ender', methods=['GET'])
def ender():
    my_main_service.ender()
    return jsonify(message='Stopped!'), 200


# call API para recibir informacion de distancia
@iotApi.route('distance', methods=['GET'])
def distance():
    response = my_sensores.distance()
    send_b(str(response))
    return jsonify(response), 200


# call API para recibir informacion de temperatura y humedad
@iotApi.route('temp-and-humi', methods=['GET'])
def temp_and_humi():
    response = my_sensores.temp_and_humi()
    return jsonify(response), 200


# call API para recibir informacion de luz
@iotApi.route('light', methods=['GET'])
def light():
    response = my_sensores.light()
    return jsonify(response), 200
