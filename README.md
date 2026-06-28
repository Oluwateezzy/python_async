# Python Concurrency & Asynchronous Programming Playground

Welcome to the **Python Concurrency Playground**! This repository is designed as an interactive, educational space to learn, practice, and explore Python's various concurrency paradigms: **Asynchronous Programming (`asyncio`)**, **Multithreading (`threads`)**, and **Multiprocessing (`multiprocessing`)**.

---

## Quick Start: Setup and Execution

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
Since the files are organized into subdirectories, invoke them by specifying their folder path:
```bash
# Running an asyncio example
python asyncio/coroutine.py

# Running a multithreading example
python threads/basic.py

# Running a multiprocessing example
python multiprocessing/basic.py
```

---

## 📚 Table of Contents

Below is a roadmap of the educational modules in this repository:

### ⚡ Asynchronous Programming (`asyncio/`)

| File | Concept | Focus Area |
| :--- | :--- | :--- |
| [coroutine.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/coroutine.py) | **Async Fundamentals** | Coroutines, `asyncio.sleep`, task creation, and concurrent gathering (`asyncio.gather`). |
| [taskgroup.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/taskgroup.py) | **Structured Concurrency** | Managing task lifetimes safely with `asyncio.TaskGroup` (Python 3.11+). |
| [cancelled.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/cancelled.py) | **Cancellation & Cleanup** | Graceful cancellation handling using `asyncio.CancelledError`. |
| [timeouts.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/timeouts.py) | **Timeouts & Deadlines** | Limiting execution time using `asyncio.wait_for`. |
| [blocking.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/blocking.py) | **Non-blocking Executors** | Running blocking CPU/IO code in threads via `run_in_executor`. |
| [async_for.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/async_for.py) | **Async Iteration** | Building asynchronous generators (`yield`) and `async for` loops. |
| [async_context.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/async_context.py) | **Async Resource Management** | Writing clean cleanup blocks using `async with` (`__aenter__`/`__aexit__`). |
| [async_queue.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/async_queue.py) | **Queue Pipelines** | Coordinating producer-consumer worker flows using `asyncio.Queue`. |
| [asyncio_threading.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/asyncio_threading.py) | **Async Synchronization** | Native async concurrency control using `Lock`, `Semaphore`, and `Event`. |
| [test.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/asyncio/test.py) | **Practical Web Scraping** | Parallel HTTP calls with `aiohttp` and custom SSL context verification workaround. |

### 🧵 Multithreading (`threads/`)

| File | Concept | Focus Area |
| :--- | :--- | :--- |
| [basic.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/basic.py) | **Thread Spawning** | Starting threads via functions and subclassing `threading.Thread`, joining, and daemon threads. |
| [race_condition.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/race_condition.py) | **Race Conditions & Mutexes** | Protecting shared state from concurrent modification bugs using `threading.Lock`. |
| [synchronization.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/synchronization.py) | **Locking & Signaling** | Differences between `Lock` and `RLock`, limiting access via `Semaphore`, and client-server sync with `Event`. |
| [condition.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/condition.py) | **Conditional Notification** | Coordinating producers and consumers using `threading.Condition` wait/notify flows. |
| [barrier.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/barrier.py) | **Barrier Checkpoints** | Synchronizing a fixed number of threads at a checkpoint using `threading.Barrier`. |
| [thread_local.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/thread_local.py) | **Isolated Thread Storage** | Storing thread-specific variables using `threading.local`. |
| [thread_docs.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/thread_docs.py) | **Thread Introspection** | Retrieving counts, listing threads, and gathering thread IDs (`get_ident`, `get_native_id`). |
| [queeue.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/threads/queeue.py) | **Thread-Safe Pipelines** | Building multi-worker task distribution systems with the thread-safe `queue.Queue`. |

### ⚙️ Multiprocessing (`multiprocessing/`)

