import time

def time_func(func):
    start_time = time.time()
    for i in range(36):
        func(i)
    end_time = time.time()
    return end_time - start_time

original_time = time_func(func)
memoized_time = time_func(func)

print("Original time:", original_time)
print("Memoized time:", memoized_time)
