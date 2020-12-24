import argparse
import logging

from rpi_rf import RFDevice


class RadioReader:
    FIRST_BUTTON_SIGNAL = 5592332
    SECOND_BUTTON_SIGNAL = 5592512
    THIRD_BUTTON_SIGNAL = 5592323
    FOURTH_BUTTON_SIGNAL = 5592368

    def __init__(self):
        parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
        parser.add_argument('-g', dest='gpio', type=int, default=27,
                            help="GPIO pin (Default: 27)")
        args = parser.parse_args()
        self.__rf_device = RFDevice(args.gpio)
        self.__rf_device.enable_rx()
        self.__timestamp = None
        logging.info("Listening for codes on GPIO " + str(args.gpio))

    def get_button_pushed(self):
        if self.__rf_device.rx_code_timestamp != self.__timestamp:
            self.__timestamp = self.__rf_device.rx_code_timestamp
            if self.__rf_device.rx_code == self.FIRST_BUTTON_SIGNAL:
                return 1
            if self.__rf_device.rx_code == self.SECOND_BUTTON_SIGNAL:
                return 2
            if self.__rf_device.rx_code == self.THIRD_BUTTON_SIGNAL:
                return 3
            if self.__rf_device.rx_code == self.FOURTH_BUTTON_SIGNAL:
                return 4
        return 0

    def cleanup(self):
        self.__rf_device.cleanup()
