from sieve import drop_divisible, sieve

def test_drop_divisible():
    assert drop_divisible(3, [2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 7, 8, 10]

def test_sieve():
    assert sieve(10) == [2, 3, 5, 7]