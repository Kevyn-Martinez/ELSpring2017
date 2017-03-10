#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def Blink():
	for i in range(0,3):
		print "blink #" + str(i+1)
		GPIO.output(17,True)
		time.sleep(0.1)
		GPIO.output(17,False)
		time.sleep(0.1)
	time.sleep(5)
	for j in range(0,4):
		print "blink #" + str(j+1)
		GPIO.output(17,True)
		time.sleep(0.1)
		GPIO.output(17,False)
		time.sleep(0.1)
	print "Done!!"

Blink()
time.sleep(5)
Blink()
