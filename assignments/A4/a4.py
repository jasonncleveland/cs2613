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

