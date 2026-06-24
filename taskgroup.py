import asyncio
import asyncio

async def fetch(n):
    await asyncio.sleep(n)
    print(f"Fetched {n}")
    return n

async def main():
    results = []
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch(1))
        t2 = tg.create_task(fetch(2))
        t3 = tg.create_task(fetch(3))
    print(t1.result(), t2.result(), t3.result())

asyncio.run(main())