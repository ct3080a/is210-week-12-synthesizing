#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


class BaseError(Exception):
    """Creates a class for BaseError, subclass of Exception"""


class StringError(BaseError, TypeError):
    """Creates a class for StringError, subclass of BaseError and TypeError"""


class NumberError(BaseError, TypeError):
    """Creates a class for NumberError, subclass of BaseError and TypeError"""


class NonZeroError(NumberError):
    """Creates a class for NonZeroError, subclass of NumberError"""
