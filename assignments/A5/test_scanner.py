import pytest

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

def test_scan_currency():
    scanner = Scanner("100 100.00 100.42 -123.45")
    assert list(scanner) == [
        Token(Type.CURRENCY, 10000),
        Token(Type.CURRENCY, 10000),
        Token(Type.CURRENCY, 10042),
        Token(Type.CURRENCY, -12345)
    ]

def test_scan_bad():
    scanner = Scanner("&crash")
    with pytest.raises(ValueError, match="&crash"):
        next(scanner)
