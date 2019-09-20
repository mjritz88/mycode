#!/usr/bin/python3
"""
challenge5     Issue 1.0   09/19/2019  Mike Ritz   Verizon

                USAGE:  challenge5

Gathers information from Star War's API Planets website and posts it to website
"""
import requests
from flask import Flask #, redirect, url_for, render_template

planets = {}
max = 25  # how many planets to retrieve from swapi.co

app = Flask(__name__)

@app.route('/planets')
def print_planets():
    for i in range(1,(max+1)):
        r = requests.get(f'https://swapi.co/api/planets/{i}/?format=json')
    
        data = requests.get(f'https://swapi.co/api/planets/{i}/?format=json').json()

        planets.update({data['name']:data['climate']})

    return(planets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)  # IP 0.0.0.0 will run on system's external IP address
