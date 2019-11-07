import counter

def test_count():
    _counter = counter.make_counter(100)
    _counter2 = counter.make_counter2(100)

    for j in range(0, 100):
        assert next(_counter) == _counter2()