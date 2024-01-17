#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase"""

    for char in str:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print("")
