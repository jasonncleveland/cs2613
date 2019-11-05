from parse_csv import split_csv, strip_quotes

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

def test_split_1():
    assert split_csv(test_string_1) == table1

def test_strip_quotes():
    assert strip_quotes('"hello"') == 'hello'
    assert strip_quotes('hello') == 'hello'

def test_split_2():
    assert split_csv(test_string_2) == table1
