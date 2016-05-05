#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Function docstring.

    Args:
        arg1 (mixed): values for argument 1
        arg2 (mixed): values for argument 2
        arg3 (mixed): values for argument 3

    Return:
        caught (bool): Tests boolean value of arguments.

    Examples:

        >>> exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
        >>> exception_test(['apple'], 0, x)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'x' is not defined
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True
    else:
        caught = False
    return caught
