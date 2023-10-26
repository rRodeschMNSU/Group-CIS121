file = open('password.txt')
contents = file.readlines()

class Decode:

    def __init__(self, site):
        self.site = site
    
    def __call__(self):
        print(f'Decoding {self.site}\'s password')
        for line in contents:
            if contents.split()[0] == line:
                print()