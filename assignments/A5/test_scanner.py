import pytest

from scanner import Scanner
from token_ import Token
from type_ import Type

def test_scan_keywords():
    '''check that keywords are scanned correctly, regardless of case'''
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
    '''check that non-keywords are identified as identifiers'''
    scanner = Scanner("equity cash end_of_the_world_fund")
    assert list(scanner) == [
        Token(Type.IDENT, "equity"),
        Token(Type.IDENT, "cash"),
        Token(Type.IDENT, "end_of_the_world_fund")
    ]

def test_scan_currency():
    '''check that currency is identified and stored correctly'''
    scanner = Scanner("100 100.00 100.42 -123.45")
    assert list(scanner) == [
        Token(Type.CURRENCY, 10000),
        Token(Type.CURRENCY, 10000),
        Token(Type.CURRENCY, 10042),
        Token(Type.CURRENCY, -12345)
    ]

def test_scan_currency_round():
    '''check that currency is rounded if there are more than two decimals'''
    scanner = Scanner("100.00 100.420 100.429")
    assert list(scanner) == [
        Token(Type.CURRENCY, 10000),
        Token(Type.CURRENCY, 10042),
        Token(Type.CURRENCY, 10043)
    ]

def test_scan_bad():
    '''check that invalid data properly triggers an exception'''
    scanner = Scanner("&crash")
    with pytest.raises(ValueError, match="&crash"):
        next(scanner)

def test_scan_good_bad():
    '''check that a valid keyword but invalid character triggers an exception'''
    scanner = Scanner("!balance")
    with pytest.raises(ValueError, match="!balance"):
        next(scanner)
