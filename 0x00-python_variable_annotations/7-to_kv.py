#!/usr/bin/env python3
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of string and a float """
    return (k, v*v)
