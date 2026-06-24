import asyncio
import asyncio
import random

async def producer(queue: asyncio.Queue, n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"Consumed {item}")
        await asyncio.sleep(0.2)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue, 5),
        consumer(queue)
    )

asyncio.run(main())