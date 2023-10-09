#!/usr/bin/env python3
""" Concurent Running of Multiple coroutines """
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """ Run n numbers of coroutines of the random function """

    list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list: List = await asyncio.gather(*list)

    return list
