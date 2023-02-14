import sys
import json
import timeit
import matplotlib.pyplot as plt
import threading
threading.stack_size(33554432)
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

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

file = open('ex2.json')
data = json.load(file)

base = []
arrtime = []

for x in range(len(data)):
    base.append(x)
    arrtime.append(timeit.repeat(lambda: func1(data[x], 0, len(data[x]) - 1), number=1, repeat=1))


plt.plot(base, arrtime, label="unoptimized")
plt.xlabel('n (array size in thousands avg)')
plt.ylabel('Time (in seconds)')
plt.title('Quick Sort Computation Time')
plt.show()