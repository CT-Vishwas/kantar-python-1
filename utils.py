import time

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"The time taken is: {time.time() -start}s")
        return result
    return wrapper