#!/usr/bin/python3

def main():
    ## create an empty list
    anotheremptylist = []

    ## This will throw an ERROR
    ## the extend method expects exactly one argument

    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    ## display our list
    print(anotheremptylist)

main()
