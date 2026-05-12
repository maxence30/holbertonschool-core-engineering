#!/usr/bin/env python3
"""Square module."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize square size."""
        self.__size = size

    @property
    def size(self):
        """Get square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print square with #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)