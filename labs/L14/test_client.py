#!/usr/bin/python3

from client import approximate_size

def test_1000():
    assert approximate_size(1000000000000) == "1.0 TB"

def test_docstring():
    assert approximate_size.__doc__ is not None
