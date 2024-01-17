#!/usr/bin/python3

def islower(c):
    """checks for lowercase character"""

    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
