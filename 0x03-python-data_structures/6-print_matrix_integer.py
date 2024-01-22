#!/usr/bin/python3

for col in matrix:
    for row in col:
        print("{:d}".format(row), end=" " if row != col[-1] else "")
    print()
