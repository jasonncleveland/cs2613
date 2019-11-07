import csv

def read_csv(filename):
    """Read a CSV file, return list of rows"""
    rows = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            rows.append(row)
    return rows
