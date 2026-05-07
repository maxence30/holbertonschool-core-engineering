#!/usr/bin/python3
def uppercase(str):
    """
    Affiche une chaîne en majuscules suivie d'un saut de ligne.
    """
    result = ""

    for c in str:
        ascii_val = ord(c)

        # Si c'est une lettre minuscule (a-z)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += c

    print(result)