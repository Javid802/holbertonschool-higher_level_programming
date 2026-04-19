#!/usr/bin/python3
"""Defines a MyList class that inherits from list"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
