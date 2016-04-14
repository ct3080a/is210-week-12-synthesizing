#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """function docstring.
    Args:
        arg1(bool), arg2(bool), arg3(bool)
    Returns:
        Returns other exceptions
    Examples:
        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
          File "<pyshell#0>", line 1, in <module>
            exception_test(['apple'], 0, x)
        NameError: name 'x' is not defined
        >>> exception_test(44, 2, 2)
        True
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (LookupError, TypeError, IndexError):
        caught = True
    return caught
