# learning to use try and except

def add_stuff():
        try:
            i = input('What number do you want to add to 100? ')
            x = 100 + float(i)
            print(x)

        except ValueError:
            print(f"'{i}' is not a valid real number")

        except KeyboardInterrupt:   # Signal 2, typically CTRL-C
            print("\nInterrupt key detected -- Exiting")

add_stuff()
