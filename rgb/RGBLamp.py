import logging
import RPi.GPIO as GPIO


class RGBLamp:
    RED_PIN = 5
    GREEN_PIN = 6
    BLUE_PIN = 13

    @staticmethod
    def cleanup():
        logging.info('Destructor called, RGB Lamp deleted.')
        GPIO.cleanup()

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RED_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)
        self.__red_state = 0
        self.__green_state = 0
        self.__blue_state = 0
        logging.info("Setup RGB Lamp ")

    def switch_red(self):
        self.__red_state = (self.__red_state + 1) % 2
        logging.info("Set Red to %s", self.__red_state)
        GPIO.output(self.RED_PIN, self.__red_state)

        return self.__red_state

    def switch_green(self):
        self.__green_state = (self.__green_state + 1) % 2
        logging.info("Set Green to %s", self.__green_state)
        GPIO.output(self.GREEN_PIN, self.__green_state)

        return self.__green_state

    def switch_blue(self):
        self.__blue_state = (self.__blue_state + 1) % 2
        logging.info("Set Blue to %s", self.__blue_state)
        GPIO.output(self.BLUE_PIN, self.__blue_state)

        return self.__blue_state

    def turn_on_red(self):
        logging.info("Turn on red")
        GPIO.output(self.RED_PIN, GPIO.HIGH)

    def turn_on_green(self):
        logging.info("Turn on green")
        GPIO.output(self.GREEN_PIN, GPIO.HIGH)

    def turn_on_blue(self):
        logging.info("Turn on blue")
        GPIO.output(self.BLUE_PIN, GPIO.HIGH)

    def turn_off_red(self):
        logging.info("Turn off red")
        GPIO.output(self.RED_PIN, GPIO.LOW)

    def turn_off_green(self):
        logging.info("Turn off green")
        GPIO.output(self.GREEN_PIN, GPIO.LOW)

    def turn_off_blue(self):
        logging.info("Turn off blue")
        GPIO.output(self.BLUE_PIN, GPIO.LOW)

    def get_red_state(self):
        return self.__red_state

    def get_green_state(self):
        return self.__green_state

    def get_blue_state(self):
        return self.__blue_state
