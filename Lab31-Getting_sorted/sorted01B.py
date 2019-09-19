#!/usr/bin/python3

data = []

myfile = open('LIST', 'r')
data = myfile.readlines()
myfile.close()

#print(data)
#print(data[0].rstrip('\n'))
#print(len(data[0]))
#print(data[0][0-10])

#print(sorted(data))

for item in data:
    print(item.rstrip('\n'))

print("======================================")

for item in sorted(data):
    print(item.rstrip('\n'))
