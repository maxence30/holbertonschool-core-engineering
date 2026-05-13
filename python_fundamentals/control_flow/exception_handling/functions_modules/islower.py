#!/usr/bin/env python3
def islower(c):
    """
    Vérifie si un caractère est une lettre minuscule.
    Retourne True si c est entre 'a' et 'z', sinon False.
    """
    return ord('a') <= ord(c) <= ord('z')
