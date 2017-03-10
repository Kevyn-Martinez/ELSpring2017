import os
import time
import sqlite3 as mydbase
import sys

def readTemp():
	temperature = open("/sys/bus/w1/devices/28-031689bff5ff/w1_slave")
	temperature_txt = temperature.read()
	currTime = time.strftime('%x %X %Z')
	temperature.close()
	temperatureinC = float(temperature_txt.split("\n")[1].split("t=")[1])/1000
	temperatureinF = temperatureinC*9.0/5.0+32.0
	return [currTime, temperatureinC, temperatureinF]

con = mydbase.connect('temperature.db')
with con:
        #con.execute('DROP TABLE IF EXISTS 'temperatureTable'')
        con.execute(''' CREATE TABLE temperatureTable
                                (TIME TEXT NOT NULL, CELSIUS FLOAT NOT NULL, FAHR FLOAT NOT NULL);''')
def storeTemp():

			[time,C,F] = readTemp()
			print "Current temperature is: %s F" %F
			cur = con.cursor()
			sql = "insert into temperatureTable values(?,?,?)"
			cur.execute('insert into temperatureTable values(?,?,?)',(time,C,F))
			print "Temperature has been Stored"

def wloop():

	x = 0;
	while(x<20):
		storeTemp()
		time.sleep(30)
		x = x + 1

wloop()
