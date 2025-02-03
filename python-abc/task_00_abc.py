#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Class Animal
"""


class Animal(ABC):
    """
    Class Animal
    """
    @abstractmethod
    def sound(self):
        """
        sound method
        """
        pass


class Dog(Animal):
    """
    Class Dog
    """

    def sound(self):
        """
        sound method
        """
        return "Bark"


class Cat(Animal):
    """
    Class Cat
    """

    def sound(self):
        """
        sound method
        """
        return "Meow"
