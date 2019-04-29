
# Import standard python modules
import time
 
# import GPIO library
import RPi.GPIO as GPIO
 
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
 
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'your AIO key'

 
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
#ADAFRUIT_IO_USERNAME = 'praneetheddu'
ADAFRUIT_IO_USERNAME = 'your AIO username' 
# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a ' feed

    up = aio.feeds('up')
    down = aio.feeds('down')
    left = aio.feeds('left')
    right = aio.feeds('right')

except RequestError: # create a feed

    feed5 = Feed(name="down")
    down = aio.create_feed(feed5)
    
    feed6 = Feed(name="left")
    left = aio.create_feed(feed6)
    
    feed7 = Feed(name="right")
    right = aio.create_feed(feed7)
    
    feed8 = Feed(name="up")
    up = aio.create_feed(feed8)
    
  
while True:
	# Create feeds
    upVal = aio.receive(up.key)
    downVal = aio.receive(down.key)
    leftVal = aio.receive(left.key)
    rightVal = aio.receive(right.key)

    # Set the Motor values accordingly when any of directional keys are pressed.
    if int(upVal.value):
        print("Motor up is HIGH")
        file = open("MotorWrite.txt", "w")
        file.write("1")
        file.close()
    elif int(downVal.value):
        print("Motor down is HIGH")
        file = open("MotorWrite.txt", "w")
        file.write("2")
        file.close()
    elif int(leftVal.value):
        print("Motor left is HIGH")
        file = open("MotorWrite.txt", "w")
        file.write("3")
        file.close()
    elif int(rightVal.value):
        print("Motor right is HIGH")
        file = open("MotorWrite.txt", "w")
        file.write("4")
        file.close()
    else:
        print("Motor is LOW")
        file = open("MotorWrite.txt", "w")
        file.write("0")
        file.close()
    time.sleep(1.0)
