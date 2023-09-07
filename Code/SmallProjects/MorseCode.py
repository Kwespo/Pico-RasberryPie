import machine as Machine
import utime


Dot = Machine.Pin(1, Machine.Pin.OUT)
Dot.value(0)
Dash = Machine.Pin(5, Machine.Pin.OUT)
Dash.value(0)


MessageMorse = (input("Input your message in morse code to add spaces please add a forwards slash or space between the words.")) #gets the message in morse code
MessageList = list(MessageMorse)

for i in MessageList:
  if i == ".":
    Dot.value(1)
    Dash.value(0)
    utime.sleep(0.5)
    Dot.value(0)
    Dash.value(0)
    utime.sleep(0.2)
  elif i == "-":
    Dash.value(1)
    Dot.value(1)
    utime.sleep(0.5)
    Dot.value(0)
    Dash.value(0)
    utime.sleep(0.2)
  elif i == "/" or i == " ":
    utime.sleep(1)
  else: 
    print(f"Invalid Char '{i}' in message. Please enter message")