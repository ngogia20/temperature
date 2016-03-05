import RPi.GPIO as GPIO
import dht11
import time
import datetime

import requests
import json

url = 'http://imfpush.ng.bluemix.net/imfpush/v1/apps/b5af80bd-8f14-4e51-afde-7dd1b36ad2f0/messages'
appSecret = 'e1152f70-123f-4b27-bbd9-335fc2a6fb7f'
ctype = 'application/json'
values = {"message": { "alert": "Test Message from Python" }}
head = { 'Content-Type' : ctype,'appSecret' : appSecret }


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)

while True:
	result = instance.read()
	if result.is_valid():
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d %%" % result.humidity)
		values = {"message": { "alert": result.temperature }}
		req = requests.post(url, data=json.dumps(values), headers=head)
    		
	time.sleep(1)
