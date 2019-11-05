from parse_csv import split_csv, strip_quotes, split_row_3, split_row

test_string_1 = """OPEID,INSTNM,TUITIONFEE_OUT
02503400,Amridge University,6900
00100700,Central Alabama Community College,7770
01218200,Chattahoochee Valley Community College,7830
00101500,Enterprise State Community College,7770
00106000,James H Faulkner State Community College,7770
00101700,Gadsden State Community College,5976
00101800,George C Wallace State Community College-Dothan,7710
"""

table1 = [
    ['OPEID', 'INSTNM', 'TUITIONFEE_OUT'],
    ['02503400', 'Amridge University', '6900'],
    ['00100700', 'Central Alabama Community College', '7770'],
    ['01218200', 'Chattahoochee Valley Community College', '7830'],
    ['00101500', 'Enterprise State Community College', '7770'],
    ['00106000', 'James H Faulkner State Community College', '7770'],
    ['00101700', 'Gadsden State Community College', '5976'],
    ['00101800', 'George C Wallace State Community College-Dothan', '7710']
]

test_string_2 = '''OPEID,INSTNM,TUITIONFEE_OUT
02503400,"Amridge University",6900
00100700,"Central Alabama Community College",7770
01218200,"Chattahoochee Valley Community College",7830
00101500,"Enterprise State Community College",7770
00106000,"James H Faulkner State Community College",7770
00101700,"Gadsden State Community College",5976
00101800,"George C Wallace State Community College-Dothan",7710
'''

test_string_3 = '''OPEID,INSTNM,TUITIONFEE_OUT
02503400,"Amridge University",6900
00100700,"Central Alabama Community College",7770
01218200,"Chattahoochee Valley Community College",7830
00101500,"Enterprise State Community College",7770
00106000,"James H Faulkner State Community College",7770
00101700,"Gadsden State Community College",5976
00101800,"George C Wallace State Community College, Dothan",7710
'''

table2 = [
    ['OPEID', 'INSTNM', 'TUITIONFEE_OUT'],
    ['02503400', 'Amridge University', '6900'],
    ['00100700', 'Central Alabama Community College', '7770'],
    ['01218200', 'Chattahoochee Valley Community College', '7830'],
    ['00101500', 'Enterprise State Community College', '7770'],
    ['00106000', 'James H Faulkner State Community College', '7770'],
    ['00101700', 'Gadsden State Community College', '5976'],
    ['00101800', 'George C Wallace State Community College, Dothan', '7710']
]

test_string_4 = '''OPEID,INSTNM,PCIP52,TUITIONFEE_OUT
00103800,Snead State Community College,0.0811,7830
00573400,H Councill Trenholm State Community College,0.0338,7524
00573300,"Bevill, State, Community College",0.0451,7800
00884300,Alaska Bible College,0,9300
00107100,Arizona Western College,0.0425,9530
00107200,"Cochise County Community College, District",0.0169,6000
'''

table3=[
    ['OPEID', 'INSTNM', 'PCIP52', 'TUITIONFEE_OUT'],
    ['00103800', 'Snead State Community College', '0.0811', '7830'],
    ['00573400', 'H Councill Trenholm State Community College', '0.0338', '7524'],
    ['00573300', 'Bevill, State, Community College', '0.0451', '7800'],
    ['00884300', 'Alaska Bible College', '0', '9300'],
    ['00107100', 'Arizona Western College', '0.0425', '9530'],
    ['00107200', 'Cochise County Community College, District', '0.0169', '6000']
]

def test_split_1():
    assert split_csv(test_string_1) == table1

def test_strip_quotes():
    assert strip_quotes('"hello"') == 'hello'
    assert strip_quotes('hello') == 'hello'

def test_split_2():
    assert split_csv(test_string_2) == table1

def test_split_row_3():
    assert split_row_3('00101800,"George C Wallace State Community College, Dothan",7710') == ['00101800', 'George C Wallace State Community College, Dothan', '7710']

def test_split_3():
    '''Check handling of quoted commas'''
    assert split_csv(test_string_3) == table2

def test_split_row():
    assert split_row('00101800,"George C Wallace State Community College, Dothan",7710,",,,"') == ['00101800', 'George C Wallace State Community College, Dothan', '7710',',,,']

def test_split_4():
    assert split_csv(test_string_4) == table3
