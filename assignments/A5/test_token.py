from type_ import Type
from token_ import Token

def test_token():
    token = Token(Type.IDENT, "hello")
    assert token.type == Type.IDENT
    assert token.value == "hello"

def test_str():
    id = Token(Type.IDENT, "hello")
    assert str(id) == '[IDENT: hello]'
    money = Token(Type.CURRENCY, 10042)
    assert str(money) == '[CURRENCY: 100.42]'

def test_equal_ident():
    assert Token(Type.IDENT, "Bob") == Token(Type.IDENT, "Bob")
    assert Token(Type.IDENT, "Bob") != Token(Type.IDENT, "b0b")

def test_equal_keywords():
    assert Token(Type.TRANSFER, "transfer") != Token(Type.OPEN, "open")
    assert Token(Type.OPEN, "OPEN") == Token(Type.OPEN, "open")
    assert Token(Type.BALANCE, "BALANCE") == Token(Type.BALANCE, "balance")

def test_equal_currency():
    assert Token(Type.CURRENCY, 1000) == Token(Type.CURRENCY, 1000)
    assert Token(Type.CURRENCY, 1000) != Token(Type.CURRENCY, 1001)
