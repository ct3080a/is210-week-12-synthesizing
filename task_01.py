#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating custom class exceptions"""


class BaseError(Exception):
    """A class exception"""
    pass


class StringError(BaseError, TypeError):
    """A subclass of BaseError"""
    pass


class NumberError(BaseError, TypeError):
    """A subclass of BaseError"""
    pass


class NonZeroError(NumberError):
    """A subclass of BaseError"""
    pass
