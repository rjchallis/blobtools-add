#!/usr/bin/env python3
"""Example second module."""


def cube(x):
    """
    Return the cube of number.

    >>> cube(2)
    8
    >>> cube(-2)
    -8
    """
    return x ** 3


if __name__ == '__main__':
    import doctest
    doctest.testmod()
