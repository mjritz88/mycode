#!/usr/bin/python3
"""
breathe01   Issue 1.0   Mike Ritz   09/17/2019  Verizon

USAGE:  breathe01

Gathers data from the US Air Quality website
"""

# imports always go at the top of your code
import requests

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-01-21&distance=25&API_KEY=B26E70B2-4246-4475-BFFC-57B8CB9D4C31'

def main():
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the methods available to our new object
    print( dir(r) )
    print(r.json())


main()
