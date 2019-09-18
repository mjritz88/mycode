import re

text = 'So do all who live to see such times.  But that is not for them to decide.  All we have to decide is what to do with the time that is given to us.'
pattern = r' [A-Za-z][A-Za-z] '     # need the 'r' to indicate raw input

m = re.search(pattern, text)    # only gets the first occurrence of regex match

print(m)

found = re.findall(pattern, text)   # gets all matches of regex

print(found)

pattern = input("Input your regex: ")   # keyboard input is already raw so no "r" needed

found = re.findall(pattern, text)   # gets all matches of regex

print(found)
