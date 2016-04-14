#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exception Classes"""


class BaseError(Exception):
    """BaseError Class Exception"""
    pass


class StringError(BaseError, TypeError):
    """StringError Class"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError Class"""
    pass


class NonZeroError(NumberError):
    """NonZeroError Class"""
    pass
