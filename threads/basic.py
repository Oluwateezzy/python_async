import threading
import time

def worker(name, delay):
    print(f"[{name}] starting")
    time.sleep(delay)
    print(f"[{name}] done after {delay}s")

t1 = threading.Thread(target=worker, args=("Alpha", 2))
t2 = threading.Thread(target=worker, args=("Omega", 2))

t1.start()
t2.start()

print("This is working")

t1.join()
t2.join()

print("All threads done")


class DownloadThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.result = None
    
    def run(self):
        time.sleep(1)
        self.result = f"data from {self.url}"

t = DownloadThread("https://example.com")
t.start()
t.join()
print(t.result)

def background_heartbeat():
    while True:
        print("heartbeat")
        time.sleep(5)

t3 = threading.Thread(target=background_heartbeat, daemon=True)
t3.start()