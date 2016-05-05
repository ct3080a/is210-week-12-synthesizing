#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Synthesizing task 02 module - Error classes"""


class CustomError(Exception):
    """ Error subclass

    Attributes:
        see Exception superclass.
    """

    def __init__(self, message=None, cause=None):
        """ Constructor for Error subclass

        Args:
            message (string): Error meesage string.
            cause (string): Error cause description string.

        Attributes:
            see Exception superclass.
            cause (string): Error cause description string.
        """
        super(CustomError, self).__init__(message)
        self.cause = cause
