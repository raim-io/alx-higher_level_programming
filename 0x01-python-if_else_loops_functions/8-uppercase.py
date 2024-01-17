#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase"""
    
    for char in str:
        if 97 <= ord(c) <= 122:
            char = chr(ord(c)-32)
        print("{}".format(c), end="")
    print("")
