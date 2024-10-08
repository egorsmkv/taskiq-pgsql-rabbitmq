from broker import broker


@broker.task
async def best_task_ever() -> str:
    """Solve all problems in the world."""

    # await asyncio.sleep(5.5)

    print("All problems are solved!")

    return "OK"
