import logging

from flask_socketio import Namespace, emit
from auth import login_required
from lamp import LampRelay


class LightSockets(Namespace):
    def __init__(self, lamp_control: LampRelay, namespace=None):
        super().__init__(namespace)
        self.lamp_control = lamp_control

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    @login_required
    def on_change_lamp(self, data):
        logging.info("Switch lamp testsocket")
        lamp_state = self.lamp_control.switch_lamp()
        emit('state', {'lamp': lamp_state}, broadcast=True)
