import numpy as np

matrix = np.array([
    np.random.randint(i+1, i+9, 5) for i in range(4)
])

print(matrix)

row_mean = np.mean(matrix, axis=1)
col_mean = np.mean(matrix, axis=0)

row_std = np.std(matrix, axis=1)
col_std = np.std(matrix, axis=0)

result = {
    "mean": "row-wise" if row_mean.mean() > col_mean.mean() else "column-wise",
    "std": "row-wise" if row_std.mean() > col_std.mean() else "column-wise"
}

print(result)
