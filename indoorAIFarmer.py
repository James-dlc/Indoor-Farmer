#indoorAIFarmer.py
#by: James De La Cruz
#This program monitors a plant (or multiple) by opening valves from a distilled
#water tank. Uses relays for water valves, heater to warm water, and temperature
#and humidity monitoring (plant's environment). Watering will be on a daily
#or every other day schedule, needs depend on the plant.

#importing PiCamera, gpio io, datetime/time, schedule and bme280 file libraries
from picamera import PiCamera
import RPi.GPIO as GPIO
import datetime
import time
import schedule
import board
import digitalio
from adafruit_bme280 import basic as adafruit_bme280


#Initialize SPI bus with default values
#Using:
#Pin#1 (3.3V) -> VIN
#Pin#20 (GND) -> GND
#Pin#23 (GPIO 11) -> SCK
#Pin#21 (GPIO 9) -> SDO
#Pin#19 (GPIO 10) -> SDI
#Pin#29 (GPIO 5) -> CS
spi = board.SPI()
bme_cs = digitalio.DigitalInOut(board.D10)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

#Once all tests are done, uncomment this line to remove unnecessary
#errors for cleaner output.
#**Re-comment when debugging and doing future tests
#GPIO.setwarnings(False)


            ###Functions###
#---------------------------------------#

#Function to be called for the time lapse picture. To be stored in
#/home/pi/Pictures/PiCam/Time-Lapse
def timeLapsePic():
    print('Time Lapse func called..')
    print('Initializing camera..')
    #intializing PiCamera object
    #sets camera resolution, proper orientation, and a brief pause to let camera
    #physically adjust
    camera = PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.resolution = (1920, 1080)
    time.sleep(3)
    
    #takes picture and 
    file_name = "/home/pi/Pictures/PiCam/Time-Lapse/img_" + datetime.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p") + ".jpg"
    print('Taking picture..')
    camera.capture(file_name)
    camera.close()
    print("Done!\nStored in directory: /home/pi/Pictures/PiCam/Time-Lapse")
    print('End Time Lapse func')

def waterPlant():
    print('Water Plant func called..')
    print('Initializing GPIO pins..')
    #GPIO assignments:
    #Relay1 = Pin#37 (GPIO 26),
    #Relay2 = Pin#38 (GPIO 20),
    #Relay3 = Pin#40 (GPIO 21)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37,GPIO.OUT)
    
    #Relay1 dedicated to control the water valve. Time is in seconds,
    #will be adjusted based off how long the plant needs
    print('Opening valve')
    GPIO.output(37, True)
    time.sleep(3)
    print('Closing valve')
    GPIO.output(37, False)
    GPIO.cleanup()
    
def climateCheck():
    #Return index 0 for temperature and index 1 humidity
    return bme280.temperature, bme280.relative_humidity
    
#---------------------------------------#
            ###END Functions###


                ###Main###
#---------------------------------------#

while True:
    




