#!/usr/bin/env python3

# From the book Programmation efficace (ISBN 9782340-010055)
# tryalgo.org
#
# 14.1 Greatest common divisor between two or more integers
#
# implementor : Pierre Faivre
# date : 2016-09-09
#
# complexity :

import sys


def gcd(a, b):
    """Returns the GCD of two numbers"""
    return a if b == 0 else gcd(b, a % b)


def gcd_list_recursive(integers):
    """Returns the GCD of an an arbitrary amount of numbers (recursive method)
       /!\ Bad way to do it: huge amount of memory used for the stack
    """
    if len(integers) >= 2:
        # Combine the two first into their GCD
        new_list = [gcd(integers[0], integers[1])] + integers[2:]
        return gcd_list_recursive(new_list)
    else:
        # Until there is only one left
        return integers[0]


def gcd_list(integers):
    """Returns the GCD of an an arbitrary amount of numbers (loop method)"""
    while len(integers) > 1:
        # Combine the two first into their GCD
        integers[0] = gcd(integers.pop(0), integers[0])

    # Until there is only one left
    return integers[0]


if __name__ == "__main__":
    integers = list(map(int, sys.stdin.readline().rstrip('\n').split(" ")))

    print(gcd_list(integers))
