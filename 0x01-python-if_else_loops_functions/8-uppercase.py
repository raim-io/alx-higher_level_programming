#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase"""

    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
        print("{}".format(upper_char), end="")
    print("")
