import logging

from flask_socketio import Namespace, emit
from auth import login_required
from rgb import RGBLamp


class RGBSockets(Namespace):
    def __init__(self, rgb_control: RGBLamp, namespace=None):
        super().__init__(namespace)
        self.rgb_control = rgb_control

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    @login_required
    def on_change_red(self, data):
        logging.info("Switch red testsocket")
        red_state = self.rgb_control.switch_red()
        emit('state', {'red': red_state})

    @login_required
    def on_change_green(self, data):
        logging.info("Switch green testsocket")
        green_state = self.rgb_control.switch_green()
        emit('state', {'green': green_state})

    @login_required
    def on_change_blue(self, data):
        logging.info("Switch blue testsocket")
        blue_state = self.rgb_control.switch_blue()
        emit('state', {'blue': blue_state})
