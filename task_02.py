#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 02"""


class CustomError(Exception):
    """CustomError class that is subclasses to Exception"""

    def __init__(self, myerr, cause):
        """Docstring for CustomError constructor.

        Args:
            myerr (str): Error string that a user receives.
            cause (str): Reason of error that user encountered.

        Attribute:
            cause (str): Reason of error that user encountered.

        Examples:

            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up!

        """
        myerr = Exception.__init__(self, myerr)
        self.cause = cause
