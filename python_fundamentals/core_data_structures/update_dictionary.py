#!/usr/bin/env python3
"""Module defines a function to update or add a key/value in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Update a dictionary by adding or replacing a key/value pair."""
    a_dictionary[key] = value
    return a_dictionary