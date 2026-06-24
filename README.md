# Python Asynchronous Programming Playground

Welcome to your **Python Async/Await Playground**! This repository is designed as an interactive, educational space to learn, practice, and refresh your memory on the core concepts of asynchronous programming in Python using `asyncio`.

---

## 🚀 Quick Start: Setup and Execution

To run these examples without polluting your global Python environment, we use **`uv`**, a super-fast Python package and environment manager.

### 1. Initialize the Virtual Environment
Create and activate the environment, then install the required dependencies (`aiohttp` and `certifi`):
```bash
# Create virtual environment
uv venv

# Activate on macOS/Linux
source .venv/bin/activate

# Install third-party requirements
uv pip install aiohttp certifi
```

### 2. Running the Files
Run any file in the workspace using the virtual environment's Python interpreter:
```bash
python <filename>.py

# Example:
python test.py
```

---

## 📚 Table of Contents

Below is a roadmap of the educational modules in this repository:

| File | Concept | Focus Area |
| :--- | :--- | :--- |
| [coroutine.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/coroutine.py) | **Async Fundamentals** | Coroutines, `asyncio.sleep`, task creation, and `asyncio.gather`. |
| [taskgroup.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/taskgroup.py) | **Structured Concurrency** | Managing task lifetimes safely with `asyncio.TaskGroup` (Python 3.11+). |
| [cancelled.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/cancelled.py) | **Cancellation & Cleanup** | Graceful cancellation handling using `asyncio.CancelledError`. |
| [timeouts.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/timeouts.py) | **Timeouts & Deadlines** | Limiting execution time using `asyncio.wait_for`. |
| [blocking.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/blocking.py) | **Non-blocking Executors** | Running blocking CPU/IO code in threads via `run_in_executor`. |
| [async_for.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_for.py) | **Async Iteration** | Building asynchronous generators (`yield`) and `async for` loops. |
| [async_context.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_context.py) | **Async Resource Management** | Writing clean cleanup blocks using `async with` (`__aenter__`/`__aexit__`). |
| [async_queue.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_queue.py) | **Queue Pipelines** | Coordinating producer-consumer worker flows using `asyncio.Queue`. |
| [asyncio_threading.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio_threading.py) | **Concurrency Control** | Restricting resource access using `Lock`, `Semaphore`, and `Event`. |
| [test.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/test.py) | **Practical Web Scraping** | Performing parallel HTTP calls with `aiohttp` and custom SSL context. |

---

## 🧠 Educational Concept Sheets

### 1. Coroutines & Task Gathering
*Demonstrated in:* [coroutine.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/coroutine.py)
* **What is it?** Asynchronous code relies on *coroutines* (defined with `async def`). When you call a coroutine, it doesn't run immediately; it returns a coroutine object.
* **Tasks**: Wrapping a coroutine in `asyncio.create_task()` registers it on the event loop, allowing it to start running concurrently in the background.
* **Gathering**: `asyncio.gather(*tasks)` runs multiple awaitables concurrently and waits for all of them to finish.
  * Use `return_exceptions=True` to prevent a single failing coroutine from stopping the entire gather result list.

---

### 2. Structured Concurrency (`asyncio.TaskGroup`)
*Demonstrated in:* [taskgroup.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/taskgroup.py)
* **What is it?** Added in Python 3.11, `asyncio.TaskGroup()` is the modern way to manage group task lifetimes.
* **Why it's better than `gather`**: If one task in the group raises an unhandled exception, **all other active tasks in the group are immediately cancelled**. This prevents resource leaks and orphaned background tasks.
```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch(1))
    task2 = tg.create_task(fetch(2))
# Both tasks are guaranteed completed or cleaned up when exiting the context block
```

---

### 3. Task Cancellation & Cleanup
*Demonstrated in:* [cancelled.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/cancelled.py)
* **What is it?** You can cancel a running task at any time using `task.cancel()`.
* **How it works**: This injects an `asyncio.CancelledError` into the coroutine at the next `await` statement.
* **Crucial Rule**: Always wrap tasks in a `try...except asyncio.CancelledError` block if they need to close database connections or clean up files before quitting. Make sure to **re-raise** the exception so the event loop knows the task is successfully aborted.

---

