import threading
from typing import List
import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)
    print(f"crawl ended for {link}")


links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

threads: List[threading.Thread] = []

for link in links:
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
    threads.append(t)

for t in threads:
    t.start()

print(threading.active_count())
print(threading.enumerate())
print(f"main {threading.main_thread()}")

for t in threads:
    t.join()

print(threading.active_count())
print(threading.current_thread())
print(threading.get_native_id())
print(threading.get_ident())
print(threading.enumerate())