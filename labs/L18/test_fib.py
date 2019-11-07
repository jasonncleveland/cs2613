import fib

def test_fib():
    fun = fib.fib2(1000)
    lst2 = []
    while True:
        n = fun()
        if n != None:
            lst2.append(n)
        else:
            break
    assert lst2 == list(fib.fib(1000))