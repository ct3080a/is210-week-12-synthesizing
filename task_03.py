#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Function that test exceptions and return True, false or Error message.

    Args:
        arg1 (mixed): first argument to be checked with exceptions.
        arg2 (mixed): second argument to be checked with exceptions.
        arg3 (mixed): third argument to be checked with exceptions.

    Return:
        True, False or error message.

    Examples:
        >>> exception_test(['apple'], a, 'p')
        Fasle

        >>> exception_test(43, 1, 1)
        True

        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
        NameError: name 'x' is not defined.
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (LookupError, TypeError):
        caught = True

    return caught
