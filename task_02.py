#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: exception class customererror, subclassed exception
calling exception.__init__() but also takes third param named cause
and stores the value as self.cause"""


class CustomError(Exception):
    """custom constructor that calls exception.__init__(), takes
    third param named cause"""
    def __init__(self, msg, cause):
        """constructor, initializer"""
        Exception.__init__(self, msg, cause)
        self.msg = msg
        self.cause = cause
