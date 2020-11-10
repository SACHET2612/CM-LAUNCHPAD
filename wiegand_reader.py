import RPi.GPIO as GPIO     #import RPi.GPIO module
from time import sleep      #pin no. as per BOARD, GPIO18 as per BCM
from array import *
import time

D0 = 37
D1 = 36

GPIO.setwarnings(False)     #disable warnings
GPIO.setmode(GPIO.BOARD)    #set pin numbering format

# arr0 = []
# arr1 = []

GPIO.setup(D0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(D1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True :
 arr0 = []
 arr1 = []

 while(GPIO.input(D0) or GPIO.input(D0)):
  pass
 #print(time.perf_counter()) 

 if (not(GPIO.input(D0))):
  for i in range(0,30): 
   temp = GPIO.input(D0)
   arr0.append(temp)
   #sleep(0.001)   #100us sleep
 #elif(not(GPIO.input(D1))): 
  for i in range(0,30):
   temp = GPIO.input(D1)
   arr1.append(temp)
  sleep(0.001)  #100us sleep

 print("D0",arr0)
 print("D1",arr1)
 sleep(0.1)




