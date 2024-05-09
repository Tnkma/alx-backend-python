#!/usr/bin/env python3
""" Run time for four parallel comprehension"""
import asyncio
import time
from typing import List

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """ runs async_comp * 4 and measures the total time"""
    start_time = time.perf_counter()
    tasks = [async_comp() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
