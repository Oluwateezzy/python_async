import multiprocessing

def square(n, result_queue):
    result_queue.put(n * n)

if __name__ == "__main__":
    q = multiprocessing.Queue()

    processes = [
        multiprocessing.Process(target=square, args=(i, q))
        for i in range(1, 6)
    ]
    for p in processes: p.start()
    for p in processes: p.join()

    results = [q.get() for _ in processes]
    print(sorted(results))