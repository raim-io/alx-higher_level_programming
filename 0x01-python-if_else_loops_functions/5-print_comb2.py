#!/usr/bin/python3
"""prints numbers 0 - 99"""

for number in range(100):
    if number == 99:
        print("{number}")
    else:
        print("{number:02}, ", end="")
