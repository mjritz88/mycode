#!/usr/bin/python3

import argparse, socket
from datetime import datetime

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x
    
if __name__ == '__main__':
    choices = { 'client': client, 'server': server }
    parser = argparse.ArgumentParser(description='Description: Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-v', '--verbose', help='turn on debug mode', action='store_true')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')

args = parser.parse_args()

if args.verbose:
    print("Verbose option selected")

function = choices[args.role]

if args.verbose:
    print(f"function='{function}'; args.p='{args.p}'")

print(function(args.p))
