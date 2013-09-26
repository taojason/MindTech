#! /opt/local/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from NeuroPy import NeuroPy
from time import time, sleep

def mindWave(duration):
	mind = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)
	mind.start()
	cur_time = time()
	while time() < cur_time + duration:
		cur.execute("INSERT INTO Waves VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (time(), mind.delta, mind.theta, mind.lowAlpha, mind.highAlpha, mind.lowBeta, mind.highBeta, mind.lowGamma, mind.midGamma, mind.attention, mind.meditation))
		sleep(0.5)

con = None

try:
	con = lite.connect('../data/test.db')

	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')

	data = cur.fetchone()

	print "SQLite version: %s" % data

	cur.execute("CREATE TABLE Waves(Time REAL, Delta INT, Theta INT, Low_Alpha INT, High_Alpha INT, Low_Beta INT, High_Beta INT, Low_Gamma INT, Mid_Gamma INT, Attention INT, Meditation INT)")

	duration = 60
	mindWave(duration)

	con.commit()

except lite.Error, e:
	print "Error %s: "  % e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()










