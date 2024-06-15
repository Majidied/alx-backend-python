#!/usr/bin/env python3
"""
This module contains the function zoom_array.
"""
from typing import Tuple, List


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given list by repeating each item a certain number
    of times.

    Args:
        lst (Tuple): The input list to zoom in on.
        factor (int, optional): The number of times to repeat each item.
        Defaults to 2.

    Returns:
        List: The zoomed-in list with repeated items.

    """
    zoomed_in: List[Tuple] = [(item, i) for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
