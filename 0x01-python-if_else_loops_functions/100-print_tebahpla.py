#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        case = 0
    else:
        case = 32
    print("{}".format(chr(i - case)), end="")
