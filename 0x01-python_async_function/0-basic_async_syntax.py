#!/usr/bin/env python3
"""
Module to basic async
""" 


import asyncio, random

async def wait_random(max_delay: int = 10) -> float:
    """
    function to async wait between 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return rand
