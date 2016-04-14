#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Creates a function for testing exceptions.

        Args:
            arg1 (mixed)
            arg2 (mixed)
            arg3 (mixed)

        Returns:
            boolean: True or False whether error was caught.
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, IndexError, KeyError):
        caught = True
    return caught
