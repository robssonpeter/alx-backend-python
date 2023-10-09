#!/usr/bin/env python3
""" Function to call the rando function """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ The function to create a task """
    task = asyncio.create_task(wait_random(max_delay))
    return task
