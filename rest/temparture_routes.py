from flask import Blueprint, jsonify
from flask_jwt import jwt_required

from temp import Thermometer


def create_temperature_page(thermometer: Thermometer):
    temperature_page = Blueprint('temperature_page', __name__)

    @temperature_page.route('/celsius')
    @jwt_required()
    def get_celsius_temperature():
        return jsonify(thermometer.read_celsius())

    @temperature_page.route('/kelvin')
    @jwt_required()
    def get_kelvin_temperature():
        return jsonify(thermometer.read_kelvin())

    @temperature_page.route('/fahrenheit')
    @jwt_required()
    def get_fahrenheit_temperature():
        return jsonify(thermometer.read_fahrenheit())

    return temperature_page
