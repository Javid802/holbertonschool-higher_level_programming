#!/usr/bin/python3
def islower(c):
    if c == '"':
        raise ValueError
    if len(c) != 1:
        return False
    if c >= "a" and c <= "z":
        return True
    else:
        return False