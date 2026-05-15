#!/usr/bin/env python3
"""
Module dragon

Demonstrates the use of mixins in Python.
"""


class SwimMixin:
    """
    Mixin class that adds swimming behavior.
    """

    def swim(self):
        """
        Print a swimming message.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds flying behavior.
    """

    def fly(self):
        """
        Print a flying message.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon that can
    both swim and fly.
    """

    def roar(self):
        """
        Print a roaring message.
        """
        print("The dragon roars!")