import functools

@functools.lru_cache(maxsize=100, typed=False)
def fibonacci(n):

    if n < 0:
        raise ValueError
 
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 