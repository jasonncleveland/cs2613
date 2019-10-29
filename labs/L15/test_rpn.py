from rpn import process, stack

def test_push():
    process("1")
    process("2")
    assert stack == [1, 2]

def test_plus():
    process("+")
    assert stack == [3]

def test_minus():
    process("1")
    process("-")
    assert stack == [2]

def test_mult():
    process("2")
    process("*")
    assert stack == [4]

def test_div():
    process("2")
    process("/")
    assert stack == [2]
