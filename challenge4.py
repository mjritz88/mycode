#!/usr/bin/python3
"""
challenge4     Issue 1.0   09/18/2019  Mike Ritz   Verizon

                USAGE:  challenge4

Gathers information from Star War's API website
"""

### Uses requests library to get the json from a URL instead of importing json and urllib
### and having to decode it, resulting in less lines of code

import requests
import argparse

## Trace the ISS
URL='https://swapi.co/api/people/1/?format=json'

def main():
    parser = argparse.ArgumentParser(description='Description: Retrieve attributes of Star Wars characters from swapi.co')
    parser.add_argument('-a', '--attribute', metavar='ATTRIBUTE', default='hair_color', help='attribute of the Star Wars character')
    parser.add_argument('-p', '--person', metavar='PERSON', default='1', help='Star Wars character ID')

    ## Call the webservice

    for i in range(1,17):
        r = requests.get(f'https://swapi.co/api/people/{i}/?format=json')
    
        data = r.json()
    
        name = data['name']
        hair = data['hair_color']

        print(f"{i}. {name}'s hair color is {hair}.")
    
    ## end of main()


##### BEGINNING OF MAIN PROGRAM #####

main()
