import random # import random module for randomizing encryption key

valid_chars = 'abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&' # initialize a string of all valid characters
# Shuffler
def shuffle_indices(lst):
    n = len(lst)
    for i in range(n):
        for _ in range(i, n):
            # Generate a random index between i and n-1
            random_index = random.randint(i, n-1)
            # Swap elements at i and random_index
            lst[i], lst[random_index] = lst[random_index], lst[i]
    return lst
# Randomizes the valid_chars string to create an encryption key
def generate_sub_list():
    lst = [*valid_chars]
    lst = shuffle_indices(lst)
    return lst

# Encrypts the input string using the encryption key
def encode_with_sublist(lst, string):
    lst = [*lst]
    char_map = {valid_chars[i]: lst[i] for i in range(len(valid_chars))} # initialize a dictionary matching each character to the key
    encoded_string = ''
    for char in string: # encrypt string
        if char in char_map:
            encoded_string += char_map[char]
        else: # if a character isn't a part of the char_map dictionary, leave it as is
            encoded_string += char
    return encoded_string

# Writes password to local passwrod storage
def save_to_local(append):
    file = open("source\\passwords.txt", "a")
    file.write(f"{append}\n")

# Class for importing in other methods
class Encode:
    def __init__(self, site, password): # identifies the site and password & creates properties for the sublist and encoded string
        self.site = site
        self.password = password
        self.sublist = ""
        self.encoded = ""
    def __call__(self): # generate encryption key, then encrypt & write to passwords.txt
        self.sublist = "".join(generate_sub_list())
        self.encoded = encode_with_sublist(self.sublist, self.password)
        save_to_local(f"{self.site} {self.encoded} {self.sublist}")
    def __str__(self): # return the following when requested as a string
        return f"The hashed password for {self.site} is {self.encoded}"