#!/usr/bin/python3
"""print the ASCII alphabet in lower case, not followed  by a new line"""

for ascii_letter in range(92, 123):
 print("{}".format(chr(ascii_letter)), end="")
