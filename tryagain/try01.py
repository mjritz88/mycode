#!/usr/bin/python3

# Start with an infinite loop
while True:
    try:
        print('Enter a file name: ')
        name = input()
        myfile = open(name, 'w')
    except:
        print('Error with that file name! Try again...')
        continue

    myfile.close()
    break
