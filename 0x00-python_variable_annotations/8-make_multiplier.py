#!/usr/bin/env python3
""" Complex types Functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ creates a function that can be called"""
    def func(num: float) -> float:
        """this inner function multiples  num and multiplier"""
        return num * multiplier
    return func
