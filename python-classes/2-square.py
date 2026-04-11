#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    def __init__(self,size=0):
        if not isinstance(size,int):
            raise TypeError("integer olsun")
        elif size < 0:
            raise ValueError("teref menfi olmaz")
        else:
            self.__size = size
        
