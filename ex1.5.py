import timeit
import matplotlib.pyplot as plt

base = []
arr = []
arrtime = []
arr2 = []
arr2time = []

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

for x in range(36):
    base.append(x)
    arr.append(func(x))
    arrtime.append(timeit.repeat(lambda: func(x),number=1,repeat=1))


cache = dict()

def fib(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n-1) + fib(n-2)
            return cache[n]

for x in range(36):
    arr2.append(fib(x))
    arr2time.append(timeit.repeat(lambda: fib(x),number=1,repeat=1))

plt.plot(base, arrtime, label="unoptimized")
plt.plot(base, arr2time, label="optimized")
plt.xlabel('n (input to fib_memo function)')
plt.ylabel('Time (in seconds)')
plt.title('Fibonacci Sequence Computation Time with Memorization')
plt.show()