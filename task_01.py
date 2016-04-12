#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Synthesizing task 01 module - Error classes"""


class BaseError(Exception):
    """ Error subclass

    Attributes:
        see Exception superclass.
    """
    pass


class StringError(BaseError, TypeError):
    """ Error subclass

    Attributes:
        see Exception superclass.
    """
    pass


class NumberError(BaseError, TypeError):
    """ Error subclass

    Attributes:
        see Exception superclass.
    """
    pass


class NonZeroError(NumberError):
    """ Error subclass

    Attributes:
        see Exception superclass.
    """
    pass
