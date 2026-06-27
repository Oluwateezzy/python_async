import threading, time, queue

work_queue = queue.Queue()
result_queue = queue.Queue()

def producer():
    for i in range(10):
        work_queue.put(f"job-{i}")
        print(work_queue.queue)
        time.sleep(5)
    work_queue.put(None)

def worker(name):
    while (True):
        job = work_queue.get()
        if job is None:
            work_queue.put(None)
            break
        result = f"{job}-result"
        result_queue.put(result)
        print(f"[{name}] processed {job}")

def results_printer():
    count = 0
    while count < 10:
        result = result_queue.get()
        print(f"RESULT: {result}")
        count += 1

t_producer = threading.Thread(target=producer)
workers = [threading.Thread(target=worker, args=(f"W{i}",)) for i in range(3)]
t_printer = threading.Thread(target=results_printer)

t_producer.start()
for w in workers: w.start()
t_printer.start()

t_producer.join()
for w in workers: w.join()
t_printer.join()