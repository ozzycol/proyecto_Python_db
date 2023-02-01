import sqlite3


# Connect to a database
conn = sqlite3.connect('master.db')

# Create a cursor
cursor = conn.cursor()

# Execute a query to retrieve data
cursor.execute('SELECT * FROM users_basic_info')

# Fetch the results
results = cursor.fetchall()

# Loop through the results and print them
for result in results:
    print(result)

# Commit changes
conn.commit()

# Close the connection
conn.close()