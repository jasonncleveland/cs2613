import re

def strip_quotes(string):
    strip_regex = re.compile(r'^"?([^"]+)"?$')
    search = strip_regex.search(string)
    if search:
        return search.group(1)
    else:
        return None

def split_csv(string):
    return [split_row_3(line) for line in string.splitlines()]

def split_row_3(string):
    split_regex = re.compile(
        r'''^   # start
        ("[^"]*"|[^,]+)  # first column
        ,
        ("[^"]*"|[^,]+)  # second column
        ,
        ("[^"]*"|[^,]+)  # third column
        $''',
        re.VERBOSE
    )
    search = split_regex.search(string)
    if search:
        return [strip_quotes(col) for col in search.groups()]
    else:
        return None
