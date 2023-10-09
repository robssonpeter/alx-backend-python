#!/usr/bin/env python3
""" Concurent Running of Multiple coroutines """
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """ Run n numbers of coroutines of the random function """

    delays = []

    async def get_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [get_delay() for _ in range(n)]
    await asyncio.gather(*tasks)

    return sorted(delays)
