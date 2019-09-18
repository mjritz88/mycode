#!/usr/bin/python3

# From Python standard library
import re

with open('networktrace.txt') as trace:
    for line in trace:

        # parse out the contact string using our regex logic
        conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)

        # searches test True if they find a match
        # False if no match
        if conobj:
            print(conobj)

            # display the match
            print(conobj.group())
            print("The phone number is...")
            print(conobj.group(1))
            print("The IPv6 is...")
            print(conobj.group(2))
            print("The port is...")
            print(conobj.group(3))
