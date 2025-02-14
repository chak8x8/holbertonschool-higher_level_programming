#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)
        
    def pop(self, index = None):
        if index is None:
            pop_item = super().pop()
        else:
            pop_item = super().pop(index)
        print("Popped [{}] from the list.".format(popped_item))
