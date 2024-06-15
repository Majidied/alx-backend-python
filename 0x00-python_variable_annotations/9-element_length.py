#!/usr/bin/env python3
"""
This module contains the function element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples of the elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The list of elements to return.

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples of the elements
        and their lengths.
    """
    return [(i, len(i)) for i in lst]
