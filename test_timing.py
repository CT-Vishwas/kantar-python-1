from utils import time_func

@time_func
def slow_func():
    k = 0
    for i in range(100000000):
        k += i
    
    return k


val = slow_func()
print(val)