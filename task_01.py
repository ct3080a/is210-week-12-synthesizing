#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


class BaseError(Exception):
    """BaseError Class."""
    pass


class StringError(BaseError, TypeError):
    """BaseError & typeError Subclass."""
    pass


class NumberError(BaseError, TypeError):
    """BaseError` & ``TypeError Subclass."""
    pass


class NonZeroError(NumberError):
    """NumberError Subclass."""
    pass
