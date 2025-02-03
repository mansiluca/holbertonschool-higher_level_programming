#!/usr/bin/python3
"""
Class Fish
"""


class Fish:
    """
    Class Fish
    """

    def swim(self):
        """
        Fish is swimming
        """
        print("Fish is swimming")

    def habitat(self):
        """
        Fish lives in water
        """
        print("Fish lives in water")


class Bird:
    """
    Class Bird
    """

    def fly(self):
        """
        Bird is flying
        """
        print("Bird is flying")

    def habitat(self):
        """
        Bird lives in the sky
        """
        print("Bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class FlyingFish
    """

    def fly(self):
        """
        FlyingFish is soaring
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        FlyingFish is swimming
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        FlyingFish lives both in water and the sky
        """
        print("The flying fish lives both in water and the sky!")
