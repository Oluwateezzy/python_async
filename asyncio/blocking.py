import asyncio

# A blocking, synchronous, CPU or IO-bound function.
# It uses standard time.sleep() which blocks the execution thread.
# Running this directly in an async function would freeze the whole event loop.
def blocking_io():
    import time
    time.sleep(2)  # Blocks the active thread
    return "done"

async def main():
    # Retrieve the running event loop instance.
    loop = asyncio.get_running_loop()
    
    # run_in_executor runs the blocking function in a separate thread.
    # First argument 'None' defaults to the loop's ThreadPoolExecutor.
    # This allows the main thread's event loop to keep processing other tasks concurrently.
    result = await loop.run_in_executor(None, blocking_io)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
