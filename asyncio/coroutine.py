from datetime import time
import asyncio
import asyncio, time

# Synchronous
def say_hello():
    print("Hello...")
    time.sleep(5)
    print("...World!")

async def say_hello_sync():
    print("Hello...")
    await asyncio.sleep(5)
    print("...World!")

async def fetch(n):
    print(f"Start fetch {n}")
    await asyncio.sleep(2)
    print(f"Done fetch {n}")
    return n * 10

# asyncio.run(say_hello_sync())
# say_hello()

async def main():
    start = time.time()
    r1 = await fetch(1)
    r2 = await fetch(2)
    end = time.time()

    print(r1, r2)
    print(f"Total: {time.time() - start:.1f}s")

# asyncio.run(main())

async def main2():
    start = time.time()
    task1 = asyncio.create_task(fetch(1))
    task2 = asyncio.create_task(fetch(2))
    end = time.time()

    r1 = await task1
    r2 = await task2

    print(r1, r2)
    print(f"Total: {time.time() - start:.1f}s")

# asyncio.run(main2())

async def fetch2(n):
    await asyncio.sleep(n)
    return f"Result {n}"

async def main3():
    results = await asyncio.gather(
        fetch2(1),
        fetch2(2),
        fetch2(3)
    )
    print(results)

# asyncio.run(main3())

async def risky():
    await asyncio.sleep(1)
    raise ValueError("boom")


async def main4():
    try:
        await asyncio.gather(risky(), fetch(2))
    except ValueError as e:
        print("Caught:", e)

async def main5():
    results = await asyncio.gather(risky(), fetch(2), return_exceptions=True)
    print(results)

asyncio.run(main5())