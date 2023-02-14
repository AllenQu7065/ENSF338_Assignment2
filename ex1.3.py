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