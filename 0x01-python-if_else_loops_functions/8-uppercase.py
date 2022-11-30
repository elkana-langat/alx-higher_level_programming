#!/usr/bin/python3

def uppercase(str):
    for e in str:
        tmp = ord(e)
        if tmp >= 97 and tmp <= 122:
            fn = chr(tmp - 32)
        else:
            fn = e
        print("{}".format(fn), end="")
    print()
