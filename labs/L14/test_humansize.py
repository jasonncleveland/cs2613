#!/usr/bin/python3

from humansize import approximate_size

def test_1000():
    assert approximate_size(1000000000000, False) == "1.0 TB"

def test_1024():
    assert approximate_size(1000000000000) == "931.3 GiB"

### Second part

def test_4000_positional_args():
    assert approximate_size(4000, a_kilobyte_is_1024_bytes=False) == "4.0 KB"

def test_4000_keyword_args():
    assert approximate_size(size=4000, a_kilobyte_is_1024_bytes=False) == "4.0 KB"

def test_4000_keyword_args_out_of_order():
    assert approximate_size(a_kilobyte_is_1024_bytes=False, size=4000) == "4.0 KB"
