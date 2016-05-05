#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


class CustomError(Exception):
    """Creates a custom error class, a sublcass of Exception."""

    def __init__(self, errormsg, cause):
        """Creates a constructor for the CustomError class

            Args:
                errormsg (str) = Error message to the user.
                cause (str) = Cause of the error

        """
        Exception.__init__(self, errormsg)
        self.cause = cause
