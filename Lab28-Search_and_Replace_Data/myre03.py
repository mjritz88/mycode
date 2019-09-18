#!/usr/bin/python3

import re

wood = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

print(f"Searching through the following string:\n\n{wood}\n")

search1 = re.findall(r"wo\w+", wood)    # \w indicates any word; this should find all words beginning with "wo"

print("Results of pattern 'wo\w+':")
print(search1)

search2 = re.findall(r"o+", wood)   # find all words containing an "o"

print()
print("Results of pattern 'o+':")
print(search2)

search3 = re.findall(r"carrots", wood)

print()
print("Results of pattern 'carrots':")
print(search3)

hobbit = "In a hole in the ground there lived a hobbit. \
Not a nasty, dirty, wet hole, filled with the ends of \
worms and an oozy smell, nor yet a dry, bare, sandy \
hole with nothing in it to sit down on or to eat: \
it was a hobbit-hole, and that means comfort. It \
had a perfectly round door like a porthole, \
painted green, with a shiny yellow brass knob \
in the exact middle. The door opened on to a \
tube-shaped hall like a tunnel: a very comfortable tunnel \
without smoke, with panelled walls, and floors tiled \
and carpeted, provided with polished chairs..."

search4 = re.findall(r"th\w+", hobbit)

print()
print("Results of pattern 'th\w+' on hobbit string:")
print(search4)

search5 = re.findall(r"th\w+", hobbit, re.IGNORECASE)

print()
print("Results of pattern 'th\w+' on hobbit string with case ignored:")
print(search5)
