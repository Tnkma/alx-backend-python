#!/usr/bin/env python3
""" return a list of wait_times"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ waits for random delay time and returns it in seconds"""
    time_waited = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(time_waited)
