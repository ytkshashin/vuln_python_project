import hashlib

def store_password(password):
    # Vulnerable: MD5 is considered a weak hashing algorithm
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"Stored password hash: {hashed_password}")

if __name__ == "__main__":
    # Hardcoded credentials
    password = "supersecretpassword"
    store_password(password)
