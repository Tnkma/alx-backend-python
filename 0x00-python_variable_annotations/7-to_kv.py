#!/usr/bin/env python3
""" String and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Taskes a str and int|float and returns a tuple"""
    return (k, float(v**2))
