#!/usr/bin/env python3
import asyncio
import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function  that measures the total execution
    time for wait_n(n, max_delay), and returns total_time / n"""
    start_time = time.time()

    async def run_wait_n():
        await wait_n(n, max_delay)

    asyncio.run(run_wait_n())

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
