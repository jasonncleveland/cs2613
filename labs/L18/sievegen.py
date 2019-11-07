#!/usr/bin/python3

from math import sqrt, ceil

def drop_divisible(n, lst):
    for x in lst:
        if x == n or x % n != 0:
            yield x

def sieve_with(candidates, lst):
    for c in candidates:
        lst = drop_divisible(c, lst)
    return lst

def sieve(n):
    return sieve_with(range(2, ceil(sqrt(n)) + 1), range(2, n))
