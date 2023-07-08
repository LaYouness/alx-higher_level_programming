#!/usr/bin/python3
"""
adding two integers
"""


def add_integer(a, b=98):
    """Take the args to add.

    a: One of the num, default not def.
    b: The other num, default 98.

    Return: int(a + b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
