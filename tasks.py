import asyncio
import random

from broker import broker


@broker.task
async def best_task_ever() -> str:
    """Solve all problems in the world."""

    # Sleep with random time to simulate work
    secs = random.randint(1, 5)
    await asyncio.sleep(secs)

    if secs == 2:
        raise ValueError("Failed to solve the problem")

    print("All problems are solved!")

    return "OK"
