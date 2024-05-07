#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ waits for random delay time and returns it in seconds"""
    sleep_time = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
