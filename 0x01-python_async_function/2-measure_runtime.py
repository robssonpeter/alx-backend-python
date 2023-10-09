#!/usr/bin/env python3
import asyncio
import time
""" Measuring the run time """


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay) -> float:
    """ The function to keep track of the execution time """
    asyncio.run(wait_n(n, max_delay))
    time_taken = time.perf_counter()
    return time_taken/n
