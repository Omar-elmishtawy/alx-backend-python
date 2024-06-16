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
    x = asyncio.gather(*list(map(lambda _: wait_random(max_delay), range(n))))

    return x
