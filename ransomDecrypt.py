#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

path = input("Type the path of the directory to decrypt: ")

files = []

def iterator(directoryPath):
    
    for item in os.listdir(directoryPath):
        
        if item != __file__ and item != 'ransomEncrypt.py' and item != "ransomKey.key":
            
            item = os.path.join(directoryPath, item)
            
            if os.path.isfile(item):
                files.append(item)
                
            elif os.path.isdir(item):
                iterator(item)

try:
    iterator(path)
except:
    print("Upsss, something went wrong! Take a look for the typed path")

pathKey = input("Type the path of the key to decrypt:")

with open(pathKey, 'rb') as key:
    secretKey = key.read()

for file in files:
    with open(file, "rb") as fileToDecrypt:
        contents = fileToDecrypt.read()
    contentsDecrypt = Fernet(secretKey).decrypt(contents)
    
    with open(file, "wb") as fileToDecrypt:
        fileToDecrypt.write(contentsDecrypt)
        
#   NOTE: THIS CODE WAS ORIGINALLY CREATED BY NETWORKCHUCK IN HIS YOUTUBE CHANNEL BUT I'VE MODIFIED IT IN SOME DETAILS AND ADDED NEW FUNCTIONALITIES
