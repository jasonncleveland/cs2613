def header_map(row):
    """Maps the index of a row column to its value"""
    headers = {}
    for i, label in enumerate(row):
        headers[label] = i
    return headers
