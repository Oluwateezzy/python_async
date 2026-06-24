import asyncio
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(0.5)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource")
        await asyncio.sleep(0.5)

async def main():
    async with AsyncResource() as r:
        print("Using resource")

asyncio.run(main())