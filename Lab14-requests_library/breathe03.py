#!/usr/bin/python3
"""
breathe03   Issue 1.0   Mike Ritz   09/17/2019  Verizon

USAGE:  breathe03

Gathers data from the US Air Quality website
"""

# imports always go at the top of your code
import requests

#ZIP = '23111'
#DATE = '2019-09-16'
ZIP='17042'   #from lab workbook
DATE='2019-01-21'   #from lab workbook
LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=' + ZIP + '&date=' + DATE + '&distance=25&API_KEY=B26E70B2-4246-4475-BFFC-57B8CB9D4C31'

def main():
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the methods available to our new object
    #print( dir(r) )
    #print(r.json())

    print("Weather Forecast")
    print("----------------")

    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("Discussion"))


main()
