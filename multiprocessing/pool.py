import multiprocessing, time


def cpu_task(n):
    return sum(i * i for i in range(n))


# if __name__ == "__main__":
    