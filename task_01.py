#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for task 01"""


class BaseError(Exception):
    """BaseError exception class that extends Exception."""
    pass


class StringError(BaseError, TypeError):
    """StringError class subclassed to BaseError and TypeError."""
    pass


class NumberError(BaseError, TypeError):
    """NumberError class subclassed to BaseError and TypeError."""
    pass


class NonZeroError(NumberError):
    """NonZeroError class subclassed to NumberError class."""
    pass
