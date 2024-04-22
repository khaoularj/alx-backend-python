#!/usr/bin/env python3
import asyncio
import importlib
module = importlib.import_module('0-basic_async_syntax')
wait_random = module.wait_random


async def wait_n(n, max_delay):
    """async routine that takes in 2 int arguments
    (in this order): n and max_delay"""
    tasks = []
    results = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in tasks:
        result = await task
        results.append(result)
    return results
