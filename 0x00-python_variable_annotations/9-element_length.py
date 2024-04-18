#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that return a list of
    tuples containing elements and their lengths"""
    return [(i, len(i)) for i in lst]
