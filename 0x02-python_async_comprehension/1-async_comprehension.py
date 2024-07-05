#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio
import random
from typing import List


async def async_comprehension() -> List[float]:
    """
    async_comprehension: coroutine that collects 10 random numbers using an
    async comprehensing over an async generator
    """
    return [i async for i in async_generator()]

async_generator = __import__('0-async_generator').async_generator
