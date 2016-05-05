#!/usr/bin/env python;((
# -*- coding: utf-8 -*-
"""Additional functionality in debugging errors."""


class CustomError(Exception):
    """Class docstring"""

    def __init__(self, message, cause):
        """Constructor for CustomError

        Args:
           cause (mixed): A varible

        Attributes:
            cause: The reason
        """
        Exception.__init__(self, message, cause)
        self.cause = cause
