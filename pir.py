import RPi.GPIO as GPIO


class PassiveInfraredSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def motion_detected(self):
        return GPIO.input(self.pin)
