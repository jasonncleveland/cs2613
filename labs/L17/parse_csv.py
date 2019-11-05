def split_csv(string):
    output = []
    lines = string.splitlines()
    for line in lines:
        output.append(line.split(','))
    return output
