
import logging
import RPi.GPIO as GPIO


class LampRelay:
    RELAY_PIN = 17

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RELAY_PIN, GPIO.OUT)
        GPIO.output(self.RELAY_PIN, GPIO.HIGH)
        logging.info("Relay switch for lamp set on HIGH")
        self.__lamp_output = 1

    def switch_lamp(self):
        self.__lamp_output = self.increment_lamp_state()
        GPIO.output(self.RELAY_PIN, self.increment_lamp_state())

        return self.__lamp_output

    def increment_lamp_state(self):
        return (self.__lamp_output + 1) % 2

    def turn_on_lamp(self):
        self.__lamp_output = 0
        GPIO.output(self.RELAY_PIN, self.__lamp_output)

    def turn_off_lamp(self):
        self.__lamp_output = 1
        GPIO.output(self.RELAY_PIN, self.__lamp_output)

    def get_lamp_state(self):
        return self.__lamp_output

    def cleanup(self):
        GPIO.output(self.RELAY_PIN, GPIO.LOW)
        # GPIO.cleanup()
