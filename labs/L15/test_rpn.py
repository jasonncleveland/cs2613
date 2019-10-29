from rpn import process, process_list, stack

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

def test_dup():
    process("clear")
    process("4")
    process("2")
    process("dup")
    assert stack == [4, 2, 2]

def test_pop():
    process("clear")
    process("4")
    process("2")
    process("pop")
    assert stack == [4]

def test_swap():
    process("clear")
    process("4")
    process("2")
    process("swap")
    assert stack == [2, 4]

def test_print():
    process("clear")
    process("3")
    process("4")
    retv = process("print")
    otherv = process("+")
    assert retv == 4
    assert otherv == None
    assert stack == [7]

def test_list_plus():
    ops = "clear 3 4 + print".split()
    assert process_list(ops) == [7]
    
def test_list_mult():
    ops = "clear 3 4 *  print".split()
    assert process_list(ops) == [12]

def test_list_combo():
    ops = "clear 3 4 * print 2 + print".split()
    assert process_list(ops) == [12, 14]
    
def test_list_quit():
    ops = "clear 3 4 * print 2 + quit print".split()
    assert process_list(ops) == [12]
