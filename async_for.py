import asyncio

async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.6)
        yield i

async def main():
    async for value in async_range(5):
        print(value)

asyncio.run(main())