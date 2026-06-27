import multiprocessing, time, os

def cpu_heavy(n):
    print(f"PID {os.getpid()} starting work on {n}")
    total = sum(i * i for i in range(n))
    return total

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=cpu_heavy, args=(5_000_000,))
    p2 = multiprocessing.Process(target=cpu_heavy, args=(5_000_000,))
    print(p1.name, p2.name)
    start = time.perf_counter()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"Done in {time.perf_counter() - start:.2f}s")