password = "mypassword123" # wrong method .


# Hashing using Hashlib

import hashlib

password = "mypassword123"

# Convert to hash
hashed = hashlib.sha256(password.encode()).hexdigest()

print("Hashed password:", hashed)
