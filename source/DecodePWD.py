valid_chars = 'abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&'

file = open('password.txt')
contents = file.readlines()

def decode(password, key):
    char_map = {key[i]: valid_chars[i] for i in range(len(key))}
    decoded_password = ''
    for char in password:
        if char in char_map:
            decoded_password += char_map[char]
        else:
            decoded_password += char
    return decoded_password

class Decode:

    def __init__(self, site):
        self.site = site
    
    def __call__(self):
        print(f'Decoding {self.site}\'s password')
        for line in contents:
            if line.split()[0] == self.site:
                decoded_password = decode(line.split()[1], line.split()[2])
        print(f'The decoded password for {self.site} is {decoded_password}')