#!/usr/bin/python3
"""
Task 3. Count
"""


class CountedIterator:
    """
    CountedIterator class
    """

    def __init__(self, data):
        """
        Initializes a new CountedIterator instance.
        """
        self.data = iter(data)
        self.count = 0

    def get_count(self):
        """
        Returns the number of items iterated.
        """
        return self.count

    def __next__(self):
        """
        Returns the next item in the iteration.
        """
        try:
            item = next(self.data)
            self.count += 1
            return item
        except StopIteration:
            raise
