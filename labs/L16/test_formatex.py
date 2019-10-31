import formatex

def test_equality():
    assert sorted(formatex.strings_plus) == sorted(formatex.strings_format)
