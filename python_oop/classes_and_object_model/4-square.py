#!/usr/bin/env python3
"""Square module."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        self.__size = size

    # Getter
    def get_size(self):
        """Get the size of the square."""
        return self.__size

    # Setter
    def set_size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value