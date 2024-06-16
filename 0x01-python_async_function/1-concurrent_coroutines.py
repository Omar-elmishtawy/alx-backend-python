#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutinese at the same time
    """
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    ls = await asyncio.gather(*task)

    return ls
