#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""


class BaseError(Exception):
    """This is the Parent Class."""


class StringError(BaseError, TypeError):
    """This is the sub class."""


class NumberError(BaseError, TypeError):
    """This is the sub class."""


class NonZeroError(NumberError):
    """Subclass of NumberError."""
