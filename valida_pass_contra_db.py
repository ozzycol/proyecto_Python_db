
import sqlite3
import hashlib
import getpass
import os

os.system("cls")

def hash_password(password):
    # Create a hash object
    sha256 = hashlib.sha256()

    # Hash the password
    sha256.update(password.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

# Connect to a database
conn = sqlite3.connect('master.db')
# Create a cursor
cursor = conn.cursor()

# Take user input
print("\t\t\t\tValidador de Contraseña\n\n")
user_id = input("Enter ID: ")
password = getpass.getpass(prompt="Enter your password: ")
hashed_password = hash_password(password)


# Execute a query to retrieve data
sql="SELECT * FROM users_basic_info WHERE id = ? AND password = ?"
val= (user_id, hashed_password)
cursor.execute(sql,val)

# Fetch the results
results = cursor.fetchall()

# Loop through the results and print them #Lo comento porque no quiero imprimir la consulta solo me interesa validar pass e id
# este sirve para traer resultados de una consulta en pantalla
#for result in results:
 #   print(result)

# Commit changes
conn.commit()

# Close the connection
conn.close()

# Check if any records were found
if len(results) > 0:
    print("Login successful.")
else:
    print("Login failed. Incorrect ID or password.")