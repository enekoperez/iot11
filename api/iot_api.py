from flask import Blueprint, request, jsonify

from services.main_service import MainService

iotApi = Blueprint('iotApi', __name__)

my_main_service = MainService()


@iotApi.route('example', methods=['GET'])
def example():
    return jsonify(message='example working ok'), 200


@iotApi.route('execute', methods=['GET'])
def execute():
    if request.is_json:
        my_main_service.main(request.json)
        return jsonify(message='ok'), 200


@iotApi.route('ender', methods=['GET'])
def ender():
    my_main_service.ender()
    return jsonify(message='ender done'), 200
