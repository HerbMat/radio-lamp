import threading
import time

from lamp import LampRelay
from radio import RadioReader
from rgb import RGBLamp


class RadioLamp(threading.Thread):
    def __init__(self, lamp_relay: LampRelay, radio_reader: RadioReader, rgb_lamp: RGBLamp, socketio):
        super().__init__()
        self.lamp_relay = lamp_relay
        self.radio_reader = radio_reader
        self.rgb_lamp = rgb_lamp
        self.socketio = socketio

    def run(self):
        while True:
            pushed_button = self.radio_reader.get_button_pushed()
            if 1 == pushed_button:
                lamp_state = self.lamp_relay.switch_lamp()
                self.socketio.emit('state', {'lamp': lamp_state}, namespace='/lamp')
            if 2 == pushed_button:
                red_state = self.rgb_lamp.switch_red()
                self.socketio.emit('state', {'red': red_state}, namespace='/rgb')
            if 3 == pushed_button:
                green_state = self.rgb_lamp.switch_green()
                self.socketio.emit('state', {'green': green_state}, namespace='/rgb')
            if 4 == pushed_button:
                blue_state = self.rgb_lamp.switch_blue()
                self.socketio.emit('state', {'blue': blue_state}, namespace='/rgb')
            time.sleep(0.01)
