#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """A simple docstring.

    Args:
        arg1 (mixed): An argument.
        arg2 (mixed): Another argument.
        arg3 (mixed): Yet another argument.

    Returns:
        mixed: What's caught.

    Examples:
        >>> exception_test(2, [1 ,3], 7)
        True
        >>> exception_test(2, wallet, 7)

        Traceback (most recent call last):
          File "<pyshell#3>", line 1, in <module>
        exception_test(2, wallet, 7)
        NameError: name 'wallet' is not defined
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, LookupError):
        caught = True

    return caught
