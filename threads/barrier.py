import threading, time

barrier = threading.Barrier(3)

def worker(name):
    print(f"{name} doing phase 1")
    time.sleep(1)
    barrier.wait()
    print(f"{name} doing phase 2")

for name in ["W2", "W3", "W5"]:
    threading.Thread(target=worker, args=(name,)).start()