from machine import Pin
from utime import sleep

LEDPin = Pin(0, Pin.OUT)

while True:
  LEDPin.toggle()
  sleep(0.5)
  print("Light Flashing")