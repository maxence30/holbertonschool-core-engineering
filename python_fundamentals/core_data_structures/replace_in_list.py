#!/usr/bin/env python3
"""Module defines a function to replace an element in a list."""


def replace_in_list(my_list, idx, element):
    """Replace element at index idx if valid, else return original list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list