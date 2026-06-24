from socket import timeout
import asyncio
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "done"


async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=6)
    except asyncio.TimeoutError:
        print("time out!")

asyncio.run(main())