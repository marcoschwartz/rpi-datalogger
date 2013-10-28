import serial
import sqlite3
import time

# Connect to DB
conn = sqlite3.connect('logger.db')

# Create table
c = conn.cursor()
c.execute('''CREATE TABLE data(recording_time text, recorded_data text)''')
conn.commit()

# Close DB
conn.close()