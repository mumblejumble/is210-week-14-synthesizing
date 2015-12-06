#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""

import task_01


def fibo(count):
    """This function returns Fibonacci numbers as a list.

    Args:
        count(int): the number of Fibonacci numbers to be returned.

    Returns:
        a list of number of in Fibonacci style.

    Example:
        >>> fibo(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    return [item for item in task_01.xfibo(count)]
