#!/usr/bin/env python3
""" The module containing to_kv function """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of string and a float """
    return (k, v*v)
