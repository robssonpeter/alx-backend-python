#!/usr/bin/env python3
import asyncio
import time
""" Measuring the run time """


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ The function to keep track of the execution time """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.perf_counter()
    time_taken = finish_time - start_time
    return time_taken/n
