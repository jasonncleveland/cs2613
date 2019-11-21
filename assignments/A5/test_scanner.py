from scanner import Scanner
from token_ import Token
from type_ import Type

def test_scan_keywords():
    scanner = Scanner('''
        TrAnsFer transfer
        OPEN BALANCE balance''')
    toks = [
        Token(Type.TRANSFER, "TrAnsFer"),
        Token(Type.TRANSFER, "transfer"),
        Token(Type.OPEN, "OPEN"),
        Token(Type.BALANCE, "BALANCE"),
        Token(Type.BALANCE, "balance")
    ]

    assert [tok for tok in scanner] == toks
    # iterate a second time
    assert [tok for tok in scanner] == toks

def test_scan_identifiers():
    scanner = Scanner("equity cash end_of_the_world_fund")
    assert list(scanner) == [
        Token(Type.IDENT, "equity"),
        Token(Type.IDENT, "cash"),
        Token(Type.IDENT, "end_of_the_world_fund")
    ]
    
