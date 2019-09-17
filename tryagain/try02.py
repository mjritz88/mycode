#!/usr/bin/python3

import sys

# Start with an infinite loop
while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
        print()

    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    # general error handling
    # a practical use might be exceptions we haven't designed solution for yet
    except:
        # sys.exc_info returns a 3 tuple with info abut the exception handled
        print("\nWe did not anticipate that:", sys.exc_info()[0])
        # raise by itself simply calls the previous exception that was thrown
        raise
