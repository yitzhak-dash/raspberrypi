#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from alarm_manager import *
from camera import *
import commander

PIR_OUT_PIN = 11  # pin11

TIME_TO_SLEEP_SEC = 0.3


class MotionDetector:
    def __init__(self, alarm_manager):
        self.alarm_manager = alarm_manager

    def setup(self):
        GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        GPIO.setup(PIR_OUT_PIN, GPIO.IN)  # Set BtnPin's mode is input

    def loop(self):
        while True:
            if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
                time.sleep(TIME_TO_SLEEP_SEC)
            else:
                self.alarm_manager.movement_detected()
                commander.send_message('enemy is detected')
                time.sleep(TIME_TO_SLEEP_SEC)

    def destroy(self):
        self.dispose()

    def dispose(self):
        GPIO.cleanup()  # Release resource
        self.alarm_manager.dispose()
