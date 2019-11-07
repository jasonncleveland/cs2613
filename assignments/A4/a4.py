def header_map(row):
    """Maps the index of a row column to its value"""
    headers = {}
    for i, label in enumerate(row):
        headers[label] = i
    return headers

def select(table, columns):
    """Filter table data to only provided columns"""
    headers = header_map(table[0])
    filtered_data = []
    for row in table:
        filtered_data.append([row[headers[col]] for col in columns])
    return filtered_data

def row2dict(headers, row):
    """Create a dictionary from a row and provided headers"""
    converted = {}
    for key in headers.keys():
        converted[key] = row[headers[key]]
    return converted

def compare_values(left, right, op):
    """Evaluate the left and right parameters according to the operator"""
    # Attempt to convert both sides to an int if either is an int
    if isinstance(left, int) or isinstance(right, int):
        try:
            left = int(left)
            right = int(right)
        except ValueError:
            return False
    if op == '==':
        return left == right
    elif op == '!=':
        return left != right
    elif op == '<':
        return left < right
    elif op == '>':
        return left > right
    elif op == '<=':
        return left <= right
    elif op == '>=':
        return left >= right

def check_row(row, condition):
    """Evaluate whether a row satisfies the given conditional"""
    op = condition[1]
    if op in ['AND', 'OR']:
        if op == 'AND':
            return check_row(row, condition[0]) and check_row(row, condition[2])
        elif op == 'OR':
            return check_row(row, condition[0]) or check_row(row, condition[2])
    else:
        left = row[condition[0]] if condition[0] in row else condition[0]
        right = row[condition[2]] if condition[2] in row else condition[2]
        return compare_values(left, right, op)
