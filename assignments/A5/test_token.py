from type_ import Type
from token_ import Token

def test_token():
    '''check that a Token object is properly created'''
    token = Token(Type.IDENT, "hello")
    assert token.type == Type.IDENT
    assert token.value == "hello"

def test_str():
    '''check that the string representation of a Token object is correct'''
    id = Token(Type.IDENT, "hello")
    assert str(id) == '[IDENT: hello]'
    money = Token(Type.CURRENCY, 10042)
    assert str(money) == '[CURRENCY: 100.42]'

def test_equal_ident():
    '''check that Token attributes are equal'''
    assert Token(Type.IDENT, "Bob") == Token(Type.IDENT, "Bob")
    assert Token(Type.IDENT, "Bob") != Token(Type.IDENT, "b0b")

def test_equal_keywords():
    '''check that Token attributes are equal'''
    assert Token(Type.TRANSFER, "transfer") != Token(Type.OPEN, "open")
    assert Token(Type.OPEN, "OPEN") == Token(Type.OPEN, "open")
    assert Token(Type.BALANCE, "BALANCE") == Token(Type.BALANCE, "balance")

def test_equal_currency():
    '''check that currency is compared correctly'''
    assert Token(Type.CURRENCY, 1000) == Token(Type.CURRENCY, 1000)
    assert Token(Type.CURRENCY, 1000) != Token(Type.CURRENCY, 1001)
    assert Token(Type.CURRENCY, 1234) == Token(Type.CURRENCY, 1234)

def test_equal_currency_negative():
    '''check that negative currency is stored correctly'''
    assert Token(Type.CURRENCY, -1000) == Token(Type.CURRENCY, -1000)
    assert Token(Type.CURRENCY, -5000) != Token(Type.CURRENCY, 5000)
