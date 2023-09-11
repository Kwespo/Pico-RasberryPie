from machine import Pin
from utime import sleep


#Defining the pins.
OnboardLED = Pin(25, Pin.OUT)
OnboardLED.value(0) # the light starts as off.

GreenLightLED = Pin(1, Pin.OUT)
GreenLightLED.value(0) # the light starts as on

BlueLightLED = Pin(5, Pin.OUT)
BlueLightLED.value(0) # the light is on

def OnBoardLEDFlash():
  while True:
    OnboardLED.toggle()
    sleep(0.5)

def FlashingLight_Pin1():
  while True:
    GreenLightLED.toggle()
    sleep(0.5)
    print("Im Flashing!")

def AlternatingLights_Pin1_5():
  while True:
    GreenLightLED.value(0)
    sleep(0.1)
    BlueLightLED.value(1)
    sleep(0.1)
    GreenLightLED.value(1)
    sleep(0.1)
    BlueLightLED.value(0)
    sleep(0.1)


OnBoardLEDFlash()