import sqlite3

# Connect to a database (creates the database if it doesn't exist)
conn = sqlite3.connect('master.db')

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_basic_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit changes
conn.commit()

# Close the connection
conn.close()