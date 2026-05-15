#!/usr/bin/env python3
"""
Module animals

Defines an abstract Animal class and concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.
    """

    def sound(self):
        """
        Return the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.
    """

    def sound(self):
        """
        Return the sound made by the cat.
        """
        return "Meow"
    