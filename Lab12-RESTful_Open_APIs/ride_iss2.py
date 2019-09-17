#!/usr/bin/python3
"""
ride_iss2     Issue 1.0   09/16/2019  Mike Ritz   Verizon

                USAGE:  ride_iss2

Gathers information from NASA's website and prints the astronauts
and what spacecraft they are currently on
"""

### Uses requests library to get the json from a URL instead of importing json and urllib
### and having to decode it, resulting in less lines of code

import requests

## Trace the ISS
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    r = requests.get(MAJORTOM)
    
    helmetson = r.json()
    
    ## display our Pythonic data
    #print("\n\nconverted Python data:")
    #print(helmetson)
    #print()
    
    print(f"The following data was obtained from NASA's website:\n\t{MAJORTOM}\n")
    print(f"There are currently {helmetson['number']} astronauts in space: ")

    for people in helmetson['people']:
        #print(people)
        print(f"\t{people['name']} is on the {people['craft']}")
    
    ## end of main()


##### BEGINNING OF MAIN PROGRAM #####

main()
