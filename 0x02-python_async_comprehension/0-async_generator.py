#!/usr/bin/env python3
""" The module for random number returning """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ The function async generator """

    for i in range(10):
        await asyncio.sleep(1)

        yield random.randint(0, 10)
