import logging

import RPi.GPIO as GPIO
from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_socketio import SocketIO

from RadioLamp import RadioLamp
from auth import authenticate, identity
from configuration import sso_properties
from event import RGBSockets, LightSockets
from lamp import LampRelay
from radio import RadioReader
from rest import create_lamp_page, create_rgb_page, create_temperature_page
from rgb import RGBLamp
from temp import Thermometer

if __name__ == '__main__':
    lamp_control = None
    radio = None
    rgb_lamp = None
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                            format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )
        lamp_control = LampRelay()
        rgb_lamp = RGBLamp()
        radio = RadioReader()
        app = Flask(__name__)
        cors = CORS(app)
        app.config['SECRET_KEY'] = sso_properties.get_secret_key()
        socket_io = SocketIO(app, cors_allowed_origins="*", ping_timeout=10, ping_interval=5, async_mode='threading')
        socket_io.on_namespace(RGBSockets(rgb_lamp, '/rgb'))
        socket_io.on_namespace(LightSockets(lamp_control, '/lamp'))
        radio_lamp = RadioLamp(lamp_relay=lamp_control, radio_reader=radio, rgb_lamp=rgb_lamp, socketio=socket_io)
        radio_lamp.start()
        jwt_app = JWT(app, authenticate, identity)
        app.register_blueprint(create_rgb_page(rgb_lamp), url_prefix='/rgb')
        app.register_blueprint(create_lamp_page(lamp_control), url_prefix='/lamp')
        app.register_blueprint(create_temperature_page(Thermometer()), url_prefix='/temperature')

        socket_io.run(app, host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        lamp_control.cleanup()
        radio.cleanup()
        rgb_lamp.cleanup()
        GPIO.cleanup()
