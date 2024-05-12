#!/usr/bin/env python3
""" Lets duck type an iterable object"""
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """computes the length"""
    return [(i, len(i)) for i in lst]
