#!/usr/bin/env python3
""" Concurent Running of Multiple coroutines """
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Run n numbers of coroutines of the random function """

    if (max_delay == 0):
        return [0.0 for _ in range(n)]
    list: List = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]
    lst: List = await asyncio.gather(*list)

    return sorted(lst)
