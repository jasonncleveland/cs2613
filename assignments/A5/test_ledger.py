from ledger import ledger

def test_empty():
    assert list(ledger("")) == []

def test_balance():
    assert list(
        ledger('''
            balance cash
            balance stock
        ''')) == [("cash", 0), ("stock", 0)]

def test_open():
    assert list(
        ledger('''
            open cash 100
            balance cash
        ''')) == [("cash", 10000)]

def test_transfer():
    assert list(
        ledger('''
            open cash 100
            open expenses 0
            transfer cash expenses 50
            balance cash
            balance expenses
        ''')) == [("cash", 5000), ("expenses", 5000)]

def test_transfer2():
    """test transfer with floating point"""
    assert list(
        ledger('''
            open cash 100.30
            open expenses 0
            transfer cash expenses 50.10
            balance cash
            balance expenses
        ''')) == [("cash", 5020), ("expenses", 5010)]

def test_transfer3():
    """test transfer with negative starting balance"""
    assert list(
        ledger('''
            open cash 1000
            open expenses -100.30
            transfer cash expenses 50.10
            balance cash
            balance expenses
        ''')) == [("cash", 94990), ("expenses", -5020)]
