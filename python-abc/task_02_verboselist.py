#!/usr/bin/python3
"""
Define VerboseList, a class that extends Python's built-in list with extra
notifications whenever items are added or removed.
"""

class VerboseList(list):
    """
    Extends Python's built-in list to print notification messages
    whenever certain operations modify the list:
      - append
      - extend
      - remove
      - pop
    """

    def append(self, item):
        """
        Append an item to the end of the list, then print a message
        indicating which item was added.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extend the list by appending elements from the given iterable,
        then print how many items were added.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """
        Remove the first occurrence of the specified item from the list,
        printing a message before removal.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """
        Remove and return the item at the specified index (defaulting to
        the last item if no index is provided), then print a message
        indicating which item was popped.
        """
        if index is None:
            popped_item = super().pop()
        else:
            popped_item = super().pop(index)
        print("Popped [{}] from the list.".format(popped_item))
        return popped_item
