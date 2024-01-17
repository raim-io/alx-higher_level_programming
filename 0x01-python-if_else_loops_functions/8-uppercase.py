#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase"""

    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
