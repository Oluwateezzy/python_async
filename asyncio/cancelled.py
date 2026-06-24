import asyncio

async def long_task():
    try:
        print("Task started")
        await asyncio.sleep(10)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task was cancelled, cleaning up...")
        raise

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Main: Confirmed task cancelled")

asyncio.run(main())