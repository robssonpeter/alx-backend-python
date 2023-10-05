#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum of integers and floats of a mixed list """
    sum = 0
    for item in mxd_lst:
        sum = sum + item
    return sum
