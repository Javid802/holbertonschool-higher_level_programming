#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if i.islower():
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()
