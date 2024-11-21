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

partial_key = '6c7578696f5f756e6c6f636b735f34'
iv = 16 * '\x00'

# Currently does nothing but return same values
# not using hash values for cipher
def processing(key,iv):
    #key = hashlib.sha256(key.encode('utf-8')).digest()
    #iv = hashlib.sha256(iv.encode('utf-8')).digest()[0:16]
    key = key
    iv = iv
    return key, iv

# Create cipher and decrypt file with it
def decrypt(encrypted_file,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_file = cipher.decrypt(base64.b64decode(encrypted_file))
    return decrypted_file

# Write decrypted file to a new file named RunMe.exe
def testFile(decrypted_file):
    with open('RunMe.exe', 'wb') as f:
        f.write(decrypted_file)
    print(magic.from_file('RunMe.exe'))

# Open file and store content in variable
file = open('LOCKED', 'rb')
encrypted_file = file.read()

### Iterate through key possiblities
# if first x is number loop
for i in range(0, 10):
    inter_key = ''.join((partial_key, str(i)))
    #if second x is number
    for j in range(1, 10):
        key = ''.join((inter_key, str(j)))
        test_key, test_iv = processing(key, iv)
        test_file = decrypt(encrypted_file, test_key, test_iv)
        testFile(test_file)
        print(test_key)
        print(test_iv)
    # if second x is letter
    for a in ascii_lowercase:
        if a=='g':
            break
        key = ''.join((inter_key, a))
        test_key, test_iv = processing(key, iv)
        test_file = decrypt(encrypted_file, test_key, test_iv)
        testFile(test_file)
        print(test_key)
        print(test_iv)
# if first x is a letter loop
for b in ascii_lowercase:
    if b=='g':
        break
    inter_key = ''.join((partial_key, b))
    #if second x is number
    for k in range(0, 10):
        key = ''.join((inter_key, str(k)))
        test_key, test_iv = processing(key, iv)
        test_file = decrypt(encrypted_file, test_key, test_iv)
        testFile(test_file)
        print(test_key)
        print(test_iv)
    #if second x is letter
    for c in ascii_lowercase:
        if c=='g':
            break
        key = ''.join((inter_key, c))
        test_key, test_iv = processing(key, iv)
        test_file = decrypt(encrypted_file, test_key, test_iv)
        testFile(test_file)
        print(test_key)
        print(test_iv)

print("Finished")
              