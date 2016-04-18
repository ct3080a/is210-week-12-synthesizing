#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


class CustomError(Exception):
    """A subclassed to Exception"""

    def __init__(self, astring, cause):
        """Constructor that calls Exeption.__init__()."""
        Exception.__init__(self)
        self.astring = astring
        self.cause = cause
