#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 03"""


def exception_test(arg1, arg2, arg3):
    """Catch TypeErrors, KeyErrors, and IndexErrors.

    Args:
        arg1 (mixed): First argument.
        arg2 (mixed): Second argument.
        arg3 (mixed): Second argument.

    Returns:
        caught (bool): Truthy or Falsey value if the error is caught.

    Examples:

        >>>expection_test(['apple'], 0, 'p')
        False

        >>>exception_test(43, 1, 1)
        True
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True

    return caught
