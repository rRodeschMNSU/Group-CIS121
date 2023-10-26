import random
valid_chars = 'abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&'
def generate_sub_list():
    lst = [*valid_chars]
    random.shuffle(lst)
    return lst

def encode_with_sublist(lst, string):
    lst = [*lst]
    char_map = {valid_chars[i]: lst[i] for i in range(len(valid_chars))}
    encoded_string = ''
    for char in string:
        if char in char_map:
            encoded_string += char_map[char]
        else:
            encoded_string += char
    return encoded_string

# Writes password to local passwrod storage
def save_to_local(append):
    file = open("passwords.txt", "a")
    file.write(f"{append}\n")

# Class for importing in other methods
class Encode:
    def __init__(self, site, password):
        self.site = site
        self.password = password
        self.sublist = ""
        self.encoded = ""

    def __call__(self):
        self.sublist = "".join(generate_sub_list())
        self.encoded = encode_with_sublist(self.sublist, self.password)
        save_to_local(f"{self.site} {self.encoded} {self.sublist}")
    def __str__(self):
        return f"The hashed password for {self.site} is {self.encoded}"
coded = Encode("youtu.be", "o#211657o")
coded()
print(coded)