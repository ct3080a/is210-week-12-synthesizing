#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: custom exceotion classes"""


class BaseError(Exception):
    """extends exception"""
    pass


class StringError(BaseError, TypeError):
    """StringError subclassed to BaseError and TypeError"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError subclassed to BaseError and ``TypeError"""
    pass


class NonZeroError(NumberError):
    """NonZeroError subclassed to NumberError"""
    pass
