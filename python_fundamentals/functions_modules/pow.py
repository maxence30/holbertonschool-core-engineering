#!/usr/bin/python3
def pow(a, b):
    """
    Retourne a élevé à la puissance b.
    """
    result = 1

    for _ in range(b):
        result *= a

    return result