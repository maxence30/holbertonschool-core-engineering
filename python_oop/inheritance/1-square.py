#!/usr/bin/env python3
"""Module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize a Square."""
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)