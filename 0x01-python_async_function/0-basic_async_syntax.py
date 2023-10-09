#!/usr/bin/env python3
""" Async Coroutine for random delay """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ The function that wait for a random period of time """

    number = random.randint(0, max_delay)
    await asyncio.sleep(number)
    return number + random.random()
