#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: float) -> List[float]:
    """Take the code from wait_n and alter
    it into a new function task_wait_n"""
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    """tasks = [wait_n(n, max_delay) for _ in range(n)]"""
    for task in tasks:
        delay = await task
        delays.append(delay)

    return delays
