fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
    print wrap