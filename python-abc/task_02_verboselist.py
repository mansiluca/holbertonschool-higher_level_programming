#!/usr/bin/python3
"""
Class VerboseList
"""


class VerboseList(list):
    """
    Class VerboseList
    """

    def append(self, item):
        """
        append method
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        extend method
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, value):
        """
        remove method
        """
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """
        pop method
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
