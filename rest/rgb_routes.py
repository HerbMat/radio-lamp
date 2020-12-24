from flask import Blueprint, jsonify
from flask_jwt import jwt_required
from flask_socketio import emit
from rgb import RGBLamp
import logging


def create_rgb_page(rgb_lamp: RGBLamp):
    rgb_page = Blueprint('rgb_page', __name__)

    @rgb_page.route('/red', methods=['PUT'])
    @jwt_required()
    def switch_red():
        logging.info("Switch red")
        red_state = rgb_lamp.switch_red()
        emit('state', {'data': red_state})

        return jsonify(red_state)

    @rgb_page.route('/blue', methods=['PUT'])
    @jwt_required()
    def switch_blue():
        logging.info("Switch blue")

        return jsonify(rgb_lamp.switch_blue())

    @rgb_page.route('/green', methods=['PUT'])
    @jwt_required()
    def switch_green():
        logging.info("Switch green")

        return jsonify(rgb_lamp.switch_green())

    @rgb_page.route('/red', methods=['GET'])
    @jwt_required()
    def get_state_red():
        return jsonify(rgb_lamp.get_red_state())

    @rgb_page.route('/blue', methods=['GET'])
    @jwt_required()
    def get_blue_state():
        return jsonify(rgb_lamp.get_blue_state())

    @rgb_page.route('/green', methods=['GET'])
    @jwt_required()
    def get_green_state():
        return jsonify(rgb_lamp.get_green_state())

    return rgb_page
