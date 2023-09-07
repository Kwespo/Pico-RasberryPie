import machine as Machine
import utime


Dot = Machine.Pin(1, Machine.Pin.OUT)
Dot.value(0)
Dash = Machine.Pin(5, Machine.Pin.OUT)#Dash it not its own LED. 
                                      #Its working in conjunction with DOT to 
                                      #make a long dash in LED.
Dash.value(0)


MessageMorse = (input("Input your message in morse code to add spaces please add a forwards slash or space between the words: ")) #gets the message in morse code
MessageList = list(MessageMorse)

for i in MessageList:
  if i == ".":#if its a dot it makes the dot LED display
    Dot.value(1)
    Dash.value(0)
    utime.sleep(0.5)#keeps the light on for 0.5 seconds
    Dot.value(0) #turns off the light
    Dash.value(0)
    utime.sleep(0.2)#waits 0.2 seconds before showing the next set of LED
  elif i == "-": #if its a dash it makes both LEDs turn on
    Dash.value(1)
    Dot.value(1)
    utime.sleep(0.5)
    Dot.value(0)
    Dash.value(0)
    utime.sleep(0.2)
  elif i == "/" or i == " ":#if its a space or '/' it makes a gap between the next message
    utime.sleep(1)
  else: 
    print(f"Invalid Char '{i}' in message. Please re-enter message")
    #If the character isn't one of the 3 choosen it will say that the char (and shows the 
    #incorrect char) isnt allowed and asks to re enter the messages