#!/usr/bin/env python3
"""
This module contains the function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The float to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies a float by a
        multiplier.
    """
    def multiply(n: float) -> float:
        """
        Returns the product of a float and a multiplier.

        Args:
            n (float): The float to multiply.

        Returns:
            float: The product of the float and the multiplier.
        """
        return n * multiplier
    return multiply
