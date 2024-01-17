#!/usr/bin/python3
"""prints numbers from 0 to 99"""

for i in range(9):
    for j in range(i + 1, 10):
        if i != 8:
            print("{:02d}, ".format(i * 10 + j), end="")
        else:
            print("{:02d}".format(i * 10 + j))
