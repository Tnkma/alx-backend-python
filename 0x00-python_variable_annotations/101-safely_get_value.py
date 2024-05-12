#!/usr/bin/env python3
""" More type annotation"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Defv = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defv = None) -> Res:
    """gets the key of dict or return default value"""
    if key in dct:
        return dct[key]
    else:
        return default
