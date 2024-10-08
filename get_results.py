import asyncio

from broker import psqlpy_result_backend


async def main():
    await psqlpy_result_backend.startup()

    result = await psqlpy_result_backend.get_result("b29c4c25b01a43c6abeab84968280f89")

    print(result, type(result))

    await psqlpy_result_backend.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
