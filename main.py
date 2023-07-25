#template: py main.py <command> <filename> <key>

import sys
import base64
import hashlib

from Cryptodome import Random
from Cryptodome.Cipher import AES 

arg = sys.argv
bs = AES.block_size    #bs -> Block Size

def _pad(data):
    return data + (bs - len(data) % bs) * chr(bs - len(data) % bs)

def _unpad(data):
    return data[:-ord(data[len(data-1):])]

def encrypt(filename, key):   #encrypt given file using the given key.
    try:
        file = open(filename)
        data = file.read()
        file.close()

        print(f"{filename} successfully encrypted!")
    except FileNotFoundError:
        print("Error! File not found!")

def decrypt(filename, key):    #decrypt given file using the given key.
    try:
        file = open(filename)
        data = file.read()
        file.close()

        print(f"{filename} successfully decrypted!")
    except FileNotFoundError:
        print("Error! File not found!")

def decrypt_im(filename, key):
    try:
        file = open(filename)
        data = file.read()
        file.close()

    except FileNotFoundError:
        print("Error! File not found!")

if len(arg) != 4:
    print("Error! Incorrect arguement given!")
else:
    if arg[1] == "-e":
        print("Encrypting...")
        encrypt(arg[2], arg[3])
    elif arg[1] == "-d":
        print("Decrypting...")
        decrypt(arg[2], arg[3])
    elif arg[1] == "-dim":
        print("Decrypting...")
        decrypt_im(arg[2], arg[3])
    else:
        print("Error! Incorrect command in the given arguement!")