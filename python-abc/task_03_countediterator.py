#!/usr/bin/python3
"""Defines a CountedIterator that tracks iteration count."""


class CountedIterator:
    """A custom iterator that 
    counts the number of times __next__ is called."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """Returns the number of items iterated over."""
        return self.__counter

    def __iter__(self):
        """Returns itself as an iterator."""
        return self

    def __next__(self):
        """Fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration
