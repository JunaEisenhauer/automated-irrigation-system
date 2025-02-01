# sudo pip3 install RPi.GPIO
import RPi.GPIO as GPIO


class Pump:
    def __init__(self, gpio: bytes):
        self.gpio = gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)
        self.stop()

    def start(self) -> None:
        GPIO.output(self.gpio, GPIO.LOW)

    def stop(self) -> None:
        GPIO.output(self.gpio, GPIO.HIGH)

    def is_running(self) -> bool:
        return GPIO.input(self.gpio) == GPIO.LOW
