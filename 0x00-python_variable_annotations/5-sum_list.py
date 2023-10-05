#!/usr/bin/env python3
""" The module for finding the sum of a list items """
from typing import List



def sum_list(input_list: List[float]) -> float:
    """ returs the sum of the list """
    sum = 0
    for entry in input_list:
        sum = sum + entry
    return sum
