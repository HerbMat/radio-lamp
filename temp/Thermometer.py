import glob
import time
from typing import List


class Thermometer(object):
    DEV_BASE_DIR = '/sys/bus/w1/devices/'
    TEMP_READING_FILE = '/w1_slave'
    WORKING_THERMOMETER_READING = 'YES'
    TEMPERATURE_READING_TEXT_BEGINNING = 't='

    def read_celsius(self) -> float:
        return self.read_temp_raw() / 1000.0

    def read_fahrenheit(self) -> float:
        temperature_celsius = self.read_celsius()

        return temperature_celsius * 9.0/5.0 + 32.0

    def read_kelvin(self):
        return self.read_celsius() + 273.15

    def read_temp_raw(self) -> float:
        temperature_file_text_lines = self.__read_temperature_file()
        while temperature_file_text_lines[0].strip()[-3:] != self.WORKING_THERMOMETER_READING:
            time.sleep(0.2)
            temperature_file_text_lines = self.__read_temperature_file()
        temperature_reading_pos = temperature_file_text_lines[1].find(self.TEMPERATURE_READING_TEXT_BEGINNING)
        if temperature_reading_pos != -1:
            return float(temperature_file_text_lines[1][temperature_reading_pos + 2:])

    def __read_temperature_file(self) -> List[str]:
        device_folder = glob.glob(self.DEV_BASE_DIR + '28*')[0]
        with open(device_folder + self.TEMP_READING_FILE, 'r') as temperature_file:
            return temperature_file.readlines()
