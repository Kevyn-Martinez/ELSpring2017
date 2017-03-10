import os
import time
import sqlite3 as mydbase
import sys

def readTime():
	xDate = time.strftime('%Y-%m-%d')
	xTime = time.strftime('%H-%M-%S')
	return [xdate, xtime]
	
