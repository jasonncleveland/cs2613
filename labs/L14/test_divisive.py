from divisive import fraction

def test_fraction_init():
    assert fraction(4, 2) == 2

def test_fraction_NaN():
    assert fraction(4, 0) == 'NaN'