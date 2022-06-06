#!/usr/bin/env python3
def no_c(my_string):
    ken = " "

    for x in my_string:
        if x != 'C' and x != 'c':
            ken += x
    return ken
