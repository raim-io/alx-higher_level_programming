#!/usr/bin/python3

for col in matrix:
    for row in col:
        print("{:d}".format(col), end=" " if row != col[-1] else "")
    print()
