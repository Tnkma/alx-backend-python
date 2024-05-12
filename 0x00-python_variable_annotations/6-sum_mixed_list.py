#!/usr/bin/env python3
"""complex mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """takes list of integers and floats and return the sum"""
    return float(sum(mxd_lst))
