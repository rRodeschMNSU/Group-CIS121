import hashlib
import random

# This encodes the password via SHA-256 salting
# https://en.wikipedia.org/wiki/Salt_(cryptography)

def generate_salt(length: int):
    salt = ""
    for PLACEHOLDER in range(length):
        is_num = bool(random.randint(0, 1))
        if is_num:
            salt += str(random.randint(0, 9))
        else:
            salt += str(chr(random.randint(0, 25) + ord("a")))
    return salt

# Writes password to local passwrod storage

def save_to_local(append):
    file = open("passwords.txt", "a")
    file.write(append)

# Generates radon salt
# https://en.wikipedia.org/wiki/Salt_(cryptography)

def hash_it(salt, password):
    hasher = hashlib.sha256()
    hasher.update(salt.encode("utf-8"))
    hasher.update(password.encode("utf-8"))
    return hasher.hexdigest()

# Class for importing in other methods
class Encode:
    def __init__(self, site, password):
        self.site = site
        self.password = password
        self.hashed = ""

    def __call__(self):
        print(f"Encoding {self.site}'s password and saving to local storage")
        salt = generate_salt(5)
        self.hashed = hash_it(salt, self.password)
        formatted_append = f"{self.site} {self.hashed} {salt}\n"
        save_to_local(formatted_append)

    def __str__(self):
        return f"The hashed password for {self.site} is {self.hashed}"
