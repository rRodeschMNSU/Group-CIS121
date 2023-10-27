# Import the encode and decoding modules
from EncodePWD import Encode
from DecodePWD import Decode

# Encoding function
def encode_user_in(site: str):
    passcode =  input("Enter desired password to encode: ")
    try:
        encoder = Encode(site, passcode) # Create an Encode object before calling it
        encoder()
    except: # If encoding fails for whatever reason
        "Encoding failed due to an error withn your input, please restart and try again."
        exit()
    print("Password saved successfully.")

# Decoding function
def decode_user_in(site: str):
    decoded = Decode(site) # Create a Decode object before calling it
    decoded()
    pass

while True: # Loop program while it is running
    is_decode = bool(int(input("Encode: 1\nDecode: 2\n"))-1) # Prompt for whether to encode or decode & convert to boolean
    site = input("Enter site URL:")
    if not is_decode:
        encode_user_in(site)
    elif is_decode:
        decode_user_in(site)