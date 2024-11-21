# CIS 6323
# Cryptanalysis Lab
# Dustin Walters - UHID 1776474
### Program to decrypt LOCKED file ###
#Uses "pycrypto" and "python-magic" packages

import base64
import hashlib
import magic
from Crypto.Cipher import AES
from string import ascii_lowercase

# fill in key found in main.py
key = '6c7578696f5f756e6c6f636b735f34xx'
iv = 16 * '\x00'




file = open('LOCKED', 'rb')
encrypted_file = file.read()
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_file = cipher.decrypt(base64.b64decode(encrypted_file))
print(key)
print(iv)
open('RunMe.exe', 'wb').write(decrypted_file)
print(magic.from_file('RunMe.exe'))  
print("Finished")