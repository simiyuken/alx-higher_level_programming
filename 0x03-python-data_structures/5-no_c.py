#!/usr/bin/env python3
def no_c(my_string):
    new_string = " "

    for x in my_string:
        if x != 'C' and x != 'c':
            new_string += x
    return new_string
