from type_ import Type

def test_enum():
    '''check that defined enum type matches assignment'''
    assert sorted([ member.name for member in Type ]) == ['BALANCE', 'CURRENCY', 'IDENT', 'OPEN', 'TRANSFER']

def test_get_type_by_name():
    '''check that the correct type is found irregardless of case'''
    assert Type.get_type_by_name('OPEN') == Type.OPEN
    assert Type.get_type_by_name('Transfer') != Type.OPEN
    assert Type.get_type_by_name('bAlaNCe') == Type.BALANCE

def test_get_type_by_name_default():
    '''check that IDENT is returned when an invalid type is given'''
    assert Type.get_type_by_name('IDENT') == Type.IDENT
    assert Type.get_type_by_name('not found') == Type.IDENT
