#import mysql.connector
import sqlite3
import hashlib
import getpass
import os


# Connect to the database
conn = sqlite3.connect('master.db')
#db = mysql.connector.connect(
#    host="localhost",
#    user="username",
#    password="password",
#    database="database_name"
#)

# Create a cursor to execute SQL commands
#cursor = db.cursor()
cursor=conn.cursor()
os.system("cls")

def hash_password(password):
    # Create a hash object
    sha256 = hashlib.sha256()

    # Hash the password
    sha256.update(password.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

# Take user input
print("\t\t\t\t CAPTURA DE DATOS BASICOS DEL COLABORADOR \n")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
address = input("Enter address: ")
phone = input("Enter phone: ")
email = input("Enter email: ")
password = getpass.getpass(prompt="Enter your password: ")
hashed_password = hash_password(password)


# Insert the user data into the database
#sql = "INSERT INTO users_basic_info (first_name, last_name, address, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
sql = "INSERT INTO users_basic_info (first_name, second_name, address, phone, email, password) VALUES(?,?,?,?,?,?)"
val = (first_name, last_name, address, phone, email, hashed_password)
#cursor.execute(sql, val)
cursor.execute(sql,val)

# Commit the changes
#db.commit()
conn.commit()

# Close the cursor and database connection
cursor.close()
#db.close()
conn.close()

print("Data inserted successfully.")
print(password)
print(hashed_password)