### 4. Timeouts & Deadlines
*Demonstrated in:* [timeouts.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/timeouts.py)
* **What is it?** Prevent tasks from hanging indefinitely using `asyncio.wait_for(coro(), timeout=N)`.
* **Behavior**: If the operation exceeds `timeout` seconds, it is automatically cancelled and raises `asyncio.TimeoutError`.

---

### 5. Running Blocking Code (`run_in_executor`)
*Demonstrated in:* [blocking.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/blocking.py)
* **The Problem**: Python's event loop runs on a single thread. If you perform a blocking operation (like `time.sleep()`, synchronous database queries, or heavy CPU tasks), you block the *entire event loop*, freezing all other tasks!
* **The Solution**: Offload blocking work to a thread pool executor.
```python
loop = asyncio.get_running_loop()
# Executes blocking_io() in a separate OS thread, allowing the event loop to keep ticking
result = await loop.run_in_executor(None, blocking_io)
```

---

### 6. Asynchronous Generators
*Demonstrated in:* [async_for.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_for.py)
* **What is it?** Standard Python generators yield items. Asynchronous generators do the same but are allowed to run asynchronous operations (like fetching database rows or hitting an API) before yielding.
* **Usage**: Defined using `async def` containing `yield`. Consumed using `async for item in async_gen()`.

---

### 7. Asynchronous Context Managers
*Demonstrated in:* [async_context.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_context.py)
* **What is it?** Objects that define asynchronous setup and tear-down logic.
* **How to build them**: Implement special methods `async def __aenter__(self)` and `async def __aexit__(self, exc_type, exc, tb)`.
* **Usage**: Executed using `async with MyContext() as ctx:`.

---

### 8. Producer-Consumer Pipelines (Queues)
*Demonstrated in:* [async_queue.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/async_queue.py)
* **What is it?** An `asyncio.Queue` is designed to securely pass data between different concurrent tasks.
* **Why use it?** It automatically blocks the consumer when the queue is empty, and blocks the producer if the queue reaches its maximum size limit (backpressure), making it the perfect tool for pipeline tasks.

---

### 9. Concurrency Control (Locks, Semaphores, Events)
*Demonstrated in:* [asyncio_threading.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio_threading.py)
* **Locks (`asyncio.Lock`)**: Ensures only *one* task can enter a critical section at any given time.
* **Semaphores (`asyncio.Semaphore(N)`)**: Limits concurrency. Excellent for rate-limiting (e.g., "only allow up to 3 HTTP requests to run concurrently").
* **Events (`asyncio.Event`)**: Allows tasks to pause and wait until another task triggers the event via `event.set()`.

---

### 10. Practical HTTP Fetching (aiohttp + macOS SSL Verification Workaround)
*Demonstrated in:* [test.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/test.py)
* **`aiohttp`**: The industry standard for asynchronous HTTP requests in Python.
* **⚠️ macOS SSL Cert Verification Gotcha**: Homebrew and standard macOS Python installs often fail to load system SSL root certificates, raising an `SSLCertVerificationError` when hitting HTTPS endpoints.
* **How to solve it**:
  1. Install `certifi` (a bundle of curated root certificates).
  2. Create a custom SSL Context linked to `certifi.where()`.
  3. Pass this context to the `aiohttp.TCPConnector`.
```python
import ssl
import certifi
import aiohttp

# Create custom SSL context pointing to certifi CAs
ssl_context = ssl.create_default_context(cafile=certifi.where())
connector = aiohttp.TCPConnector(ssl=ssl_context)

# Inject connector into client session
async with aiohttp.ClientSession(connector=connector) as session:
    ...
```

---

## ⚡ Important Gotchas & Best Practices

1. **Never use local file shadowing**: Never name your local script files with names matching Python standard library packages (e.g., naming a file `queue.py` will hijack all standard library imports of `import queue`, crashing standard threading modules). Always name them uniquely (e.g., `async_queue.py`).
2. **Never block the event loop**: Always use `await asyncio.sleep()` instead of `time.sleep()`, and use `run_in_executor()` for synchronous operations.
3. **Use structured concurrency**: Favor `asyncio.TaskGroup` over `asyncio.gather` in production code to avoid leaked/runaway tasks on errors.
