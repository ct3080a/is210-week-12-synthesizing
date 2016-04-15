#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


class CustomError(Exception):
    """Exception class."""

    def __init__(self, msg, cause):
        Exception.__init__(self, msg, cause)
        self.cause = cause
