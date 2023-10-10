#!/usr/bin/env python3
""" Async generator import module """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int, float]:
    """ The function for async comprehension """
    lst = [i async for i in async_generator()]
    return lst