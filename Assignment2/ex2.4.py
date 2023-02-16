import sys 
import json
import timeit
import matplotlib.pyplot as plt
import threading

threading.stack_size(33554432)
sys.setrecursionlimit(20000)

with open('ex2.json', 'r') as f:
    inputs = [json.load(f)]


def quicksort(array):
    if len(array) < 2:
        return array
    stack = [(0, len(array)-1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        p = partition(array, low, high)
        stack.append((low, p-1))
        stack.append((p+1, high))
    return array

def partition(array, low, high):
    p = array[low]
    i = low + 1
    j = high
    while i <= j:
        if array[i] <= p:
            i += 1
        elif array[j] >= p:
            j -= 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[low], array[j] = array[j], array[low]
    return j

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

times = []
for arr in inputs:
    time_taken = timeit.timeit(lambda: quicksort(arr), number=1)
    times.append(time_taken)

plt.plot(range(len(inputs)), times, marker='o')
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort performance')
plt.show()