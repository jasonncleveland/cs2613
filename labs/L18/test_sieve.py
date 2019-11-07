import sieve
import sievegen

def test_sieve():
    assert [x for x in sievegen.sieve(1000)] == sieve.sieve(1000)
