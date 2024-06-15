#!/usr/bin/env python3
"""
This module contains the function to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and a float.

    Args:
        k (str): The string to return.
        v (Union[int, float]): The float to return.

    Returns:
        Tuple[str, float]: The tuple of the string and the float.
    """
    return (k, v * v)
