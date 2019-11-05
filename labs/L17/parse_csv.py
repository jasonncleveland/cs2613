import re

def strip_quotes(string):
    strip_regex = re.compile(r'^"?([^"]+)"?$')
    search = strip_regex.search(string)
    if search:
        return search.group(1)
    else:
        return None

def split_csv(string):
    output = []
    lines = string.splitlines()
    for line in lines:
        strip_quotes(line)
        output.append([strip_quotes(element) for element in line.split(',')])
    return output
