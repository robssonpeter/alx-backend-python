#!/usr/bin/env python3
""" Parallel Comprehension Module """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ The measure time function """
    start_time: float = asyncio.get_event_loop().time()
    insts = [
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
    ]
    await asyncio.gather(*insts)
    end_time: float = asyncio.get_event_loop().time()
    return end_time - start_time
