from a4 import header_map, select, row2dict, check_row, filter_table
from read_csv import read_csv

table = read_csv('test2.csv')

def test_header_map_1():
    hmap = header_map(table[0])
    assert hmap == { 'UNITID': 0, 'INSTNM': 1, 'CITY': 2, 'STABBR': 3, 'ZIP': 4, 'SCH_DEG': 5 }

def test_select_1():
    assert select(table[:6], {'INSTNM', 'CITY', 'STABBR'}) == [
        ['INSTNM', 'CITY', 'STABBR'],
        ['Alabama A & M University', 'Normal', 'AL'],
        ['University of Alabama at Birmingham', 'Birmingham', 'AL'],
        ['Amridge University', 'Montgomery', 'AL'],
        ['University of Alabama in Huntsville', 'Huntsville', 'AL'],
        ['Alabama State University', 'Montgomery', 'AL']
    ]

def test_row2dict():
    hmap = header_map(table[0])
    assert row2dict(hmap, table[1]) == {
        'UNITID': '100654',
        'INSTNM': 'Alabama A & M University',
        'CITY': 'Normal',
        'STABBR': 'AL',
        'ZIP': '35762', 
        'SCH_DEG': '3'
    }

def test_check_row():
    row = { 'INSTNM': 'Alabama A & M University', 'CITY': 'Normal', 'STABBR': 'AL', 'ZIP': '35762', 'SCH_DEG': '3' }
    assert check_row(row, ('INSTNM', '==', 'Alabama A & M University'))
    assert check_row(row, ('SCH_DEG', '==', 3))
    assert not check_row(row, ('CITY', '==', 9))
    assert check_row(row, ('ZIP', '>=', '35762'))
    assert check_row(row, ('ZIP', '<=', 35763))
    assert check_row(row, ('CITY', '!=', 'Birmingham'))

def test_check_row_logical():
    row = { 'INSTNM': 'Alabama A & M University', 'CITY': 'Normal', 'STABBR': 'AL', 'ZIP': '35762', 'SCH_DEG': '3' }
    assert check_row(row, (('CITY', '==', 'Birmingham'), 'OR', ('ZIP', '>=', '35762')))
    assert not check_row(row, (('INSTNM', '==', 'Alabama A & M University'), 'AND', ('CITY', '==', 9)))

def test_filter_table1():
    assert filter_table(table, ('STABBR', '==', 'WA')) == [
        ['UNITID', 'INSTNM', 'CITY', 'STABBR', 'ZIP', 'SCH_DEG'],
        ['102845', 'Charter College', 'Vancouver', 'WA', '98683-7575', '1']
    ]

def test_filter_table2():
    assert filter_table(table, (('STABBR', '==', 'AK'), 'AND', ('SCH_DEG', '==', 1))) == [
        ['UNITID', 'INSTNM', 'CITY', 'STABBR', 'ZIP', 'SCH_DEG'],
        ['102580', 'Alaska Bible College', 'Palmer', 'AK', '99645', '1'],
        ['102711', 'AVTEC-Alaska\'s Institute of Technology', 'Seward', 'AK', '99664-0889', '1'],
        ['103501', 'Alaska Career College', 'Anchorage', 'AK', '99507-1033', '1']
    ]
