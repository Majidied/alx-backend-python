#!/usr/bin/env python3
"""
This module contains the function sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of mixed floats and integers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed floats and
        integers to sum.

    Returns:
        float: The sum of the list of mixed floats and integers.
    """
    return sum(mxd_lst)
