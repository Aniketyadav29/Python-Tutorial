password = "mypassword123" # wrong method .


# Hashing using Hashlib

import hashlib

password = "mypassword123"

# Convert to hash
hashed = hashlib.sha256(password.encode()).hexdigest()

print("Hashed password:", hashed)

# Password verify code :-

def verify_password(input_password, stored_hash):
    return hashlib.sha256(input_password.encode()).hexdigest() == stored_hash


# SQL Injection Attack:-
username = input("Enter username: ")

query = f"SELECT * FROM users WHERE username = '{username}'"





