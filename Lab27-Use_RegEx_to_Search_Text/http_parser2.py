#!/usr/bin/python3

import urllib.request
import re

url = input("Enter the URL: ")

print("Great!  I will try to open this url " + url + " to search for the phrase.")

searchMe = urllib.request.urlopen(url).read().decode("utf-8")

not_finished = True

while not_finished:
    print()
    searchFor = input("Enter pattern or 'quit': ")

    if searchFor == 'quit':
        not_finished = False
    else:
        matches = re.findall(searchFor, searchMe)
    
        if matches:
            print(f"Found {len(matches)} matches!")
        else:
            print("No matches!")
