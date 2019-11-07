def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

def fib2(max):
    a, b = 0, 1
    def next():
        nonlocal a, b
        retval = a
        a, b = b, a + b
        if retval < max:
            return retval
        else:
            return None
    
    return next
