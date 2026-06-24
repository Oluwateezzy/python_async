import asyncio

# An Asynchronous Context Manager
# Enables resource setup and teardown using async/await within 'async with' blocks.
class AsyncResource:
    # Called when entering the 'async with' block.
    # Can run asynchronous setup tasks (e.g. connecting to a database).
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(0.5)  # Simulating async setup/connection time
        return self

    # Called when exiting the 'async with' block (even if an error occurs).
    # Can run asynchronous teardown/cleanup tasks (e.g. closing connection).
    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource")
        await asyncio.sleep(0.5)  # Simulating async cleanup/teardown time

async def main():
    # Using the context manager
    async with AsyncResource() as r:
        print("Using resource")

if __name__ == '__main__':
    asyncio.run(main())