| File | Concept | Focus Area |
| :--- | :--- | :--- |
| [basic.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/multiprocessing/basic.py) | **Parallel Processing** | Spawning concurrent processes (`multiprocessing.Process`) to bypass the Python GIL for CPU-bound tasks. |
| [queue_mult.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/multiprocessing/queue_mult.py) | **Inter-Process Comm (IPC)** | Safely passing objects between processes using `multiprocessing.Queue`. |
| [pool.py](file:///Users/oluwatobiloba/Desktop/personal/python_async/multiprocessing/pool.py) | **Process Pooling** | Mapping execution lists over a pool of background worker processes. |

---

## 🧠 Educational Concept Sheets

### 1. Asynchronous Programming (`asyncio`)

* **What is it?** Asynchronous code runs on a single-threaded cooperative event loop. Coroutines (defined with `async def`) voluntarily yield control back to the event loop using `await` when waiting for I/O operations, allowing other tasks to run.
* **Tasks**: Wrapping a coroutine in `asyncio.create_task()` registers it on the event loop, allowing it to start running concurrently in the background.
* **Structured Concurrency**: Favor `asyncio.TaskGroup()` (Python 3.11+) over `asyncio.gather()`. If any subtask in a `TaskGroup` raises an unhandled exception, all other active tasks in the group are automatically cancelled, preventing orphaned tasks and leaks.
* **Task Cancellation**: Tasks can be cancelled via `task.cancel()`. Make sure to catch `asyncio.CancelledError` if you need to run cleanup operations, and remember to re-raise it.
* **Never Block the Event Loop**: Since everything runs on one thread, calling blocking functions (like `time.sleep()`, synchronous DB calls, or heavy math operations) blocks the entire event loop. Use `loop.run_in_executor(None, blocking_func)` to run them in a background thread.
* **Synchronization Primitives**: In `asyncio_threading.py`, we demonstrate that async-native programs can still use `Lock`, `Semaphore`, and `Event` to protect and coordinate shared asynchronous workflows.
* **macOS SSL Workaround**: Standard macOS Python builds often fail to find system root SSL certificates when using `aiohttp`. Resolve this by passing a custom SSL context constructed using `certifi.where()` to `aiohttp.TCPConnector`.

---

### 2. Multithreading (`threads`)

* **What is it?** Spawns multiple threads of execution within the *same* process. All threads share the process's memory space, which allows easy sharing of objects but introduces race conditions.
* **The Global Interpreter Lock (GIL)**: Standard Python (CPython) has a GIL, which prevents multiple native threads from executing Python bytecodes at once. As a result, multithreading in Python **does not** provide parallel CPU computation, but it is highly effective for I/O-bound operations (e.g., scraping webs, reading disks) where threads spend most of their time waiting.
* **Race Conditions & Locks**: When multiple threads read and write to the same memory location, a race condition occurs. Use a `threading.Lock` to guarantee that only one thread executes a critical section of code at a time.
* **Re-entrant Locks (`RLock`)**: Unlike standard locks, an `RLock` can be acquired multiple times by the *same* thread without deadlocking. It must be released the same number of times it was acquired.
* **Producer-Consumer Coordination (`Condition`)**: A `Condition` variable allows one or more threads to wait until they are notified by another thread. It acts as a lock combined with a signaling mechanism.
* **Barrier Checkpoint**: A `Barrier` blocks a predefined number of threads at `barrier.wait()` until all of them have reached the barrier, at which point they are all released simultaneously.
* **Thread-Local Storage**: Objects created using `threading.local()` store attributes that are strictly private/isolated to the executing thread, preventing cross-thread pollution.
* **Thread-Safe Queues**: The `queue.Queue` module handles locking under the hood, making it the perfect tool to build multi-producer, multi-consumer worker patterns safely.

---

### 3. Multiprocessing (`multiprocessing`)

* **What is it?** Spawns completely separate OS processes, each with its own Python interpreter and isolated memory space.
* **GIL Bypass**: Because each process has its own GIL, multiprocessing allows **true parallelism** on multi-core systems. This is the correct choice for CPU-bound tasks (e.g., intensive math, image processing).
* **Inter-Process Communication (IPC)**: Since processes do not share memory, you cannot easily modify a global variable from a child process. Use specialized, serialized communication channels like `multiprocessing.Queue` or `Pipe` to exchange data.
* **The `if __name__ == "__main__":` Guard**: You **must** wrap process start code in this guard. On systems using `spawn` (like macOS and Windows), child processes import the main module to set up their execution environment. Failing to use the guard will trigger an infinite loop of process spawning.

---

## 📊 Concurrency Cheat Sheet: Which Should I Use?

| Metric / Paradigm | Asynchronous (`asyncio`) | Multithreading (`threads`) | Multiprocessing (`multiprocessing`) |
| :--- | :--- | :--- | :--- |
| **Concurrency Type** | Cooperative Single-Threaded | Preemptive Multi-Threaded | Parallel Multi-Process |
| **GIL Bound?** | Yes | Yes (Limited to 1 CPU core) | **No** (Bypasses GIL) |
| **Memory State** | Shared (Single Process) | Shared (Single Process) | **Isolated** (Separate Processes) |
| **Best For** | Network I/O, many sockets (10k+) | Disk & Network I/O, quick background tasks | Heavy mathematical/CPU computation |
| **Primary Risk** | Blocking the loop halts everything | Race conditions, deadlocks | High memory overhead, IPC serialization cost |
