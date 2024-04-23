#!/usr/bin/env python3
"""sync coroutine that measures the total runtime
of parallel async_comprehension calls"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """this coroutine should measure the total runtime and return it"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
