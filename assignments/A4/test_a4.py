from a4 import header_map, select
from read_csv import read_csv

table = read_csv('test1.csv')

def test_header_map_1():
    hmap = header_map(table[0])
    assert hmap == { 'name': 0, 'age': 1, 'eye colour': 2 }

def test_select_1():
    assert select(table, {'name', 'eye colour'}) == [
        ['name', 'eye colour'],
        ['Bob', 'blue'],
        ['Mary', 'brown'],
        ['Vij', 'green']
    ]
