#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for d in str:
        if ord(d) >= 97 and ord(d) <= 122:
            d = chr(ord(d) - 32)
        print("{}".format(d), end="")
    print("")
