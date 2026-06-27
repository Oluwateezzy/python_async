from time import sleep
import threading

condition = threading.Condition()
items = []

def producer():
    for i in range(5):
        print(f"Prooducer: {i}")
        sleep(1)
        with condition:
            items.append(i)
            condition.notify()
        sleep(0.5)

def consumer():
    while len(items) < 5:
        with condition:
            condition.wait()
            print(f"Consumed: {items[-1]}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()