#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
import random
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
