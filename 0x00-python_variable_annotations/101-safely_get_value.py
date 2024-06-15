#!/usr/bin/env python3
"""
This module contains the function safely_get_value.
"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value of a key in a dictionary if it exists, otherwise the
    default value.

    Args:
        dct (Mapping): The dictionary to search.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None]): The default value to return if the key does
        not exist in the dictionary.

    Returns:
        Union[Any, T]: The value of the key in the dictionary if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
