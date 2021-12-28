from flask import Blueprint, request, jsonify

from services.main_service import MainService
from services.sensores import Sensores

iotApi = Blueprint('iotApi', __name__)

my_main_service = MainService()
my_sensores = Sensores()


@iotApi.route('execute', methods=['GET'])
def execute():
    if request.is_json:
        my_main_service.main(request.json)
        return jsonify(message='ok'), 200


@iotApi.route('ender', methods=['GET'])
def ender():
    my_main_service.ender()
    return jsonify(message='ender done'), 200

@iotApi.route('temp-and-humi', methods=['GET'])
def temp_and_humi():
    if request.is_json:
        conf_temp = request.json['conf_temp']
        conf_humi = request.json['conf_humi']
        response = my_sensores.temp_and_humi(conf_temp=conf_temp, conf_humi=conf_humi)
        return jsonify(response), 200
