from rpn import process, stack

def test_push():
    process("1")
    process("2")
    assert stack == [1, 2]

def test_plus():
    process("clear")
    process("1")
    process("2")
    process("+")
    assert stack == [3]

def test_minus():
    process("clear")
    process("4")
    process("2")
    process("-")
    assert stack == [2]

def test_mult():
    process("clear")
    process("2")
    process("2")
    process("*")
    assert stack == [4]

def test_div():
    process("clear")
    process("4")
    process("2")
    process("/")
    assert stack == [2]

def test_clear():   
    process("1")
    process("2")
    process("clear")
    assert stack == []
