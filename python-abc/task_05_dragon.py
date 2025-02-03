#!/usr/bin/python3
"""
Class Base
"""


class SwimMixin:
    """
    Class SwimMixin
    """

    def swim(self):
        """
        The creature swims
        """
        print('The creature swims!')


class FlyMixin:
    """
    Class FlyMixin
    """

    def fly(self):
        """
        The creature flies
        """
        print('The creature flies!')


class Dragon(SwimMixin, FlyMixin):
    """
    Class Dragon
    """

    def roar(self):
        """
        The dragon roars
        """
        print('The dragon roars!')
