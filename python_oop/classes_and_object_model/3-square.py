#!/usr/bin/env python3
"""Square module."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
    