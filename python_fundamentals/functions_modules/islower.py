#!/usr/bin/python3
def islower(c):
    """
    Retourne True si c est une lettre minuscule, False sinon.
    """
    if len(c) != 1:
        return False

    return ord('a') <= ord(c) <= ord('z')