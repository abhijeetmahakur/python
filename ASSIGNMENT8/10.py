import numpy as np
import random
import time

# -------- NumPy Method --------
start_time = time.time()

numpy_array = np.random.random((1000, 1000))

end_time = time.time()
numpy_time = end_time - start_time

print("NumPy execution time:", numpy_time)


# -------- Python Loop Method --------
start_time = time.time()

python_array = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(random.random())
    python_array.append(row)

end_time = time.time()
python_time = end_time - start_time

print("Python loop execution time:", python_time)


# -------- Comparison --------
if numpy_time < python_time:
    print("NumPy is faster")
else:
    print("Python loop is faster")
