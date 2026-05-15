#!/usr/bin/env python3
"""
Module flyingfish

Demonstrates multiple inheritance using Fish, Bird,
and FlyingFish classes.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        """
        Print a swimming message.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        """
        Print a flying message.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish using
    multiple inheritance from Fish and Bird.
    """

    def swim(self):
        """
        Print the swimming behavior of a flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print the flying behavior of a flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print the habitat of a flying fish.
        """
        print("The flying fish lives both in water and the sky!")