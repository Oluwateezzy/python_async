import threading
import threading, time

lock = threading.Lock()
with lock:
    pass

rlock = threading.RLock()
def outer():
    with rlock:
        inner()

def inner():
    with rlock:
        pass

db_pool = threading.Semaphore(3)
def query_database(thread_id):
    with db_pool:
        print(f"Thread {thread_id} using DB")
        time.sleep(1)

threads = [threading.Thread(target=query_database, args=(i,)) for i in range(10)]
for t in threads: t.start()
for t in threads: t.join()


ready = threading.Event()

def server():
    time.sleep(2)
    print("Server is up")
    ready.set()

def client(name):
    ready.wait()
    print(f"{name} connected!")

threading.Thread(target=server).start()
for name in ["Client-A", "Client-B"]:
    threading.Thread(target=client, args=(name,)).start()