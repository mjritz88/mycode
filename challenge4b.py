#!/usr/bin/python3
"""
challenge4b     Issue 1.0   09/18/2019  Mike Ritz   Verizon

         USAGE:  challenge4b [ -h | --help ]
                 challenge4b [ -p PersonID ] [ -a Attribute ]

Gathers information from Star War's API website

PersonID's range from 1-16, currently.

Possible attributes: name, height, mass, hair_color(default), skin_color, eye_color,
    birth_year, gender, homeworld, films, species, vehicles, starships, and url
"""

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Description: Retrieve attributes of Star Wars characters from swapi.co')
    parser.add_argument('-a', '--attribute', metavar='Attribute', default='hair_color', help='attribute of the Star Wars character')
    parser.add_argument('-p', '--person', metavar='PersonID', default='1', help='Star Wars character ID')

    args = parser.parse_args()

    #print(args)

    ## Call the webservice

    r = requests.get(f'https://swapi.co/api/people/{args.person}/?format=json')

    data = r.json()

    #print(data)

    name = data['name']
    attrib = data[args.attribute]

    print(f"{args.person}. {name}'s attribute for {args.attribute} is {attrib}.")
    
    ## end of main()


##### BEGINNING OF MAIN PROGRAM #####

main()
