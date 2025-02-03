#!/usr/bin/python3
"""
Module that defines a class MyList that
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Method that prints the list, but sorted
        """
        print(sorted(self))
