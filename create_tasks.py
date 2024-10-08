import asyncio

from broker import broker
from tasks import best_task_ever


async def main():
    await broker.startup()

    for _ in range(200):
        task = await best_task_ever.kiq()
        print(task)

    # result = await task.wait_result()
    # print(result, type(result))

    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
