from read_csv import read_csv

table = read_csv('test1.csv')

def test_read_csv():
    assert read_csv('test1.csv') == [
        ['name', 'age', 'eye colour'],
        ['Bob', '5', 'blue'],
        ['Mary', '27', 'brown'],
        ['Vij', '54', 'green']
    ]
