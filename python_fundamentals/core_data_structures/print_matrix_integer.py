#!/usr/bin/env python3
"""Module defines a function to print a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers with proper formatting."""
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
        