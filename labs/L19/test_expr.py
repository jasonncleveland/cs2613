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
