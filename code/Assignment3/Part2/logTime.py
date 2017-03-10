import os
import time
import sqlite3 as mydbase
import sys

def logTime():
	xTime = time.strftime('%Y-%m-%d')
	xDate = time.strftime('%H-%M-%S')
	return [xDate, xTime]

def log():
        con = mydbase.connect('testTime.db')
        print "Success"

        with con:
                try:
                      
                        con.execute('''CREATE TABLE testTime
                                (TIME TEXT NOT NULL, DATE TEXT NOT NULL);''')
                        cur = con.cursor()
                        listh = logTime()
                        cur.execute('INSERT INTO testTime VALUES(?,?)', listh)
                        print "Time has been logged"
                        con.commit()

                except:
                        print "Failed"


log()
