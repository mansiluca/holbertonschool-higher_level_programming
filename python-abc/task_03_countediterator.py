#!/usr/bin/python3

class CountedIterator:
    def __init__(self, data):
        self.data = iter(data)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.data)
            self.count += 1
            return item
        except StopIteration:
            raise
