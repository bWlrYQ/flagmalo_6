#!/usr/bin/python
# Author: Matthieu

from sys import argv
from time import time
from base64 import b64encode
from string import printable

def main():
    try:
        if(argv[1] == "-c" or argv[1] == "--cleartext"):
            try:
                hash_result = []
                salt = int(time())
                cleartext = argv[2]
                for char in cleartext:
                    if(char in printable):
                        continue
                    else:
                        print["[!] Cleartext should only contain printable characters"]
                        return
                for char in cleartext:
                    cipherChar = ord(char)
                    cipherChar = cipherChar * pow(cipherChar,2) + (salt-cipherChar)
                    hash_result.append(cipherChar)
                hash_str=""
                for i in range(len(hash_result)):
                    if(i == len(hash_result)-1):
                        hash_str += str(hash_result[i])
                    else:
                        hash_str += str(hash_result[i])+","
                cipher = b64encode(hash_str.encode('utf-8'))
                print(f"[>] Salt: {salt}")
                print(f"[>] Hash: {cipher}")
            except:
                print("[!] Please specify a cleartext to hash")
        else:
            print("[!] Unrecognized argument") 
            return
    except:
        print("[!] Please specify text to hash with argument -c or --cleartext")
        return
main()