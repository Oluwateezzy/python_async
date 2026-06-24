import asyncio

# An asynchronous generator
# It uses 'async def' and 'yield' statements. 
# It can await other asynchronous tasks (like network I/O or sleep) before yielding a value.
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.6)  # Simulating a non-blocking asynchronous operation
        yield i

async def main():
    # Consuming the asynchronous generator using 'async for'
    # Each iteration awaits the next yielded value from the generator.
    async for value in async_range(5):
        print(value)

if __name__ == '__main__':
    asyncio.run(main())