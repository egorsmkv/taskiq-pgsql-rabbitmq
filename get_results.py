import asyncio

from broker import db_rb


async def main():
    await db_rb.startup()

    result = await db_rb.get_result("0a1a587677d8487a86c958439f8996f2")

    print(result, type(result))

    await db_rb.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
