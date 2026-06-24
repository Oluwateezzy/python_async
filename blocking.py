import asyncio

def blocking_io():
    import time
    time.sleep(2)
    return "done"

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_io)
    print(result)

asyncio.run(main())
