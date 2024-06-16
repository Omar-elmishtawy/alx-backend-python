#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

time_Wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutinese at the same time
    """
    task = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]

    ls = await asyncio.gather(*task)

    return ls
