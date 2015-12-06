#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""


def xfibo(count):
    """This function generates numbers in Fibonacci sequence.

    Args:
        count(int): number of integers would be returned in order.

    Returns:
        a list of nubers in sequence.

    Example:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    counter = 0
    old_num = 0
    new_num = 1
    while counter < count:
        yield old_num
        counter += 1
        old_num, new_num = new_num, new_num + old_num
