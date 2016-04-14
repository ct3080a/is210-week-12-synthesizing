#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CustomError"""


class CustomError(Exception):
    """Class CustomError, Subclass of Exception"""

    def __init__(self, msg, cause):
        """CustomError Constructor.
        Arguments:
            Exception: Self(for its constructor)
            msg(string): Message
            cause(string): Input
        Returns:
            A Custom Error
        Examples:
            >>> myerror = CustomError('Danger Will Robinson',
            cause='Aliens Intruding')
            >>> print myerror.cause
            Aliens Intruding
        """
        msg = Exception.__init__(self, msg)
        self.cause = cause
