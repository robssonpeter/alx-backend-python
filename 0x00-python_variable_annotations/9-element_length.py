#!/usr/bin/env python3
""" Finding the element Length by duck typing """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function for duck typing
        Args:
            lst (Iterable)
        Returns:
            dict: dictionary object
    """
    return [(i, len(i)) for i in lst]
