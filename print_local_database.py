import sqlite3

# Connect to DB
conn = sqlite3.connect('logger.db')

# Get cursor
c = conn.cursor()

# Print DB
for row in c.execute('SELECT * FROM data'):
	print row

# Close DB
conn.close()