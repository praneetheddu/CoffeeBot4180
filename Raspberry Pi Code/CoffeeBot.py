
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
ADAFRUIT_IO_USERNAME = 'your AIO username'
 
# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
 
try: # if we have feeds
    creamerfeed = aio.feeds('creamerfeed')
    sugarfeed = aio.feeds('sugarfeed')
    sweetnerfeed = aio.feeds('sweetnerfeed')
    startfeed = aio.feeds('startfeed')
	
except RequestError: # create feeds
    feed = Feed(name="creamerfeed")
    creamerfeed = aio.create_feed(feed)
    feed2 = Feed(name="sugarfeed")
    sugarfeed = aio.create_feed(feed2)
    feed3 = Feed(name="sweetnerfeed")
    sweetnerfeed = aio.create_feed(feed3)
    feed4 = Feed(name="startfeed")
    startfeed = aio.create_feed(feed4)

 
oneTeaSpoonTime = 1.5 # flow rate for 1 table spoon

#Relay GPIO setup
creamerGPIO = 21 
sweetnerGPIO = 20
sugarGPIO = 12
CoffeeGPIO = 16

RelayPins = [12, 21, 20, 16]

##Set the relay switches to low before the program starts
GPIO.setmode(GPIO.BCM)
for pin in RelayPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
 
while True:
	## Feeds setup
    creamer = aio.receive(creamerfeed.key)
    sugar = aio.receive(sugarfeed.key)
    sweetner = aio.receive(sweetnerfeed.key)
    start = aio.receive(startfeed.key)
    
    
    if (int(start.value)): #Indicates that start is pressed
        ## Set LED to high 
        file = open("LEDWrite.txt", "w")
        file.write("1")
        file.close()
		## Flows the desired liquids customized by the user in tea spoons increments
        if int(sweetner.value) > 0:
            GPIO.output(sweetnerGPIO, GPIO.LOW)
            time.sleep(int(sweetner.value) * oneTeaSpoonTime)
            GPIO.output(sweetnerGPIO, GPIO.HIGH)
        if int(sugar.value) > 0:
            GPIO.output(sugarGPIO, GPIO.LOW)
            time.sleep(int(sugar.value) * oneTeaSpoonTime)
            GPIO.output(sugarGPIO, GPIO.HIGH)
        if int(creamer.value) > 0:
            GPIO.output(creamerGPIO, GPIO.LOW)
            time.sleep(int(creamer.value) * oneTeaSpoonTime)
            GPIO.output(creamerGPIO, GPIO.HIGH)
        
		# Coffee flow code. Pouring in increments gives enough time for the coffee to drain into the cup 
        for i in range (5):
            GPIO.output(CoffeeGPIO, GPIO.LOW)
            time.sleep(3)
            GPIO.output(CoffeeGPIO, GPIO.HIGH)
            time.sleep(10)
			
			
			   
    
	## LED value is 0 for inactivity
    file = open("LEDWrite.txt", "w")
    file.write("0")
    file.close()
    time.sleep(1.0)
