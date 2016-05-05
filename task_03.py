#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """ Sample function for testing error handling.

    Args:
        arg1 (indexable list):
        arg2 (indexable sublist):
        arg3 (index):
    Returns:
        boolean: whether error was raised (True) or not (False)
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True

    return caught
