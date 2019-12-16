from ages import Ages

def test_simple():
    """Simplest matching case"""
    assert list(Ages("Bob is 123")) == [("Bob", 123)]

def test_capital():
    """Names must be capitalized"""
    assert list(Ages("bob is 123")) == []

def test_multiple():
    """Multiple matches"""
    iter_ = Ages("Bob is 42, Mary is 43")
    assert list(iter_) == [("Bob", 42), ("Mary", 43)]

def test_restart():
    """Iterator can be reused"""
    iter_ = Ages("Bob i s 42, Mary is 43")
    list1 = list(iter_)
    list2 = list(iter_)
    assert list1 == list2

def test_next():
    """next() skips matches. for loops work"""
    iter_ = Ages("Ali is 45,Bob is 52,Cher is 25,Dan is 18")
    result = []
    for pair in iter_:
        result.append(pair)
        next(iter_)
    assert result == [("Ali", 45), ("Cher", 25)]


############################### Added Test Cases ###############################

def test_empty():
    """Empty strings are valid"""
    assert list(Ages("")) == []

def test_invalid():
    """Invalid strings mixed with valid strings"""
    iter_ = Ages("Bob is 42, 43 Mary is,banana")
    assert list(iter_) == [("Bob", 42)]

def test_return_type():
    """Function returns a string name and integer age"""
    iter_ = Ages("Bob is 42, Mary is 43")
    assert not list(iter_) == [("Bob", "42"), ("Mary", 43)]
