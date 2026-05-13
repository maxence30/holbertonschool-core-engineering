#!/usr/bin/env python3
"""Square module."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
        