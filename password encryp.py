
# Codigo python que pide password con una mascara lo encripta
import hashlib
import getpass

def hash_password(password):
    # Create a hash object
    sha256 = hashlib.sha256()

    # Hash the password
    sha256.update(password.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

# Example usage

password = getpass.getpass(prompt="Enter your password: ")
hashed_password = hash_password(password)
print("The hashed password is:", hashed_password)
print(password)