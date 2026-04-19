#!/usr/bin/python3
"""Defines a function that reads a UTF-8 text file and prints it"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
