#!/usr/bin/python3
import globex

def test_for():
    assert sorted(globex.python_files_for) == sorted(globex.python_files_comp)

def test_map():
    assert sorted(globex.python_files_comp) == sorted(globex.python_files_map)
