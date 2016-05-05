#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


class BaseError(Exception):
    """Class exception"""
    pass


class StringError(BaseError, TypeError):
    """Subclassed to BaseError and TypeError"""
    pass


class NumberError(StringError):
    """Subclassed to StringError"""
    pass


class NonZeroError(NumberError):
    """Subclassed to NumberError"""
    pass
