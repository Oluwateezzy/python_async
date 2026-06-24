import asyncio
import asyncio

lock = asyncio.Lock()

async def critical_selection():
    async with lock:
        print("In critical section")
        await asyncio.sleep(1)

sem = asyncio.Semaphore(3)

async def limitedFetch(n):
    async with sem:
        print(f"Fetching {n}")
        await asyncio.sleep(5)
        return n

events = asyncio.Event()

async def waiter():
    print("Waiting for event....")
    await events.wait()
    print("Event received....")

async def setter():
    await asyncio.sleep(2)
    events.set()

async def main():
    await asyncio.gather(*(limitedFetch(i) for i in range(10)))
    await asyncio.gather(
        waiter(),
        setter()
    )


asyncio.run(main())

