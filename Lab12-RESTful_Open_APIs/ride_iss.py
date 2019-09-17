#!/usr/bin/python3
"""
ride_iss     Issue 1.0   09/16/2019  Mike Ritz   Verizon

                USAGE:  ride_iss

Gathers information from NASA's website and prints the astronauts
and what spacecraft they are currently on
"""

import urllib.request
import json

## Trace the ISS
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    
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
