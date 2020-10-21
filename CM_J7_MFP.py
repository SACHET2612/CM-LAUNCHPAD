import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
#from time import sleep # Import the sleep function from the time module
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW ) # Turn off
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)


while True: # Run forever
 GPIO.output(11, GPIO.HIGH)  
 GPIO.output(13, GPIO.HIGH) # Turn on
 GPIO.output(15, GPIO.HIGH)
 GPIO.output(29, GPIO.HIGH)
 GPIO.output(31, GPIO.HIGH)
 time.sleep(1) # Sleep for 1 second
 GPIO.output(13, GPIO.LOW) # Turn off
 GPIO.output(15, GPIO.LOW) # Turn off
 GPIO.output(29, GPIO.LOW) # Turn off
 GPIO.output(11, GPIO.LOW)
 
 time.sleep(1) # Sleep for 1 second