import sqlite3

# Connect to a database
conn = sqlite3.connect('example.db')

# Create a cursor
cursor = conn.cursor()

# Insert data into the database
cursor.execute("INSERT INTO users (name, email) VALUES (?,?)", ("John Doe", "john.doe@example.com"))

# Commit changes
conn.commit()

# Close the connection
conn.close()


