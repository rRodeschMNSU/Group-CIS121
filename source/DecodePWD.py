valid_chars = 'abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&'

# Substitution cipher reversal
def decode(password, key):
    # Maps each char in reverse to that of the inital cipher
    char_map = {key[i-1]: valid_chars[i-1] for i in range(len(key))}
    decoded_password = ''
    # Check each char
    for char in password:
        if char in char_map:
            decoded_password += char_map[char]
        else:
            decoded_password += char # If the character is not in the permitted set, append it wihtout changes.
    return decoded_password

class Decode:

    def __init__(self, site):
        self.site = site
    
    def __call__(self):
        # Open local storage
        file = open('source\\passwords.txt')
        contents = file.readlines()
        print(f'Decoding {self.site}\'s password')
        decoded_password = ''
        # Check each site in passwords.txt for a match
        for line in contents:
            if line.split(" ")[0] == self.site:
                # Split the password and cipher key into their respective variables
                decoded_password = decode(line.split(" ")[1], line.split(" ")[2])
        print(f'The decoded password for {self.site} is {decoded_password}')