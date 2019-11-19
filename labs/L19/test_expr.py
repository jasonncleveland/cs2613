from expr import Expr
from copy import deepcopy

six_plus_nine = Expr('+', 6, 9)
six_times_nine = Expr('*', 6, 9)
compound1 = Expr('+', six_times_nine, six_plus_nine)
compound2 = Expr('*', six_times_nine, compound1)
compound3 = Expr('+', compound2, 3)

def test_equality():
    assert six_plus_nine == deepcopy(six_plus_nine)
    assert compound1 == deepcopy(compound1)
    assert compound2 == deepcopy(compound2)
    assert compound3 == deepcopy(compound3)

def test_basic():
    assert six_plus_nine.eval() == 15
    assert six_times_nine.eval() == 54
    assert deepcopy(six_plus_nine).eval() == 15
    assert deepcopy(six_times_nine).eval() == 54

def test_recur():
    assert compound1.eval() == 69
    assert compound2.eval() == 3726
    assert compound3.eval() == 3729
    assert deepcopy(compound1).eval() == 69
    assert deepcopy(compound2).eval() == 3726
    assert deepcopy(compound3).eval() == 3729
