#!/usr/bin/python3
def no_c(my_string):

    # Create a translation table to remove 'c' and 'C'
    translation_table = {ord('c'): None, ord('C'): None}

    # Use translate() with the translation table
    my_string = my_string.translate(translation_table)
    return my_string
