import serial
import sqlite3
import time
import datetime
import MySQLdb
import parameters
import sys

# Configure serial port
try:
	#ser = serial.Serial(parameters.serial_port, parameters.serial_speed, parameters.timeout)
	debug = True
except:
	print "Serial port not available"
	sys.exit()

while(True):

	# Get data from RS232 (your own serial operation)
	try:
		# data = ser.read()
		# ser.write()
		# ...
		recorded_data = "the_data"
		data_recorded = True
	except:
		data_recorded = False
		print "Serial device not available, retrying later"

	if (data_recorded == True):

		# Connect to local DB
		conn = sqlite3.connect('logger.db')

		# Get cursor
		c = conn.cursor()

		# Get time
		recording_time = str(datetime.datetime.now());

		# Store in local DB
		c.execute("insert into data (recording_time, recorded_data) values (?, ?)",
	            (recording_time, recorded_data))
		conn.commit()
		print "Data saved in local database"

		# Close local DB
		conn.close()

		# Save information into remote DB
		try:
			# Connect to distant DB
			myDB = MySQLdb.connect(parameters.host,parameters.port,parameters.user,parameters.passwd,parameters.db)
			
			# Get cursor
			c = conn.cursor()

			# Store in remote DB
			c.execute("insert into data (recording_time, recorded_data) values (?, ?)",
		            (recording_time, recorded_data))
			conn.commit()
			print "Data saved in remote database"

			# Close remote DB
			conn.close()

		except:
			print "Remote database not available"

	# Delay (in seconds)
	time.sleep(parameters.delay)