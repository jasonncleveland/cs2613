from fib import Fib
from fibgen import fibgen

def test_fib_list():

    genfibs = list(fibgen(100))
    fibber = Fib(100)

    fibs = []
    while True:
        try:
            fibs.append(next(fibber))
        except:
            break
    
    assert genfibs == fibs

def test_fib_list_2():
    genfibs = list(fibgen(100))
    classfibs = list(Fib(100))
    assert genfibs == classfibs

def test_fib_restart():
    fibobj = Fib(100)
    list1 = list(fibobj)
    list2 = list(fibobj)
    assert list1 == list2
