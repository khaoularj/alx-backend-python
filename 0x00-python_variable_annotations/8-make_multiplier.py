#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that
multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier"""
    def f_multiplier(x: float) -> float:
        """function that return the product of a float and the multiplier"""
        return x * multiplier
    return f_multiplier
