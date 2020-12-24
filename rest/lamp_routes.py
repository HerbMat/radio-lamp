from flask import Blueprint, jsonify
from flask_jwt import jwt_required
from lamp import LampRelay

import logging


def create_lamp_page(lamp_relay: LampRelay):
    lamp_page = Blueprint('lamp_page', __name__)

    @lamp_page.route('', methods=['PUT'])
    @jwt_required()
    def switch_lamp():
        logging.info("Switch lamp")

        return jsonify(lamp_relay.switch_lamp())

    @lamp_page.route('')
    @jwt_required()
    def get_lamp_state():
        return jsonify(lamp_relay.get_lamp_state())

    return lamp_page
