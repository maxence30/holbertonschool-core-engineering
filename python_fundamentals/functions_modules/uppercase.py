#!/usr/bin/env python3
def uppercase(str):
    """
    Affiche une chaîne en majuscules suivie d'un saut de ligne.
    """
    result = ""

    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c

    print(result)