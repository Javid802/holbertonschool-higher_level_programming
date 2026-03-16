#!/usr/bin/python3
def isupper(c):
    if len(c) != 1:
        raise ValueError("Input must be a single character")
    if 'A' <= c <= 'Z':
        return True
    elif 'a' <= c <= 'z':
        return None
    else:
        return None
