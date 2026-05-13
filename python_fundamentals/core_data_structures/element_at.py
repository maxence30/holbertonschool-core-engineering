#!/usr/bin/env python3
"""Module defines a safe list element access function."""


def element_at(my_list, idx):
    """Return element at index idx if valid, else None."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
