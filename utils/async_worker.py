from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=2)


def run_in_thread(func, *args):
    future = executor.submit(func, *args)
    return future.result()
