#!/usr/bin/env python3
"""
This module contains the function element_length.
"""
from typing import Sequence, Union, Any, List, Tuple


def element_length(lst: Sequence[Union[Any, Any]]) -> List[Tuple[Any, int]]:
    """
    Returns a list of tuples of the elements and their lengths.

    Args:
        lst (Sequence[Union[Any, Any]]): The list of elements to return.

    Returns:
        List[Tuple[Any, int]]: The list of tuples of the elements and their
        lengths.
    """
    return [(i, len(i)) for i in lst]
