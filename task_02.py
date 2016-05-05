#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""


class CustomError(Exception):
    """Creates an custom error class."""

    def __init__(self, message='try again', cause='invalid syntax'):
        """Creates a custom error for the subclass.

        Args:
            message(str): An error message
            cause(str): Cause of the error

        """
        Exception.__init__(self)
        self.message = message
        self.cause = cause
