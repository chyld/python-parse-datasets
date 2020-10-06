import csv
import numpy as np

matrix = []
with open('data/some_tabular_data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        data = [*map(lambda s: float(s), row)]
        matrix.append(data)

npmatrix = np.array(matrix)
